<template>
  <!-- 로그인, 비로그인 사용자에게 공통적으로 추천하는 영화들 -->
  <div class="movie-list">
    <h3>Movie List 컴포넌트</h3>
    <!-- <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in newMovies"
        :key="`n-${index}`"
        :movie="movie"
      />
    </div> -->
    <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in hotMovies"
        :key="`h-${index}`"
        :movie="movie"
      />
    </div>
    <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in koreanMovies"
        :key="`k-${index}`"
        :movie="movie"
      />
    </div>
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
    // newMovies() {
    //   return this.movies?.map((movie)=>{
    //     movie['release_date'] = parseInt(movie?.['release_date'].replace(/\-/g,''))
    //     return movie
    //   })
    // },
    // 국내 영화
    koreanMovies(){
      return this.movies?.filter((movie)=>{
            return movie['original_language'] === 'ko'
      })
    },
    // 해외영화
    internationalMovies() {
      return this.movies?.filter((movie)=>{
            return movie['original_language'] != 'ko'
      }).slice(20)
    },
    hotMovies() {
      // 리스트 깊은 복사
      const tmpMovies = this.movies?.slice()
      // 투표수를 기준으로 모든 영화에 대하여 내림차순 정렬
      return tmpMovies?.sort(function (a, b){
        return b['vote_count'] - a['vote_count']
      }).slice(20)
    },
  },
}
</script>

<style>
.movie-list{
  border : solid 2px blue;
  display: flex;
  flex-direction: column;
  width : 80vw;
  margin: auto;
}

.movie-list-box{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

</style>