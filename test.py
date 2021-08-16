import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 20, "name": "The Rock", "views": 13},
#         {"likes": 4420, "name": "stupid", "views": 13145},
#         {"likes": 2, "name": "my wife", "views": 1}]

# for i in range(len(data)):
#     response = requests.put(
#         BASE + "video/" + str(i), data[i])
#     print(response.json())


# input()
# response = requests.patch(
#     BASE + "video/2", {"views": 100000, "name": "My hot wife"})
# print(response.json())

# input()

# response = requests.get(BASE + "video/2")
# print(response.json())
response = requests.delete(
    BASE + "video/2"
)
input()
response = requests.get(BASE + "video/2")
print(response.json())
