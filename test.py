import sys

from servers.server_template import Server
import multiprocessing as mp


class TestServer1(Server):
    HOST = "localhost"
    PORT = 32456


class TestServer2(Server):
    HOST = "localhost"
    PORT = 32434

    def handle(self, message):
        return f"got: {message}"


def run1():
    s1 = TestServer1()
    s1.run()


def run2():
    s2 = TestServer2()
    s2.run()


if __name__ == "__main__":
    import sys
    print(sys.argv)
    mp.set_start_method('spawn')
    p1 = mp.Process(target=run1)
    p2 = mp.Process(target=run2)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
