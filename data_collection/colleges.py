from common import *
import pprint
import requests
import json
from mitmproxy import io
from mitmproxy.exceptions import FlowReadException
import sys

def begin():
	flow = get_flow_from_file("objects/admit_flow")
	headers = get_dict_from_obj(flow.request.headers)
	url = get_url(flow)
	data = flow.request.text
	r = requests.post(url = url, headers = headers, data = data)
	pprint (r.text)



def get_json_of_college(college_name):
	profiles = []
	with open("objects/" + college_name, "rb") as logfile:
		freader = io.FlowReader(logfile)
		pp = pprint.PrettyPrinter(indent=4)
		try:
			for f in freader.stream():
				if (f.request.host == "admits.fyi" and f.request.method == 'POST'):
					try:
						formatted_json = json.loads(f.response.text)
						pagination = formatted_json.get('result',None)
					except:
						continue
					if not pagination:
						continue
					data = pagination.get('data')
					if not data:
						pp.pprint(pagination)
						break
					profiles.extend(data)
		except FlowReadException as e:
			print("Flow file corrupted: {}".format(e))
	f = open("jsons/" + college_name + ".json", "w")
	d = {}
	d['data'] = profiles
	json.dump(d, f)


def parse_json(college_name):
	with open("jsons/" + college_name + ".json", "r") as f:
		data = json.load(f)
	profiles = data['data']
	

get_json_of_college("umdcp")