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
        <router-link :to="{ name : 'userinfo', params: { id: user_id } }">My Page</router-link>
        <button @click='logout' v-if="isLogin">logout</button>
      </div>
    </nav>
    <router-view class="router-view" @login="login" :isLogin="isLogin"/>
    <div class="about-us-btn" @click="toAboutUs"></div>
    <div class="scroll-downs">
      <div class="mousey">
        <div class="scroller"></div>
      </div>
    </div>
  </div>
</template>

<script src="lodash.js"></script>
<script>
import jwt_decode from "jwt-decode"

export default {
  name: 'App',
  data: function () {
    return {
      isLogin : localStorage.getItem('jwt') ? true : false,
      user_id : null
    }
  },
  methods: {
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
        this.$router.push({ name: 'login' })
      }
    },
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
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

/* 마우스 아이콘 */
.scroll-downs {
  position: fixed;
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
