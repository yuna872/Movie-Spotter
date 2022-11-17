<template>
  <div class="recommend">
    <h3>로그인된 사용자에게 보여질 영화 추천 컴포넌트</h3>
    <MovieItem/>
    <MovieItem/>
    <MovieItem/>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem';

export default {
  name: 'Recommend',
  components: {
    MovieItem,
  }

}
</script>

<style>

</style>