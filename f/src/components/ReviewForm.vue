<template>
  <div class="review-form" >
      <i class="fa-solid fa-x fa-lg x-btn" @click="modalToggle" style="cursor:pointer"></i>
      <div class="review-text">이 영화, 어떠셨나요?</div>
      <form @submit.prevent="postReview" class="form">
        <div class="star-div">
          <star-rating
            v-model="star"
            :increment="0.5"
            :star-size="30"
            :clearable="true"
            :show-rating="false"
          />
        </div>
        <textarea rows="30" class="review-content1 scroll-div" type="text" @input="content=$event.target.value" maxlength='200' placeholder="영화 리뷰를 작성해주세요."></textarea>
        <button class="review-submit">리뷰 등록</button>
      </form>
  </div>
  
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"
import StarRating from 'vue-star-rating'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'ReviewForm',
  components: {
    StarRating,
  },
  data() {
    return {
      star: null,
      content : null,
      modal: false,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    postReview() {
      // 로그인 되어있지 않다면

      // 내용이 입력되지 않으면 alert
      if (this.star===0 || this.star === null) {
        alert('별점을 입력하세요!')
        return
      } else if (this.content===null) {
        alert('내용을 입력하세요!')
        return
      }

      const token = localStorage.getItem('jwt')
      const now_user_id = jwt_decode(token).user_id

      console.log(now_user_id)
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie?.id}/reviews/`,
        data: {
          rank: this.star,
          content: this.content,
          user_id: now_user_id
        },
        headers: {
          'Authorization' : `Bearer ${token}`
        }
      })
      .then(()=>{
        this.$emit('add-review')
        this.star = null
        this.content = null
        this.$emit('modal-toggle')
        return
      })
      .catch((err)=>{console.log(err)})
    },
    modalToggle() {
      this.$emit('modal-toggle')
    }
  },
}

</script>

<style>
/* 모달창 */

 .review-form{
  width : 50vw;
  /* height: 40vw; */
  margin : auto;
  background: #343440; 
  border-radius: 5px;
  padding : 15px 0;
  position: absolute;
  top: 20vh; left: 20vw;
  z-index: 4;
}

.form {
  display: flex;
  flex-direction: column;
  width : 100%;
  /* height : 80%; */
  margin : 30px auto;
  justify-content: space-between;
  /* border : 2px solid red; */
}

.x-btn {
  position: absolute;
  right: 10px;
  top: 20px;
}
.x-btn:hover {
  color : #F6BE00
}

.review-text {
  margin-top: 2rem;
  margin-bottom: 1rem;
  font-size : 1.8em;
}


.star-div{
  margin: auto;
}

.review-content1 {
  margin: 20px auto;
  height: 13rem;
  background-color: #25252e;
  color : white;
  width : 70%;
  overflow-y: scroll;
  font-size : 1.3em;
}

.review-submit {
  width: 25%;
  margin: auto;
  border-radius: 50px;
  border : none;
  color : #25252e;
  height : 50px;
  font-size : 1.2em;
}

.review-submit:hover {
  scale : 1.02;
}
</style>