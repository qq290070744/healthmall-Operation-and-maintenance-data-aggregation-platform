#!/usr/bin/env python
#coding:utf-8
# from grafana_api_client import GrafanaClient
# client = GrafanaClient(("pmm", "ngiISI0Q4g9gfqWz89folKJSi"), host="121.201.72.168", port=50080)
# # client.org
import requests

ret = requests.get('http://121.201.72.168:50080/')

print(ret.text)