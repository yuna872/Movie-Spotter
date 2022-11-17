<template>
  <div class="recommend">
    <h3>로그인된 사용자에게 보여질 영화 추천 컴포넌트</h3>
    <MovieItem/>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem';

export default {
  name: 'Recommend',
  components: {
    MovieItem,
  },
  props: {
    movies: Array,
  },
  methods: {
    // 커뮤니티 기반 추천 알고리즘
    // 컨텐츠 기반 추천 알고리즘
  }

}
</script>

<style>

</style>