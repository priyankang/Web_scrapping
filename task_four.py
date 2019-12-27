from task_third import *
url_2="https://www.imdb.com/title/tt0986264/"
def scrap_movie_details(movie_url):
    data_dic={}
    # list_data=[]
    # for i in movie_url:
    #     print (i)
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
    # director=soup_2.find("div",class_="credit_summary_item").a.get_text()
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
    # genre=soup_2.find("div",attrs={"class":"article","id":"titleStoryLine"})
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
    # time=soup_2.find('div',class_="title_block")
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
    # return (list_data)
    return data_dic
# pprint.pprint(scrap_movie_details(url_2))
movies_url2=(scrap_movie_details(url_2))
pprint.pprint(movies_url2)