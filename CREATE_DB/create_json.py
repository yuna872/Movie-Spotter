import requests
import json

TMDB_API_KEY = '633fd9754acba9ddc40773b19c562ed9'

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 500):
        request_url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}'
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                if movie.get('vote_average') > 7:
                    fields = {
                        'title': movie['title'],
                        'release_date': movie['release_date'],
                        'adult': movie['adult'],
                        'vote_average': movie['vote_average'],
                        'overview': movie['overview'],
                        'backdrop_path': movie['backdrop_path'],
                        'poster_path': movie['poster_path'],
                        'genres': movie['genre_ids'],
                        'original_language': movie['original_language'],
                        'vote_count': movie['vote_count'],
                    }

                    data = {
                        "pk": movie['id'],
                        "model": "movies.movie",
                        "fields": fields
                    }

                    total_data.append(data)

            if len(total_data) == 50:
                with open('movies.json', 'w', encoding='UTF-8') as file:
                    file.write(json.dumps(total_data, ensure_ascii=False)) 
                return

get_movie_datas()
print('?')