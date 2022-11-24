<template>
  <div  
    @click="modalLike"
    class="firsttime-items"
    :class="{'shadow-light': is_like}"
    :style="{'backgroundImage':`url(${posterUrl})`}">
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'MovieItem2',
  props : {
    movie : Object,
  },
  data() {
    return {
      is_like : false,
    }
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
    modalLike() {
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
          this.$emit('modal-like')
        })
        .catch((err)=>{console.log(err)})
    },
  }
}
</script>

<style>

</style>