<template>
  <div class="movie-item" @click="goDetail" :style="{'backgroundImage':`url(${posterUrl})`}">
    {{ movie?.title }}
    {{ movie?.['vote_average'] }}
    <button>좋아요 버튼</button>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie : Object,
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
    }
  }
}
</script>

<style>
.movie-item {
  width : 16vw;
  height : 24vw;
  background-size: cover;
  margin-top : 10px;
}
</style>