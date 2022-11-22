<template>
  <div class="review-form" >
      <button @click="modalToggle" class="x-btn">X</button>
      <div class="review-text">이 영화, 어떠셨나요?</div>
      <form @submit.prevent="postReview" class="form">
        <input type="number" v-model="star">
        <input class="review-content1" type="text" @input="content=$event.target.value" maxlength='200' placeholder="영화 리뷰를 작성해주세요.">
        <button class="review-submit">리뷰 등록</button>
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
      // 로그인 되어있지 않다면

      // 내용이 입력되지 않으면 alert
      if (this.star===null) {
        alert('별점을 입력하세요!')
        return
      } else if (this.content===null) {
        alert('내용을 입력하세요!')
        return
      }

      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      console.log(now_user_id)
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
        this.star = null
        this.content = null
        this.$emit('modal-toggle')
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

 .review-form{
  width : 60%;
  height: 50%;
  margin : auto;
  background: #343440; 
  border-radius: 5px;
  padding : 15px 0;
  position: absolute;
  top: 40vh; left: 20vw;
  z-index: 4;
}

.form {
  display: flex;
  flex-direction: column;
  width : 80%;
  /* height : 80%; */
  margin : auto;
  justify-content: space-between;
}

.x-btn {
  position: absolute;
  right: 10px;
}

.review-text {
  margin-top: 2rem;
  margin-bottom: 1rem;
}

.review-content1 {
  margin-top: 20px;
  margin-bottom: 20px;
  height: 9rem;
}

.review-submit {
  width: 30%;
  margin: auto;
}
</style>