Netdiscover can reveal the vendor name, local IP address, and MAC address of the devices connected to your network. viewDevices-server will expose this information.

Run main.py using root's cron, and details from netdiscover will periodically be upload to Loggly.com and also be saved as an json file on the filesystem (which can be served by nginx if required).
