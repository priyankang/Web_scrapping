from bs4 import BeautifulSoup
import requests
import pprint
url="https://www.imdb.com/india/top-rated-indian-movies/"
# print(url)
response=requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
# print(soup)
def scrape_top_list():
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")
# print(tbody)
#### thead=main_div.find("thead").get_text()
#### print(thead)
#### th=thead.find("th").get_text()
#### print(th)
    list=[]
    count=0
    for i in trs:
        my_dict={}
        th=i.find("td",class_="titleColumn").get_text().strip()
        # print(th)
        movie_name = i.find("td",class_="titleColumn").a.get_text()
        # print(movie_name)
        year= i.find("span",class_="secondaryInfo").get_text().strip()
        # print(year[1:5])
        position= i.find("td",class_="titleColumn1")
        count=count+1
        # print(count)
        ratting= i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        # print(ratting)
        url= i.find("td",class_="titleColumn").a['href']
        # # print(url)
        link="https://www.imdb.com"+url
        # print(link)
        my_dict["movie_name"]=movie_name
        # list.append(my_dict)
        my_dict["position"]=count
        # list.append(my_dict)
        my_dict["year"]=(year[1:5])
        # print (type (my_dict))
        # list.append(my_dict)
        my_dict["ratting"]=ratting
        # list.append(my_dict)
        my_dict["url"]=link
        list.append(my_dict)
        # print(my_dict)
    return list
scraped_data = scrape_top_list()
pprint.pprint(scraped_data)