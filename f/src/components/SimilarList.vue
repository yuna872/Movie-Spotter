<template>
  <div class="similar-list">
    <h3>비슷한 콘텐츠 컴포넌트</h3>
    <div class="similar-list-box">
      <MovieItem
        v-for="(movie, index) in similarList"
        :key="`s-${index}`"
        :movie="movie"
      />
    </div>
  </div>
</template>
 
<script>
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
  },
  data() {
    return {
      similarList: [],
    }
  },
  methods: {
    getSimilarList() {
      // console.log(this.genres)
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

        console.log(this.similarList)

        if (this.similarList.length <= 20) {
          return this.similarList.slice(0, this.similarList.length)
        } else {
          return this.similarList.slice(0, 20)
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
.similar-list-box{
  width : 85vw;
  margin : auto;
  display: flex;
  flex-wrap: wrap;
}
</style>