from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint

driver = webdriver.Chrome()
driver.get("https://www.zomato.com/ncr")


page = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

soup = BeautifulSoup(page,"html.parser")
place_zm = soup.find("div",class_="ui segment row")
a = place_zm.findAll('a')

b=1
name_of_url=[]
for j in a:
	url = (j.get('href'))
	name_of_url.append(url)
	name = j.get('href')[27:-18]
	b+=1
	print(b,name)
user = int(input("please_enter_the_place_namen...=>>"))	

server = webdriver.Chrome()
server.get(name_of_url[user-1])



page1 = server.execute_script("return document.documentElement.outerHTML")
server.quit()

soup1 = BeautifulSoup(page1,"html.parser")
st = soup1.find_all('div',class_="white-bg sub-cat-container mbot")
	

list_of_url=[]
a=1
for k in st:
	url_of_hotel = (k.find("div",class_="ta-right").a["href"])
	name_of_hotel = (k.find("div",class_="fontsize1 semi-bold mt2").text).strip()
	print(a,name_of_hotel)
	a+=1
	list_of_url.append(url_of_hotel)
user1 = int(input('please_enter_the_hotle_name..=>'))

go_to = webdriver.Chrome()
go_to.get(list_of_url[user1-1])


link = go_to.execute_script("return document.documentElement.outerHTML")
go_to.quit()

soup1 = BeautifulSoup(link,"html.parser")
seacrh = soup1.find_all('div',class_="col-s-12")
# dict1={}
for div in seacrh:
	name_div = div.find('a',class_="result-title hover_feedback zred bold ln24 fontsize0")
	hotel_name = (name_div.text)
	ft = (hotel_name.split())
	naa = (",".join(ft))
	# print(naa)
	hi=div.find('a',class_='ln24 search-page-text mr10 zblack search_result_subzone left')
	hotel_name = naa,hi.text
	print(hotel_name)

ratting_votes=soup1.find_all("div",class_="ta-right floating search_result_rating col-s-4 clearfix")
for k in ratting_votes:
	name_= (k.text)
	real = (name_.strip().split())
	ratting_votes = (",".join(real))
	print(ratting_votes)
	

rupes = soup1.find_all("div",class_="res-cost clearfix")
for r in rupes:
	rupay = (r.text)
	print(rupay)

	# print(rupay)
	# print(ratting_votes)
	# print(naa)
	# dict1["hotel_name"]=hotel_name
	# dict1["ratting_votes"]=ratting_votes
	# dict1["rupes"]=rupay
	# pprint(dict1)

				















	





