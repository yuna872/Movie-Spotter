<template>
  <div class="section">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
            <h6 class="mb-0 pb-3"><span>log in </span><span @click="goSignup" style="cursor:pointer">sign up</span></h6>
              <input class="checkbox" type="checkbox" id="reg-log" name="reg-log"/>
              <label for="reg-log"></label>
              <div class="card-3d-wrap mx-auto">
                <div class="card-3d-wrapper">
                  <div class="card-back">
                    <div class="center-wrap">
                      <div class="section text-center">
                        <h4 class="mb-4 pb-3">Sign Up</h4>
                        <form @submit.prevent="signUp">
                          <div class="form-group">
                            <input type="text" id="username" v-model="username" class="form-style" placeholder="예) ssafy8888" autocomplete="off">
                            <i class="input-icon fas fa-user"></i>
                          </div>
                          <p v-show="valid.username">특수문자를 제외한 ID를 입력해주세요. (4-12자)</p>
                          <div class="form-group mt-2">
                            <input type="password" id="password" v-model="password" class="form-style" placeholder="영문, 숫자, 특수문자 조합 8-16자" autocomplete="off">
                            <i class="input-icon fas fa-lock"></i>
                          </div>
                          <p v-show="valid.password">영문,숫자,특수문자를 조합하여 입력해주세요. (8-16자)</p>
                          <div class="form-group mt-2">
                            <input type="password" id="password2" v-model="password2" class="form-style" placeholder="비밀번호 확인" autocomplete="off">
                            <i class="input-icon fas fa-lock"></i>
                            <!-- <i class="input-icon fas fa-check fa-stack-1x" style="color:#343440"></i> -->
                          </div>
                          <p v-show="valid.pwcorrect">비밀번호가 일치하지 않습니다</p>
                          <div class="form-group mt-2">
                            <input type="text" id="nickname" v-model="nickname" class="form-style" placeholder="닉네임" autocomplete="off">
                            <i class="input-icon fa-solid fa-user-pen"></i>
                          </div>
                          <input type="submit" class="btn mt-4" value="SUBMIT">
                        </form>
                      </div>
                    </div>
                  </div>
                  <div class="card-front">
                    <div class="center-wrap">
                      <div class="section text-center">
                        <h4 class="mb-4 pb-3">Log In</h4>
                        <form @submit.prevent="logIn">
                          <div class="form-group">
                            <input type="text" id="username" v-model="username" class="form-style" placeholder="Your Username" autocomplete="off">
                            <i class="input-icon fas fa-user"></i>
                          </div>
                          
                          <div class="form-group mt-2">
                            <input type="password" id="password" v-model="password" class="form-style" placeholder="Your Password" autocomplete="off">
                            <i class="input-icon fas fa-lock"></i>
                          </div>

                          <input type="submit" class="btn mt-4" value="logIn">
                        </form>
                      </div>
                      <div>
                        <hr>
                        <p>회원이 아니라면?</p>
                        <router-link style="color:#F6BE00" :to="{ name: 'signup' }">Sign Up</router-link>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
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
      password2: null,
      nickname: null,
      valid: {
        username: false,
        password: false,
        pwcorrect: false,
        nickname: false,
      },
    }
  },
  watch: {
    'username': function() {
      this.checkUsername()
    },
    'password': function() {
      this.checkPassword()
      console.log('현재 비밀번호 상태',this.valid.password)
    },
    'nickname': function() {
      this.checkNickname()
    },
    'password2': function() {
      this.checkPwcorrect()
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
          alert('아이디 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.')
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
          this.logIn()
          this.$emit('first-time')
        })
        .catch((err)=> {
          console.log(err)
          alert('중복된 아이디입니다.')
          this.username=null
        })
    },
    checkUsername() {
      const validateUsername = /^[a-zA-z0-9]{4,12}$/
      if (!validateUsername.test(this.username) || !this.username) {
        this.valid.username = true
        return
      } this.valid.username = false
    },
    checkPassword() {
      const validatePassword = /^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]).{8,16}$/
      if (!validatePassword.test(this.password) || !this.password) {
        this.valid.password = true
        return
      } this.valid.password = false
    },
    checkPwcorrect() {
      if (this.password !== this.password2){
        this.valid.pwcorrect = true
      } else {
        this.valid.pwcorrect = false
      }
    },
    goSignup() {
      this.$router.push({name : 'signup'})
    },
  }
}

</script>