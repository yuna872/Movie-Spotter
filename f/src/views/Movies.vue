<template>
  <div class="movies">
    
    <div class="banner">
      <h3>MOVE SPOTTER</h3>
      <form @submit.prevent="searchInputData">
        <input type="text"  @input="inputData=$event.target.value" placeholder="영화 제목으로 검색하세요."><br>
        <button>검색하기</button>
        <div class="display-array-container">
          <div class="display-array-box">
          <MovieItem
            v-for="(movie, index) in displayArray"
            :key="`d-${index}`"
            :movie="movie"
          /> 
        </div> 
        </div>
      </form>
    </div>
    <LoginRequest/>
    <Recommend :movies="movies"/>
    <div class="movies-box">
      <MovieList :movies="movies"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import _ from 'lodash';

import LoginRequest from '@/components/LoginRequest';
import MovieList from '@/components/MovieList';
import Recommend from '@/components/Recommend';
import MovieItem from '@/components/MovieItem';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Movies',
  components: {
    LoginRequest,
    MovieList,
    Recommend,
    MovieItem,
  },
  data() {
    return {
      movies : [],
      inputData : null,
      bannerImageUrl : null,
      displayArray : [],
    }
  },
  methods: {
    // getBannerImage() {
    //   console.log(_.sample(this.movies))
    // },
    getMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`
      })
      .then((res)=>{
        // 평점을 기준으로 모든 영화에 대하여 내림차순 정렬
        this.movies = res.data.sort(function (a, b){
          return b['vote_average'] - a['vote_average']
        })
      })
      .catch((err)=>{console.log(err)})
    },
    searchInputData() {
      this.displayArray = this.movies.filter((movie)=>{
        return movie.title.includes(this.inputData) 
      }) 
    }
  },
  watch: {
    inputData: function() {
      if (this.inputData.trim().length == 0) {
        this.displayArray = []
      }
      else {
        this.searchInputData()
      }
    }

  },
  created() {
    this.getMovies()
    // this.getBannerImage()
  }
}
</script>

<style>
/* 배너 & 검색 페이지 */
.banner {
  width : 100vw;
  height : 100vh;
  background: linear-gradient(
    to left,
      rgba(20, 20, 20, 0) 10%,
      rgba(20, 20, 20, 0.25) 25%,
      rgba(20, 20, 20, 0.5) 50%,
      rgba(20, 20, 20, 0.75) 75%,
      rgba(20, 20, 20, 1) 100%
  );
  border: solid 2px red;
}

.display-array-container {
  width : 80vw;
  border: solid 2px red;
  margin: auto;
}

.display-array-box {
  width : 90%;
  display: flex;
  flex-wrap: wrap;
}

/* 로그인 제안(?) 페이지 */
/* 추천 알고리즘 페이지 */
/* 공통 추천 영화 페이지 */
.movies-box{
  width: 100vw;
  height: 200vh;
}


</style>
