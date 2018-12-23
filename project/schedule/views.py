from django.shortcuts import render
import json

def station_list(request):
	with open('schedule/station_list.json', 'r', encoding='utf-8') as f:
		maininfo = json.load(f)
		f.close()
	return render(request, 'schedule/station_list.html', {'station_list': maininfo})

def station(request, station):
	with open('schedule/train_list.json', 'r', encoding='utf-8') as f:
		data = json.load(f)
		f.close()
	arrival = []
	departure = []
	for train in data:
		if train['departure'] == station:
			departure.append(train)
		if train['arrival'] == station:
			arrival.append(train)
	return render(request, 'schedule/station_info.html', {'departure': departure, 'arrival': arrival, 'station': station})

def train(request, t_id):
	with open('schedule/train_list.json', 'r', encoding='utf-8') as f:
		data = json.load(f)
		f.close()
	info = []
	for trip in data:
		if trip['id'] == t_id:
			info.append(trip)
	return render(request, 'schedule/train.html', {'info': info})

def login(request):
	return render(request, 'schedule/login.html')

def auth(request):
	if request.POST:
		with open('schedule/admin.json', 'r', encoding='utf-8') as f:
			admin_info = json.load(f)
			f.close()
		for inf in admin_info:
			if inf["login"] == request.POST.get("login") and inf["password"] == request.POST.get("password"):
				return render(request, 'schedule/admin_page.html', {'access': 'admin'})
	return(render, 'schedule/login.html')

def add_train(request):
	if request.POST:
		t_id = request.POST.get("train_id")
		model = request.POST.get("train_model")
		t_type = request.POST.get("train_type")
		arrival = request.POST.get("train_arrival")
		departure = request.POST.get("train_departure")
		arrival_date = request.POST.get("train_arrival_date")
		departure_date = request.POST.get("train_departure_date")

		data = {
        	"id" : t_id,
        	"model": model,
        	"type": t_type,
        	"arrival": arrival,
        	"departure": departure,
        	"arrival_date": arrival_date,
        	"departure_date": departure_date
        }

		with open('schedule/train_list.json', 'r', encoding='utf-8') as f:
			maininfo = json.load(f)
			f.close()

		with open('schedule/train_list.json', 'w', encoding='utf-8') as f:
			maininfo.append(data)
			f.write(json.dumps(maininfo, indent=4))
			f.close()
		return render(request, 'schedule/admin_page.html', {'access': 'admin'})
	return render(request, 'schedule/login.html')

def add_station(request):
	if request.POST:
		name = request.POST.get('station_name')
		info = request.POST.get('station_info')

		station = {
			"name": name,
			"info": info
		}

		with open('schedule/station_list.json', 'r', encoding='utf-8') as f:
			info = json.load(f)
			f.close()
		with open('schedule/station_list.json', 'w', encoding='utf-8') as f:
			info.append(station)
			f.write(json.dumps(info, indent=4))
			f.close()
		return render(request, 'schedule/admin_page.html', {'access': 'admin'})
	return render(request, 'schedule/login.html')

def edit_train(request):
	if request.POST:
		t_id = request.POST.get("train_id")
		model = request.POST.get("train_model")
		t_type = request.POST.get("train_type")
		arrival = request.POST.get("train_arrival")
		departure = request.POST.get("train_departure")
		arrival_date = request.POST.get("train_arrival_date")
		departure_date = request.POST.get("train_departure_date")

		with open('schedule/train_list.json', 'r', encoding='utf-8') as f:
			info = json.load(f)
			f.close()

		for train in info:
			if train['id'] == t_id:
				train['model'] = model
				train['type'] = t_type
				train['arrival'] = arrival
				train['departure'] = departure
				train['arrival_date'] = arrival_date
				train['departure_date'] = departure_date

		with open('schedule/train_list.json', 'w', encoding='utf-8') as f:
			f.write(json.dumps(info, indent=4))
			f.close()
		return render(request, 'schedule/admin_page.html', {'access': 'admin'})
	return render(request, 'schedule/login.html')
