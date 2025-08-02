# Dictionary and sets
# dict={
#     "name":"siri",
#     "class":14,
#     "age":19
# }
# print(dict)#{'name': 'siri', 'class': 14, 'age': 19}
# print(dict["name"])#siri
# dict["name"]="giri"
# print(dict)# {'name': 'giri', 'class': 14, 'age': 19}
#  it can also store tuples and lists and can also add diff dicts
# Nested Dictionary 
# info={
#     "name": "siri",
#     "marks":{
#         "maths":99,
#         "physics":98,
#         "chemistry":100

#     },
#     "university":"sandip university"

# } 
# print(info["marks"]["chemistry"])
# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("name")) 
# info.update({"class":14}) # udate method is different
# print(info)
# sets 
# repeated items are stored only once 
# collection={1,3,4,5,5,5,"siri","venu"}
# print(collection)
# print(len(collection))
# empty set set()
# tuples are passed through set but lists are not passed
# nums={3,5,6,78,9}
# nums.clear()
# print(nums) # set()
# union
# setA={1,4,5,6745,78}
# setB={"SIRI","HARI","VENU"}
# print(setA | setB) 
# print( setA.union(setB))
