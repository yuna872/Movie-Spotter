<template>
  <div class="movies">
    <div>
      <h3>MOVE SPOTTER</h3>
      <form @submit.prevent="searchInputData">
        <input type="text" v-model="inputData" placeholder="영화 제목으로 검색하세요."><br>
        <button>검색하기</button>
      </form>
    </div>
    <LoginRequest/>
    <Recommend :movies="movies"/>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import axios from 'axios';

import LoginRequest from '@/components/LoginRequest';
import MovieList from '@/components/MovieList';
import Recommend from '@/components/Recommend';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Movies',
  components: {
    LoginRequest,
    MovieList,
    Recommend,
  },
  data() {
    return {
      movies : null,
      inputData : null,
    }
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
