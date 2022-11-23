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
    backdrop : Object,
  },
  methods: {
    goSignup() {
      this.$router.push({name : 'signup'})
    }
  },
  computed: {
    backdropUrl() {
      return 'https://image.tmdb.org/t/p/original/' + this.backdrop?.backdrop_path
    }
  }
}
</script>

<style>
.login-request {
  width : 100vw;
  height : 100vh;
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
  font-size : 3.5em;
  animation:ani 1.6s infinite alternate;
  margin-bottom : 15px;  
}
@keyframes ani{
   0%{transform:translate(0,0);}
   100%{transform:translate(0,17px);}
}  

.login-request-content {
  font-size : 2em;
  animation:ani 1.6s infinite alternate;  
}

.login-request-btn {
  width : 25%;
  height : 60px;
  background-color: #F6BE00;
  border : none;
  border-radius : 50px;
  margin-top : 5vh;
  font-size : 1.2em;
  /* animation:ani 2s infinite alternate;   */
}

.login-request-btn:hover{
    transform: translate(0, -10%);
    scale: 1.02;
    box-shadow: 2px 5px 15px rgba(0, 0, 0, 0.7);
}

</style>