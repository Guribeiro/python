import requests
import json

username = str(input('Digite seu username no github: '))

api = requests.get(f'https://api.github.com/users/{username}')

userdata = json.loads(api.text)

htmlurl = userdata['html_url']
usertype = userdata['type']
nome = userdata['name']
email = userdata['email']
bio = userdata['bio']
avatar = userdata['avatar_url']
print(userdata)
print(f'Username: {username}\nEmail: {email}\nBio: {bio}\nAvatar: {avatar}')

#Teste rápido e mal construído