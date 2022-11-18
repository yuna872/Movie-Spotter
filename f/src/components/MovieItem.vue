<template>
  <div class="movie-item" @click="goDetail" :style="{'backgroundImage':`url(${posterUrl})`}">
    {{ movie?.title }}
    {{ movie?.['vote_average'] }}
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie : Object,
  },
  computed:{
    posterUrl() {
      return `https://image.tmdb.org/t/p/w500/${this.movie?.poster_path}`
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
  width : 15vw;
  height : 25vw;
  background-size: cover;
  margin-top : 10px;
}
</style>