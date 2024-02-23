import os
import re
import ctypes
import sys

ips = []


def is_admin():
    """ check admin rights """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return 0


def delete_current_routes(ips):
    for ip in ips:
        os.system(rf'C:\Windows\System32\route.exe delete {ip}')


def add_routes(ips, interface):
    for ip in ips:
        os.system(rf'C:\Windows\System32\route.exe add {ip} mask 255.255.255.255 {interface}')


if __name__ == '__main__':
    if not is_admin():
        # Re-run the program with admin rights
        print("Re-run with admin rights, args:", sys.argv[1:])
        re_run_file = __file__ + ' ' + \
            ' '.join(sys.argv[1:]) if len(sys.argv[1:]) > 0 else __file__
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, re_run_file, None, 1)
        sys.exit()

    ipconfig = os.popen('ipconfig')
    ipconfig = ipconfig.read()

    # find the "PPP adapter sjtu" and extract the IPv4 address
    match = re.search(
        r"PPP adapter sjtu:.*?IPv4 Address\. .+? : (\d+\.\d+\.\d+\.\d+)", ipconfig, re.DOTALL)

    interface = match.group(1) if match else "IPv4 address not found"
    if match:
        interface = match.group(1)
    else:
        raise ValueError("IPv4 address not found")

    delete_current_routes(ips)
    add_routes(ips, interface)
