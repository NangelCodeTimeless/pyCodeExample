import subprocess


def ping(ip):
    subprocess.call(['ping', '-c', 1, ip])


while True:
    ip = input('ENTER IP:')
    if ip == 'exit':
        break
    ping(ip)
