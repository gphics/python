"""
    getting the age of a user and allowing the user to vote
    if the age is up to satisfaction
"""

vote_info = """
    cast your vote:
    1) Dr Mustapha
    2) Dr Francis
    3) Dr Okandeji
"""

user_name = input("what is your name ? ")
print("saving in progress ....")
print("saved ...")

user_age = int(input("how old are you ?"))
print("saving in progress ....")
print("saved ...")


if user_age == 0:
    print("bad response")
    user_age = int(input("how old are you ?"))
if user_age < 18:
    print("you are not eligible to vote")
else:
    vote = input(vote_info)
    print("you have successfully voted your candidate")
"""
# loops
"""
i = 45
while i <= 200:
    if i % 18 == 0 and not i == 54:
        print(f"{i} is divisible by 18")
        break
    else:
        i += 1

