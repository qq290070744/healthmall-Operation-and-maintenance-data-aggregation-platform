#!/usr/bin/env python
#coding:utf-8
# from grafana_api_client import GrafanaClient
# client = GrafanaClient(("pmm", "ngii"), host="1268", port=50)
# # client.org
import requests

ret = requests.get('http://121.201.72.168:50080/')

print(ret.text)
