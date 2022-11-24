<template>
  <div class="about-us">
    <div class="about-us-box">
      <div class="flip">  
        <div class="flip-card">
          <div class="front">
            <div class="profile">
             <div class="profile-img1"></div>
            </div>
            <div class="profile-name">김팀장</div>
            <div class="profile-part">Full Stack :)</div>
          </div>
          <div class="back">
            <p class="profile-comment-title">유나's comment</p>
            <p class="profile-comment">안녕하세요! 김팀장 인사 올려드립니다 꾸벅. 모두모두 건강하세요</p>
            <div class="profile-btn-box">
              <div class="link-git" @click="goToLink('https://github.com/yuna872')"><i class="fa-brands fa-github fa-3x"></i></div>
              <div class="link-tistory" @click="goToLink('https://yunae.tistory.com/')"><div class="tistory-logo"></div></div>
            </div>
          </div>
      </div>
     </div>
     <div class="flip">  
        <div class="flip-card">
          <div class="front">
            <div class="profile">
            <div class="profile-img2"></div>
            </div>
            <div class="profile-name">최팀장</div>
            <div class="profile-part">Full Stack :)</div>

          </div>
          <div class="back">
            <p class="profile-comment-title">지우's comment</p>
            <p class="profile-comment">안녕하세요! 최팀장 인사 올려드립니다 꾸벅. 모두모두 건강하세요</p>
            <div class="profile-btn-box">
              <div class="link-git" @click="goToLink('https://github.com/choizlor')"><i class="fa-brands fa-github fa-3x"></i></div>
              <div class="link-tistory" @click="goToLink('https://choizlor.tistory.com/')"><div class="tistory-logo"></div></div>
            </div>
          </div>
      </div>
     </div>
     <div class="flip">  
        <div class="flip-card">
          <div class="front">
            <div class="profile">
            <div class="profile-img3"></div>
            </div>
            <div class="profile-name">박팀장</div>
            <div class="profile-part">git pull Stack :)</div>
          </div>
          <div class="back">
            <p class="profile-comment-title">시형's comment</p>
            <p class="profile-comment">안녕하세요! 박팀장 인사 올려드립니다 꾸벅. 모두모두 건강하세요</p>
            <div class="profile-btn-box">
              <div class="link-git" @click="goToLink('https://github.com/psihyeong')"><i class="fa-brands fa-github fa-3x"></i></div>
            </div>
          </div>
      </div>
     </div>
    </div>
    <div class="about-us-btn" @click="toHome">🏠</div>
  </div>
    
</template>

<script>
export default {
  name: 'AboutUs',
  methods: {
    goToLink(link) {
      window.open(link)
    },
    toHome() {
      this.$router.push({ name : 'movies' })
    },
  }
}
</script>

<style>
.about-us {
  width : 100vw;
  height : 100vh;
  display: flex;
  margin : auto;
  align-items: center;
  padding-bottom : 15vh;
}
.about-us-box {
  width : 90%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  justify-content: space-evenly;
  display: flex;
  margin : auto;
}
.flip { 
  width: 21vw;
  height : 27vw;;
  perspective: 1100px;
  /* border: solid 2px white; */
}

.flip-card {
  /* border: solid 2px white; */
  width : 100%;
  height : 100%;
  position: relative;
  transition: .7s;
  transform-style: preserve-3d;
}	

.front, .back {
  /* padding-top : 150%;  */
  position: absolute;
  width: 100%; 
  height: 100%;
  backface-visibility: hidden;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.front {
  background: #F6BE00; 
}

.profile {
  width:65%;
  margin-bottom:10%;
}
.profile-img1 {
  padding-bottom: 100%;
  border-radius: 100%;
  background-size: cover;
  background-image:url('@/assets/kim.png')
}
.profile-img2 {
  padding-bottom: 100%;
  border-radius: 100%;
  background-size: cover;
  background-image:url('@/assets/choi.png')
}
.profile-img3 {
  padding-bottom: 100%;
  border-radius: 100%;
  background-size: cover;
  background-image:url('@/assets/park.png')
}

.profile-name {
  font-size : 2em;
}

.profile-part {
  font-size : 1.5em;
}

.profile-comment-title {
  font-family: 'Jost', sans-serif;
  font-size : 1.5em;
  margin-bottom: 10%;
}

.profile-comment {
  width : 80%;
  height: 40%;
  font-size : 1.5em;
  border-bottom : 2px solid white;
  padding-bottom: 10%;
}

.back { 
  background : #343440;
  /* background: royalblue;  */
  transform: rotateY(180deg);
}

.profile-btn-box {
  display: flex;
}


.flip:hover .flip-card {
  transform: rotateY(180deg);
}

.flip:hover .about-us {
  background: #F6BE00; 
}

.link-git {
  margin : 10px;
}
.link-tistory {
  margin : 10px;
  border-radius: 50%;
  width : 50px;
  height : 50px;
  background-image: url('@/assets/tis_logo.png');
  background-size : cover;
}


</style>