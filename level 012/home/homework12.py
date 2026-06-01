age = int(input("enter your age:"))

if age > 0 and age < 12:
    print("bavshvi xar")
elif age > 13 and age < 19:
    print("teenager xar")
elif age > 19 and age < 64:
    print("adult xar")
elif age > 64 and age < 120:
    print("xanshi shesuli xart")
elif age > 120:
    print("wizard an witch xar!")
elif age < 0:
    print("incorrect info")