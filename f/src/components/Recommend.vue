<template>
  <div class="movie-list">
    <div class="recommend1">
      <div class="recommend-title">
        <p>Only For Movie Spotters</p>
      </div>
      <div class="comment1">
        <p>{{ userinfo?.nickname }}님의 취향저격</p>
        <div style="display:flex;justify-content:left">
          <span>베</span>
          <span>스</span>
          <span>트</span>
          <span>&nbsp;</span>
          <span>콘</span>
          <span>텐</span>
          <span>츠</span>
          <span>&nbsp;</span>
          <span><i class="fa-regular fa-thumbs-up"></i></span>
        </div>
        <p style="font-size:1.4em;margin-top:30px">회원님이 좋아하시는 영화들을 기반으로<br/>많은 비중을 차지하는 장르의 영화를 추천해드립니다!</p>
      </div>
      
  
      <div id="carouselExampleInterval" class="carousel slide container by-likes" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div @click ='goDetail(recommendMoviesByMyLikes?.[0])' class="carousel-item active inner-container" data-bs-interval="1000">
            <img :src="`https://image.tmdb.org/t/p/original/${ recommendMoviesByMyLikes?.[0].poster_path }`" class="poster" >
          </div>
          <div class="carousel-item" data-bs-interval="2000">
            <img @click ='goDetail(recommendMoviesByMyLikes?.[1])' :src="`https://image.tmdb.org/t/p/original/${ recommendMoviesByMyLikes?.[1].poster_path }`" class="poster" >
          </div>
          <div  @click ='goDetail(movie)' class="carousel-item" v-for="(movie,index) in recommendMoviesByMyLikes?.slice(2,)" :key="`n-${index}`">
            <!-- {{ movie }} -->
            <img :src="`https://image.tmdb.org/t/p/original/${ movie?.poster_path }`" class="poster" >
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>      
    </div>
        

    <div class="recommend2" v-if="recommendMoviesByMyFollowings?.length">
      
      <div class="recommend-title">
        <p>Only For Movie Spotters</p>
      </div>
      <div class="comment2">
        <p>{{ userinfo?.nickname }}님의 친구들은?</p>
        <div>
          <span>지</span>
          <span>금</span>
          <span>&nbsp;</span>
          <span>이</span>
          <span>&nbsp;</span>
          <span>영</span>
          <span>화</span>
          <span>&nbsp;</span>
          <span><i class="fa-solid fa-clapperboard"></i></span>
        </div>

        <p style="font-size:1.4em;margin-top:30px">회원님이 팔로워하고 있는 사람들 중, 나와 비슷한 취향의 친구가<br/>현재 관심 있어하는 영화들을 추천해드립니다!</p>
        
      </div>
    
      <div id="carousel2Interval" class="carousel slide container by-follower" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div 
            @click ='goDetail(recommendMoviesByMyFollowings?.[0])'
            class="carousel-item active inner-container" 
            data-bs-interval="1000"
            >
            <img :src="`https://image.tmdb.org/t/p/original/${ recommendMoviesByMyFollowings?.[0].poster_path }`" class="poster" >
          </div>
          <div @click ='goDetail(recommendMoviesByMyFollowings?.[1])' class="carousel-item" data-bs-interval="1000">
            <img :src="`https://image.tmdb.org/t/p/original/${ recommendMoviesByMyFollowings?.[1].poster_path }`" class="poster" >
          </div>
          <div @click ='goDetail(movie)' class="carousel-item" v-for="(movie,index) in recommendMoviesByMyFollowings?.slice(2)" :key="`ff-${index}`">
            <img :src="`https://image.tmdb.org/t/p/original/${ movie?.poster_path }`" class="poster" >
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carousel2Interval" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carousel2Interval" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>

    </div>
</template>

<script>
import MovieItem from '@/components/MovieItem';
import axios from 'axios'
import jwt_decode from "jwt-decode"

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Recommend',
  components: {
    MovieItem,
  },
  data() {
    return {
      isLoading : false,
      userinfo:null,
      recommendMoviesByMyLikes: null,
      recommendMoviesByMyFollowings: null,
      swiperOption: {
          slidesPerView: 5,
          spaceBetween: 20,
          slidesPerGroup: 5,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          },
          autoplay: {
            delay: 3500,
            disableOnInteraction: false
          },
        }
    }
  },
  methods: {
    // 커뮤니티 기반 추천 알고리즘
    // 컨텐츠 기반 추천 알고리즘
    goDetail(movie) {
      this.$router.push({name: 'detail', params: { id : movie.id }})
    },
    getuserinfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
          method: 'get',
          url: `${API_URL}/accounts/${now_user_id}`,
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.userinfo = res.data
        })
        .catch((err)=>{console.log(err)})
    },
    getRecommendByMyLikes() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      this.isLoading = false
      axios({
          method: 'post',
          url: `${API_URL}/movies/recommendbymylikes/`,
          data: {
            user_id: now_user_id,
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.recommendMoviesByMyLikes = res.data
          this.isLoading = true
        })
        .catch((err)=>{console.log(err)})
    },
    getRecommendByMyFollowings() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
          method: 'post',
          url: `${API_URL}/movies/recommendbymyfollowings/`,
          data: {
            user_id: now_user_id,
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.recommendMoviesByMyFollowings = res.data
          console.log(res.data)
        })
        .catch((err)=>{console.log(err)})
    },
  },
  created() {
    this.getRecommendByMyLikes()
    this.getRecommendByMyFollowings()
    if (localStorage.getItem('jwt')) {
      this.getuserinfo()
    }
  }

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@700&family=Secular+One&display=swap');
.movie-list {
  width : 100%;
  height : 100%;
}

.recommend1 {
  position: relative;
  display: flex;
  align-items: center;
  width:100vw;
  height : 100vh;
  background: radial-gradient(circle closest-corner at 70%, rgba(255,210,60,0.8), rgba(255,210,60,0.5),  rgba(0,0,0,0.7),rgba(0,0,0,1));
}

.recommend-title {
  justify-content: center;
  display: flex;
  flex-direction: column;
  position: absolute;
  top:3vh;right: 0;left:0
}

.recommend-title p {
  font-size: 1.7em;
  font-family: 'Libre Baskerville', serif;
}



.by-follower {
  position: absolute;
  right : 45%;
}

.by-likes {
  position: absolute;
  left : 45%;
}
.recommend2 {
  position: relative;
  display: flex;
  align-items: center;
  width: 100vw;
  height : 100vh;
  background: radial-gradient(circle closest-corner at 30%, rgba(255,210,60,0.8), rgba(255,210,60,0.5),  rgba(0,0,0,0.7),rgba(0,0,0,1));
}

.poster {
  border-radius: 20px;
  height:60vh;
}

.poster:hover {
  cursor: pointer;
  scale : 1.02;
}

.poster-div {
  width : 40vw;
  display: inline-block;
  text-align: center;
  border-radius: 20px;
}

.poster-div:hover {
  scale : 1.02;
  border-radius: 20px;
}
.container {
  width : 45vw;
}

.comment1 {
  position: absolute;
  left : 10%;
  padding-bottom: 5%;
}

.comment1 p {
  font-size: 4em;
  text-align: left;
}
.comment1 span {
  font-size: 4em;
  text-align: left;
}

.comment2 {
  padding-bottom: 5%;
  position: absolute;
  right : 10%;
}

.comment2 p {
  font-size: 4em;
  text-align: right;
}

.comment2 span {
  font-size: 4em;
  text-align: right;
}

.comment1 span {position:relative;  display: inline-block; color:white; letter-spacing:-0.8px;
animation:txtup 1.5s infinite; -webkit-animation:txtup 1.5s infinite;  -ms-animation:txtup 1.5s infinite;   -moz-animation: txtup 1.5s infinite; 
}
.comment1 span:nth-of-type(1){animation-delay:0.1s;}
.comment1 span:nth-of-type(2){animation-delay:0.2s;}
.comment1 span:nth-of-type(3){animation-delay:0.3s;}
.comment1 span:nth-of-type(4){animation-delay:0.4s;} 
.comment1 span:nth-of-type(5){animation-delay:0.5s;}
.comment1 span:nth-of-type(6){animation-delay:0.6s;} 
.comment1 span:nth-of-type(7){animation-delay:0.7s;}  
.comment1 span:nth-of-type(8){animation-delay:0.8s;}  
.comment1 span:nth-of-type(9){animation-delay:0.9s;}  


@-webkit-keyframes txtup {
    0%{top:0;}
    20% {top:-0.3rem;}
    40% {top:0;}
    60% {top:0;}
    80% {top:0;}
    100% {top:0}
}
@keyframes txtup {
    0% {top:0;}
    20% {top:-0.3rem;}
    40% {top:0}
    60% {top:0}
    80% {top:0}
    100% {top:0}
}


.comment2 span {
  color:rgba(255,210,60);
  opacity: 0;
  transform: translate(-300px, 0) scale(0);
  animation:txtE 1.5s infinite;
}

@keyframes txtE {
  60% {
    transform: translate(20px, 0) scale(1);
    color:white;
  }

  80% {
    transform: translate(20px, 0) scale(1);
    color:rgba(255,210,60 0.5);    
  }

  90% {
    transform: translate(0) scale(1.2);
    /* color:rgba(255,210,60); */
    color:white;
  }

  100% {
    transform: translate(0) scale(1);
    opacity: 1;
    color:white;
  }
}
.comment2 span:nth-of-type(2) {
  animation-delay: .1s;
}
.comment2 span:nth-of-type(3) {
  animation-delay: .2s;
}
.comment2 span:nth-of-type(4) {
  animation-delay: .3s;
}
.comment2 span:nth-of-type(5) {
  animation-delay: .4s;
}
.comment2 span:nth-of-type(6) {
  animation-delay: .5s;
}
.comment2 span:nth-of-type(7) {
  animation-delay: .6s;
}
.comment2 span:nth-of-type(8) {
  animation-delay: .7s;
}
.comment2 span:nth-of-type(9) {
  animation-delay: .8s;
}


.desc {
  width: 30vw;
  margin-top : 20px;
  font-size: 1.5em;
}

</style>