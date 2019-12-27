from task_six import*
def analyse_movies_directors (movies_detail_list):
    directors = {}
    for names in movies_detail_list:
        # print(names)
        for name in names['director']:
            if name in directors:
                directors[name] +=1
            else:
                directors[name]=1
    return directors
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) 
pprint.pprint(analyse_movies_directors(movies_detail_list))

from task_six import*
def analyse_movies_genre(movies_detail_list):
    genre = {}
    for names in movies_detail_list:
        # print(names)
        for name in names['genre']:
            if name in genre:
                genre[name] +=1
            else:
                genre[name]=1
    return genre
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) 
pprint.pprint(analyse_movies_genre(movies_detail_list))