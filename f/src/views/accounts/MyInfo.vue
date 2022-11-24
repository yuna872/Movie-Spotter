<template>
  <div class="userinfo">
    <div class="userinfo-top">
      <div><p class="info-id">{{ userinfo?.username }}님의 마이 페이지</p>
      <p class="info-nickname">닉네임 : {{ userinfo?.nickname }} 😉</p>
      <p class="info-follow"><i class="fa-solid fa-user-group"></i> &nbsp; followers {{ userinfo?.followers.length }} &nbsp;&nbsp; | &nbsp;&nbsp; followings {{ userinfo?.followings.length }}</p></div>
      <div class="user-profile">
        <div class="user-profile-img"></div>>
      </div>
      <!-- 상세정보 -->
    </div>
    <div class="userinfo-top-top">
      <div class="review-wrap">
        <p style="font-size : 1.4em;margin-top:20px;">내가 쓴 리뷰 📑</p>
        <div class="myreview-list scroll-div">
          <div 
            v-for="(review, index) in reviewinfo" 
            :key="index"
            class="info-div"  
          > 
            <div class='review-rank'> <i class="fa-solid fa-star fa-sm" style="color:#F6BE00"></i> 
              &nbsp;{{ review.rank }}점
            </div>
          <div class='review-content'>{{ review.content }}</div>
            <div class = 'review-like'>
              <i class="fa-solid fa-thumbs-up"></i>&nbsp;
              {{ review.like_users.length }}&nbsp;likes
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="userinfo-top-bottom">

      <div class="swiper-box">
        <div>
          <div class="semi-title">내가 좋아요 누른 컨텐츠</div>
            <swiper class="swiper" :options="swiperOption">
              <swiper-slide class="swiper-slide" v-for="(movie, index) in movies" :key="`n-${index}`">
                <MovieItem class="movie-item1" :movie="movie"/>
              </swiper-slide>
              <div class="swiper-button-prev" slot="button-prev"></div>
              <div class="swiper-button-next" slot="button-next"></div>
            </swiper>
          </div>
        </div> 
      </div>
  </div>
</template>



<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import MovieItem from '@/components/MovieItem.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyInfo',
  components : {
    swiper,
    swiperSlide,
    MovieItem,
  },
  data() {
    return {
      movies:[],
      userinfo : null,
      reviewinfo : null,
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
  created() {
    this.getuserinfo()
    this.getuserreviews()
    this.getMovies()
  },
  methods: {
    getMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`
      })
      .then((res)=>{
        const likeMovies = this.userinfo?.like_movies
        this.movies = res.data.filter((movie)=>{
          if (likeMovies.includes(movie.id)) {
            return movie
          }
        }
      )})
      .catch((err)=>{console.log(err)})
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
          console.log(this.userinfo)
        })
        .catch((err)=>{console.log(err)})
    },
    getuserreviews() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
          method: 'get',
          url: `${API_URL}/movies/reviews/${now_user_id}`,
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.reviewinfo = res.data
        })
        .catch((err)=>{console.log(err)})
    },
  },
}
  

</script>

<style>

.userinfo {
  width : 100vw;
  /* height : 100vh; */
}
.userinfo-box {
  display: flex;
  flex-direction: column;
  width : 90%;
  margin : auto;
  border : 3px solid green;
}
.userinfo-top {
  background-image: url('@/assets/caramel.jpg');
  background-size: cover;
  height : 40vh;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  border : 3px solid red;
}

.userinfo-top-bg {
  position: absolute;
  height: 20vh;
  top : 20vh;
  right:0;left:0;
  background-color: #25252e;
  border : 3px solid blue;
}
.user-profile {
  width : 15vw;
  margin-left : 10vw;
  position: absolute;
  z-index: 1;
}
.user-profile-img{
  border-radius: 100%;
  padding-bottom : 100%;
  background-image: url('@/assets/null.png');
  background-size: cover;
}

.info-id{
  display: inline-block;
  width : auto;
  border : 3px solid blue;
  font-size : 1.1em;
}



.userinfo-top-top p {
  text-align: center;
  margin-bottom: 5px;
}

.review-wrap {
  width : 100vh;
  display: flex;
  flex-direction: column;
}

.review-rank {
  border : 3px solid blue;

}

.review-content {
  border : 3px solid blue;

}
.review-like {
  border : 3px solid blue;
}

.info-div {
  text-align: left;
  justify-content: space-between;
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  font-size : 1.1em;
  align-items: center;
  border-bottom: solid 2px white;
  padding-bottom : 10px;
  width : 90%;
  margin : auto;
}


.info-id {
  margin-left: 10vw;
  font-size : 2.5em;
  border : 3px solid blue;
}
.info-nickname {
  font-size : 1.8em;
}

.info-follow {
  font-size : 1.2em;
}

.userinfo-top-bottom {
  height : 40%;
}

.myreview-list {
  height : 50%;
  width : 60%;
  margin : auto;
  overflow-y: scroll;
}

</style>