from django.shortcuts import render
from django.http import JsonResponse
import requests

def place_search(request):
	key = "AIzaSyABKeTIiQ6CSNcl5UPUWqCFxxtaKx_oV4I"
	# query = "starbucks"
	query = request.GET.get("query","")
	print(query)
	# url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key, query)
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+key+"&region=kw"
	token = request.GET.get("pt")
	if token:
		url += "&pagetoken=%s"%(token)

	response = requests.get(url).json()
	context = {
	"response":response,


	}

	# return JsonResponse(response, safe=False)
	return render(request, "places.html", context)

def place_detail(request):
	key = "AIzaSyABKeTIiQ6CSNcl5UPUWqCFxxtaKx_oV4I"
	place_id = request.GET.get("id")
	url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s&region=kw"%(place_id, key)

	response = requests.get(url).json()
	context = {
		"response":response,
	}
	# return JsonResponse(response, safe=False)
	return render(request, "detail.html", context)


