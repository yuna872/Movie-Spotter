<template>
  <div class="detail">
    <div class="detail-bg">
      <div class="detail-content">
        <div style="display:flex;align-items:center;">
          <div class="detail-title">{{ movie?.title }}</div>
          <!-- 좋아요 버튼 -->
          <div v-if="is_login">
            <button @click="movieLike" class='like-btn1' v-if="!is_like">
              <i class="fa-solid fa-heart" style="color:red"></i>
            </button>
            <button @click="movieLike" class='like-btn1' v-if="is_like">
              <i class="fa-regular fa-heart" style="color:red"></i>
            </button>
          </div>
      </div>

        <div style="display:flex;align-items:center;">
          <div class="detail-vote"><i class="fa-solid fa-star fa-sm" style="color:#F6BE00"></i>&nbsp;{{ movie?.['vote_average'] }}</div>
        </div>
        <div class="detail-date">개봉일: {{ movie?.['release_date'].slice(0,4) }} / {{ movie?.['release_date'].slice(5,7) }} / {{ movie?.['release_date'].slice(8) }}</div>
        <div class="detail-genres">
          <!-- {{ movie?.genres }} -->
          <div class="detail-genre" 
            v-for="(genre, index) in movie?.genres"
            :key="index"
          >
          <p>#{{genre?.name}}</p>
          </div>
        </div>
        <div class="detail-overview">{{ movieOverview }}</div>
        <div v-if="movie?.video === 'novideo'">
          <div class="detail-video">
            예고편이 없습니다.
          </div>
        </div>
        <div v-else>
          <div class="detail-video" style="cursor:pointer" @click="onClickVideo">
            <div @click="onClickVideo" style="cursor:pointer">
              예고편 보러가기
            </div>
          </div>
        </div>
        <!-- 감독, 배우 출력 -->
        <div class="people">
          <div class="detail-actor-div director">
            <div v-if="director==null" class="actor-null"></div>
            <div v-else-if="director?.image === null" class="actor-null"></div>
            <div v-else class="detail-actor" :style="{'backgroundImage': `url(https://image.tmdb.org/t/p/original${director?.image})`}"></div>
            <i class="fa-solid fa-clapperboard"></i> {{ director? director?.name :'Director'}}
          </div>
          <div class="actors">
            <div
              v-for="(actor,index) in actors"
              :key="index">
              <div class="detail-actor-div">
                <div v-if="actor.role === 'Actor'">
                  <div v-if="actor.image === null" class="actor-null"></div>
                  <div v-else class="detail-actor" :style="{'backgroundImage': `url(https://image.tmdb.org/t/p/original${actor.image})`}"></div>
                  {{ actor.name }}
                </div>
              </div>
            </div>
          </div>
        </div>
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
            <div class="rank-avg">{{ rankAverage == NaN?  0.0 : rankAverage  }}</div>
            <div class="star-box">
              <div class="star">
                <div v-if="rankAverage <= 0.5">
                  <img src="@/assets/star_1.png" style="width : 35px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 1">
                  <img src="@/assets/star_2.png" style="width : 35px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 1.5">
                  <img src="@/assets/star_3.png" style="width : 70px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 2">
                  <img src="@/assets/star_4.png" style="width : 70px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 2.5">
                  <img src="@/assets/star_5.png" style="width : 105px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 3">
                  <img src="@/assets/star_6.png" style="width : 105px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 3.5">
                  <img src="@/assets/star_7.png" style="width : 140px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 4">
                  <img src="@/assets/star_8.png" style="width : 140px; height : 35px;"></div>
                <div v-else-if="rankAverage <= 4.5">
                  <img src="@/assets/star_9.png" style="width : 175px; height : 35px;"></div>
                <div v-else>
                  <img src="@/assets/star_10.png" style="width : 175px; height : 35px;"></div>
              </div>
              <div class="review-count">총 {{ reviews.length }}개의 리뷰</div>
        </div>
          </div>
          <div class="review-left-bottom">
              <div class="content3" @click="goLogin" v-if="!is_login" style="cursor:pointer">로그인이 필요합니다.</div>
              <div class="content1" v-if="is_login">{{ movie?.title }} 어떠셨나요?</div> 
              <div class="content2" v-if="is_login">다른 사용자가 참고할 수 있도록 리뷰를 남겨보세요</div>
              <!-- 리뷰 버튼/여기에 modalToggle넣기 -->
              <div v-if="is_login" @click="modalToggle" style="cursor:pointer" class="review-btn">
                리뷰 작성하기
              </div>
          </div>
        </div>
        <div class="review-right-box scroll-div">
          <ReviewItem
            v-for="(review, index) in reviews"
            :key="index"
            :review="review"
            @deleted="getReviews"
            @update-review="getReviews"
          />
        </div>
      </div>
    </div>
    <div class="similar-box">
      <SimilarList :genres="movie?.genres" :movieTitle="movie?.title"/>
      <!-- {{ movie?.genres }} -->
    </div>
  <div class="about-us-btn" @click="toAboutUs">👨‍👧‍👧</div>
  </div>
</template>

<script>
import axios from 'axios'
import vClickOutside from 'v-click-outside'
import jwt_decode from 'jwt-decode'

// import StarRating from 'vue-star-rating'

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
    // StarRating,
  },
  data() {
    return {
      star : null,
      movie : null,
      movie_id : this.$route.params.id,
      reviews: [],
      is_show : false,
      director : null,
      actors : [],
      is_login: false,
      is_like : null,
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
      if (!total) {
        return Math.round(0).toFixed(1)
      }
      const average = Math.ceil((total / this.reviews?.length) * 10) / 10
      return average.toFixed(1)
    },
    videoUrl() {
      return `http://www.youtube.com/watch_popup?v=${this.movie?.video}`
    },
    movieOverview() {
      if (this.movie?.overview.length >= 200) {
        return this.movie?.overview.slice(0, 200) + "..."
      } else {
        return this.movie?.overview
      }
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
        this.getActors()
        this.getReviews()
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
    },
    onClickVideo() {
      var options = 'top=10, left=10, width=1200, height=600, status=no, menubar=no, toolbar=no, resizable=no';
      window.open(this.videoUrl, '얍', options)
    },
    getActors() {
      this.actors = this.movie?.actors.filter((actor)=>{
          if (actor.role === 'Actor') {
            return actor
          } else {
            this.director = actor
          }
      })
    },
    goLogin() {
      this.$router.push({'name' : 'login'})
    },
    isLogin() {
      const token = localStorage.getItem('jwt')
      if (token) {
        this.is_login = true
      }
    },
    movieLike() {
      if (!localStorage.getItem('jwt')) {
        alert('로그인이 필요한 서비스 입니다!')
        return
      }
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
          method: 'post',
          url: `${API_URL}/movies/${this.movie.id}/movielikes/`,
          data: {
            user_id: now_user_id
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.is_like = res.data
          this.getMovieLikeInfo()
        })
        .catch((err)=>{console.log(err)})
    },
    getMovieLikeInfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie?.id}/`,
        headers: {
            'Authorization' : `Bearer ${token}`
        }
      })
        .then((res) => {
          this.movieinfo = res.data
          if (this.movieinfo.like_users.includes(now_user_id)) {
            this.is_like = false
          } else {
            this.is_like = true
          }
        })
        .catch((err)=>{console.log(err)})
    },
    toAboutUs() {
      this.$router.push({ name : 'aboutus' })
    },

  },
  created() {
      this.getMovieDetail()
      this.isLogin()
  },
  watch: {
    'movie' : function() {
      this.getMovieLikeInfo()
    }
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
  /* height: 40%; */
  position: absolute;
  bottom : 10vh;
  left : 5vw;
}



.like-btn1 {
    width :40px;
    height : 40px;
    border-radius: 50%;
    background-color: white;
    border: none;
    filter: drop-shadow(0px 0px 2px gray);
    opacity: 0.75;
    margin-left : 10px;
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

.detail-genres {
  display: flex;
  flex-wrap : wrap;
}
.detail-genre {
  padding : 10px 15px;
  height : 40px;
  border-radius: 20px;
  display:flex;
  align-content: center;
  justify-content: center;
  margin : 5px 5px;
  background: rgba(255,255,255,0.4);
}
.detail-genre p {
  font-size: 1em;
}

.detail-overview {
  font-size:1.2em;
  width : 30vw;
  margin-top : 5px;
  margin-bottom: 15px; 
}
.detail-video {
  border: 3px solid white;
  width : 12vw;
  border-radius: 50px;
  height : 60px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  padding : 5px;
  margin-bottom: 20px;
}
.detail-video:hover {
  color: black;
  background-color: white
}
.detail-actor-div {
  width: 90px;
  padding-right: 25px;
}
.detail-actor {
  padding-bottom: 100%;
  border-radius: 100%;
  background-size: cover;
}

.actor-null {
  padding-bottom: 100%;
  border-radius: 100%;
  background-size: cover;
  background-image:url('@/assets/null.png')
}

.people {
  font-size: 12px;
  display: flex;
  flex-direction: column;
}


.actors {
  display: flex;
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
  width : 70%; 
  height: 70%;
  margin : auto;
  justify-content: space-between;
  border-radius: 30px;
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
.content3 {
  width : 90%;
  margin : 10px auto;
  font-size : 1.3em;
}
.content3:hover {
  color: #F6BE00;
  text-decoration-line: underline;
}
.review-right-box {
  display: flex;
  flex-direction: column;
  width : 55%;
  margin : 5%;
  overflow-y: scroll;
  background-color: rgba( 255, 255, 255, 0.1 );
  border-radius: 5px;
  padding: 1%;
}

.rank-avg {
  font-size: 7em;
  width : 50%;
  height : 80%;
}

.star-box {
  width : 50%;
  display:flex;
  flex-direction:column;
}


.star {
  height : 60%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.review-count {
  font-size: 1.3em;
  padding : 10px;
}

.review-btn {
  width: 50%;
  margin: auto;
  border-radius: 50px;
  border : none;
  color : #25252e;
  height : 40px;
  background-color: rgb(230, 227, 227);
  display: flex;
  text-align: center;
  justify-content: center;
  padding-top: 7px;
}

.review-btn:hover {
  scale: 1.02;
  background-color: rgb(199, 198, 198);
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