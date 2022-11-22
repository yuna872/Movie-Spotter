<template>
  <div class="about-us">
    <div class="about-us-box">
      <div class="flip">  
        <div class="flip-card">
          <!-- 앞면 -->
          <div class="front">
          </div>
          <!-- 뒷면 -->
          <div class="back">
            <div>사진</div>
            <div>역할</div>
            <div>한줄 소개</div>
            <div>
              <div class="link-btn"><i class="fa-brands fa-github"></i></div>
              <div class="link-btn"></div>
            </div>
          </div>
      </div>
     </div>
     <div class="flip">  
        <div class="flip-card">
          <!-- 앞면 -->
          <div class="front"></div>
          <!-- 뒷면 -->
          <div class="back"></div>
      </div>
     </div>
     <div class="flip">  
        <div class="flip-card">
          <!-- 앞면 -->
          <div class="front"></div>
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
  border: solid 2px white;
  margin : auto;
  align-items: center;
  padding-bottom : 15vh;
}
.about-us-box {
  width : 90%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  justify-content: space-evenly;
  border: solid 2px white;
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
}

.front {
  background: #F6BE00; 
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