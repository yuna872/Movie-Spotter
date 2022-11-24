<template>

  <div class="userinfo">
    <div class="userinfo-top">
      <div class="userinfo-top-bg"></div>
      <div class="userinfo-top-box">
        <!-- {{userinfo}} -->
        <p class="info-id">{{ userinfo?.username }}님의 페이지</p>
        <p class="info-nickname">닉네임 : {{ userinfo?.nickname }} 😉</p>
        <p class="info-follow"><i class="fa-solid fa-user-group"></i> &nbsp; followers {{ userinfo?.followers.length }} &nbsp;&nbsp; | &nbsp;&nbsp; followings {{ userinfo?.followings.length }}</p>
        <div @click='follow' class="info-follow-btn" v-if="is_follow==='Follow'">
          <div>{{ is_follow }}</div>
        </div>
        <div @click='follow' class="info-unfollow-btn" v-if="is_follow==='UnFollow'">
          <div>{{ is_follow }}</div>
        </div>
      </div>
    </div>

    <div class="userinfo-top-bottom">
      <div class="swiper-box">
        <div>
          <div class="semi-title">{{ userinfo?.username }}님이 좋아하는 컨텐츠</div>
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
import axios from 'axios'
import jwt_decode from "jwt-decode"
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import MovieItem from '@/components/MovieItem.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UserInfo',
  components: {
    swiper,
    swiperSlide,
    MovieItem,
  },
  data() {
    return {
      userinfo : null,
      is_follow : null,
      movies: [],
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
    follow() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.$route.params.id}/follow/`,
        data: {
          user_id: now_user_id
        },
        headers: {
          'Authorization' : `Bearer ${token}`
        }
      })
        .then((res) => {
          if (res.data === true){
            this.is_follow = 'UnFollow'
          } else if (res.data === false) {
            this.is_follow = 'Follow'
          }
          this.getuserinfo()
        })
        .catch((err)=>{console.log(err)})
    },
    getuserinfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
     
      axios({
        method: 'get',
        url: `${API_URL}/accounts/${this.$route.params.id}`,
        headers: {
          'Authorization' : `Bearer ${token}`
        }
      })
        .then((res)=>{
          this.userinfo = res.data
          if (this.userinfo.followers.includes(now_user_id)) {
            this.is_follow = 'UnFollow'
          } else {
            this.is_follow = 'Follow'
          }
          this.getMovies()
        })
        .catch((err)=>{console.log(err)})
      
    },
    toAboutUs() {
      this.$router.push({ name : 'aboutus' })
    },
  },
}
  

</script>

<style>
.info-follow-btn {
  width : 20%;
  height : 50px;
  /* border : 3px solid white; */
  margin: 20px auto;
  border-radius: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: white;
  background-color: #0d6efd;
}

.info-unfollow-btn {
  width : 20%;
  height : 50px;
  /* border : 3px solid white; */
  margin: 20px auto;
  border-radius: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: white;
  background-color: #6c757d;
}

.flex-div {
  display: flex;
  flex-direction: column;
}
</style>