<template>
  <div class="movie-item" @click="goDetail" :style="{'backgroundImage':`url(${posterUrl})`}">
    {{ movie?.title }}
    {{ movie?.['vote_average'] }}
    <button @click="movieLike">{{ is_like }}</button>
  </div>
</template>

<script>
import axios from 'axios'
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
        })
        .catch((err)=>{console.log(err)})
    },
    getMovieLikeInfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
        method: 'get',
        url: `${API_URL}/movies/${movie.id}/`,
      })
      .then((res) => {
        this.movieinfo = res.data
        if (this.movieinfo.like_movies.includes(now_user_id)) {
          this.is_like = false
        } else {
          this.is_like = true
        }
      })
    }
  },
  created() {
    getMovieLikeInfo()
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
}
</style>