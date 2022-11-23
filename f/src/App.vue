<template>
  <div id="app">
    <nav>
      <div class="nav-left" @click="toHome">
        <img src="@/assets/logo.png" class="nav-logo">
        <div class="nav-title">Movie Spotter</div>
      </div>
      <div class="nav-right">
        <router-link :to="{ name : 'movies' }">Home</router-link>
        <router-link :to="{ name : 'login' }" v-if="!isLogin">Login</router-link>
        <router-link :to="{ name : 'signup' }" v-if="!isLogin">Signup</router-link>
        <!-- 유저 아이디에 해당하는 UserInfo 라우터 링크 -->
        <router-link :to="{ name : 'myinfo' }" v-if="isLogin">My Page</router-link>
        <a @click='logout' v-if="isLogin">logout</a>
      </div>
    </nav>
    <router-view class="router-view" @first-time="getFirstTime" @login="login" :isLogin="isLogin"/>
    <!-- 개발자 소개 페이지 버튼 -->
    <div class="about-us-btn" @click="toAboutUs">👨‍👧‍👧</div>
    
    <!-- 페이지 위로 가는 버튼 -->
    <button class="top-btn" onclick="window.scrollTo(0,0);">
    </button>
    
    <!-- 모달 -->
    <div class="black-bg" v-if="firstTime" >
      <div class="firsttime-modal">
        <div class="firsttime-title">앗, Movie Spotter가 처음이시군요?</div>
        <div class="firsttime-box scroll-div">
          <MovieItem2
            v-for="(movie, index) in randomMovies"
            :key="`rr-${index}`"
            :movie="movie"
            @modal-like='getuserinfo'
            />
          </div>
        <div class="firsttime-btn" @click="exitModal">
          <div>제출하기</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="https://kit.fontawesome.com/059237378d.js" crossorigin="anonymous"></script>
<script src="lodash.js"></script>
<script>
import 'swiper/dist/css/swiper.css'

import axios from 'axios';
import jwt_decode from "jwt-decode"

import MovieItem from '@/components/MovieItem'
import MovieItem2 from '@/components/MovieItem2'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data: function () {
    return {
      isLogin : localStorage.getItem('jwt') ? true : false,
      user_id : null,
      firstTime : false,
      randomMovies : [],
      modalPicks: null,
    }
  },
  components: {
    MovieItem,
    MovieItem2
  },
  methods: {
    getRandomMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`
      })
      .then((res)=>{
        // 평점을 기준으로 모든 영화에 대하여 내림차순 정렬
        this.randomMovies = _.sampleSize(res.data.sort(function (a, b){
          return b['vote_count'] - a['vote_count']
        }), 30)
        console.log(this.randomMovies)
      })
      .catch((err)=>{console.log(err)})
    },
    getuserinfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
          method: 'get',
          url: `${API_URL}/accounts/${now_user_id}`,
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.modalPicks = res.data.like_movies.length
        })
        .catch((err)=>{console.log(err)})
    },
    exitModal() {
      if (this.modalPicks) {
        this.firstTime = false
      } else {
        alert('영화를 선택하세요!')
      }
    },
    login() {
      this.isLogin = true
    },
    toAboutUs() {
      this.$router.push({ name : 'aboutus' })
    },
    toHome() {
      this.$router.push({ name : 'movies' })
    },
    logout() {
      const token = localStorage.getItem('jwt')
      if (token) {
        localStorage.removeItem('jwt')
        this.isLogin = false
        this.$router.push({ name: 'movies' }).catch(()=>{})
      }
    },
    getFirstTime() {
      this.firstTime = true
    },

  },
  watch: {
    firstTime: function() {
      this.getRandomMovies()
    }
  },
  created() {
    if (this.isLogin == true) {
      const token = localStorage.getItem('jwt')
      this.user_id = jwt_decode(token).user_id
    }
    this.getRandomMovies()
    }
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@1,700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Secular+One&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@500&display=swap');
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center; 
}

.scroll-div::-webkit-scrollbar { 
width: 10px; /*스크롤바의 너비*/ } 

.scroll-div::-webkit-scrollbar-thumb { 
background-color: rgba(255,255,255,0.7); /*스크롤바의 색상*/ 
border-radius: 10px; /*스크롤바 라운드*/
} 

.scroll-div::-webkit-scrollbar-track { 
background-color: rgba(0,0,0,0.6); /*스크롤바 트랙 색상*/ 
border-radius: 10px; /*스크롤바 트랙 라운드*/ 
box-shadow: inset 0px 0px 5px rgba(0,0,0,0.2); /*스크롤바 트랙 안쪽 그림자*/}




/* 네비게이션 */
nav {
  position: absolute;
  z-index: 2;
  width : 100%;
  height : 5vh;
  display: flex;
  justify-content: space-between;
  color : white;
  cursor: pointer;
  background: linear-gradient(
    to top,
      rgba(20, 20, 20, 0) 0%,
      rgba(20, 20, 20, 0.25) 25%,
      rgba(20, 20, 20, 0.5) 50%,
      rgba(20, 20, 20, 0.75) 75%,
      rgba(20, 20, 20, 1) 100%
  );
}

nav a {
  color : white;
  text-decoration: none;
  margin : 0 5px;
}

.nav-left {
  margin : auto 15px;
  display: flex;
}
.nav-logo{
  background-image: url('../src/assets/logo.png');
  background-size: cover;
  width : 35px;
  height : 35px;
  margin-right : 10px;
}
.nav-title {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Secular One', sans-serif;
  font-size: 1.5em;
}

.nav-right {
  margin : 5px;
  display: flex;
  align-items: center;
}

/* 라우터 뷰 */
.router-view {
  position: absolute;
  z-index: 1;
}

/* AboutUs 버튼 */
.about-us-btn{
  width : 50px;
  height : 50px;
  background-color : #F6BE00;
  position: fixed;
  bottom : 20px;
  right: 20px;
  z-index: 5;
}

/* 정보 수집 모달 */
.firsttime-modal {
  width : 80vw;
  height : 90vh;
  margin : auto;
  background: #343440; 
  border-radius: 5px;
  padding : 15px 0;
  position: fixed;  
  top :1vh; bottom: 0;
  left : 0; right: 0;
  z-index: 4;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.black-bg {
  position: fixed;    
  height: 100%;
  top : 0; bottom: 0;
  left : 0; right: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 3;
}
.firsttime-box {
  width : 90%;
  height : 85%;
  margin : auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  justify-content: space-between;
  overflow-y: scroll;
}
.firsttime-title {
  font-size: 2em;
}

.firsttime-items {
  width : 13vw;
  height : 19vw;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  margin-top : 20px;
  border-radius: 10px;
  display: inline;
}

.firsttime-items:hover {
  scale: 1.02;
}

.shadow-light {
  padding: 1rem;
  color: rgb(36, 255, 102);
  filter: drop-shadow(0 0 2px rgba(36, 255, 102, 0.7))
    drop-shadow(0 0 5px rgba(36, 255, 102, 0.7))
    drop-shadow(0 0 15px rgba(36, 255, 102, 0.7));
}

.firsttime-btn {
  width : 20%;
  padding :7px;
  margin : auto;
  color: #FFD23C;
  border : #FFD23C 3px solid;
  border-radius: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1em;
  cursor: pointer;
}

.top-btn {
  width : 40px;
  height : 40px;
  background-color : white;
  opacity: 0.6;
  border-radius: 50%;
  position: fixed;
  bottom : 20px;
  left: 20px;
  z-index: 5;
  border: none;
}

.top-btn:hover {
  transform: scale( 1.05 );
  filter: drop-shadow(0px 0px 2px black);
}
</style>