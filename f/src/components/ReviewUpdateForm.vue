<template>
  <div class="review-form" >
      <i class="fa-solid fa-x fa-lg x-btn" @click="modalToggle" style="cursor:pointer"></i>
      <div class="review-text" style="text-align:center">이 영화, 어떠셨나요?</div>
      <form @submit.prevent="putReview" class="form">
        <div class="star-div">
          <star-rating
            v-model="star"
            :increment="0.5"
            :star-size="30"
            :clearable="true"
            :show-rating="false"
          />
        </div>
        <textarea rows="30" class="review-content1 scroll-div" type="text" v-model="content" maxlength='200' placeholder="영화 리뷰를 작성해주세요."></textarea>
        <button class="review-submit">리뷰 등록</button>
      </form>
  </div>
  
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'ReviewForm',
  components: {
    StarRating,
  },
  props: {
    rank: Number,
    text: String,
    reviewid: Number,
    wr: String,
  },
  data() {
    return {
      star: this.rank,
      content: this.text,
      id: this.reviewid,
      modal: false,
    }
  },
  methods: {
    putReview() {
      const token = localStorage.getItem('jwt')

      if (this.star===null || this.star===0) {
        alert('별점을 입력하세요!')
        return
      } else if (this.content===null) {
        alert('내용을 입력하세요!')
        return
      }

      axios({
        method: 'put',
        url: `${API_URL}/movies/reviews/${this.id}/`,
        data: {
          rank: this.star,
          content: this.content,
          writer: this.wr
        },
        headers: {
              'Authorization' : `Bearer ${token}`
        }
      })
      .then(()=>{
        this.$emit('update-review')
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