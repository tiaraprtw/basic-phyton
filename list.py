#data set list mengandung bbp variable, bisa juga diulang2 fungsinya
#list biasanya simbolnya [], kalo set {}

mylist = [1, 2, 3 ,4, 5]
print(mylist)
#kalo mau nambahin data  baru, pake fungsi append
mylist.append(6)
mylist.append(10)
#print(mylist)
#print(mylist[6])

#mylist2= []
#mylist2.append("aduh")
#mylist2.append("ngantuk")
#print(mylist2)
#misal mau ngeprint nya satu2, pake fungsi forloop
for x in mylist:
    print("nilai"+str(x))