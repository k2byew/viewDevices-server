#!/bin/sh

netdiscoverOutput="/tmp/netdiscover.output"
macList="/tmp/macs.list"
vendorList="/tmp/vendors.list"
ipList="/tmp/ips.list"

# Doing sudo here so all this works when root adds main.py into crontab
# Update IP range used by netdiscover to suit your network

sudo netdiscover -r 192.168.1.0/24 -i eth0 -c 20 -P > $netdiscoverOutput
sudo grep -o -i '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}' $netdiscoverOutput > $macList
sudo cut -c52- $netdiscoverOutput | tail -n +4 | head -n -2 > $vendorList
sudo grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' $netdiscoverOutput > $ipList