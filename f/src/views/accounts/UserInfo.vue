<template>
  <div class="user-info">
    <h3>회원 정보 페이지</h3>
    <p>{{userinfo.username}}님 안녕하세요?</p>
    <p>제 닉네임은 {{userinfo.nickname}} 입니다.</p>
    <p>팔로워: {{userinfo.followers.length}} | 팔로잉: {{userinfo.followings.length}}</p>
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
    }
  },
  created() {
    const token = localStorage.getItem('jwt')
    axios({
        method: 'get',
        // 이거는 유나랑......
        url: `${API_URL}/accounts/3`,
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
  }

</script>

<style>

</style>