# file = open("my_file.txt")
# contents = file.read()
# print(contents)

# Another way of achieving the same as above

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
#
# with open("my_file.txt", mode='a') as file:
#     file.write("\nNew line written in python")
#
# with open("new_file.txt", mode="a") as file:
#     file.write("\nthis is the new file")
