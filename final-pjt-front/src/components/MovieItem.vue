<template>
  <div :style="{'backgroundImage':`url(${posterUrl})`}">
    <!-- 좋아요 버튼 -->
    <div v-if="isLogin" class="like-btn-p">
      <button @click="movieLike" class='like-btn' v-if="!is_like">
        <i class="fa-solid fa-heart" style="color:red"></i></button>
      <button @click="movieLike" class='like-btn' v-if="is_like">
        <i class="fa-regular fa-heart" style="color:red"></i></button>
    </div>
    <!-- 아이템 배경 -->
    <div @click="goDetail" class="item-hover">
      <div style="font-weight:bold">{{ movie?.title }}</div>
      <div>
        <i class="fa-solid fa-star fa-sm" style="color:#F6BE00"></i> {{ movie?.['vote_average'] }}
      </div>
      <p><i class="fa-solid fa-thumbs-up"></i> {{ movieinfo?.like_users.length }} likes</p>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieItem',
  props: {
    movie : Object,
  },
  data() {
    return {
      isLogin : localStorage.getItem('jwt') ? true : false,
      is_like: null,
      movieinfo : null,
    }
  },
  beforeRouteUpdate(to, from, next){
    console.log(to.params)
    this.movie = to.params.movie
    next()
  },
  computed:{
    posterUrl() {
      // 포스터 이미지가 있는 경우에만
      if (this.movie?.poster_path != undefined){
        return `https://image.tmdb.org/t/p/original/${this.movie?.poster_path}`
      } else {
        return 'https://ifh.cc/g/8DmqKt.png'
      }
    }
  },
  methods: {
    goDetail() {
      this.$router.push({name: 'detail', params: { id : this.movie.id }})
    },
    movieLike() {

      if (!localStorage.getItem('jwt')) {
        alert('로그인이 필요한 서비스 입니다!')
        return
      }
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
          method: 'post',
          url: `${API_URL}/movies/${this.movie.id}/movielikes/`,
          data: {
            user_id: now_user_id
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.is_like = res.data
          this.getMovieLikeInfo()
        })
        .catch((err)=>{console.log(err)})
    },
    getMovieLikeInfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie.id}/`,
        headers: {
            'Authorization' : `Bearer ${token}`
        }
      })
        .then((res) => {
          this.movieinfo = res.data
          if (this.movieinfo.like_users.includes(now_user_id)) {
            this.is_like = false
          } else {
            this.is_like = true
          }
        })
        .catch((err)=>{console.log(err)})
    }
  },
  created() {
    this.getMovieLikeInfo()
  }
}
</script>

<style>
.movie-item1 {
  position: relative;
  padding-top : 150%;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  border-radius: 10px;
  border: none;
  opacity: 0.8;
  color : black;
}

.movie-item2 {
  position: relative;
  width : 16vw;
  padding-bottom :150%;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  border: none;
  border-radius: 10px;
}

.item-hover:hover {
    background-color : white;
    opacity: 0.8;
    color : black;
  }

.item-hover {
    border-radius: 10px;
    position: absolute;
    top:0;
    right:0;
    left :0;
    bottom :0;
    opacity: 0;
    display: flex;
    flex-direction : column;
    justify-content: center;
    justify-items: center;
    text-align : center;
    font-size : 30px;
  }

  .item-hover p {
    font-size: 20px;
  }

.like-btn-p {
  position: absolute;
  top:5px;bottom:0;left:0;
}
.like-btn {
    width :40px;
    height : 40px;
    border-radius: 50%;
    background-color: white;
    border: none;
    filter: drop-shadow(0px 0px 2px gray);
    opacity: 0.75;
    position: absolute;
    top: 1; right: 1;
    z-index: 1;
  }

</style>