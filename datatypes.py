# a=2
# b=3.98
# c=1j
# d='khadeeja'
# e=' beevi'
mylist1=["apple",(1,1.4)]  #tuple inside list
mylist2=["apple",[1,1.4]] 
print(mylist2[0])
mylist3=list(("apple","banana","grapes"))
mytuple=("apple","banana","grapes")
myset={"apple","banana","grapes"}
# print(a+b)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print('my name is '+ d+e)
print(mylist1)
print(mylist2)
print(mylist3)
print(mytuple)
print(myset)

k={'student1':{
    'name':'khadeeja',
    'age':22,
    'marks':{
        'maths':46,
        'english':89,
        'cs':90
    }},
   'student2' :{
       'name':'khadeeja',
    'age':22,
    'marks':{
        'maths':46,
        'english':89,
        'cs':90
   }
   }
}

# print(k['student1']) #take data from each key , use get or []
# print(k.get('student1'))
# print(k.get('student1').get('marks'))

# #update a field in dictionary
# k['name']='kavya'
# del k['marks']

# len() # display the length of the list

l1=[5,3,0,2]
l2=l1.copy()
print(l1)
l1.append(7)
print(l2)

set1={1,2,3,4,5}
set2={'a','b','c','d',4,5,6,8}
print(set1)
print(set2)