()#!/usr/bin/env python

import urllib2, re

def writeYAML():
	yamlFile = open('/etc/logstash/dictionary.d/statuscakeIP.yaml','w')
	url='https://app.statuscake.com/Workfloor/Locations.php?format=txt'
        request = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 OPR/64.0.3417.61"})
	html = urllib2.urlopen(request).read()
	for line in html.split():
		yamlFile.write("\"" + line + "\": \"YES\"" + "\n")
	yamlFile.close()

if __name__=="__main__":
	writeYAML()
