<template>
  <div class="review-item">
    <p @click="goProfile">리뷰쓴이 : {{ review.user }}</p>
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