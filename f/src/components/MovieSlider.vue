<template>
  <div class="slider-container" >
    슬라이더
    <!-- width : 16vw;
  height : 24vw; -->
    <button @click="pre" v-bind:class="{ hidden: currentNumber == 0 }">이전</button>
    <div class="slider" :style="{'transform': 'translate(-' + (currentNumber-1)*80 + 'vw, 0px)'}">
      <MovieItem
      v-for="(movie,index) in movies"
      :key="`q-${index}`"
      :movie="movie"
    />
    </div>
    <button @click="next" v-bind:class="{ hidden: currentNumber == length }">다음</button>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem';

export default {
  name : 'MovieSlider',
  components: {
    MovieItem
  },
  props: {
    movies : Array,
  },
  data() {
    return {
      length : this.movies?.length,
      currentNumber : 0,
    }
  },
  methods: {
    next() {
      if (this.currentNumber == this.length) {
        this.currentNumber = 0;
      } else {
        this.currentNumber = this.currentNumber + 5;
      }
      console.log(this.currentNumber);
    },
    pre() {
      if (this.currentNumber == 0) {
        this.currentNumber = this.length;
      } else {
        this.currentNumber = this.currentNumber - 5;
      }
      console.log(this.currentNumber);
    }
  }
}
</script>

<style>
.slider-container {
  width : 100%;
  display: flex;
  border : solid 2px blue;
  overflow: hidden;
}
.slider {
  width : 100%;
  display: flex;
  border : solid 2px blue;
}

.pre {
  position: absolute;
  left: 5px;
  top: 50%;
  cursor: pointer;
}
.next {
  position: absolute;
  right: 5px;
  top: 50%;
  cursor: pointer;
}

.hidden {
  display: hidden;
}

</style>