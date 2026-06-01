num_1 = int(input("enter num1:"))
num_2 = int(input("enter num2:"))
num_3 = int(input("enter num3:"))

if num_1 > num_2 and num_1 > num_3:
    print(f"{num_1} is the biggest number!")
elif num_2 > num_1 and num_2 > num_3:
    print(f"{num_2} is the biggest number!")
elif num_3 > num_1 and num_3 > num_2:
    print(f"{num_3} is the biggest number!")
