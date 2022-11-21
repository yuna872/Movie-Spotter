<template>
  <div class="review-item">
    <div @click="goProfile">{{ review.writer }}님 작성</div>
    <div>{{ review.content }}</div>
    <div>{{ review.rank }}</div>
    <button @click="reviewLike">{{ is_like }}</button>
    <p>{{ reviewinfo?.like_users.length }}</p>
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

</style>