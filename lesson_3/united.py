import csv
import json
import operator
import gpxpy.geo

with open('data.csv', 'r', encoding='windows 1251') as data_file:
    fields = ["ID", "Name", "Longitude_WGS84", "Latitude_WGS84", "Street", "AdmArea", "District", 
              "RouteNumbers", "StationName", "Direction", "Pavilion", "OperatingOrgName", "EntryState", 
              "global_id", "geoData"]
    bus_stops = {}
    reader = csv.DictReader(data_file, fields, delimiter=';')
    for row in reader:
        bus_stops[row["ID"]] = (row["Latitude_WGS84"], row["Longitude_WGS84"])

stations = {}
with open('metro.json', 'r', encoding='windows 1251') as data_file:
    stations_data = json.load(data_file)
    for station_data in stations_data:
        stations[station_data["global_id"]] = (station_data["NameOfStation"], station_data["Latitude_WGS84"], station_data["Longitude_WGS84"])

number_of_stops = {}
for station in stations.values():

    nearest_stops = []
    for stop in bus_stops.values():
        try:
            if gpxpy.geo.haversine_distance(float(stop[0]), float(stop[1]), float(station[1]), float(station[2])) <= 500:
                nearest_stops.append(stop)
        except:
            pass
    number_of_stops.setdefault(station[0], 0)
    number_of_stops[station[0]] += len(nearest_stops)
print(number_of_stops)

max_value = max(number_of_stops.items(), key=operator.itemgetter(1))
print(max_value)
