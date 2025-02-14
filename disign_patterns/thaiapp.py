from thai import ThaiCitizen
import requests
url = 'https://dummyjson.com/users'
data = requests.get(url).json()
print(data['users'][0])
users = data['users']
thai = []
for user in users:
    u = ThaiCitizen(
        first_name=user['firstName'],
        last_name=user['lastName'],
        image=user['image'],
        country=user['address']['country']
    )
    thai.append(u)

for t in thai:
    print(t.image)
    print(t.first_name)