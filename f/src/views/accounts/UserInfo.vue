<template>
  <div class="user-info">
    <h3>회원 정보 페이지</h3>
    <p>{{userinfo.username}}님 안녕하세요?</p>
    <p>제 닉네임은 {{userinfo.nickname}} 입니다.</p>
    <p>팔로워: {{userinfo.followers.length}} | 팔로잉: {{userinfo.followings.length}}</p>
    <p>팔로워들 : {{userinfo.followers}}</p>
    <button @click='follow'>{{is_follow}}</button>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UserInfo',
  data() {
    return {
      userinfo : null,
      is_follow : null,
    }
  },
  created() {
    const token = localStorage.getItem('jwt')
    axios({
        method: 'get',
        url: `${API_URL}/accounts/${this.$route.params.id}`,
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
  methods: {
    follow() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.$route.params.id}/follow/`,
        data: {
          user_id: now_user_id
        },
        headers: {
          'Authorization' : `Bearer ${token}`
        }
      })
        .then((res) => {
          if (res.data === true){
            this.is_follow = '언팔로우'
          } else if (res.data === false) {
            this.is_follow = '팔로우'
          }       
        })
        .catch((err)=>{console.log(err)})

      
    }
  
  }
}
  

</script>

<style>

</style>