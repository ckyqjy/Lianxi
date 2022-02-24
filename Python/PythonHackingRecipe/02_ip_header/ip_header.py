#!/usr/bin/env python3
import os
import struct
import argparse
from socket import *
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Print ip header
"""

# --------------------------------------------------
def parse_packet(host):
    """ Parse packet without promiscous mode """

    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP

    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))

    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    packet_no = 0
    try:
        while True:
            packet_no+=1
            data=sock.recvfrom(65535)
            print(f"{packet_no} th packet\n")
            parse_ip_header(data)

    except KeyboardInterrupt: 
        sock.close()


# --------------------------------------------------
def parse_ip_header(data):
    """ Parse ip headers """

    ip_headers, ip_payloads = parse_ip(data[0])
    print("version: ", ip_headers[0] >> 4)
    print("Header Length: ", ip_headers[0] & 0x0F)
    print("Type of Service: ", ip_headers[1])
    print("Total Length: ", ip_headers[2])
    print("Identification: ", ip_headers[3])
    print("IP Flags, Fragment Offset: ", parse_flags_offset(ip_headers[4]))
    print("Time To Live: ", ip_headers[5])
    print("Protocol: ", ip_headers[6])
    print("Header Checksum: ", ip_headers[7])
    print("Source Address: ", inet_ntoa(ip_headers[8]))
    print("Destination Address: ", inet_ntoa(ip_headers[9]))
    print("=" * 50)


# --------------------------------------------------
def parse_ip(ip_header):
    """ Parse ip headers and payloads """

    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payloads = ip_header[:20]

    return ip_headers, ip_payloads


# --------------------------------------------------
def parse_flags_offset(int_num):
    """ Parse flags and fragment offset """

    byte_num = int_num.to_bytes(2, byteorder="big")
    x = bytearray(byte_num)
    flags_offset = bin(x[0])[2:].zfill(8)+bin(x[1])[2:].zfill(8) 
    
    return flags_offset[:3], flags_offset[3:]


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        usage='ip_header.py [-h] ip',
        description='Print ip header structure per packet',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('ip',
                        metavar='ip',
                        help='Ip address')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main function starts here """

    host = get_args().ip
    print(f"Listening at [{host}]")
    parse_packet(host)


# --------------------------------------------------
if __name__ == '__main__':
    main()
