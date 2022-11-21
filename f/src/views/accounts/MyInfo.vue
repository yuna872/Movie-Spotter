<template>
  <div class="user-info">
    <div class="user-info-box">
      <p>{{ userinfo?.username }}님의 마이 페이지</p>
      <p>제 닉네임은 {{ userinfo?.nickname }} 입니다.</p>
      <p>팔로워: {{ userinfo?.followers.length }} | 팔로잉: {{ userinfo?.followings.length }}</p>
      <p>내가 좋아요한 영화는 {{ userinfo?.like_movies }}</p>
      <p>내가 쓴 리뷰 {{ reviewinfo }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyInfo',
  data() {
    return {
      userinfo : null,
      reviewinfo : null,
    }
  },
  created() {
    this.getuserinfo()
    this.getuserreviews()
  },
  methods: {
    getuserinfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
          method: 'get',
          url: `${API_URL}/accounts/${now_user_id}`,
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.userinfo = res.data
          console.log(this.userinfo)
        })
        .catch((err)=>{console.log(err)})
    },
    getuserreviews() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      
      axios({
          method: 'get',
          url: `${API_URL}/movies/reviews/${now_user_id}`,
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.reviewinfo = res.data
        })
        .catch((err)=>{console.log(err)})
    },
  },
}
  

</script>

<style>

.user-info-box {
  margin : 100px auto;

}

</style>