import pandas as pd
excel_data=pd.read_excel(r'G:\Program Guru\pythonprogram\bmi_data.xlsx')#path to excel sheet
print(excel_data)
df=pd.DataFrame(excel_data,columns=['Height','Weight',"Size"])
list1=excel_data['Height'].tolist()
list2=excel_data['Weight'].tolist()
list3=excel_data['Size'].tolist()
print("List1 is: ",list1)
print("List2 is: ",list2)
print("List3 is: ",list3)
n1=int(input("Enter height: "))
n2=int(input("Enter weight: "))
print("Your prediction is under process....")
#n3?
s1=[]
for i in range(0,len(df)):
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
