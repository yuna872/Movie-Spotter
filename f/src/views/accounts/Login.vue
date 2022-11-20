<template>
  <div>
    <h1>Login Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
    <div>
      <hr>
      <p>회원이 아니라면?</p>
      <router-link :to="{ name: 'signup' }">회원가입</router-link>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      username: null,
      password: null,
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
          this.$router.push({name:'movies'})
          this.$emit('login')
        })
        .catch((err) => {
          console.log(err)
          alert('회원정보가 존재하지 않습니다! 회원가입 해주세요.')
        })
    }
  }
}
</script>
