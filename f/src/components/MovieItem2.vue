<template>
  <div  
    class="firsttime-items"
    :style="{'backgroundImage':`url('https://image.tmdb.org/t/p/original/${movie?.poster_path}'`}">
    
  </div>
</template>

<script>
export default {
  name : 'MovieItem2',
  props : {
    movie : Object,
  },
  data() {
    return {
      is_liked : false
    }
  }
}
</script>

<style>

</style>