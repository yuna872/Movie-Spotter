<template>
  <div class="userinfo">
    <div class="userinfo-box">
    <div class="userinfo-top">
      <!-- 상세정보 -->
      <div class="userinfo-top-top">
        <p class="info-id">{{ userinfo?.username }}님의 마이 페이지</p>
        <p class="info-nickname">닉네임 : {{ userinfo?.nickname }} 😉</p>
        <p class="info-follow"><i class="fa-solid fa-user-group"></i> &nbsp; followers {{ userinfo?.followers.length }} &nbsp;&nbsp; | &nbsp;&nbsp; followings: {{ userinfo?.followings.length }}</p>
        <p style="font-size : 1.4em;margin-top:20px;">내가 쓴 리뷰 📑</p>
        <div class="myreview-list scroll-div">
          
          <div 
            v-for="(review, index) in reviewinfo" 
            :key="index"
            class="info-div"  
          > 
            <div> <i class="fa-solid fa-star fa-sm" style="color:#F6BE00"></i> 
              &nbsp;{{ review.rank }}점
            </div>
           <p>
            <!-- {{ movies.id }} -->
           </p>
           <p>{{ review.content }}</p>
            <p>
              <i class="fa-solid fa-thumbs-up"></i>&nbsp;
              {{ review.like_users.length }}&nbsp;likes
            </p>
          </div>
        </div>
      </div>
      <div class="userinfo-top-bottom">
      <!-- 좋아요 누른 영화 -->
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
  height : 100vh;
}
.userinfo-box {
  display: flex;
  flex-direction: column;
  width : 90%;
  margin : auto;
}
.userinfo-top {
  height : 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;


}
.userinfo-top-top {
  height : 40%;
  width : 70%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin : auto;
  /* border : solid 2px red; */

}

.userinfo-top-top p {
  text-align: center;
  margin-bottom: 5px;
}

.info-div {
  display: flex;
  justify-content: space-evenly;
  font-size : 1.1em;
  align-items: center;
  border-bottom: solid 2px white;
  padding-bottom : 10px;
  width : 90%;
  margin : auto;
}

.info-div p {
  font-size : 1.1em;
}
.info-id {
  font-size : 2.5em;
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
  /* border : solid 2px red; */
  height : 50%;
  width : 60%;
  margin : auto;
  overflow-y: scroll;
}

</style>