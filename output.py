#this is just some code for an example 
#when working with github

# Assumes that the package 'weather-util' has been installed.
#   sudo apt-get install weather-util
#   weather -iKAUS

import subprocess

weather=subprocess.check_output(["weather", "-iKAUS"])

print "Current weather for Austin:\n\n%s" % weather
