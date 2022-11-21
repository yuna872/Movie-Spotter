<template>
  <div class="detail">
    <div class="detail-box" :style="{'backgroundImage':`url(${backdropUrl})`}">
      {{ movie?.title }}
      {{ movie?.title }}
      {{ movie?.['vote_average'] }}
      {{ movie?.adult }}
      {{ movie?.['release_date'] }}
      {{ movie?.['original_language'] }}
    </div>
    <div>
      {{ movie.genres }}
    </div>
    <div class="review-box">
      <!-- 리뷰 작성 모달 -->
      <div class="black-bg" v-if="is_show == true" >
        <ReviewForm 
          @modal-toggle="modalToggle"
          v-if="is_show" 
          @add-review="getReviews" 
          :movie="movie"
          v-click-outside="onClickOutside"
        />
      </div>
      <!-- 리뷰 리스트  -->
      <div class="review-list-box">
        <div class="review-left-box">
          <div>{{ rankAverage}}</div>
          <div></div>
          <button @click="modalToggle"> 리뷰 작성하기 </button>
        </div>
        <div class="review-right-box" >
          <ReviewItem
            v-for="(review, index) in reviews"
            :key="index"
            :review="review"
          />
        </div>
      </div>
    </div>
    <div class="similar-box">
      <SimilarList :genres="movie?.genres"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import vClickOutside from 'v-click-outside'

import ReviewForm from '@/components/ReviewForm';
import ReviewItem from '@/components/ReviewItem';
import SimilarList from '@/components/SimilarList';


const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'Detail',
  components: {
    ReviewForm,
    ReviewItem,
    SimilarList,
  },
  data() {
    return {
      movie : null,
      movie_id : this.$route.params.id,
      reviews: [],
      is_show : false,
    }
  },
  beforeRouteUpdate(to, from, next){
    console.log(to.params.id)
    this.movie_id = to.params.id
    this.getMovieDetail()
    next()
  },
  directives: {
    clickOutside: vClickOutside.directive
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/original/${this.movie?.backdrop_path}`
    },
    rankAverage(){
      const total = this.reviews?.reduce((total, review) => total + review.rank, 0)
      return total / this.reviews?.length
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method : 'get',
        url : `${API_URL}/movies/${this.movie_id}`
      })
        .then((res)=>{
          this.movie = res.data
          console.log(this.movie, '🚍')
        })
        .catch((err)=>{console.log(err)})
    },
    getReviews() {
      this.movie_id = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie_id}/reviews/`
      })
        .then((res)=>{
          this.reviews = res.data
        })
        .catch((err)=>{console.log(err)})
    },
    modalToggle() {
      this.is_show = !this.is_show
      // console.log(this.is_show)
    },
    onClickOutside() {
      this.is_show = !this.is_show
      // console.log(this.is_show)
    }
  },
  created() {
      this.getMovieDetail()
      this.getReviews()
  }
}
</script>

<style>
/* 영화 세부 정보 */
.detail-box {
  width : 100vw;
  height : 100vh;
  background: linear-gradient(
    to left,
      rgba(20, 20, 20, 0) 10%,
      rgba(20, 20, 20, 0.25) 25%,
      rgba(20, 20, 20, 0.5) 50%,
      rgba(20, 20, 20, 0.75) 75%,
      rgba(20, 20, 20, 1) 100%
  );
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
}

/* 리뷰 컴포넌트 */
.review-box {
  border: solid 2px red;
  width : 100vw;
  height : 100vh;
}

.review-list-box {
  display: flex;
  border: solid 2px red;
  width : 90%; 
  margin : auto;
}

.review-left-box {
  display: flex;
  flex-direction: column;
  border: solid 2px red;
  width : 30%;
}
.review-right-box {
  display: flex;
  flex-direction: column;
  border: solid 2px red;
  width : 60%;
}


/* 모달 클릭시 배경 어둡게 */
.black-bg {
  position: fixed;
  top:0; left: 0; bottom: 0; right: 0;
  background: rgba(0, 0, 0, 0.6);
}


/* 비슷한 콘텐츠 */
.similar-box {
  border: solid 2px green;
  width : 100vw;
  height : 100vh;
}
</style>