#name = input("enter name:")

#for i in name:
    #if i == "d":
        #print("sybau")
    #else:
        #print("it's fine")               #nevermind, got cooked#


weather = input("enter weather:")

for i in weather:
    if i == "მზიანი":
        print("ვივარჯიშებ გარეთ")
    elif i == "მოღრუბლული":
        print("ვივარჯიშებ გარეთ ოღონდ მოგვიანებით")
    else:
        print("საერთოდ არ ვივარჯიშებ დღეს")
        break



for i in range(1, 1000):
    if i == 461:
        print("this is it")
        break
    else:
        print("nooo")


for i in range(1, 100):
    if i % 2 == 0:
        if i % 3 == 0:
            if i % 5 == 0:
                print(i)
                break
    else:
        continue