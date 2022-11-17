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
      </div>
      <!-- 유저 아이디에 해당하는 UserInfo 라우터 링크 -->
      <!-- <router-link :to="{ name : 'Userinfo', params: {id: user.id }}">My Page</router-link> -->
    </nav>
    <router-view @login="login"/>
    <div class="about-us-btn" @click="toAboutUs"></div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin : localStorage.getItem('jwt') ? localStorage.getItem('jwt') : false
    }
  },
  methods: {
    login() {
      this.isLogin = true
      console.log(this.isLogin)
    },
    toAboutUs() {
      this.$router.push({ name : 'aboutus' })
    }
  },
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

/* AboutUs 버튼 */
.about-us-btn{
  width : 50px;
  height : 50px;
  background-color : #F6BE00;
  position: fixed;
  bottom : 20px;
  right: 20px;
}
</style>
