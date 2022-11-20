<template>
  <div>
    <h1>Sign Up</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2"><br>

      <label for="nickname"> nickname : </label>
      <input type="text" id="nickname" v-model="nickname">
      
      
      <input type="submit" value="가입">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      username: null,
      password: null,
      password2: null,
      nickname: null,
    }
  },

  methods: {
    logIn() {
      axios({
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
        },
        url: 'http://127.0.0.1:8000/api/token/',
        data: {
          username: this.username,
          password: this.password
        }
      })
        .then((res) => {
          console.log(res)
          const token = res.data.access
          localStorage.setItem('jwt', token)
          this.$router.push({ name: 'movies' })
          this.$emit('login')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp() {
      if (this.password != this.password2) {
        alert('비밀번호가 틀렸습니다.')
        return
      }
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: {
          username: this.username,
          password: this.password,
          password2: this.password2,
          nickname: this.nickname,
        },
      })
        .then(() => {
          // login 메서드 넣고싶어여
          this.logIn()
        })
        .catch((err)=> {
          console.log(err)
        })
    }
  }
}

</script>
