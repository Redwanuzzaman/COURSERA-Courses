# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]


# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = []
#
# for files in filenames:
#     if files.endswith(".hpp"):
#         idx = files.index(".hpp")
#         newfilenames.append(files[:idx] + ".h")
#     else:
#         newfilenames.append(files)
#
# print(newfilenames)


# def pig_latin(text):
#     say = ""
#     # Separate the text into words
#     words = text.split()
#     for word in words:
#         say += word[1:] + word[0] + "ay "
#     return say.strip()
#
#
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


# def group_list(group, users):
#   members = ""
#   for i in users:
#     members += i + ", "
#   return "{}: {}".format(group, members[:len(members)-2])
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"


# def guest_list(guests):
#     for person in guests:
#         name, age, profession = person
#         print("{} is {} years old and works as {}".format(name, age, profession))
# 
# 
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
