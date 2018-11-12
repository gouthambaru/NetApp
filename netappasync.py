import time
import requests
import ssl
import json
from pprint import pprint

from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#ssl.create_default_https_context=ssl.create_unverified_context
ClusterMVIP=str(raw_input("Enter IP address \n"))
version=str(input("Enter Element OS Version.  Please note enter the OS version with decimal. For example Element OS 10 should be entered as 10.0 \n"))
SFnode="https://"+ClusterMVIP+"/json-rpc/"+version #default node command line


headers={'content-type':'application/json'}	#json header file
payload={"method":"ListVolumeStats",
	"params":{"volumeIDs":[7] },
	"id":1}
payload=json.dumps(payload)   #converting payload data into json format

usname="admin"
passwd="netapp123!"

def check(SFnode,usname,passwd):#function taking values and checing the asyncdelay
	response=requests.post(SFnode,auth=HTTPBasicAuth(usname,passwd),verify=False,headers=headers,data=payload,timeout=25)
	#data=(response.text)
	data1=(response.json())
	time.sleep(5)
	pprint("the async delay is"+((data1["result"]["volumeStats"][0]["asyncDelay"]).encode('utf-8')))

while True:
	check(SFnode,usname,passwd)
