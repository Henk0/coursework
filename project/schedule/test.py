import json

with open('train_list.json', 'r', encoding='utf-8') as f:
	station = "Saint-Petersburg"
	json = json.load(f)
	f.close()
	arrival = []
	departure = []
	for train in json:
		if train['departure'] == station:
			departure.append(train)
		if train['arrival'] == station:
			arrival.append(train)
print(arrival)