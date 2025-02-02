from tpk4128.server import SocketServer
from tpk4128.camera_opencv import Camera


def main():
    camera = Camera()
    server = SocketServer('localhost', 50007)

    while True:

        data = server.recv()
        print(data)
        if not data:
            break

        img = camera.capture()
        buf = img.tostring(None)
        server.sendall(buf)


if __name__ == '__main__':
    main()
