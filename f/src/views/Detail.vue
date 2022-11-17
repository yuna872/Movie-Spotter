<template>
  <div class="detail">
    <h3>영화 정보 상세 페이지</h3>
    {{ movie?.title }}
    {{ movie?.['vote_average'] }}
    {{ movie?.adult }}
    {{ movie?.['release_date'] }}
    {{ movie?.['original_language'] }}
    {{ movie?.genres }}
    <ReviewList/>
    <SimilarList/>
  </div>
</template>

<script>
import axios from 'axios'

import ReviewList from '@/components/ReviewList';
import SimilarList from '@/components/SimilarList';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'Detail',
  components: {
    ReviewList,
    SimilarList,
  },
  data() {
    return {
      movie : null,
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
      })
      .catch((err)=>{console.log(err)})
    }
  },
  created() {
    this.getMovieDetail()
  }
}
</script>

<style>

</style>