
import requests

while True:
    query = input("Input adress name ... ")
    url = f"http://ip-api.com/json/{query}"
    res = requests.get (url)
    data = res.json()
    if data["status"] == "success":
        print ("\n")
        print ("~" * 25)
        print ("Country: ", data['country'] )
        print ("~" * 25)
        print ("Name: ", data['isp'] )
        print ("~" * 25)
        print ("Query: ", data['query'] )
        print ("\n")
    else:
        print("These adress Not found")
    continue_programm = input("Continue - y/n >>> ")
    if continue_programm == "y":
        continue
    else:
        break



