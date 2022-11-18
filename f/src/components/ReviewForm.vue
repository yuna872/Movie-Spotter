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
  props: {
    movie: Object,
  },
  data() {
    return {
      star : null,
      content : null,
    }
  },
  methods: {
    postReview() {
      axios({
        method: 'post',
        url: `${API_URL}/${this.movie.pk}/reviews/`
      })
    }
  }
}
</script>

<style>

</style>