<template>
  <div class="login-request" :style="{'backgroundImage':`url(${backdropUrl})`}">
    <div class="login-request-box">
      <div>MOVIE SPOTTER가 처음이세요?</div>
      <div>지금 가입하시면 당신에게 딱 맞는 영화를 추천해드려요~</div>
      <button @click="goSignup">Sign Up</button>
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
        bottom : 200vh;
        background-color: #000;
}

</style>