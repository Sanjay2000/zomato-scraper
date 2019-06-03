import requests,json
from pprint import pprint 
from bs4 import BeautifulSoup


url="https://www.flipkart.com/search?q=mi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2&as-pos=0&as-type=HISTORY"
page=requests.get(url).text
soup=BeautifulSoup(page,"html.parser")


search=soup.find_all("div",class_="_1UoZlX")
mi_mobile=[]
dict1={}
for j in search:
	name=(j.find("div",class_="_3wU53n").text)
	ratting=j.find("div",class_="hGSR34").getText()
	detail=j.find("ul",class_="vFw0gD").text
	price=j.find("div",class_="_1vC4OE _2rQ-NK").text
	url=("https://www.flipkart.com/"+j.find('a').get("href"))
	dict1["Detail"]=detail
	dict1["Ratting"]=ratting
	dict1["model"]=name
	dict1["price"]=price
	dict1["url"]=url
	mi_mobile.append(dict1)
pprint(mi_mobile)


