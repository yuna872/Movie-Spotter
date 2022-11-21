<template>
  <div class="movie-item" :style="{'backgroundImage':`url(${posterUrl})`}">
    <div class="item-bg" @click="goDetail">
      {{ movie?.title }}
      {{ movie?.['vote_average'] }}

      <p>{{ movieinfo?.like_users.length }}</p>
    </div>
    <div v-if="isLogin" class="like-btn-p">
      <button @click="movieLike" class='like-btn' v-if="!is_like">
        <i class="fa-solid fa-heart fa-sm" style="color:red"></i></button>
      <button @click="movieLike" class='like-btn' v-if="is_like">
        <i class="fa-regular fa-heart fa-sm" style="color:red"></i></button>
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
.movie-item {
  width : 16vw;
  height : 24vh;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  border-radius: 10px;
}

.movie-item:hover .item-bg{
    background-color : white;
    opacity: 0.8;
    color : black;
  }

.item-bg {
    opacity: 0;
    width : 100%;
    height : 100%;
    display: flex;
    flex-direction : column;
    justify-content: center;
    justify-items: center;
    text-align : center;
    border-radius: 10px;
  }

.like-btn-p {
    position: relative;
    top : -98%; right : -2%;
}

.like-btn {
    width : 29px;
    height : 29px;
    border-radius: 50%;
    background-color: white;
    border: none;
    filter: drop-shadow(0px 0px 2px gray);
    opacity: 0.75;
    /* z-index: 3; */
  }

</style>