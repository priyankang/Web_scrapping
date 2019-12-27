from bs4 import BeautifulSoup
import requests
import pprint
url = "https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles"
response=requests.get(url)
# print(response)
# print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
main_div = soup.find ('div', class_='a-fixed-left-grid-col a-col-right')
# print(main_div)
div=main_div.find_all('div',class_='crwBucket')
# mobile = main_div.find("div",class_="crwTitle").a.get_text()
# price=main_div.find("div",class_="crwPrice").span.get_text()
# rating=main_div.find("div",class_="crwProductDetail").span.get_text()
# link=main_div.find("div",class_="crwProductImage").a.get_text()[Src]

# print(rating)
# print(price)
# print(mobile)
# print(link)



# # print(div)
list1=[]
count=0

for i in div:
    my_dict = {}
    mobile = i.find("div",class_="crwTitle").a.get_text()
    price=i.find("span",class_="crwActualPrice").span.get_text()
    rating=i.find("span",class_="a-size-small").a.get_text()
    link=i.find("div",class_="crwProductImage").a["href"]
    position=i.find("div",class_="crwRank").get_text()
    count=count+1
    # print(count)

    my_dict['position']=count
    my_dict['name'] =mobile
    my_dict['price']=price
    my_dict['rating']=rating
    my_dict['link'] =link
    # print(my_dict)
    list1.append(my_dict)   
pprint.pprint(list1)

