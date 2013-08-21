#!/usr/bin/env python
import os
import sys
import subprocess
import time
import datetime


if os.geteuid() != 0:
    print "Script not started as root. Running sudo.."
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)


def renew_dhcp():
    """ Main script to renew DHCP
    """
    try:
        renew_time = int(raw_input("Please enter a time in minutes to rewnew dhcp (example: 10): "))
    except ValueError:
        print("That was not a number, please try again (example: 10): ")
        renew_dhcp()

    renew_time = renew_time * 60

    while True:
        subprocess.call("ipconfig set en1 BOOTP", shell=True)
        subprocess.call("ipconfig set en1 DHCP", shell=True)

        for i in range(renew_time):

            time.sleep(1)
            time_left = str(datetime.timedelta(seconds=renew_time - i))

            sys.stdout.write("\r{0} until next DHCP renewal. ".format(time_left)) 
            sys.stdout.flush()


if __name__ == "__main__":
    renew_dhcp()