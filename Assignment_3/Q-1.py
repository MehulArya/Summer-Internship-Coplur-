#Dictionary
dict1 = {1:"Python", 2:"CPP",  3:"Java", 'name' : "Programming Language", 4: {1: "assembly", 2: "Syscall", 'name': "Low Level Languages"}}
print(dict1['name'])
print(dict1[3])
print(dict1[4])
print(dict1[4][2])
print(dict1)
print(type(dict1))
dict1[5] = "python"
print(dict1)
dict1[6] = {1: "Data Analytics", 2: "Web Development", 3: "System Design"}
print(dict1)
print(dict1[6])
del(dict1[3])
print(dict1)
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.keys())
dict2.pop(1)
print(dict2)
dict2.popitem()
print(dict2)
dict1[1] = "python"
print(dict1)
dict1.update(dict2)
print(dict1)


# Tuple
t = (10,20,30,40,10)
print(t)
print(type(t))
for i in t:
    print(i)
t1 = (0, 1, 2, 3)
t2 = (4, 5, 6, 7, True, False)
print(t1 + t2)
t3 = (t1,t2)
print(t3)
t4 = ("xyz ")*3
print(t4)

t = (0,1,2,3)
print(t[1:])
print(t[1:3])
print(t[::-1])

t = (0,1)
del t

lst = [0, 1, 2, 3]
t = tuple(lst)
print(t)
print(min(t))
print(max(t))
print(t.count(0))
print(t.index(3))
print(sum(t))

#Set
a = {"d", "c", "b", "a"}
b = {1, 2, 3}
print(a)
print(b)
print(type(a))
a.add("e")
print("String a after add e: ", a)
c = a.union(b)
print("String a union with b: ", c)
d = a | b
print(d)
print("String d intersection b: ", d.intersection(b))
print(d & b)
d.add(4)
print(d)