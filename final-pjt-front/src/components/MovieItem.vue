<template>
  <div class="movie-item" @click="goDetail">
    {{ movie?.title }}
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie : Object,
  },
  methods: {
    goDetail() {
      this.$router.push({name: 'detail', params: { id : this.movie.id }})
    }
  }
}
</script>

<style>

</style>