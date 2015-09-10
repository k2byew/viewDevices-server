#!/usr/bin/env python
import subprocess
import requests
import datetime
import json

#Todo: bash script so slow that new data only sent out next time script runs
#Todo: Call and directly use output without writing to disk


# Set your own USERNAME and LOGGLY-TOKEN

bashCommand = "/home/USERNAME/print_netdiscover.sh"
subprocess.Popen(bashCommand)

macs = [mac.rstrip('\n') for mac in open('/tmp/macs.list', 'r')]
vendors = [vendor.rstrip('\n') for vendor in open('/tmp/vendors.list', 'r')]
ips = [ip.rstrip('\n') for ip in open('/tmp/ips.list', 'r')]

deviceList = macs
deviceCount = len(macs)

log_data = ({
        'timestamp':datetime.datetime.utcnow().isoformat(),
        'deviceCount':deviceCount,
        'deviceList':deviceList,
        'vendorList':vendors,
        'ipList':ips
        })

# Send data to Loggly.com
loggly_token = "LOGGLY-TOKEN"
loggly_tag = "device-count"

url = "https://logs-01.loggly.com/inputs/{0}/tag/{1}/".format(loggly_token,loggly_tag)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
requests.post(url, data=json.dumps(log_data), headers=headers)

# Write json file to filesystem
jsonFile = "/tmp/currentDevices/currentDevices.json"

file = open(jsonFile, "w")
file.write(json.dumps(log_data))
file.close()

#Debug
#print json.dumps(log_data)
