#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import re

def print_header(lesson):
    print("\n")
    print("="*80)
    print("{:^80}".format(lesson))
    print("="*80)
    print("\n")

    return lesson


def enter_ip():

    try:
        #Python 2
        ip = raw_input("Enter IP Address: ")
    except NameError:
        #Python 3
        ip = input("Enter IP Address: ")

    validate_ip(ip)
    return ip


def validate_ip(ip):
    pat = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

    test = False
    if pat.match(ip):
        test = True
        print("Acceptable ip address")
    else:
        test = False
        print("Unacceptable ip address")
        enter_ip()

    return test

def main():
    # Lesson 1
    print_header("Lesson 1")

    ip1 = enter_ip()

    ip2 = "1.1.1.1"
    ip3 = "3.3.3.3"
    print("{} {} {} ".format(ip1, ip2, ip3))

    # Lesson 2
    print_header("Lesson 2")
    ip_octets = ip1.split(".")
    ip_header = []
    ip_bin = []
    ip_oct = []
    for i in range(1,5):
        ip_header.append(f"Octet{i}")
        ip_bin.append(bin(int(ip_octets[i-1])))
        ip_oct.append(oct(int(ip_octets[i-1])))


    print("{:>20}{:>20}{:>20}{:>20}".format(*ip_header))
    print("-"*80)
    # Centered on 20 space line
    # print("{:^20}{:^20}{:^20}{:^20}".format(*ip_octets))
    # Centered on 20 space line
    print("{:>20}{:>20}{:>20}{:>20}".format(*ip_octets))
    print("{:>20}{:>20}{:>20}{:>20}".format(*ip_bin))
    print("{:>20}{:>20}{:>20}{:>20}".format(*ip_oct))
    print("-"*80)


    # Lesson 3
    print_header("Lesson 3")

    my_ipv6 = "FE80::0202:B3FF:FE1E:8329"
    MYV6 = "2001:db8:0:1"
    My_ipv6 = "2607:f0d0:1002:51::4"

    if my_ipv6 == MYV6:
        print(f"1st var {my_ipv6} equals 2nd var {MYV6}!")
    else:
        print(f"NOT EQUAL! 1st var {my_ipv6} does not equal 2nd var {MYV6}!")

    print()

    if my_ipv6 != My_ipv6:
        print(f"NOT EQUAL! 1st var {my_ipv6} does not equals 3rd var {My_ipv6}!")
    else:
        print(f"EQUAL! 1st var {my_ipv6} equals 3rd var {My_ipv6}!")


    # Lesson 4
    print_header("Lesson 4")

    show_version = "*0        CISCO881-SEC-K9       FTX0000038X    ".strip()
    _ = show_version.split()

    model = _[1]

    if "cisco" in model.lower() and '881' in model:
        print("Model: \t\t{:<20}".format(model))
        print("Serial Number: \t{:<20}".format(_[2]))


    # Lesson 5
    print_header("Lesson 5")

    mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
    mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
    mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

    mac_list = [mac1, mac2, mac3]

    print("{:>20}  {:>20}".format("IP ADDR", "MAC ADDRESS"))
    print("-"*20 +"  " + "-"*20)
    for mac in mac_list:
        _ = mac.split()
        print("{:>20}  {:>20}".format(_[1], _[3]))


# Standard call to the main() function.
if __name__ == '__main__':
    main()
