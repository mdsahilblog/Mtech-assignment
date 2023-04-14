#from operator import itemgetter
listoftuple=[(167,51,"U"),(182,62,"N"),(176,69,"N"),(173,64,"N"),(172,65,"N"),(174,56,"U"),(169,58,"N"),(173,57,"N"),(170,55,"N")]
# U-Underweight, N-NormalWeight
list1,list2,list3,s1=[],[],[],[]

for x,y,z in listoftuple:
    list1.append(x)
    list2.append(y)
    list3.append(z)
print("List1 is: ",list1)
print("List2 is: ",list2)
print("List3 is: ",list3)
n1=int(input("Enter height"))
n2=int(input("Enter weight"))
print("Your prediction is under process....")
#n3?
for i in range(0,len(listoftuple)):
    m1=(n1-list1[i])**2
    m2=(n2-list2[i])**2
    s=(m1+m2)**0.5
    s1.append(s)

print("Euclidean distance is : ",s1)
merging=list(zip(list1,list2,list3,s1))
print("Merging all the lists : ",merging)

item=sorted(merging,key=lambda x:x[3])
print("After sorting : ",item)
k=int(input("enter the value for K : "))
list4,list5,list6,list7=[],[],[],[]
for t,u,v,w in item:
    list4.append(t)
    list5.append(u)
    list6.append(v)
    list7.append(w)
# print(list4)
# print(list5)
# print(list6)
# print(list7)
# convert=tuple(i for i in list6)
convert=list6
print("dependent variable column : ",convert)
items=[]
for i in range(0,k):
    items.append(convert[i])
print("dependent variable upto k no : ",items)
d={}
for i in items:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("The occurrance of each variable in dependent column : ",d)
max_value=max(d,key=d.get)
print("The maximum occurrence of item is or (predicted) for height- ",n1,"and weight- ",n2,"is : ",max_value)
