# # # # # # # # # # # # # # # name = input("enter ur name:")
# # # # # # # # # # # # # # # print(name.lower())



# # # # # # # # # # # # # # color = input("enter fav color:")
# # # # # # # # # # # # # # print(color.upper())



# # # # # # # # # # # # # city = input("enter ur city:")
# # # # # # # # # # # # # print(city.capitalize())


# # # # # # # # # # # # email = "student@university.ge"
# # # # # # # # # # # # print(email.index("@"))

# # # # # # # # # # # word = "Programming" 
# # # # # # # # # # # print(word.find("r"))


# # # # # # # # # # sentence = "მე მიყვარს ვაშლი და მსხალი."
# # # # # # # # # # print(sentence.find("ბანანი"))


# # # # # # # # # info = "Error 404: Page not found"
# # # # # # # # # print(info.find("404"))


# # # # # # # # url = "https://www.google.com" 
# # # # # # # # print(url.startswith("https://"))


# # # # # # # phone = "+995555123456"
# # # # # # # print(phone.startswith("+995"))

# # # # # # filename = "document.pdf"
# # # # # # print(filename.endswith(".pdf"))


# # # # # sent = input("enter a sentence:")
# # # # # print(sent.endswith("?"))


# # # # word = "abracadabra"
# # # # print(word.count("a"))

# # # data = "100110101011"
# # # print(data.count("1"))


# # products = "პური,რძე,კვერცხი,ყველი"
# # print(products.split(","))


# word = "hello world"
# print(word.len())


log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"

is_error = log_record.startswith(">ERROR:")

print(f"aris er erroris logi? - + is_error")

print(log_record.endswith("#urgent"))

print(log_record.count("#backup"))

print(log_record.index("failed"))

print(log_record.find("@"))