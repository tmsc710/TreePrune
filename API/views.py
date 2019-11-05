import requests
import json

from pprint import pprint
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from urllib.parse import urljoin


UPSTREAM_URL="http://core-alb-1458074199.eu-west-1.elb.amazonaws.com:7777/"

class Graph:
	def __init(self, data):
		self.parent = None
		self.children = None
		self.data = data


class Tree(View):
	def get(self, request, endpoint, *args, **kwargs):
		kpi_ids = request.GET.get('kpi_ids[]', -1)
		url = urljoin(UPSTREAM_URL, endpoint)
		response = requests.get(url=url)
		if response.status_code == 404:
			error_message = f"Endpoint <{endpoint}> not found in the upstream."
			return HttpResponseNotFound(error_message)
		x = response.json()
		cursor = x

		for theme in cursor:
			for sub_theme in theme["sub_themes"]:
				for category in sub_theme["categories"]:
					for indicator in category["indicators"]:
						if indicator["id"] and int(indicator["id"]) != int(kpi_ids):
							del indicator

		print("Just for development branch.")
		return HttpResponse(cursor)
