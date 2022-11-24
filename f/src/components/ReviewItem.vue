<template>
  <div class="review-item">
    <div class="review-item-left">
      <div v-if="review.rank === 0.5">
        <img src="@/assets/star_1.png" style="width : 15px; height : 15px;"></div>
      <div v-else-if="review.rank === 1">
        <img src="@/assets/star_2.png" style="width : 15px; height : 15px;"></div>
      <div v-else-if="review.rank === 1.5">
        <img src="@/assets/star_3.png" style="width : 30px; height : 15px;"></div>
      <div v-else-if="review.rank === 2">
        <img src="@/assets/star_4.png" style="width : 30px; height : 15px;"></div>
      <div v-else-if="review.rank === 2.5">
        <img src="@/assets/star_5.png" style="width : 45px; height : 15px;"></div>
      <div v-else-if="review.rank === 3">
        <img src="@/assets/star_6.png" style="width : 45px; height : 15px;"></div>
      <div v-else-if="review.rank === 3.5">
        <img src="@/assets/star_7.png" style="width : 60px; height : 15px;"></div>
      <div v-else-if="review.rank === 4">
        <img src="@/assets/star_8.png" style="width : 60px; height : 15px;"></div>
      <div v-else-if="review.rank === 4.5">
        <img src="@/assets/star_9.png" style="width : 75px; height : 15px;"></div>
      <div v-else>
        <img src="@/assets/star_10.png" style="width : 75px; height : 15px;"></div>
      <div>{{ review.rank }}</div>
    </div>
    <div class="review-item-right">
      <div style="display:flex;justify-content:space-between;">
        <div><a @click="goProfile" style="text-decoration-line: underline;">{{ review.writer }}</a></div>
        <div v-if="is_me" class="ud-div">
          <div @click="modalToggle" style="cursor:pointer" class="u-div"><i class="fa-solid fa-pen fa-lg"></i></div>
          <div @click="reviewDelete" style="cursor:pointer" class="u-div"><i class="fa-solid fa-trash-can fa-lg"></i></div>
        </div>
        <div class="black-bg" v-if="is_show == true">
          <ReviewUpdateForm 
            @modal-toggle="modalToggle"
            v-if="is_show"
            @update-review="letsGoDetail"
            v-click-outside="onClickOutside"
            :rank="review.rank"
            :text="review.content"
            :reviewid="review.id"
            :wr="review.writer"
          />
        </div>
      </div>
      <div class="review-con">{{ review.content }}</div>
      <div class="review-submit-btn" @click="reviewLike" :class="{'review-like-btn': !is_like}">
        <div :class="{ 'review-like-thumbs': !is_like }"><i class="fa-solid fa-thumbs-up"></i></div>
        <div>도움이 돼요 {{ reviewinfo?.like_users.length }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import vClickOutside from 'v-click-outside'
import ReviewUpdateForm from '@/components/ReviewUpdateForm';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewItem',
  components: {
    ReviewUpdateForm,
  },
  props: {
    review: Object,
  },
  data() {
    return {
      is_like: true,
      reviewinfo : null,
      is_show : false,
      is_me: null,
    }
  },
  directives: {
    clickOutside: vClickOutside.directive
  },
  methods: {
    goProfile() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      if (this.review.user === now_user_id){
        this.$router.push({ name: 'myinfo' })
      } else {
        this.$router.push({name: 'userinfo', params: {id : this.review.user}})
      }
      
    },
    reviewLike() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
          method: 'post',
          url: `${API_URL}/movies/${this.review.id}/reviewlikes/`,
          data: {
            user_id: now_user_id
          },
          headers: {
            'Authorization' : `Bearer ${token}`
          }
        })
        .then((res)=>{
          this.is_like = res.data
          this.getReviewLikeInfo()
        })
        .catch((err)=>{console.log(err)})
    },
    getReviewLikeInfo() {
      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      axios({
        method: 'get',
        url: `${API_URL}/movies/reviews/${this.review.id}/`,
        headers: {
            'Authorization' : `Bearer ${token}`
        }
      })
        .then((res) => {
          this.reviewinfo = res.data
          if (this.reviewinfo.like_users.includes(now_user_id)) {
            this.is_like = false
          } else {
            this.is_like = true
          }

          if (this.review.user === now_user_id) {
            this.is_me = true
          } else {
            this.is_me = false
          }
        })
        .catch((err)=>{console.log(err)})
    },
    reviewDelete() {
      if (!confirm("정말 삭제하시겠습니까?")){    //확인
        return
      } else {   //취소
        const token = localStorage.getItem('jwt')

        axios({
          method: 'delete',
          url: `${API_URL}/movies/reviews/${this.review.id}/`,
          headers: {
              'Authorization' : `Bearer ${token}`
          }
        })
          .then((res) => {
            this.is_me = false
            this.$emit("deleted")
            console.log(res)
          })
          .catch((err)=>{console.log(err)})
     }
    },
    modalToggle() {
      this.is_show = !this.is_show
      this.star = null
    },
    onClickOutside() {
      this.is_show = !this.is_show
    },
    letsGoDetail() {
      this.$emit("update-review")
    },
  },
  created() {
    this.getReviewLikeInfo()
  },
  watch: {
    'review': function() {
      this.getReviewLikeInfo()
    }
  }
}
</script>

<style>
.review-item {
  display: flex;
  margin : 1.5vh auto;
  width : 90%;
  background-color: rgba( 255, 255, 255, 0.2 );
  border-radius: 8px;
  padding: 5%;
  /* border-bottom : solid 1px rgba(255, 255, 255, 0.733); */
  padding-bottom : 2vh; 
}

.review-item-left {
  width : 25%;
}
.review-item-right {
  width : 70%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
}

.review-submit-btn{
  font-size : 0.85em;
  margin-top : 10px;
  border: solid 3px white;
  width : 36%;
  height : 35px;
  border-radius: 50px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  cursor:pointer;
}

.review-like-btn {
  border: solid 3px #F6BE00;
  color: #F6BE00;
}

.review-submit-btn:hover .review-like-thumbs {
  transform: scale( 1.4 ) skewX( 10deg );
  transition: 0.2s;
}

.review-con {
  font-size: 1.1em;
  margin-top : 5px;
}

.ud-div {
  display: flex;
}

.u-div {
  margin-right: 15px;
}
.u-div:hover {
  color: #F6BE00;
}
</style>
