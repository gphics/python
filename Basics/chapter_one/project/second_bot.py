intro = """
on the scale of 1 to 10 
rate your worldly experience
"""
print(intro)
rate = int(input("your rating ... "))

if rate <= 4:
    ans = """
    your experience is too low, 
    you might need to step more into the
     world gaining more experience
    """
    print(ans)
    request = input("would you like to rate again ?. answer with true or false ")

    if request == "true":
        rate = int(input("your rating ... "))
    else:
        print("alright ... ")

elif rate <= 7:
    ans = """
    this is interesting !
    great acheivement
    """
    print(ans)
    request = input("would you like to rate again ?. answer with true or false ")

    if request == "true":
        rate = int(input("your rating ... "))
    else:
        print("alright ... ")

else:
    ans = 'you are indeed a great man'
    print(ans)
    request = input("would you like to rate again ?. answer with true or false ")

    if request == "true":
        rate = int(input("your rating ... "))
    else:
        print("alright ... ")