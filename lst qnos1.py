# l=[]
# for i in range(-5,6):
#     if i%2==0:
#         i=i**2
#         l.append(i)
#     else:
#         i=i**3
#         l.append(i)
# print(l)

# lst=[i**2 if i%2==0 else i**3 for i in range(1,11)]
# print(lst)

# lst1=["apple","banana","mango"]
# l=[i[::-1] for i in lst1]
# print(l)
# print(lst1)

# l1=[i for i in range(0,101) if i%3==0 and i%5==0 ]
# print(l1)

# str="hello world"
# c=[i for i in str if i.isalpha()]
# print(c)

# l1="this is a python program"
# l2=[len(i) for i in l1.split()]
# print(l2)

l=[i for i in range(1,21) if i%2==0]
print(l)