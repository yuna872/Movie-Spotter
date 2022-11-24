<template>
  <div class="userinfo">
    <div class="userinfo-top">
      <div class="userinfo-top-bg"></div>

      <div class="userinfo-top-box">
        <p class="info-id">{{ userinfo?.username }}님의 페이지</p>
        <p class="info-nickname">닉네임 : {{ userinfo?.nickname }} 😉</p>
        <!-- {{reviewinfo}} -->
        <p class="info-follow"><i class="fa-solid fa-user-group"></i> &nbsp; followers {{ userinfo?.followers.length }} &nbsp;&nbsp; | &nbsp;&nbsp; followings {{ userinfo?.followings.length }}</p>
      </div>
  
      <!-- 상세정보 -->
    </div>
    <div class="userinfo-top-top">
      <div class="review-wrap">
        <p style="font-size : 1.4em;margin-top:20px;">내가 쓴 리뷰 📑</p>
        <div v-if="reviewinfo?.length" class="myreview-list scroll-div">
          <div 
            v-for="(review, index) in reviewinfo" 
            :key="index"
            class="info-div"  
          > 
            <div class='review-rank'> <i class="fa-solid fa-star fa-sm" style="color:#F6BE00"></i> 
              &nbsp;{{ review?.rank }}
            </div>
          <div class='review-content'>🎬 <span style="text-decoration: underline; cursor:pointer" @click="goDetail(review)">{{ review?.movie.title }}</span> <p></p> {{ review?.content }}</div>
            <div style="text-align:center">
              <i class="fa-solid fa-thumbs-up"></i>&nbsp;
              {{ review?.like_users.length }}
            </div>
          </div>
        </div>
        <div v-else style="font-size:1.5em;">리뷰가 아직 없어요 :-(</div>
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
    <div class="about-us-btn" @click="toAboutUs">👨‍👧‍👧</div>
  </div>
</template>



<script>
import _ from 'lodash'
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
    goDetail(review) {
      this.$router.push({'name' : 'detail', params : { id : review.movie.id }})
    },
    toAboutUs() {
      this.$router.push({ name : 'aboutus' })
    },
  },
  
}
  

</script>

<style>

.userinfo {
  width : 100vw;
}

.userinfo-top {
  background-image: url('@/assets/caramel.jpg');
  background-size: cover;
  height : 40vh;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  color: black;
}


.userinfo-top-box {
  padding-top : 10vh;
  height : 100%;
  display: flex;
  flex-direction: column;
  background-color: rgba(0, 0, 0, 0.6);
}

.user-profile {
  width : 15vw;
  margin-left : 10vw;
  position: absolute;
  z-index: 1;
}


.info-id{
  font-size : 3em;
  color: white;
}

/* 리뷰 */

.review-wrap {
  margin-top : 5vh;
  justify-content: center;
  display: flex;
  flex-direction: column;
}

.info-div {
  text-align: left;
  justify-content: space-between;
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  font-size : 1.1em;
  align-items: center;
  background-color: rgba( 255, 255, 255, 0.2 );
  padding : 13px;
  width : 90%;
  margin : 15px auto;
  border-radius: 13px;
}



.info-nickname {
  font-size : 1.8em;
  color: white;
}

.info-follow {
  font-size : 1.2em;
  color: white;
}

.userinfo-top-bottom {
  height : 40%;
  margin-top : 10vh;
}

.myreview-list {
  height : 400px;
  width : 60%;
  margin : auto;
  overflow-y: scroll;
}

</style>