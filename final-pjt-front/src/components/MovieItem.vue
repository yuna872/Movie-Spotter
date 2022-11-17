<template>
  <div class="movie-item">
    {{ movie?.title }}
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie : Object,
  }
}
</script>

<style>

</style>