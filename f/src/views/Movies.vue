<template>
  <div class="movies">
    <div class="banner-bg"></div>
    <!-- {{ backdropUrl }} -->
    <div class="banner" :style="{'backgroundImage':`url('https://image.tmdb.org/t/p/original/${backdropUrls[0]?.backdrop_path}')`}">
      <div class="banner-items">
        <div class="banner-title">
          <img src="@/assets/logo.png" style="width:80px;height:80px"/>&nbsp;MOVIE SPOTTER.
        </div>
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
              class="movie-item2"
            /> 
          </div> 
          </div>
        </form>
      </div>
      
    </div>
    <!-- 비로그인 사용자에게 보여줄 페이지 -->
    <LoginRequest 
      :backdrop="backdropUrls[1]" 
      v-if="!isLogin"/>
    <!-- 로그인된 사용자에게 보여줄 페이지 -->
    <Recommend 
      :movies="movies"
      class="recommend"
      v-if="isLogin"
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
      randomBackdrop: [],
      isLogin : localStorage.getItem('jwt') ? true : false,
      backdropUrls : [],
      backdrops : [
        {'id':597, 'backdrop_path' : '/3WjbxaqYB4vAbdUfdr5vbglD2JZ.jpg'},
        {'id':619803, 'backdrop_path' : '/kpM7wX8K66bGZkYvfHXIrnXvDRS.jpg'},
        {'id':568124, 'backdrop_path' : '/3G1Q5xF40HkUBJXxt2DQgQzKTp5.jpg'},
        {'id':674, 'backdrop_path' : '/5rrGVmRUuCKVbqUu41XIWTXJmNA.jpg'},
        {'id':354912, 'backdrop_path' : '/askg3SMvhqEl4OL52YuvdtY40Yb.jpg'},
        {'id':791373, 'backdrop_path' : '/pcDc2WJAYGJTTvRSEIpRZwM3Ola.jpg'},
        {'id':277834, 'backdrop_path' : '/iYLKMV7PIBtFmtygRrhSiyzcVsF.jpg'},
        {'id':730823, 'backdrop_path' : '/8Qsr8pvDL3s1jNZQ4HK1d1Xlvnh.jpg'},
        {'id':936960, 'backdrop_path' : '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg'},
        {'id':662237, 'backdrop_path' : '/ibKeXahq4JD63z6uWQphqoJLvNw.jpg'},
        {'id':299534, 'backdrop_path' : '/qJeU7KM4nT2C1WpOrwPcSDGFUWE.jpg'},
        {'id':570503, 'backdrop_path' : '/v648cPRS5xPCiaSqgTlMiVzDm6o.jpg'},
        {'id':313369, 'backdrop_path' : '/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg'},
        {'id':345940, 'backdrop_path' : '/63xBsC6u54uJggUd7mntwB6RuaN.jpg'},
        {'id':361743, 'backdrop_path' : '/1ZnbzMbxgSqKuCh9aOQCvv1mAyN.jpg'},
        {'id':259316, 'backdrop_path' : '/y82LoNF9Vu4Hb2ZNh20pE4Ip4XL.jpg'},
      ]
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
        console.log('얍')
        console.log(res.data)
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
    },
    getRandomBackdrop() {
      this.backdropUrls =  _.sampleSize(this.backdrops, 2)
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
    this.getRandomBackdrop()
    this.getMovies()
  }
}
</script>

<style>
/* 배너 & 검색 페이지 */
.banner {
  width : 100vw - 50px;
  height : 100vh;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  animation: fadein 4s;
  -moz-animation: fadein 4s; 
  -webkit-animation: fadein 4s; 
  -o-animation: fadein 4s;
}

@keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
@-moz-keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
@-webkit-keyframes fadein { 
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
@-o-keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes fadeInOpacity {
	0% {
		opacity: 0;
	}
  25% {
		opacity: 0.25;
	}
  50% {
		opacity: 0.5;
	}
  70% {
		opacity: 0.75;
	}
	100% {
		opacity: 1;
	}
}

.banner::before{
  content: "";
  opacity: 0.5;
  position: absolute;
  top: 0; right:0;left:0;
  height : 100vh;
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
  animation-name: fadeInOpacity;
	animation-iteration-count: 1;
	animation-timing-function: ease-in;
	animation-duration: 1s;
}

.banner-title {
  font-family: 'Secular One', sans-serif;
  font-size : 6em;
  width: 15ch;
  animation-delay: 2s;
  animation: typing 2.5s steps(15), blink .4s step-end infinite alternate;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid;
  display: flex;
  align-items: center;
  margin : auto;
}

@keyframes typing {
  from {
    width: 0
  }
}
    
@keyframes blink {
  50% {
    border-color: transparent
  }
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
.recommend {
  width : 90vw;
  height: 100vh;
}
/* 공통 추천 영화 페이지 */
.movies-box{
  width: 100vw;
  /* height: 25000vh; */
  display: flex;
  align-items: center;
}


</style>
