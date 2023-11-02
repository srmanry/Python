from operator import index


numberlist = [1,2,3,4,5,6,7,8,9]
# print(numberlist)

"""
print(len(numberlist))
print(type(numberlist))
print(numberlist[0])
print(numberlist[-1])
print(numberlist[+1])
print(numberlist[5])
"""


thislist = list(("apple", "banana", "cherry"))
# print(thislist)

namelist = list(("A","B","C","D"))
"""
print(namelist)
print(namelist[-1])
print(namelist[+1])
print(namelist [1:])
print("a" is namelist)
print("A" is namelist)
print("a" is not namelist)
print("A" is not namelist)
print(namelist +["E","F","G","H",7])
print(f"{namelist} Add the number")
print(namelist *2)
"""
# list Insert******************
listappend = ["E","F","G",] 
# print(listappend)
# listappend.append("H")
# print(listappend)
# listappend.insert(0,"I")
# print(listappend),
listext = ["F","G","E",] 
listextend = ["L","J","M","L","E"]
listext.extend(listextend)
print(f" Extend Keyword == {listext}")
print(len(listext))
listext.sort()
print(f"List sort == {listext}")
listext.reverse()
print(f"List reverse == {listext}")
itemcount = listext.count("E")
print(f" itemCount == {itemcount}")
itemcount = listext.index("M")
print(f" Item Index Number  == {itemcount}")




# print(namelist +3)
# print(len(namelist))

