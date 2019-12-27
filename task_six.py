from task_five import*
def analyse_movies_language(movies_detail_list):
    # print (movies_detail_list)
    languages = {}

    for langs in movies_detail_list:
        # print(langs)
    
        for lang in langs['language']:
            # print(lang)
            if lang in languages:
                    languages[lang] +=1 
            else:
                    languages[lang]= 1

            # languages['language']=lang
    return languages 
            
# print(analyse_movies_language(movies_detail_list)               
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10]) 
pprint.pprint(analyse_movies_language(movies_detail_list))