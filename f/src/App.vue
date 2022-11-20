<template>
  <div id="app">
    <nav>
      <div class="nav-left">
        <img src="@/assets/logo.png" class="nav-logo">
        <div class="nav-title">Movie Spotter</div>
      </div>
      <div class="nav-right">
        <router-link :to="{ name : 'movies' }">Movies</router-link>
        <router-link :to="{ name : 'login' }">Login</router-link>
        <router-link :to="{ name : 'signup' }">Signup</router-link>
        <router-link :to="{ name : 'firsttime' }">FirstTime</router-link>
        <!-- 유저 아이디에 해당하는 UserInfo 라우터 링크 -->
        <router-link :to="{ name : 'userinfo', params: { id: user_id } }">My Page</router-link>
      </div>
    </nav>
    <router-view class="router-view" @login="login" :isLogin="isLogin"/>
    <div class="about-us-btn" @click="toAboutUs"></div>
    <div class="scroll-downs" @click="scrollTo">
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
      isLogin : localStorage.getItem('jwt') ? localStorage.getItem('jwt') : false,
      user_id : null
    }
  },
  methods: {
    login() {
      this.isLogin = true
      console.log(this.isLogin)
    },
    toAboutUs() {
      this.$router.push({ name : 'aboutus' })
    },
    scrollTo() {
      window.scrollTo({
  top: 100,
  left: 100,
  behavior: 'smooth'
});
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
