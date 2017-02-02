import xbmcaddon
import xbmcgui
import os
import urllib
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
print "Environment:\n"
print "============\n"
for key in os.environ.keys():
  print "%30s = %s \n" % (key,os.environ[key])
print "\nProxies:\n"
print "=========\n"

proxies = urllib.getproxies()
for key in proxies.keys():
  print "%30s = %s \n" % (key,proxies[key])
  
line1 = "Hello World!"
line2 = "We can write anything we want here"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
