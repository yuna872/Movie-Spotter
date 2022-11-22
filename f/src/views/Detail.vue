<template>
  <div class="detail">
    <div class="detail-bg">
      <div class="detail-content">
        <div class="detail-title">{{ movie?.title }}</div>
        <div style="display:flex;align-items:center;">
          <div class="detail-vote"><i class="fa-solid fa-star fa-sm" style="color:#F6BE00"></i>&nbsp;{{ movie?.['vote_average'] }}</div>
          <div class="detail-adult">{{ movie?.adult ? "청소년 관람 불가" : "청소년 관람 가능" }}</div>
        </div>
        <div class="detail-date">개봉일: {{ movie?.['release_date'].slice(0,4) }}년 {{ movie?.['release_date'].slice(5,7) }}월 {{ movie?.['release_date'].slice(8) }}일</div>
        <div class="detail-overview">{{ movie?.overview }}</div>
        <div class="detail-video">
          <div>
            예고편 보러가기
          </div>
        </div>
        {{ movie?.video }}
      </div>
    </div>
    <div class="detail-box" :style="{'backgroundImage':`url(${backdropUrl})`}">
    </div>
    <div class="review-box">
      <!-- 리뷰 작성 모달 -->
      <div class="black-bg" v-if="is_show == true" >
        <ReviewForm 
          @modal-toggle="modalToggle"
          v-if="is_show" 
          @add-review="getReviews" 
          :movie="movie"
          v-click-outside="onClickOutside"
          :star="star"
        />
      </div>
      <!-- 리뷰 리스트  -->
      <div class="review-list-box">
        <div class="review-left-box">
          <div class="review-left-top">
            <div class="rank-avg">{{ rankAverage? rankAverage : "첫번째 리뷰를 작성해보세요" }}</div>
            <div class="star-box">
              <div class="star"> <div class="star-div">
                <star-rating
                  v-model="star"
                  :increment="0.5"
                  :star-size="30"
                  :clearable="true"
                  :show-rating="false"
                />
              </div></div>
              <div class="review-count">총 {{ reviews.length }}개의 리뷰</div>
        </div>
          </div>
          <div class="review-left-bottom" @click="modalToggle">
              <div class="content1">{{ movie?.title }} 어떠셨나요?</div> 
              <div class="content2">다른 사용자가 참고할 수 있도록 리뷰를 남겨보세요</div>
              <div class="star-div">
                <star-rating
                  v-model="star"
                  :increment="0.5"
                  :star-size="30"
                  :clearable="true"
                  :show-rating="false"
                />
              </div>
            </div>
        </div>
        <div class="review-right-box scroll-div">
          <ReviewItem
            v-for="(review, index) in reviews"
            :key="index"
            :review="review"
            @deleted="getReviews"
          />
        </div>
      </div>
    </div>
    <div class="similar-box">
      <SimilarList :genres="movie?.genres" :movieTitle="movie?.title"/>
      <!-- {{ movie?.genres }} -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import vClickOutside from 'v-click-outside'
import StarRating from 'vue-star-rating'

import ReviewForm from '@/components/ReviewForm';
import ReviewItem from '@/components/ReviewItem';
import SimilarList from '@/components/SimilarList';


const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'Detail',
  components: {
    ReviewForm,
    ReviewItem,
    SimilarList,
    StarRating,
  },
  data() {
    return {
      star : null,
      movie : null,
      movie_id : this.$route.params.id,
      reviews: [],
      is_show : false,
    }
  },
  beforeRouteUpdate(to, from, next){
    console.log(to.params.id)
    this.movie_id = to.params.id
    this.getMovieDetail()
    next()
  },
  directives: {
    clickOutside: vClickOutside.directive
  },
  computed: {
    backdropUrl() {
      return `https://image.tmdb.org/t/p/original/${this.movie?.backdrop_path}`
    },
    rankAverage(){
      const total = this.reviews?.reduce((total, review) => total + review.rank, 0)
      return Math.round(total / this.reviews?.length, 2).toFixed(1)
    },
    videoUrl() {
      return `http://www.youtube.com/embed/${this.movie?.video}`
    },
  },
  methods: {
    getMovieDetail() {
      axios({
        method : 'get',
        url : `${API_URL}/movies/${this.movie_id}`
      })
      .then((res)=>{
        this.movie = res.data
      })
      .catch((err)=>{console.log(err)})
    },
    getReviews() {
      this.movie_id = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie_id}/reviews/`
      })
      .then((res)=>{
        this.reviews = res.data
      })
      .catch((err)=>{console.log(err)})
    },
    modalToggle() {
      this.is_show = !this.is_show
      this.star = null
    },
    onClickOutside() {
      this.is_show = !this.is_show
    }
  },
  created() {
      this.getMovieDetail()
      this.getReviews()
  }
}
</script>

<style>
.detail-bg {
  position : absolute;
  top:0;right:0;left:0;bottom:200vh;
  background: linear-gradient(
    to left,
      rgba(20, 20, 20, 0) 10%,
      rgba(20, 20, 20, 0.25) 25%,
      rgba(20, 20, 20, 0.5) 50%,
      rgba(20, 20, 20, 0.9) 75%,
      rgba(20, 20, 20, 1) 100%
  );
  background: linear-gradient(
    60deg, rgba(0,0,0,1) 20%, rgba(0,0,0,0.5) 100%
    );
}
/* 영화 세부 정보 */
.detail-box {
  width : 100vw;
  height : 100vh;
  background-size: cover; 
  background-repeat: no-repeat;
  background-position: center;
}

.detail-content {
  text-align: left;
  height: 40%;
  position: absolute;
  bottom : 20vh;
  left : 5vw;
}

.detail-title {
  font-size:2.5em;
}
.detail-vote {
  font-size:2em;
}
.detail-adult {
  font-size:1.2em;
  text-decoration-line: underline;
  margin-left : 20px;
}
.detail-date {
  font-size:1.2em;
}
.detail-overview {
  font-size:1.2em;
  width : 30vw;
  margin : 30px 0; 
}
.detail-video {
  border: 3px solid white;
  width : 15vw;
  border-radius: 50px;
  height : 60px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  padding : 5px;
}


/* 리뷰 컴포넌트 */
.review-box {
  width : 100vw;
  height : 100vh;
  display: flex;
  align-items: center;
}

.review-list-box {
  display: flex;
  background-color:  #343440;
  width : 85%; 
  height: 70%;
  margin : auto;
  justify-content: space-between;
}

.review-left-box {
  display: flex;
  flex-direction: column;
  width : 35%;
  margin : 5%
}

.review-left-top {
  display: flex;
} 
.review-left-bottom {
  border: solid 1px white;
  width : 100%;
  margin : auto;
  display: flex;
  flex-direction: column;
  margin-top : 4vh;
  justify-content: flex-start;
  text-align: center;
  padding : 10%;
}
.content1 {
  width : 90%;
  margin : 10px auto;
  font-size : 1.2em;
}
.content2 {
  width : 90%;
  margin : 10px auto;
  font-size : 1.1em;
}
.review-right-box {
  display: flex;
  flex-direction: column;
  width : 55%;
  margin : 5%;
  overflow-y: scroll;
}

.rank-avg {
  font-size: 5em;
  width : 50%;
  height : 100%;
}

.star-box {
  width : 50%;
  display:flex;
  flex-direction:column;
}


.star {
  height : 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.review-count {
  height : 50%;
  font-size: 1.3em;
  padding : 10px;
}

/* 모달 클릭시 배경 어둡게 */
.black-bg {
  position: fixed;
  top:0; left: 0; bottom: 0; right: 0;
  background: rgba(0, 0, 0, 0.6);
}


/* 비슷한 콘텐츠 */
.similar-box {
  width : 100vw;
  height : 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>