import json

# Opening JSON file
f = open('test.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['query']:
    print(i['requestedLine'])
    res=eval(i['requestedLine'])
    i['result']=str(res)
json_object = json.dumps(data, indent=4)
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

f.close()
