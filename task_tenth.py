from Ninth_task import *
def analyse_language_and_directors(movies):
    language_and_directors={}
    c=1
    for i in movies:
        language=i['language']
        director = i['Director']
        for key in director:
            language_and_directors[key]={}
            c=1
            if key not in language_and_directors:
                language_and_directors[key]={}
            for v in language:
                if v not in language_and_directors[key]:
                    language_and_directors[key][v]=c
                else:
                    language_and_directors[key][v]+=1
            # print (dir)
        # print (language)
    return (language_and_directors)
data = analyse_language_and_directors(movies_detail_list) 
pprint.pprint(data) 