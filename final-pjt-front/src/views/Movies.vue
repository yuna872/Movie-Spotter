<template>
  <div class="movies">
    <h3>영화 목록 페이지</h3>
    <LoginRequest/>
    <Recommend/>
    <MovieList/>
  </div>
</template>

<script>
import LoginRequest from '@/components/LoginRequest';
import MovieList from '@/components/MovieList';
import Recommend from '@/components/Recommend';

export default {
  name: 'Movies',
  components: {
    LoginRequest,
    MovieList,
    Recommend,
  }
}
</script>
