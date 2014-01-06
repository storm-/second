#this is just some code for an example 
#when working with github
import subprocess

weather=subprocess.check_output(["weather", "-iKAUS"])

print "Current weather for Austin:\n\n%s" % weather
