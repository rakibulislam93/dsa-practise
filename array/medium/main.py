
# mystr = ["rakib", "sajib", "emon", "jamal", "karim"]
# mylist = []
# for name in mystr:
#     if name.startswith("j"):
#         mylist.append(name)


# print(mylist)

mydict = {}

mylist = ["rakib", "sajib", "emon", "jamal", "karim"]

for i in range(len(mylist)):
    mydict[mylist[i]] = mylist[i]


print(mydict)