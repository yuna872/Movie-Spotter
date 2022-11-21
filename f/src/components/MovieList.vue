<template>
  <!-- 로그인, 비로그인 사용자에게 공통적으로 추천하는 영화들 -->
  <div class="movie-list">
    <div class="swiper-box">
      <div class="semi-title">따끈따끈 최신작 TOP 20</div>
      <div>
        <md-card>
          <md-card-media>
            <!-- swiper -->
            <swiper class="swiper" :options="swiperOption">
              <swiper-slide v-for="(movie, index) in newMovies" :key="`n-${index}`">
                <MovieItem :movie="movie"/>
              </swiper-slide>
              <div class="swiper-button-prev" slot="button-prev"></div>
              <div class="swiper-button-next" slot="button-next"></div>
            </swiper>
          </md-card-media>
        </md-card>
      </div>
    </div>
    <div class="swiper-box">
      <div class="semi-title">투표수가 가장 많은</div>
      <div>
        <md-card>
          <md-card-media>
            <!-- swiper -->
            <swiper class="swiper" :options="swiperOption">
              <swiper-slide v-for="(movie, index) in hotMovies" :key="`h-${index}`">
                <MovieItem :movie="movie"/>
              </swiper-slide>
              <div class="swiper-button-prev" slot="button-prev"></div>
              <div class="swiper-button-next" slot="button-next"></div>
            </swiper>
          </md-card-media>
        </md-card>
      </div>
    </div>
    <div class="swiper-box">
      <div class="semi-title">국내 영화 TOP 20</div>
      <div>
        <md-card>
          <md-card-media>
            <!-- swiper -->
            <swiper class="swiper" :options="swiperOption">
              <swiper-slide v-for="(movie, index) in koreanMovies" :key="`k-${index}`">
                <MovieItem :movie="movie"/>
              </swiper-slide>
              <div class="swiper-button-prev" slot="button-prev"></div>
              <div class="swiper-button-next" slot="button-next"></div>
            </swiper>
          </md-card-media>
        </md-card>
      </div>
    </div>
    <div class="swiper-box">
      <div class="semi-title">해외 영화 TOP 20</div>
      <div>
        <md-card>
          <md-card-media>
            <!-- swiper -->
            <swiper class="swiper" :options="swiperOption">
              <swiper-slide v-for="(movie, index) in internationalMovies" :key="`i-${index}`">
                <MovieItem :movie="movie"/>
              </swiper-slide>
              <div class="swiper-button-prev" slot="button-prev"></div>
              <div class="swiper-button-next" slot="button-next"></div>
            </swiper>
          </md-card-media>
        </md-card>
      </div>
    </div>  
  </div>
</template>

<script>
// import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import MovieItem from '@/components/MovieItem.vue'

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
          loop: true,
          loopFillGroupWithBlank: true,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        }
    }
  },  
  props:{
    movies : Array,
  },
  computed: {
    newMovies() {
      const tmpArr1 = this.movies?.map((movie)=>{
        movie['release_date'] = parseInt(movie?.['release_date'].replace(/\-/g,''))
        return movie
      })
      
      tmpArr1?.sort(function (a, b){
        return b['release_date'] - a['release_date']
      })

      if (tmpArr1.length <= 20) {
        return tmpArr1.slice(0, tmpArr1.length)
      } else {
        return tmpArr1.slice(0, 20)
      }
      
    },
    // 국내 영화
    koreanMovies(){
      const tmpArr2 = this.movies?.filter((movie)=>{
            return movie['original_language'] === 'ko'
      })

      if (tmpArr2.length <= 20) {
        return tmpArr2.slice(0, tmpArr2.length)
      } else {
        return tmpArr2.slice(0, 20)
      }
    },
    // 해외영화
    internationalMovies() {
       const tmpArr3 =  this.movies?.filter((movie)=>{
            return movie['original_language'] != 'ko'
      })

      if (tmpArr3.length <= 20) {
        return tmpArr3.slice(0, tmpArr3.length)
      } else {
        return tmpArr3.slice(0, 20)
      }
    },
    hotMovies() {
      // 리스트 깊은 복사
      const tmpMovies = this.movies?.slice()
      // 투표수를 기준으로 모든 영화에 대하여 내림차순 정렬
      tmpMovies?.sort(function (a, b){
        return b['vote_count'] - a['vote_count']
      })

      if (tmpMovies.length <= 20) {
        return tmpMovies.slice(0, tmpMovies.length)
      } else {
        return tmpMovies.slice(0, 20)
      }
    },
  },
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
  border-radius: 10px;
  padding-top : 2vh;
  text-align: left;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}
.swiper-box:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  scale : 1.05;
}

.swiper-slide {
  width : 16vw;
  height : 24vh;
  /* border: solid 2px red; */
  padding : 0;
}

.swiper {
  width : 100%;
  /* border: solid 2px red; */
  height : 30vh;
  padding : 3vh;
}

.semi-title {
  font-size : 2em;
  padding-left : 3vw;
}


</style>