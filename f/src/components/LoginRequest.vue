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
  height : 100vh;
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

.login-request-title {
  font-size : 3em;
  margin-bottom : 25px;
  animation-name: fadeInOpacity;
	animation-iteration-count: 1;
	animation-timing-function: ease-in;
	animation-duration: 3s;
}

.login-request-content {
  font-size : 1.8em;
  animation-name: fadeInOpacity;
	animation-iteration-count: 1;
	animation-timing-function: ease-in;
	animation-duration: 3s;
}

.login-request-btn {
  width : 25%;
  height : 60px;
  background-color: #F6BE00;
  border-radius : 50px;
  margin-top : 3vh;
  font-size : 1.2em;
  /* box-shadow: 0 5px 4px rgba(79, 74, 49, 0.6); */
}

.login-request-btn:hover{
    transform: translate(0, -10%);
    scale: 1.02;
}

</style>