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
    <div class="about-us-btn" @click="toAboutUs"></div>
    <!-- 모달 -->
    <div class="black-bg" v-if="firstTime" >
      <div class="firsttime-modal">
        <div>앗, Movie Spotter가 처음이시군요?</div>
        <div class="firsttime-box">
          <div 
            v-for="(movie,index) in randomMovies"
            :key="`rr-${index}`"
            class="firsttime-items"
            :style="{'backgroundImage':`url('https://image.tmdb.org/t/p/original/${movie?.poster_path}')`}"
          ></div>
        </div>
        <button>제출하기</button>
      </div>
    </div>
    
    <!-- 마우스 스크롤 이벤트 -->
    <div class="scroll-downs">
      <div class="mousey">
        <div class="scroller"></div>
      </div>
    </div>
  </div>
</template>

<script src="https://kit.fontawesome.com/059237378d.js" crossorigin="anonymous"></script>
<script src="lodash.js"></script>
<script>
import axios from 'axios';
import jwt_decode from "jwt-decode"

import MovieItem from '@/components/MovieItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data: function () {
    return {
      isLogin : localStorage.getItem('jwt') ? true : false,
      user_id : null,
      firstTime : false,
      randomMovies : [],
    }
  },
  components: {
    MovieItem,
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
      console.log('😎')
      this.firstTime = true
      console.log(this.firstTime ,'😎')
    }
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

/* nav a.router-link-exact-active {
} */

/* 네비게이션 */
nav {
  position: absolute;
  z-index: 2;
  width : 100%;
  height : 50px;
  display: flex;
  justify-content: space-between;
  background-color: #343440;
  color : white;
  cursor: pointer;
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
  width : 80%;
  margin : auto;
  background: #343440; 
  border-radius: 5px;
  padding : 15px 0;
  position: fixed;  
  top : 10vh; bottom: 0;
  left : 0; right: 0;
  /* position: absolute;
  top: 40vh; left: 20vw; */
  z-index: 4;
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
  margin : auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.firsttime-items {
  width : 13vw;
  height : 19vw;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  margin-top : 10px;
  border-radius: 10px;
}

/* 마우스 아이콘 */
.scroll-downs {
  position: relative;
  bottom : 4vh;
  margin : 0 auto;
  left: 0;
  right : 0;
  width :30px;
  height: 50px;
  /* border : solid 2px blue; */
}
.mousey {
  width: 2px;
  padding: 9px 10px;
  height: 20px;
  border: 2.5px solid #fff;
  border-radius: 25px;
  opacity: 0.75;
  box-sizing: content-box;
}
.scroller {
  width: 3px;
  height: 6px;
  margin : 0 auto;
  border-radius: 25%;
  background-color: #fff;
  animation-name: scroll;
  animation-duration: 2.2s;
  animation-timing-function: cubic-bezier(.15,.41,.69,.94);
  animation-iteration-count: infinite;
}
@keyframes scroll {
  0% { opacity: 0; }
  10% { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(15px); opacity: 0;}
}
</style>
