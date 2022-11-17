<template>
  <div id="app">
    <nav>
      <router-link to="/">Movies</router-link> |
      <router-link to="/accounts/login">Login</router-link> |
      <router-link to="/accounts/signup">Signup</router-link> |
      <router-link to="/firsttime">FirstTime</router-link> |
      <router-link to="/aboutus">About Us</router-link>
      <!-- 유저 아이디에 해당하는 UserInfo 라우터 링크 -->
      <!-- <router-link :to="{ name : 'Userinfo', params: {id: user.id }}">My Page</router-link> -->
    </nav>
    <router-view @login="login"/>
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
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
