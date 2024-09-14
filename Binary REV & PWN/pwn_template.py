from pwn import *


def send_print(val):
    target.send(str(val).encode())
    print(val, end="")


def sendline_print(val):
    target.sendline(str(val).encode())
    print(val)


def recvuntil_print(val):
    resp = target.recvuntil(val)
    print(resp.decode(), end="")
    return resp.decode()


def recvline_print():
    resp = target.recvline()
    print(resp.decode(), end="")
    return resp.decode()


# target = process(argv=["python", "redacted.py"])
target = remote("24.199.110.35", 43298)

# TODO stuff here

try:
    while True:
        recvline_print()
except EOFError:
    exit()
