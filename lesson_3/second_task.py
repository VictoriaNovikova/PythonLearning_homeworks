import json

stations = []
with open('metro.json', 'r', encoding='windows 1251') as data_file:
    stations_data = json.load(data_file)
    for station_data in stations_data:
        if station_data["RepairOfEscalators"]:
            stations.append(station_data["NameOfStation"])
print(set(stations))


