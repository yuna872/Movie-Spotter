<template>
  <div class="movies">
    <div>
      <h3>MOVIE SPOTTER</h3>
      <form @submit.prevent="searchInputData">
        <input type="text" v-model="inputData" placeholder="영화 제목으로 검색하세요."><br>
        <button>검색하기</button>
      </form>
    </div>
    <LoginRequest/>
    <Recommend/>
    <MovieList/>
  </div>
</template>

<script>
// import axios from 'axios';

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
      inputData : null,
    }
  },
  methods:{
    // searchInputData() {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}`
    //   })
    // }
  }
}
</script>
