# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


w = open("thingscourse.txt", "w")

chapters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

for val in chapters:
    f = open("basiccourse.txt", "r")
    lines = f.readlines()
    for line in lines:
        w.write(line.replace('_', val))
    f.close()
w.close()
