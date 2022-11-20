<template>
  <div class="review-item">
    <div @click="goProfile">{{ review.writer }}님 작성</div>
    <div>{{ review.content }}</div>
    <div>{{ review.rank }}</div>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: Object,
  },
  methods: {
    goProfile() {
      this.$router.push({name: 'userinfo', params: {id : this.review.user}})
    }
  }
}
</script>

<style>

</style>