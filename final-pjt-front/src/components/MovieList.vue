<template>
  <!-- 로그인, 비로그인 사용자에게 공통적으로 추천하는 영화들 -->
  <div class="movie-list">
    <h3>Movie List 컴포넌트</h3>
    {{ movies }}
    <!-- 국내, 해외, 최신영화 top 10, 투표수가 많은 -->
  </div>
</template>

<script>
import axios from 'axios'
import MovieItem from '@/components/MovieItem';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'MovieList',
  components: {
    MovieItem,
  },
  data() {
    return {
      movies: null,
    }
  },
  computed: {
    // newMovies() {
    // },
    // koreanMovies(){
    // },
    // internationalMovie() {

    // },
    // hotMovie() {

    // },
  },
  methods: {
    getMovies() {
      axios({
        methods: 'get',
        url: `${API_URL}/movies/`,
      })
      .then((res)=>{
        // 평점을 기준으로 모든 영화에 대하여 내림차순 정렬
        this.movies = res.data.sort(function (a, b){
          return b['vote_average'] - a['vote_average']
        })
      })
      .catch((err)=>{console.log(err)})
    }
  },
  created() {
    this.getMovies()
  }
}
</script>

<style>

</style>