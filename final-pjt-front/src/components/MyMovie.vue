<template>
  <div class="my-movie">
    <h3>My Movie 컴포넌트</h3>
    <MovieItem/> 
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem';

export default {
  name : "MyMovie",
  components: {
    MovieItem,
  }
}
</script>

<style>

</style>