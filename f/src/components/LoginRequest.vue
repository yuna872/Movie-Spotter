<template>
  <div class="login-request" :style="{'backgroundImage':`url(${backdropUrl})`}">
    <div class="login-request-box">
      <div class='login-request-title'>MOVIE SPOTTER가 처음이세요?</div>
      <div class='login-request-content'>지금 MOVIE SPOTTER에 가입하시면</div>
      <div class='login-request-content'>당신에게 딱 맞는 영화를 추천해드립니다!</div>
      <button class='login-request-btn' @click="goSignup">영화 추천받기</button>
    </div>
  </div>
</template>

<script>
export default {
  name : 'LoginRequest',
  props: {
    randomMovie : Object,
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/original/${this.randomMovie?.backdrop_path}`
    }
  },
  methods: {
    goSignup() {
      this.$router.push({name : 'signup'})
    }
  }
}
</script>

<style>
.login-request {
  width : 100vw;
  height : 100vh;
  border : solid 2px blue;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
}

.login-request::before{
  content: "";
  opacity: 0.5;
  position: absolute;
  top: 100vh;
  left: 0px;
  right: 0px;
  bottom : 205vh;
  background-color: #000;
}

.login-request-box {
  position : absolute;
  z-index : 2;
  right :0;
  left: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
  width : 70%;
  margin : 30vh auto;
}

.login-request-title {
  font-size : 3em;
  margin-bottom : 25px;
}

.login-request-content {
  font-size : 1.8em;
}

.login-request-btn {
  width : 25%;
  height : 60px;
  background-color: #F6BE00;
  border-radius : 50px;
  margin-top : 3vh;
  font-size : 1.2em;
}

</style>