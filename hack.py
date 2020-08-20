import sys
import socket
from itertools import product


def main():
    _, ip, port = sys.argv
    chars = list(range(97, 123)) + list(range(48, 58))
    chars = [chr(i) for i in chars]

    def bruteforce(charset, length):
        return (''.join(i) for i in product(chars, repeat=length))

    length = 0
    with socket.socket() as s:
        s.connect((ip, int(port)))

        while True:
            length += 1
            for attempt in bruteforce(chars, length):
                s.send(attempt.encode())
                response = s.recv(1024).decode()

                if response == "Connection success!":
                    print(attempt)
                    return
                elif response == "Too many attempts":
                    return


if __name__ == '__main__':
    main()
