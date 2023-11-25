
mylist = ["A","B","C","D","E"]
print(mylist)

def swaplist(mylist):
    mylist[1],mylist[-1]=mylist[-1],mylist[1]
    return mylist
swaplist(mylist)
print(mylist)