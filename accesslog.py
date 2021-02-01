import urllib.request

url = 'https://raw.githubusercontent.com/linuxacademy/content-elastic-log-samples/master/access.log'
accessFile = urllib.request.urlopen(url)

ipset = set()

for line in accessFile:

    decoded_line = line.decode("utf-8")
    if not ' - - ' in decoded_line:
        continue
    ip = decoded_line.split(' - - ')[0]

    if not ip in ipset:
        ipset.add(ip)
        print(decoded_line)