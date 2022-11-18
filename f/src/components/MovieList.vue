<template>
  <!-- 로그인, 비로그인 사용자에게 공통적으로 추천하는 영화들 -->
  <div class="movie-list">
    <div>따끈따끈 최신작 TOP 20</div>
    <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in newMovies"
        :key="`n-${index}`"
        :movie="movie"
      />
    </div>
    <div>투표수가 가장 많은</div>
    <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in hotMovies"
        :key="`h-${index}`"
        :movie="movie"
      />
    </div>
    <div>국내영화 TOP 20</div>
    <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in koreanMovies"
        :key="`k-${index}`"
        :movie="movie"
      />
    </div>
    <div>해외영화 TOP 20</div>
    <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in internationalMovies"
        :key="`i-${index}`"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem';

export default {
  name : 'MovieList',
  components: {
    MovieItem,
  },
  props:{
    movies : Array,
  },
  computed: {
    newMovies() {
      const tmpArr1 = this.movies?.map((movie)=>{
        movie['release_date'] = parseInt(movie?.['release_date'].replace(/\-/g,''))
        return movie
      })
      
      tmpArr1?.sort(function (a, b){
        return b['release_date'] - a['release_date']
      })

      if (tmpArr1.length <= 20) {
        return tmpArr1.slice(0, tmpArr1.length)
      } else {
        return tmpArr1.slice(0, 20)
      }
      
    },
    // 국내 영화
    koreanMovies(){
      const tmpArr2 = this.movies?.filter((movie)=>{
            return movie['original_language'] === 'ko'
      })

      if (tmpArr2.length <= 20) {
        return tmpArr2.slice(0, tmpArr2.length)
      } else {
        return tmpArr2.slice(0, 20)
      }
    },
    // 해외영화
    internationalMovies() {
       const tmpArr3 =  this.movies?.filter((movie)=>{
            return movie['original_language'] != 'ko'
      })

      if (tmpArr3.length <= 20) {
        return tmpArr3.slice(0, tmpArr3.length)
      } else {
        return tmpArr3.slice(0, 20)
      }
    },
    hotMovies() {
      // 리스트 깊은 복사
      const tmpMovies = this.movies?.slice()
      // 투표수를 기준으로 모든 영화에 대하여 내림차순 정렬
      tmpMovies?.sort(function (a, b){
        return b['vote_count'] - a['vote_count']
      })

      if (tmpMovies.length <= 20) {
        return tmpMovies.slice(0, tmpMovies.length)
      } else {
        return tmpMovies.slice(0, 20)
      }
    },
  },
}
</script>

<style>
.movie-list{
  border : solid 2px blue;
  display: flex;
  flex-direction: column;
  width : 85%;
  margin: auto;
}

.movie-list-box{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

</style>