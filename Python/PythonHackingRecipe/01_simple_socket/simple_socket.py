#!/usr/bin/env python3
from socket import *
import os
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Manipulate Python socket library
"""

# --------------------------------------------------
def parse_packet(host):
    """ Parse packet without promiscous mode """
    # Set protocol type on OS type
    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP

    # Create raw socket(ipv4, raw socket, protocol type) and bind
    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))

    # Set socket option(ip, ip header included, ip header manual)
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    data = sock.recvfrom(65535)
    print(data[0])

    # Close socket
    sock.close()


# --------------------------------------------------
def main():
    """ Main function starts here """

    host = "127.0.0.1"
    print(f"Listening at [{host}]")
    parse_packet(host)


# --------------------------------------------------
if __name__ == '__main__':
    main()
