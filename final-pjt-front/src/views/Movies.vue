<template>
  <div class="movies">
    <h3>영화 목록 페이지</h3>
    <LoginRequest/>
    <MovieList/>
  </div>
</template>

<script>
import LoginRequest from '@/components/LoginRequest';
import MovieList from '@/components/MovieList'

export default {
  name: 'Movies',
  components: {
    LoginRequest,
    MovieList,
  }
}
</script>
