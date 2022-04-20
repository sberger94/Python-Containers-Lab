# Exercise 1
students = ['Steve', 'Sally', 'Legolas', 'Mike', 'Morlock']

print(students[1])
print(students[-1])

# Exercise 2
foods = ('gruel', 'slop', 'mash', 'mush', 'feed')
for food in foods:
  print(f"{food} is a good food")

# Exercise 3
for food in foods[3:]:
  print(food)

# Exercise 4
home_town = {
  'city': 'Denver',
  'state': 'Colorado',
  'population': 705756
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5
for key, val in home_town.items():
  print(f"{key} = {val}")

# Exercise 6
cohort = []
for i in range(len(students)):
  cohort.append({
    'student': students[i],
    'fav_food': foods[i]
  })

for entry in cohort:
  print(entry)

# Exercise 7
awesome_students = [name + ' is awesome!' for name in students]

for awesomeness in awesome_students:
    print(awesomeness)

# Exercise 8
a_foods = [food for food in foods if 'a' in food]

for item in a_foods:
    print(item)
    