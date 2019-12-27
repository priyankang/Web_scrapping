from bs4 import BeautifulSoup
import requests
import pprint
import json
import os
import time
import csv
import random
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
# pprint.pprint(scraped_data)

#*******************4th_task*********************************

# url_2="https://www.imdb.com/title/tt3417422/https:/"
def scrap_movie_details(movie_url):
    # print(movie_url)
    # random_sleep=random.randint(1,3)
    # time.sleep(random_sleep)
    #Task_8
    movie_id = ""
    for _id in movie_url[27:]:
        if '/'not in _id:
            movie_id+=_id
        else:
            break
    file_name=movie_id+'.json'
    text = None
    if os.path.exists(file_name):
        print("---------------------------------------------------")
        with open (file_name,"r") as file:
            text=file.read()
            # jdata=json.dumps(text)
            return text
    if text is None:
        print("==================")

        # Task 9th******
       

        data_dic={}
        # list_data=[]
        # for i in movie_url:
        #     print (i)sssssss
       #     # movie_url=i["url"]
        #     # print (movie_url)
        store=requests.get(movie_url)
        # pprint.pprint (store.text)
        soup_2 = BeautifulSoup(store.text,'html.parser')
        # print (soup_2)
        # main_two=soup_2.find("div",class_="wrapper")
        movie_div=soup_2.find("div",class_="title_wrapper").h1.get_text()
        splitlist= movie_div.split()
        splitlist.remove(splitlist[-1])
        movie_name=" ".join(splitlist)
        # print(movie_div[0:5])
        director=soup_2.find("div",class_="credit_summary_item").a.get_text()
        # print(director)
        summary=soup_2.find("div",class_="plot_summary")
        movie_bio=summary.find("div",class_="summary_text").get_text().strip()
        # print(movie_bio)
        director=summary.find("div",class_="credit_summary_item")
        director_list=director.find_all("a")
        director_name=[]
        for i in director_list:
            movie_director=i.get_text()
            director_name.append(movie_director)
            # print(director_name)
            country=soup_2.find("div",attrs={"class":"article","id":"titleDetails"})
            country_name=country.find_all("div",class_="txt-block")
            language_list=[]
            for i in country_name[0:5]:
                head=i.h4.get_text()
                if(head=="Country:"):
                    text=i.find("a").get_text()
                    # print(text)
                elif(head=="Language:"):
                    languages=i.find_all("a")
                    for i in languages:
                        next=i.get_text()
                        language_list.append(next)
                        # print(language_list)
                


        genre=soup_2.find("div",class_="subtext")
        genre_name=genre.find_all("a")
        genre_name.pop()
        genre_list=[]
        for i in genre_name:
                # print (i)
            main=i.get_text()
            genre_list.append(main)
            # print (genre_list)        
        movie_poster=soup_2.find("div",class_="poster").a["href"]
        movie_poster_link="https://www.imdb.com"+movie_poster
        # print(movie_poster_link)
        time=soup_2.find('div',class_="title_block")
        sub_runtime=soup_2.find("div",class_="subtext")
        runtime=sub_runtime.find("time").get_text().strip()
        # print(runtime)
        st=str(runtime)
        minut=int(st[0])*60
        # movie_runtime=str(0)
        if "min" in runtime:
            min1=int(runtime[3:].strip("min"))
            minut1=minut+min1
        else:
            minut1=minut
        # print(minut1)
        data_dic["name"]=(movie_name)
        data_dic["director"]=director_name
        data_dic["country"]=text
        data_dic["language"]=language_list
        data_dic["poster_image_url"]= movie_poster_link
        data_dic["bio"]=movie_bio
        data_dic["runtime"]=minut1
        data_dic["genre"]=genre_list
        # list_data.append(data_dic)
        # # return (list_data)
        # return data_dic
        file1 = open(file_name, 'w')
        raw = json.dumps(data_dic)
        # return(type(data_dic))
        file1.write(raw)
        file1.close()
        return(data_dic)

    # pprint.pprint(scrap_movie_details(url_2))
url_2 = scraped_data[4]['url']
mobile=scrap_movie_details(url_2)
    # pprint.pprint(movies_url2)
pprint.pprint(mobile)

##Task_5th ************
# def get_movie_list_details(top_list):
#         movies_detail_list=[]
#         for i in top_list:
#             url=i["url"]
#             movies_store=scrap_movie_details(url)
#             movies_detail_list.append(movies_store)
#         return movies_detail_list
# top_movies = scrape_top_list()
# movies_detail_list = get_movie_list_details(top_movies[:10])
# pprint.pprint(movies_detail_list)
# # movies_list= movies_detail_list