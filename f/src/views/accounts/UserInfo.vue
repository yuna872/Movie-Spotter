<!-- <template>
  <div class="user-info">
    <div class="user-info-box">
      <p>{{ userinfo?.username }}님의 페이지</p>
      <p>이분의 닉네임은 {{ userinfo?.nickname }} 입니다.</p>
      <p>팔로워: {{ userinfo?.followers.length }} | 팔로잉: {{ userinfo?.followings.length }}</p>
      <button @click='follow'>{{ is_follow }}</button>
    </div>
  </div>
</template> -->
<template>
  <div class="userinfo">
    <div class="userinfo-box">
    <div class="userinfo-top">
      <!-- 상세정보 -->
      <div class="userinfo-top-top flex-div" >
        <p class="info-id">{{ userinfo?.username }}님의 페이지</p>
        <p class="info-nickname">닉네임 : {{ userinfo?.nickname }} 😉</p>
        <p class="info-follow"><i class="fa-solid fa-user-group"></i> &nbsp; followers {{ userinfo?.followers.length }} &nbsp;&nbsp; | &nbsp;&nbsp; followings {{ userinfo?.followings.length }}</p>
        <div @click='follow' class="info-follow-btn">
          <div>{{ is_follow }}</div></div>
      </div>
    </div>
  </div>
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
    this.getuserinfo()
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
            this.is_follow = 'UnFollow'
          } else if (res.data === false) {
            this.is_follow = 'Follow'
          }
          this.getuserinfo()
        })
        .catch((err)=>{console.log(err)})
    },
    getuserinfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id
      if (now_user_id === this.$route.params.id) {
        this.$router.push({ name: 'myinfo' })
      } else {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/${this.$route.params.id}`,
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
          .then((res)=>{
            this.userinfo = res.data
            if (this.userinfo.followers.includes(now_user_id)) {
              this.is_follow = 'UnFollow'
            } else {
              this.is_follow = 'Follow'
            }
            console.log(this.userinfo)
          })
          .catch((err)=>{console.log(err)})
      }
      
    }
  },
}
  

</script>

<style>
.info-follow-btn {
  width : 20%;
  height : 50px;
  border : 3px solid white;
  margin: 20px auto;
  border-radius: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}


.flex-div {
  display: flex;
  flex-direction: column;
}
</style>