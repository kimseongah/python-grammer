data = dict()
data['사과'] = 'Apple'
data['바나나']='Banana'
data['코코넛']='Coconut'

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
key_list = list(key_list)
print(key_list)
for key in key_list:
    print(data[key])

