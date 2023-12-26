

# dicts = {
#     "bug" : "A error in programm that prevents program to run",
#     "function": "A piece of code you can easly call over and over again",
#     "Loop": "The actions of doing something over and over gain"
    
# }


# #Accessing values
# print(dicts["bug"])


# #Edit an Item 

# dicts["bug"] =  ""


# # Loop thrue a dictionary
# for key in dicts:
#     print(key)
#     print(dicts[key])
    
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇

# for student in student_scores:
#     grade = ""
#     if student_scores[student] > 91 and student_scores[student] <= 100:
#         grade = "Outstanding"
#     if student_scores[student] >= 81 and student_scores[student] <= 90:
#         grade = "Exceeds Expectations"
#     if student_scores[student] > 71 and student_scores[student] <= 80:
#           grade = "Exceeds Expectations"
#     if student_scores[student] <= 70 :
#          grade = "fail"
                   
#     student_grades[student] = grade


# # 🚨 Don't change the code below 👇
# print(student_grades)



# Nested Lists  in a Dictnories

# capitals = {
#     "France" :[ "Paris", "lille" "dijon"],
#     "Germany": "Berlin",
# }





country = "Brazil" # Add country name
visits = 12 # Number of visits
list_of_cities = ["cambodia","brazil"] # create list from formatted string

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
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(country,visits,list_of_cities):
    print(country)
    print(visits)
    print(list_of_cities)
  
    travel_log.append({
        "country" : country,
        "visits" : visits,
        "cities": ["00","003","004"]
    }) 

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")









