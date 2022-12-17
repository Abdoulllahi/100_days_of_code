'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-05 20:37:31
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-05 22:27:33
 # @ Description:
 '''

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, times_visited, cities_visited):
    travel_log.append({"country": country, "visits": times_visited, "cities": cities_visited})

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)