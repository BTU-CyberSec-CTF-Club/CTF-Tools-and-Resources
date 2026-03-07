from pwn import *


def send_print(val):
    """
    Sends the given value / string to the target (and prints the data to your stdout)

    Args:
        val: The value or string to send
    """
    target.send(str(val).encode())
    print(val, end="")


def sendline_print(val):
    """
    Sends the given value / string to the target and finishes the current line (and prints the data to your stdout)

    Args:
        val: The value or string to send
    """
    target.sendline(str(val).encode())
    print(val)


def recvuntil_print(val):
    """
    Receive data from the target until the specified value / string is found in the data
    stream.

    Example: Entering the val "Password? " will stop right after the server sends "What is the
    Password? " to you, so that you can enter it with send_print or sendline_print.

    Args:
        val: The value or string to look for
    """
    resp = target.recvuntil(val)
    print(resp.decode(), end="")
    return resp.decode()


def recvline_print():
    """
    Same as recvuntil_print, but will receive whole lines instead.
    """
    resp = target.recvline()
    print(resp.decode(), end="")
    return resp.decode()


## PWN THE SERVICE
# target = process(argv=["python", "redacted.py"])
target = remote("24.199.110.35", 43298)  # IP and Port pair

# TODO do whatever you need to do here

# Done with your script. Keep receiving the rest of the data from the server
try:
    while True:
        recvline_print()
except EOFError:
    exit()
