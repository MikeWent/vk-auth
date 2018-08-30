#!/usr/bin/env python3

import getpass

import requests

login = input("Enter login (email/phone): ")
password = getpass.getpass("Enter password: ")
code = input("2FA-code (leave empty if disabled): ")

clients = (
    (2274003, "hHbZxrka2uZ6jB1inYsH", "Android"),
    (3140623, "VeWdmVclDCtn6ihuP1nt", "iPhone"),
    (3682744, "mY6CDUswIVdJLCD3j15n", "iPad"),
    (3502557, "PEObAuQi6KloPM4T30DV", "Windows Phone"),
    (5027722, "Skg1Tn1r2qEbbZIAJMx3", "VK Messenger"),
    (2685278, "lxhD8OD7dMsqtXIm5IUY", "Kate Mobile"),
    (4580399, "wYavpq94flrP3ERHO4qQ", "Snapster"),
    (3469984, "kc8eckM3jrRj8mHWl9zQ", "Lynt"),
    (3697615, "AlVXZFMUqyrnABp8ncuU", "Windows"),
    (2037484, "gpfDXet2gdGTsvOs7MbL", "Symbian"),
    (3032107, "NOmHf1JNKONiIG5zPJUu", "BlackBerry")
)

for n, client in enumerate(clients, start=1):
    print(n, ". ", client[2], sep="")

selected = int(input("Enter app number: "))-1
client_id = clients[selected][0]
client_secret = clients[selected][1]

auth_test = requests.get("https://oauth.vk.com/token", params={
    "grant_type": "password",
    "scope": "all",
    "client_id": client_id,
    "client_secret": client_secret,
    "2fa_supported": True,
    "username": login,
    "password": password,
    "code": code,
})
response = auth_test.json()

if not response.get("access_token"):
    print("VK error: {}".format(response.get("error_description")))
    exit(1)

access_token = response.get("access_token")
with open("access_token.txt", "w") as f:
    f.write(access_token)

print("Success! Token saved to access_token.txt")
