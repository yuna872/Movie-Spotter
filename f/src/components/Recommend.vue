<template>
  <div class="movie-list">



   


        <div id="carouselExampleInterval" class="carousel slide container" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active inner-container" data-bs-interval="1000">
          <img :src="`https://image.tmdb.org/t/p/original/${ recommendMoviesByMyLikes?.[0].poster_path }`" class="w-50 poster" >
        </div>
        <div class="carousel-item" data-bs-interval="1000">
          <img :src="`https://image.tmdb.org/t/p/original/${ recommendMoviesByMyLikes?.[1].poster_path }`" class=" w-50 poster" >
        </div>
        <div class="carousel-item" v-for="(movie,index) in recommendMoviesByMyLikes?.slice(2)" :key="`n-${index}`">
          <img :src="`https://image.tmdb.org/t/p/original/${ movie?.poster_path }`" class=" w-50 poster" >
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
    getRecommendByMyLikes() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
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
          console.log(res.data)
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
.movie-list {
  /* height : 90vh; */
  margin-top: 3vh;
  width : 30vw;
  border : 2px solid blue
}
.swiper-box {
  border : 2px solid red;
}
.poster {
  border-radius: 20px;
}

.container {
  border : 3px solid pink;
}
</style>