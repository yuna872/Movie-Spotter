<template>
  <div class="similar-list">
    <h3>비슷한 콘텐츠 컴포넌트</h3>
    {{ genres }}
    {{ similarList }}
    <!-- <MovieItem/> -->
  </div>
</template>
 
<script>
import axios from 'axios';

// import MovieItem from '@/components/MovieItem';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'SimilarList',
  components: {
    // MovieItem,
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
        console.log(this.genres,'🚕')
        // 평점을 기준으로 모든 영화에 대하여 내림차순 정렬
        const movieAll = res.data.sort(function (a, b){
          return b['vote_average'] - a['vote_average']
        })

        while (this.similarList.length < 20) {
          movieAll.forEach((movie) => {
            
            for (const genre of this.genres) {
              if (this.genres.includes(genre)) {
                this.similarList.push(movie)
                break;
              }
            }
          });
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

</style>