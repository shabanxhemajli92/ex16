# shoping_list = ['bananas', 'apples', 'aple','milk']
# for item in range(len(shoping_list)):
#     if shoping_list[item] in ['bananas', 'apples', 'aple','milk']:
#         shoping_list[item] = 'bananas,apples,aple,milk'
# print(shoping_list)

l = ['bananas', 'apples', 'milk']
  
# replace Pant with Ishan
l = list(map(lambda x: x.replace('Pant,Ishan,milk'), l))
  
# print list
print(l)
