<template>
  <div class="review-form">
    <form @submit.prevent="postReview">
      <input type="number" v-model="star">
      <input type="text" @input="content=$event.target.value" maxlength='200' placeholder="영화 리뷰를 작성해주세요.">
      <button @click="modalToggle">리뷰 등록</button>
    </form>
  </div>
  
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"


const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'ReviewForm', 
  data() {
    return {
      star : null,
      content : null,
      modal: false,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    postReview() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie?.id}/reviews/`,
        data: {
          rank: this.star,
          content: this.content,
          user_id: now_user_id
        }
      })
      .then(()=>{
        this.$emit('add-review')
        return
      })
      .catch((err)=>{console.log(err)})
    },
    modalToggle() {
      this.$emit('modal-toggle')
    }
  },
}

</script>

<style>
/* 모달창 */
.review-form {
  background-color:white; 
  justify-content:center; 
  align-items:center;    
  position:fixed;                      
  display:none; 
  padding:15px; 

}

</style>