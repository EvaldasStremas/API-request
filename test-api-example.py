import requests

urls = []

file_data = open('url.txt','r') 
for line in file_data: 
    urls.append(str(line))

# for num in range(len(urls)):
#     print(urls[num])
    
print(urls[0])
r = requests.get(urls[0])

# print(r.text)

# # r.status_code
# # r.headers
# # r.encoding
# # r.text
# # r.json()

# temp = []
# num = r.text.find('Jutiminė')

# for i in range(11):
#     temp.append(r.text[num+i])
# current_temp = ''.join(temp)

# print(current_temp)

print(r.text)

# def get_temp(r):
#     temp = []
#     num = r.text.find('Jutiminė')

#     for i in range(1000):
#         temp.append(r.text[num+i])
#     current_temp = ''.join(temp)

#     return current_temp

# print(get_temp(r))