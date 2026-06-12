#slicing means splitting a list

# fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]

# print(fruits[4])



# numbers = [10, 20, 30, 40, 50]

# numbers[1] = 25

# print(numbers)



# index = int(input("enter number from 0 to 4:"))

# colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

# print(colors[index])




# animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]

# animals[4] = "ship"

# print(animals)


# index = int(input("enter ur index from 0 to 3:"))
# color = input("enter a color:")

# colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

# colors[index] = color

# print(colors)







# numbers_step = [5, 10, 15, 20, 25, 30, 35, 40]

# print(numbers_step[0:8:2])





# fruits = ["ვაშლი", "მსხალი", "ატამი", "ბალი", "ყურძენი", "ბანანი", "ფორთოხალი"]

# print(fruits[2:5])




mixed_nums = [12, 45, 8, 33, 91, 24, 10, 77]

for i in mixed_nums:
    if i % 2 ==0:
        print("even")
        break
    else:
        print("odd")
        break