<template>
  <div class="review-form">
    <form @submit.prevent="postReview">
      <input type="number" v-model="star">
      <input type="text" @input="content=$event.target.value" maxlength='200' placeholder="영화 리뷰를 작성해주세요.">
      <button>리뷰 등록</button>
    </form>
  </div>
  
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'ReviewForm', 
  data() {
    return {
      star : null,
      content : null,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    postReview() {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie?.id}/reviews/`,
        data: {
          rank: this.star,
          content: this.content,
        }
      })
      .then(()=>{
        this.$emit('add-review')
        return
      })
      .catch((err)=>{console.log(err)})
    },
  },
}
</script>

<style>

</style>