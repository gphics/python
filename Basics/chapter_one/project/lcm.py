# finding the least common factor (lcm)
first_number = int(input("type in the first number "))
second_number = int(input("type in the second number "))

greatest = 0
if first_number >= second_number:
    greatest = first_number


else:
    greatest = second_number


while greatest <= (first_number * second_number):
    if greatest % first_number == 0 and greatest % second_number == 0:
        print(f"the lcm of {first_number} and {second_number} is {greatest}")
        break
    else:
        greatest += 1
