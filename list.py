array = [i for i in range(20) if i%2==1]
print(array)

a = [i for i in range(5)]
a.append(1)
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
a.insert(3, 5)
print(a)
print(a.count(1))
a.remove(2)
print(a)

a = [1,2,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print(result)