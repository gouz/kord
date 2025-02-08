from machine import Pin, PWM
import neopixel
import network
import socket
from json import loads
from time import sleep


def urlopen(url, data=None, method="GET"):
    if data is not None and method == "GET":
        method = "POST"
    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        import tls

        port = 443
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    ai = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)
    ai = ai[0]

    s = socket.socket(ai[0], ai[1], ai[2])
    try:
        s.connect(ai[-1])
        if proto == "https:":
            context = tls.SSLContext(tls.PROTOCOL_TLS_CLIENT)
            context.verify_mode = tls.CERT_NONE
            s = context.wrap_socket(s, server_hostname=host)

        s.write(method)
        s.write(b" /")
        s.write(path)
        s.write(b" HTTP/1.0\r\nHost: ")
        s.write(host)
        s.write(b"\r\n")

        if data:
            s.write(b"Content-Length: ")
            s.write(str(len(data)))
            s.write(b"\r\n")
        s.write(b"\r\n")
        if data:
            s.write(data)

        l = s.readline()  # Status-Line
        # l = l.split(None, 2)
        # print(l)
        # status = int(l[1])  # FIXME: Status-Code element is not currently checked
        while True:
            l = s.readline()
            if not l or l == b"\r\n":
                break
            # print(l)
            if l.startswith(b"Transfer-Encoding:"):
                if b"chunked" in l:
                    raise ValueError("Unsupported " + l)
            elif l.startswith(b"Location:"):
                raise NotImplementedError("Redirects not yet supported")
    except OSError:
        s.close()
        raise

    return s

nbPixels = 5
latitude = 45.751725
longitude = 4.219661
tokenWeather = "ab302913987bf40d2488afb323da3bed"
urlWeather = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={tokenWeather}&units=metric&lang=en"

lightPower = 255

np = neopixel.NeoPixel(Pin(4), nbPixels)

motor1 = PWM(Pin(10, mode=Pin.OUT))
motor1.freq(50)
motor2 = PWM(Pin(12, mode=Pin.OUT))
motor2.freq(50)

for i in range(nbPixels):
    np[i] = (0, 0, 0)
np.write()

np[4] = (127, 0, 0)
np.write()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('bobox', 'mon joli mot de passe')
while not wlan.isconnected():
    pass
print("Connected to Wi-Fi")
np[4] = (0, lightPower, 0)
np.write()

weather = loads(urlopen(urlWeather).read())["weather"][0]["id"]

if (weather == 800):
    np[0] = (lightPower, lightPower, 0)
    np[1] = (lightPower, lightPower, 0)
    np[2] = (lightPower, lightPower, 0)
elif (weather > 800):
    np[0] = (0, 0, lightPower)
    np[1] = (lightPower, lightPower, 0)
    np[2] = (0, 0, lightPower)

np.write()

while True:
    motor1.duty_u16(1638)
    motor2.duty_u16(7864)
    sleep(1)
    motor1.duty_u16(7864)
    motor2.duty_u16(1638)
    sleep(1)