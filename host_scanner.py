import kthread 
from time import sleep
import subprocess
import sys
import os
import getmac
from datetime import datetime


def getips(host_pre, *file):
    ipadresses = {}
    def ping(ipadr):
        try:
            outputcap = subprocess.run([f'ping', ipadr, '-n', '1'], capture_output=True)
            ipadresses[ipadr] = outputcap
        except Exception as Fehler:
            print(Fehler)

    t = [kthread.KThread(target = ping, name = f"ipgetter{ipend}", args=(f'{host_pre}.{ipend}',)) for ipend in range(255)]
    [kk.start() for kk in t] #starts 255 threads

    while len(ipadresses) < 255:
        sleep(0.1)

    alldevices = []
    for key, item in ipadresses.items():
        if not 'unreachable' in item.stdout.decode('utf-8') and 'failure' not in item.stdout.decode('utf-8'):
            alldevices.append(key)

    if file:
        with open(f'{file[0]}.txt', 'w') as f:
            for ip in alldevices:
                f.write(f'IP: {ip} ||  MACaddress:{getmac.get_mac_address(ip=ip)}\n')
            else:
                print('[+] Network Scanned succecfully')
                print(f'[+] IPs Saved to {file[0]}.txt')
    else:
        with open(f'ips.txt', 'w') as f:
            for ip in alldevices:
                f.write(f'IP: {ip}  ||  MACaddress:{getmac.get_mac_address(ip=ip)}\n')
            else:
                print('[+] Network Scanned succecfully')
                print(f'[+] IPs Saved to ips.txt')

def main():
    if len(sys.argv) == 3:
        arg = sys.argv[1]
        file = sys.argv[2]
        host_prefix = arg.split('.')
        host= '.'.join(host_prefix[:3])
        getips(host, file)

    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        host_prefix = arg.split('.')
        host= '.'.join(host_prefix[:3])
        getips(host)
    elif len(sys.argv) not in range(2,4):
        print("[+] Scanning with default gateway 192.168.1.1")
        getips('192.168.1')
    else:
        print(f'Usage: python3 {os.path.basename(__file__)} *<ip> *<file>')

if __name__=='__main__':
    main()