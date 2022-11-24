<template>
  <!-- 로그인, 비로그인 사용자에게 공통적으로 추천하는 영화들 -->
  <div class="movie-list">
    <div class="swiper-box">
      <div class="semi-title">따끈따끈 최신작 TOP 20</div>
      <div>
        <!-- swiper -->
        <swiper class="swiper" :options="swiperOption">
          <swiper-slide class="swiper-slide" v-for="(movie, index) in newMovies" :key="`n-${index}`">
            <MovieItem class="movie-item1" :movie="movie"/>
          </swiper-slide>
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
      </div>
    </div>
    <div class="swiper-box">
      <div class="semi-title">투표수가 가장 많은</div>
      <div>
          <!-- swiper -->
          <swiper class="swiper" :options="swiperOption">
            <swiper-slide class="swiper-slide" v-for="(movie, index) in hotMovies" :key="`h-${index}`">
              <MovieItem class="movie-item1" :movie="movie"/>
            </swiper-slide>
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
      </div>
    </div>
    <div class="swiper-box">
      <div class="semi-title">국내 영화 TOP 20</div>
      <div>
          <!-- swiper -->
          <swiper class="swiper" :options="swiperOption">
            <swiper-slide class="swiper-slide" v-for="(movie, index) in koreanMovies" :key="`k-${index}`">
              <MovieItem class="movie-item1" :movie="movie"/>
            </swiper-slide>
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
      </div>
    </div>
    <div class="swiper-box">
      <div class="semi-title">해외 영화 TOP 20</div>
      <div>
        <!-- swiper -->
        <swiper class="swiper" :options="swiperOption">
          <swiper-slide class="swiper-slide" v-for="(movie, index) in internationalMovies" :key="`i-${index}`">
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
// import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import MovieItem from '@/components/MovieItem.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name : 'MovieList',
  components: {
    MovieItem,
    swiper,
    swiperSlide
  },
  data: function() {
    return {
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
        },
      newMovies: null,
      koreanMovies: null,
      internationalMovies: null,
      hotMovies: null,
    }
  },  

  methods: {
    getRecommend() {
      
      axios({
          method: 'get',
          url: `${API_URL}/movies/recommendformainpage`,
        })
        .then((res)=>{

          this.newMovies = res.data.new_movies
          this.koreanMovies = res.data.korean_movies
          this.internationalMovies = res.data.international_movies
          this.hotMovies = res.data.hot_movies
        })
        .catch((err)=>{console.log(err)})
    },
  },
  created() {
    this.getRecommend()
  }
}
</script>


<style>
.movie-list {
  width : 90%;
  height : 90%;
  margin : auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.swiper-box {
  border-radius: 20px;
  padding : 0.5vh;
  margin : 3vh;
  text-align: left;
  /* border: solid 2px red; */
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}
.swiper-box:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  scale : 1.01;
  border-radius: 15px;
}

.swiper-slide {
  padding : 0;
  margin : 5px;
  border-radius: 15px;
}

.swiper {

  width :100%;
  height:100%;
  padding : 3vh;
  margin : 5px;
}

.semi-title {
  font-size : 2em;
}


</style>