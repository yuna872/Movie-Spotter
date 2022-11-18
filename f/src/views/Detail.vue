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
    <div class="review-box">
      <ReviewForm @add-review="getReviews" :movie="movie"/>
      {{ reviews }}
    </div>
    <div class="similar-box">
      <SimilarList :genres="movie?.genres"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ReviewForm from '@/components/ReviewForm';
import SimilarList from '@/components/SimilarList';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'Detail',
  components: {
    ReviewForm,
    SimilarList,
  },
  data() {
    return {
      movie : null,
      movie_id : null,
      reviews: [],
    }
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.movie?.backdrop_path}`
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method : 'get',
        url : `${API_URL}/movies/${this.$route.params.id}`
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
}

/* 리뷰 컴포넌트 */
.review-box {
  border: solid 2px red;
  width : 100vw;
  height : 100vh;
}

/* 비슷한 콘텐츠 */
.similar-box {
  border: solid 2px green;
  width : 100vw;
  height : 100vh;
}
</style>