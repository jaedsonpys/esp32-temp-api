import socket

address = ('192.168.0.108', 80)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

temperature = humidity = 0.0


def get_temp() -> tuple:
    global temperature, humidity

    sock.send('s'.encode())
    data = sock.recv(3024).decode()
    data = data.strip()

    try:
        temperature, humidity = data.split(',')
    except ValueError:
        pass

    return float(temperature), float(humidity)
