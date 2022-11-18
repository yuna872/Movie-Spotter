<template>
  <div class="review-form">
    <form @submit.prevent="postReview">
      <input type="number" v-model="star">
      <input type="text" @input="content=$event.target.value" maxlength='200' placeholder="영화 리뷰를 작성해주세요.">
      <button>리뷰 등록</button>
    </form>
    <div class="review-list">
      <h3>리뷰 리스트 컴포넌트</h3>
      {{ reviews }}
      <ReviewItem/>
    </div>
  </div>
  
</template>

<script>
import axios from 'axios';
import ReviewItem from '@/components/ReviewItem';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'ReviewList',
  components: {
    ReviewItem,
  },
  props:{
    movie: Object,
  },  
  data() {
    return {
      reviews : [],
      star : null,
      content : null,
    }
  },
  methods: {
    getReviews() {
      console.log(this.movie,'🚅')
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie?.id}/reviews/`
      })
      .then((res)=>{
        this.reviews = res.data
      })
      .catch((err)=>{console.log(err)})
    },
    postReview() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie.id}/reviews/`,
        data: {
          rank: this.star,
          content: this.content,
        }
      })
      .then(()=>{
        return
      })
      .catch((err)=>{console.log(err)})
    }
  },
  created() {
    this.getReviews()
  }
}
</script>

<style>

</style>