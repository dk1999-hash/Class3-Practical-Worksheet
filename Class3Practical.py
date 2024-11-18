#Question1 
names = ["Jim", "Hetty", "Kirsten", "Theo", "Henry", "Paul"]
grouped = {}

for name in names:
    if name[0] not in grouped: #name[0] is the first element WITHIN the string
        grouped[name[0]]=[]
    grouped[name[0]].append(name)
    
    
print(grouped)

#Question2 swapping dictionaries from key value to value key
my_dict = {"computer" : "apple", "model" : "macbook pro", "processor" 
           : "M1 Pro", "year" : "2021"}
inverted_dict = {}
for key, value in my_dict.items():
    inverted_dict[value]=key
    
print(inverted_dict)

#Question 3 assessed
 
table = [[] for _ in range(10)]
index=hash("Deniz Korkmaz")%len(table)
table[index]=[]
table[index].append(["Deniz Korkmaz",99])
print(table)