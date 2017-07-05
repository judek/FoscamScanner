#!/usr/bin/env python
from nmap import PortScanner
import datetime

#print('#Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

nm = PortScanner()

nm.scan('192.168.1.*', '88')

print '<html>'
print '<head><title>Cameras</title></head>'
print '<body>'
for host in nm.all_hosts():
     if 'open' == nm[host]['tcp'][88]['state']:
          print '%s<hr><a href="http://7227.xtrahype.com/camera/%s"><img src="http://7227.xtrahype.com/camera/%s"></a><br /><br />' % (host, host, host)
           #print('Camera found : %s %s' % (host, nm[host]['addresses']['ipv4']))
          #print('State : %s' % nm[host].state())
          #print ('port : %s\tstate : %s' % ('88', nm[host]['tcp'][88]['state']))


print '</body>'
print '</html>'

