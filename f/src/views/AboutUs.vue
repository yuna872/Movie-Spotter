<template>
  <div class="about-us">
    <div class="about-us-box">
      <div class="flip">  
        <div class="flip-card">
          <!-- 앞면 -->
          <div class="front">
            <div class="profile">
             <div class="profile-img1"></div>
            </div>
            <div class="profile-name">김팀장</div>
            <div class="profile-part">Full Stack :)</div>
          </div>
          <!-- 뒷면 -->
          <div class="back">
            <p class="profile-comment-title">comment</p>
            <p class="profile-comment">안녕하세요! 김팀장 인사 올려드립니다 꾸벅. 모두모두 건강하세요</p>
            <div>
              <div class="link-btn"><i class="fa-brands fa-github fa-5x"></i></div>
              <div class="link-btn"></div>
            </div>
          </div>
      </div>
     </div>
     <div class="flip">  
        <div class="flip-card">
          <!-- 앞면 -->
          <div class="front">
            <div class="profile">
            <div class="profile-img2"></div>
            </div>
            <div class="profile-name">최팀장</div>
            <div class="profile-part">Full Stack :)</div>

          </div>
          <!-- 뒷면 -->
          <div class="back"></div>
      </div>
     </div>
     <div class="flip">  
        <div class="flip-card">
          <!-- 앞면 -->
          <div class="front">
            <div class="profile">
            <div class="profile-img3"></div>
            </div>
            <div class="profile-name">박팀장</div>
            <div class="profile-part">git pull Stack :)</div>
          </div>
          <!-- 뒷면 -->
          <div class="back"></div>
      </div>
     </div>
    </div>
  </div>
    
</template>

<script>
export default {
  name: 'AboutUs',
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
  font-size : 1.3em;
}

.profile-comment {
  width : 80%;
  font-size : 1.5em;
  border-bottom : 2px solid white;
  padding-bottom: 30px;
}

.back { 
  background : #343440;
  /* background: royalblue;  */
  transform: rotateY(180deg);
}


.flip:hover .flip-card {
  transform: rotateY(180deg);
}

.flip:hover .about-us {
  background: #F6BE00; 
}

.link-btn {

}

</style>