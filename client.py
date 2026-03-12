import requests


# response = requests.post("http://127.0.0.1:5000/adv/",
#                          json={"title": "bike", "description": "it's a new one", "author": "Andy"}
#                          )
# print(response.status_code)
# print(response.json())
#

# response = requests.get("http://127.0.0.1:5000/adv/8")
# print(response.status_code)
# print(response.json())

response = requests.delete("http://127.0.0.1:5000/adv/8")
print(response.status_code)
print(response.json())