# with open("learning/read-write-files/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("learning/read-write-files/my_file.txt", mode="w") as file:
    file.write("Hello Eli")
    contents = file.read()
    print(contents)