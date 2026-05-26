#!/bin/python3
# pwn_template.py Version 1.3 (May 2026)
from pwn import *


#############
## LIBRARY ##
##############################################################################################
class TargetWrapper:
    """
    Wraps a pwntools tube (process, remote, ...) to perform more convenient functions on them, e.g. print all sent and received data.
    """

    def __init__(self, target):
        """
        Args:
            target: A pwntools tube (e.g. process, remote).
        """
        self.target = target

    def send(self, val, raw=False, print_data=True):
        """
        Sends data to the target and optionally prints it.

        Args:
            val: The data to send. If raw is False, it is converted to str and encoded.
            raw: If True, val must be bytes and is sent unchanged.
            print_data: If True, the data sent is printed to stdout.
        """
        if raw:
            data = val
            if print_data:
                print(data.decode("utf-8", errors="replace"), end="")
        else:
            data = str(val).encode()
            if print_data:
                print(val, end="")

        self.target.send(data)

    def sendline(self, val, raw=False, print_data=True):
        """
        Sends data followed by a newline and optionally prints it.

        Args:
            val: The data to send. If raw is False, it is converted to str and encoded.
            raw: If True, val must be bytes and is sent unchanged.
            print_data: If True, the data sent is printed to stdout (with a trailing newline).
        """
        if raw:
            data = val
            if print_data:
                print(data.decode("utf-8", errors="replace"))
        else:
            data = str(val).encode()
            if print_data:
                print(val)

        self.target.sendline(data)

    def recvuntil(self, val, raw=False, print_data=True):
        """
        Receives data until the given delimiter is found, optionally prints it.

        Args:
            val: The delimiter to wait for. If raw is False, it is converted to str and encoded.
            raw: If True, val must be bytes.
            print_data: If True, the received data is printed to stdout.

        Returns:
            The received data as a string (decoded).
        """
        if raw:
            delim = val
        else:
            delim = str(val).encode()

        resp = self.target.recvuntil(delim)
        resp_str = resp.decode()

        if print_data:
            print(resp_str, end="")

        return resp_str

    def recvline(self, print_data=True):
        """
        Receives a single line and optionally prints it.

        Args:
            print_data: If True, the received line is printed to stdout.

        Returns:
            The received line as a string (decoded).
        """
        resp = self.target.recvline()
        resp_str = resp.decode()

        if print_data:
            print(resp_str, end="")

        return resp_str


###############
## YOUR CODE ##
##############################################################################################
## PWN THE SERVICE
# target = process(argv=["python", "redacted.py"])
target = remote("24.199.110.35", 43298)  # IP and Port pair

io = TargetWrapper(target)  # wrap the connection

# TODO do whatever you need to do here
# Example:
# io.recvuntil("Username: ")
# io.sendline("admin")
# io.recvline(print_data=False)   # discard a line without printing
# io.recvuntil("Password: ", print_data=True)
# io.sendline("p4ssw0rd")

# Done with your script. Keep receiving the rest of the data from the server
try:
    while True:
        io.recvline()
except EOFError:
    exit()
