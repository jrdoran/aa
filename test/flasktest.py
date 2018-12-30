
import requests
print ("jd starting ")

session = requests.Session()
session.trust_env = False
# ret = session.get(url, json=my_json)

print(requests.get('http://127.0.0.1:8080/create').json())
print(requests.get('http://127.0.0.1:8080/increment').json())


print(requests.get('http://127.0.0.1:8080/increment').json())
print(requests.get('http://127.0.0.1:8080/read').json())
print(requests.get('http://127.0.0.1:8080/increment').json())

print(requests.get('http://127.0.0.1:8080/create').json())
print(requests.get('http://127.0.0.1:8080/read').json())
