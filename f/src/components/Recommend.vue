<template>
  <div class="movie-list">
    <h3>로그인된 사용자에게 보여질 영화 추천 컴포넌트</h3>
    <div class="movie-list-box">
      <MovieItem 
        v-for="(movie,index) in recommendMovies"
        :key="`r-${index}`"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem';
import axios from 'axios'
import jwt_decode from "jwt-decode"

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Recommend',
  components: {
    MovieItem,
  },
  data() {
    return {
      recommendMovies: null,
    }
  },
  methods: {
    // 커뮤니티 기반 추천 알고리즘
    // 컨텐츠 기반 추천 알고리즘
    getRecommend() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      axios({
          method: 'post',
          url: `${API_URL}/movies/recommend/`,
          data: {
            user_id: now_user_id,
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.recommendMovies = res.data
          console.log(res.data)
        })
        .catch((err)=>{console.log(err)})
    }
  },
  created() {
    this.getRecommend()
  }

}
</script>

<style>
.recommend {
  width : 100vw;
  height : 100vh;
  border : solid 2px green;
}

</style>