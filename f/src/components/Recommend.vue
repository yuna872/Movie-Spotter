<template>
  <div class="movie-list">
    <div class="swiper-box">
      <!-- {{ recommendMoviesByFollowings }} -->

      <div class="semi-title">{{ userinfo?.nickname }}님이 좋아할 만한 컨텐츠</div>
      <div>
        <swiper class="swiper" :options="swiperOption">
          <swiper-slide class="swiper-slide" v-for="(movie, index) in recommendMovies?.slice(20,40)" :key="`n-${index}`">
            <MovieItem class="movie-item1" :movie="movie"/>
          </swiper-slide>
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
      </div>
    </div>
    <div class="swiper-box"  v-if="recommendMovies">
      <div class="semi-title">{{ userinfo?.nickname }}님의 친구들은 이 영화!</div>
      <div>
        <swiper class="swiper" :options="swiperOption">
          <swiper-slide class="swiper-slide" v-for="(movie, index) in recommendMovies?.slice(0,20)" :key="`n-${index}`">
            <MovieItem class="movie-item1" :movie="movie"/>
          </swiper-slide>
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
      </div>
    </div>
    </div>
</template>

<script>
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import MovieItem from '@/components/MovieItem';
import axios from 'axios'
import jwt_decode from "jwt-decode"

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Recommend',
  components: {
    MovieItem,
    swiper,
    swiperSlide,
  },
  data() {
    return {
      userinfo:null,
      recommendMovies: null,
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
    getRecommend() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
          method: 'post',
          url: `${API_URL}/movies/recommend/`,
          data: {
            user_id: now_user_id,
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.recommendMovies = res.data
          console.log(res.data)
        })
        .catch((err)=>{console.log(err)})
    },
  },
  created() {
    this.getRecommend()
    if (localStorage.getItem('jwt')) {
      this.getuserinfo()
    }
  }

}
</script>

<style>

</style>