<template>
  <div class="login-request" :style="{'backgroundImage':`url(${backdropUrl})`}">
    <h3>비로그인 사용자에게 보여질 로그인 요청 배너 페이지</h3>
  </div>
</template>

<script>
export default {
  name : 'LoginRequest',
  data() {
    return {
      randomMovie : null,
    }
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/original/${this.randomMovie?.backdrop_path}`
    }
  },
  // methods: {
  //   getRandomMovie(){

  //   }
  // },
  // created: {
  //   getRandomMovie()
  // }
}
</script>

<style>
.login-request {
  width : 100vw;
  height : 100vh;
  border : solid 2px blue;
}

</style>