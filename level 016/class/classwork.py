#numbers = [10, 20, 30, 40, 50, 60, 70]

#print(numbers [:3])



#text = "Hello, World!"

#print(text[:5])


#colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "შავი"]

#print(colors[-1])
#print(colors[-2])




#short_nums = [1,2,3,4,90,8,72,31,74]

#for i in short_nums:
    #print(sum(short_nums))
    #break


#get_highets = [90,81,100,23,3,98,102,90,75]

#for i in get_highets:
    #print(max(get_highets))
    #break


highest = 0

get_highets = [90,81,100,23,3,98,102,90,75]

for i in get_highets:
    if i > highest:
        highest = i

print(highest)