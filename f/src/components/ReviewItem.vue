<template>
  <div class="review-item">
    <div class="review-item-left">
      <div v-if="review.rank === 1">
        <img src="@/assets/star_1.png" style="width : 15px; height : 15px;"></div>
      <div v-else-if="review.rank === 2">
        <img src="@/assets/star_2.png" style="width : 15px; height : 15px;"></div>
      <div v-else-if="review.rank === 3">
        <img src="@/assets/star_3.png" style="width : 30px; height : 15px;"></div>
      <div v-else-if="review.rank === 4">
        <img src="@/assets/star_4.png" style="width : 30px; height : 15px;"></div>
      <div v-else-if="review.rank === 5">
        <img src="@/assets/star_5.png" style="width : 45px; height : 15px;"></div>
      <div v-else-if="review.rank === 6">
        <img src="@/assets/star_6.png" style="width : 45px; height : 15px;"></div>
      <div v-else-if="review.rank === 7">
        <img src="@/assets/star_7.png" style="width : 60px; height : 15px;"></div>
      <div v-else-if="review.rank === 8">
        <img src="@/assets/star_8.png" style="width : 60px; height : 15px;"></div>
      <div v-else-if="review.rank === 9">
        <img src="@/assets/star_9.png" style="width : 75px; height : 15px;"></div>
      <div v-else>
        <img src="@/assets/star_10.png" style="width : 75px; height : 15px;"></div>
      <div>{{ review.rank }}.0</div>
    </div>
    <div class="review-item-right">
      <div><a @click="goProfile" style="text-decoration-line: underline;">{{ review.writer }}</a>님 작성</div>
      <div class="review-content">{{ review.content }}</div>
      <div class="review-submit-btn" @click="reviewLike" :class="{'review-like-btn': !is_like}">
        <div :class="{ 'review-like-thumbs': !is_like }"><i class="fa-solid fa-thumbs-up"></i></div>
        <div>도움이 돼요 {{ reviewinfo?.like_users.length }}</div>
      </div>
      <button @click="reviewDelete">DELETE</button>
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
    },
    reviewDelete() {
      const token = localStorage.getItem('jwt')

      axios({
        method: 'delete',
        url: `${API_URL}/movies/reviews/${this.review.id}/`,
        headers: {
            'Authorization' : `Bearer ${token}`
        }
      })
        .then((res) => {
          this.$emit("deleted")
          console.log(res)
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
  margin : 1.5vh auto;
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

.review-like-btn {
  border: solid 3px #F6BE00;
  color: #F6BE00;
}

.review-submit-btn:hover .review-like-thumbs {
  transform: scale( 1.4 ) skewX( 10deg );
  transition: 0.2s;
}

.review-content {
  font-size: 1.3em;
  margin-top : 5px;
}
</style>