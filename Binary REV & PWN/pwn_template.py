from pwn import *


def send_print(val):
    """
    Sends the given value / string to the target (and prints the data to your console)

    Args:
        val: The value or string to send
    """
    target.send(str(val).encode())
    print(val, end="")


def sendline_print(val):
    """
    Sends the given value / string to the target and finishes the current line (and prints
    the data to your console)

    Args:
        val: The value or string to send
    """
    target.sendline(str(val).encode())
    print(val)


def recvuntil_print(val):
    """
    Receive data from the target until the specified value / string is found in the data
    stream.

    Example: Entering the val "Password? " will stop right after the server sends "What is
    the Password? " to you. That way you can can enter a password with send_print or
    sendline_print afterwards.

    Args:
        val: The value or string to look for

    Returns: The data (string) you received
    """
    resp = target.recvuntil(val)
    print(resp.decode(), end="")
    return resp.decode()


def recvline_print():
    """
    Receives a single line from the target and prints it to the console.

    Returns: The data (string) you received
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
