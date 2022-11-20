<template>
  <div class="movie-item" :style="{'backgroundImage':`url(${posterUrl})`}">
    <div class="item-bg">
      {{ movie?.title }}
      {{ movie?.['vote_average'] }}
      <button @click="movieLike">{{ is_like }}</button>
      <p>{{ movieinfo?.like_users }}</p>
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
  height : 24vw;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  margin-top : 10px;
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

</style>