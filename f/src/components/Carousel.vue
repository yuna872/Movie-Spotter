<template>
 <div id="carouselExampleInterval" class="carousel slide container by-likes" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active inner-container" data-bs-interval="1000">
            <img :src="`https://image.tmdb.org/t/p/original/${ recommendMovies?.[0].poster_path }`" class="poster" >
          </div>
          <div class="carousel-item" data-bs-interval="2000">
            <img :src="`https://image.tmdb.org/t/p/original/${ recommendMovies?.[1].poster_path }`" class="poster" >
          </div>
          <div class="carousel-item" v-for="(movie,index) in recommendMovies?.slice(2)" :key="`n-${index}`">
            <img :src="`https://image.tmdb.org/t/p/original/${ movie?.poster_path }`" class="poster" >
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
</template>

<script>
export default {
  name : 'Carousel',
  props: {
    recommendMovies : Array,
  },
}
</script>

<style>

</style>