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
    getSimilarList() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`
      })
      .then((res)=>{
        // 평점을 기준으로 모든 영화에 대하여 내림차순 정렬
        const movieAll = res.data.sort(function (a, b){
          return b['vote_average'] - a['vote_average']
        })


        this.similarList = movieAll.filter((movie)=>{
          for (const genre of this.genres) {
            const movieGenres = movie.genres.map((genre)=>{
              return genre.id
            }) 
            return movieGenres.includes(genre.id)
          }
        })

        if (this.similarList.length <= 10) {
          return this.similarList.slice(0, this.similarList.length)
        } else {
          this.similarList = _.sampleSize(this.similarList, 10)
        }
      })
      .catch((err)=>{console.log(err)})
    }
  },
  created() {
    this.getSimilarList()
  }
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