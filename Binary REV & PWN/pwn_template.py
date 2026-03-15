from pwn import *


def send_print(val, raw=False):
    """
    Sends the given value / string to the target (and prints the data to your console)

    Args:
        val: The value or string to send
        raw: If True, data will be sent as is (as bytes). Otherwise, it is assumed to be a
             string that will be encoded.
    """
    if raw:
        target.send(val)
        print(val.decode("utf-8", errors="replace"), end="")
    else:
        target.send(str(val).encode())
        print(val, end="")


def sendline_print(val, raw=False):
    """
    Sends the given value / string to the target and finishes the current line (and prints
    the data to your console)

    Args:
        val: The value or string to send
        raw: If True, data will be sent as is (should be given as bytes). Otherwise, it
             will be taken as a string (or converted to one) and sent to the server that way.
    """
    if raw:
        target.sendline(val)
        print(val.decode("utf-8", errors="replace"))
    else:
        target.sendline(str(val).encode())
        print(val)


def recvuntil_print(val, raw=False):
    """
    Receive data from the target until the specified value / string is found in the data
    stream.

    Example: Entering the val "Password? " will stop right after the server sends "What is
    the Password? " to you. That way you can can enter a password with send_print or
    sendline_print afterwards.

    Args:
        val: The value or string to look for
        raw: If True, data will be sent as is (should be given as bytes). Otherwise, it
             will be taken as a string (or converted to one) and sent to the server that way.

    Returns: The data (string) you received
    """
    if raw:
        resp = target.recvuntil(val)
    else:
        resp = target.recvuntil(str(val).encode())
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
