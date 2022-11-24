<template>
  <div class="similar-list">
    <div class="semi-title">"{{ movieTitle }}"와(과) 비슷한 컨텐츠</div>
    <div class="similar-list-box">
      <MovieItem
        v-for="(movie, index) in similarList"
        :key="`s-${index}`"
        :movie="movie"
        class="movie-item3"
      />
    </div>
  </div>
</template>
 
<script>
import _ from 'lodash';
import axios from 'axios';

import MovieItem from '@/components/MovieItem';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'SimilarList',
  components: {
    MovieItem,
   
  },
  props: {
    genres:Array,
    movieTitle: String,
  },
  data() {
    return {
      similarList: [],
    }
  },
  methods: {
    // 이건 뭔가요
    // 현재 무비의 장르들을 하나라도 포함하면 보여줘요
    // 10개 넘으면 랜덤으로 10개
    getSimilarList() {
      axios({
        method: 'POST',
        url: `${API_URL}/movies/similarmovies`,
        data: {
          genres: this.genres,
          title: this.movieTitle
        },
      })
      .then((res)=>{
        this.similarList = res.data
      })
      .catch((err)=>{console.log(err)})
    }
  },
  watch: {
    'genres': function() {
      this.getSimilarList()
    },
  }
  // created() {
  //   this.getSimilarList()
  // }
}
</script>

<style>
.similar-list {
  margin : auto;
  width : 90%;
  text-align: left;
}
.similar-list-box{
  width : 90vw;
  margin : auto;
  margin-top : 20px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
}

.movie-item3 {
  position: relative;
  width : 15vw;
  padding-bottom :130%;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
  border: none;
  border-radius: 10px;
  margin-bottom : 1vh;
}
</style>