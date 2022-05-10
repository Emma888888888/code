#list
list=[]
list.append("orange")
print(list)

list1=["orange","grape","apple"]
list += list1
print(list)

list.pop(-1)
print(list)

list.remove("orange")
print(list)

list2=["emma","hannah"]
list.extend(list2)
print(list)

position=list.index("emma")
print(position)

print(list.index("emma"))

#dictionary
dictionary={'name':'emma','gender':10,'grade':2}
print(dictionary)

dictionary['suburb']='sunnybank'
dictionary1={'postcode':4109}
dictionary.update(dictionary1)
print(dictionary)

print(len(dictionary))

dictionary.pop('postcode')
print(dictionary)

print(dictionary.get('name'))

a=dictionary.items()
print(a)

print(dictionary)
print(dictionary.popitem())
print(dictionary)
dictionary[1]='makeup'
print(dictionary)

# print(dictionary.pop(1))
# print(dictionary)

print(dictionary.pop(2,'hannah'))

print(dictionary.values())

print(dictionary.keys())