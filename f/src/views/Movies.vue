<template>
  <div class="movies">
    <div class="banner-bg"></div>
    <!-- {{ backdropUrl }} -->
    <div class="banner" :style="{'backgroundImage':`url(${backdropUrl})`}">
      <div class="banner-items">
        <div class="banner-title">MOVIE SPOTTER</div>
        <!-- {{ backdropUrl }} -->
        <form class="banner-form" @submit.prevent="searchInputData">
          <input
            class="banner-input" 
            type="text"  
            @input="inputData=$event.target.value" 
            placeholder="영화 제목으로 검색하세요.">
          <!-- <div class="banner-btn">영화 찾기</div> -->
          <div class="display-array-container" v-if="displayArray.length">
            <div class="display-array-box">
            <MovieItem
              v-for="(movie, index) in displayArray"
              :key="`d-${index}`"
              :movie="movie"
              style="margin:10px auto;"
            /> 
          </div> 
          </div>
        </form>
      </div>
      
    </div>
    <!-- 비로그인 사용자에게 보여줄 페이지 -->
    <LoginRequest :randomMovie="randomMovie[1]"/>
    <!-- 로그인된 사용자에게 보여줄 페이지 -->
    <Recommend 
      :movies="movies"
    />
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
      randomMovie : [],
    }
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/original/${this.randomMovie[0]?.backdrop_path}`
    }
  },
  methods: {
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

        this.randomMovie = _.sampleSize(this.movies, 2)
        console.log(this.randomMovie)
      })
      .catch((err)=>{console.log(err)})
    },
    searchInputData() {
      this.displayArray = this.movies.filter((movie)=>{
        return movie.title.includes(this.inputData) 
      }) 
    },
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
  /* background-color: rgba(0, 0, 0, 0.6); */
  width : 100vw - 50px;
  height : 100vh;
  border: solid 2px pink;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  /* background-color: rgba(0, 0, 0, 0.6); */
}

.banner::before{
        content: "";
        opacity: 0.5;
        position: absolute;
        top: 0px;
        left: 0px;
        right: 0px;
        bottom : 300vh;
        background-color: #000;
}
.banner-items {
  position : absolute;
  z-index : 2;
  right :0;
  left: 0;
  display: flex;
  flex-direction: column;
  width : 70%;
  margin : 30vh auto;
}

.banner-title {
  font-family: 'Secular One', sans-serif;
  font-size : 6em;
}

.banner-input{
  border: none;
  width : 70%;
  height: 55px;
  margin :auto;
  background-color: #343440;
  padding-left: 2vw;
  font-size: 1.3em;
  color: white;
}

.banner-form {
  margin-top : 3vh;
  display: flex;
  flex-direction: column;
  align-content: center;
  align-items: center;
}

.banner-btn {
  width : 25%;
  background-color: #F6BE00;
  margin-top : 5vh; 
  height: 4.5vh;
  border-radius: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.4em;
}

.display-array-container {
  margin-top : 25px;
  background-color: rgba(0, 0, 0, 0.6);
  width : 90vw;
  border-radius: 10px;
  padding : 20px;
}

.display-array-box {
  width : 100%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  /* display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; */
}

/* 로그인 제안(?) 페이지 */
/* 추천 알고리즘 페이지 */
/* 공통 추천 영화 페이지 */
.movies-box{
  width: 100vw;
  height: 200vh;
}


</style>
