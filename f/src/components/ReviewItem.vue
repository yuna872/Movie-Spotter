<template>
  <div class="review-item">
    <div class="review-item-left">
      ⭐⭐⭐⭐⭐
      <div>{{ review.rank }}</div>
    </div>
    <div class="review-item-right">
      <div><a @click="goProfile" style="text-decoration-line: underline;">{{ review.writer }}</a>님 작성</div>
      <div class="review-content">{{ review.content }}</div>
      <div class="review-submit-btn" @click="reviewLike">
        <div><i class="fa-solid fa-thumbs-up"></i></div>
        <div>도움이 돼요 {{ reviewinfo?.like_users.length }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewItem',
  props: {
    review: Object,
  },
  data() {
    return {
      is_like: null,
      reviewinfo : null,
    }
  },
  methods: {
    goProfile() {
      this.$router.push({name: 'userinfo', params: {id : this.review.user}})
    },
    reviewLike() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
          method: 'post',
          url: `${API_URL}/movies/${this.review.id}/reviewlikes/`,
          data: {
            user_id: now_user_id
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.is_like = res.data
          this.getReviewLikeInfo()
        })
        .catch((err)=>{console.log(err)})
    },
    getReviewLikeInfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
        method: 'get',
        url: `${API_URL}/movies/reviews/${this.review.id}/`,
        headers: {
            'Authorization' : `Bearer ${token}`
        }
      })
        .then((res) => {
          this.reviewinfo = res.data
          if (this.reviewinfo.like_users.includes(now_user_id)) {
            this.is_like = false
          } else {
            this.is_like = true
          }
        })
        .catch((err)=>{console.log(err)})
    }
  },
  created() {
    this.getReviewLikeInfo()
  }
}
</script>

<style>
.review-item {
  display: flex;
  margin : 10vh auto;
  width : 90%;
  border-bottom : solid 1px white;
  padding-bottom : 2vh; 
}

.review-item-left {
  width : 25%;
}
.review-item-right {
  width : 70%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
}

.review-submit-btn{
  font-size : 0.9em;
  margin-top : 15px;
  border: solid 3px white;
  width : 35%;
  height : 43px;
  border-radius: 50px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

.review-content {
  font-size: 1.3em;
  margin-top : 5px;
}
</style>