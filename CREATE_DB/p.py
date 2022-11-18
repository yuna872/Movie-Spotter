import requests


def GET_CREDIT_VIDEO(movie_id):
    movie_id = 851644
    Get_Credit = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=633fd9754acba9ddc40773b19c562ed9&language=ko').json()

    actors = []
    for i in Get_Credit['crew']:
        if i['known_for_department'] == 'Directing':
            actors.append(i['name'])
            break
    for i in Get_Credit['cast']:
        actors.append(i['name'])
        if len(actors) == 4:
            break

    return actors

movie_id =965080
def VIDEO(movie_id):
    Get_Video = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=633fd9754acba9ddc40773b19c562ed9&language=ko').json()
    print(Get_Video)
    # return Get_Video['results'][0]['key']


print(VIDEO(965080))
   
