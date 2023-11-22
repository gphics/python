"""
X = [[1, 2, 3], [4, 2, 3], [8, 6, 4]]
Y = [[4, 9, 3], [6, 1, 3], [4, 2, 4]]
result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for u in range(len(X)):
    for v in range(len(X[0])):
        result[u][v] = X[u][v] + Y[u][v]
    print(result)
"""
"""
movie = {"title": "Battle through the heavens", "age": 12," region": "China", "year": 2011}
movie["region"] = 'Nigeria'
# print(movie["region"])

employees = [
    {"name":"John Mckee", "age":38, "department":"sales"},
    {"name":"Lisa Crawford", "age":29, "department":"marketing"},
    {"name":"Sujan Patel", "age":33, "department":"hr"},
]

for x in range(len(employees)):
    for y in employees[x].items():
        print(y)
"""
"""
weekdays_tuple = ("Monday", "Tuesday")
weekdays_tuple[3] = "poli"
print(weekdays_tuple[0])
"""
"""
num = [1, 2, 3]
alphabelt = ["a", "b", "c"]
employee = {"name": "Gordon", "age": 24}
employer = {"name": "Smith", "age": 54}
adv = zip(employee, employer)
print(dict(adv))
"""

num_set = set(["a", 1, 2, 3, "c", 5, 5, 5, 0])
sec_num_set = {1, "b", 1, 1, 1, 4, 5, 2, 3, 6, 7}
# print(num_set)
joint = num_set.union(sec_num_set)
print(joint)
