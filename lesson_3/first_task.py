import csv
import operator


with open('data.csv', 'r', encoding='windows 1251') as data_file:
    fields = ["ID", "Name", "Longitude_WGS84", "Latitude_WGS84", "Street", "AdmArea", "District", 
              "RouteNumbers", "StationName", "Direction", "Pavilion", "OperatingOrgName", "EntryState", 
              "global_id", "geoData"]
    number_of_stop = 0
    streets = {}
    reader = csv.DictReader(data_file, fields, delimiter=';')
    for row in reader:
        number_of_stop += 1
        streets.setdefault(row["Street"], 0)
        streets[row["Street"]] += 1
print("Всего остановок - {}".format(number_of_stop))
max_value = max(streets.items(), key=operator.itemgetter(1))
print(max_value)

