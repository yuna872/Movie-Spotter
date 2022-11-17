<template>
  <div class="similar-list">
    <h3>비슷한 콘텐츠 컴포넌트</h3>
    <MovieItem/>
  </div>
</template>
 
<script>
import MovieItem from '@/components/MovieItem';
export default {
  name : 'SimilarList',
  components: {
    MovieItem,
  }
}
</script>

<style>

</style>