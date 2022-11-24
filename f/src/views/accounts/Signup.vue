<template>
  <div class="section">
  <link rel="stylesheet" href="https://unicons.iconscout.com/release-pro/v4.0.0/css/solid.css">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
            <h6 class="mb-0 pb-3"><span>Sign Up </span><span @click="goLogin" style="cursor:pointer">Log In</span></h6>
              <input class="checkbox" type="checkbox" id="reg-log" name="reg-log"/>
              <label for="reg-log"></label>
              <div class="card-3d-wrap mx-auto">
                <div class="card-3d-wrapper">
                  <div class="card-front">
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
                  <div class="card-back">
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
                        <p class="signupbtn" @click="check">Sign Up</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
    <div class="about-us-btn" @click="toAboutUs">👨‍👧‍👧</div>
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
      valid: {
        username: false,
        password: false,
        pwcorrect: false,
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
    'password2': function() {
      this.checkPwcorrect()
    }
  },

  methods: {
    check() {
      this.$router.go()
    },
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
        alert('비밀번호가 일치하지 않습니다.')
        return
      }
      if (this.valid.username) {
        alert('아이디가 유효하지 않습니다.')
        this.username = null
        return
      }
      if (this.valid.password) {
        alert('패스워드가 유효하지 않습니다.')
        this.password = null
        this.password2 = null
        return
      }
      if (this.valid.pwcorrect) {
        alert('패스워드가 일치하지 않습니다.')
        this.password2 = null
        return
      }
      console.log(this.valid.username)
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
    goLogin() {
      this.$router.push({name: 'login'})
    },
    toAboutUs() {
      this.$router.push({ name : 'aboutus' })
    },
  }
}

</script>

<style>
/* @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css%27'); */

.section{
  position: relative;
  width: 100%;
  display: block;
}

a {
  cursor: pointer;
  transition: all 200ms linear;
}
a:hover {
  text-decoration: none;
}
.link {
  color: #c4c3ca;
}
.link:hover {
  color: #F6BE00;
}
p {
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}
h4 {
  font-weight: 600;
}
h6 span{
  padding: 0 20px;
  text-transform: uppercase;
  font-weight: 700;
}
.section{
  position: relative;
  width: 100%;
  display: block;
}
.full-height{
  min-height: 100vh;
}
[type="checkbox"]:checked,
[type="checkbox"]:not(:checked){
  position: absolute;
  left: -9999px;
}
.checkbox:checked + label,
.checkbox:not(:checked) + label{
  position: relative;
  display: block;
  text-align: center;
  width: 60px;
  height: 16px;
  border-radius: 8px;
  padding: 0;
  margin: 10px auto;
  cursor: pointer;
  background-color: #F6BE00;
}
.checkbox:checked + label:before,
.checkbox:not(:checked) + label:before{
  position: absolute;
  display: block;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  color: #F6BE00;
  background-color: #343440;
  font-family: FontAwesome;
  content: "\f060";
  z-index: 20;
  top: -10px;
  left: -10px;
  line-height: 36px;
  text-align: center;
  font-size: 24px;
  transition: all 0.5s ease;
  transform: rotate(45deg);
}
.checkbox:checked + label:before {
  transform: translateX(44px) rotate(-240deg);
}

.card-3d-wrap {
  position: relative;
  width: 500px;
  max-width: 100%;
  height: 454px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  perspective: 800px;
  margin-top: 60px;
}
.card-3d-wrapper {
  width: 100%;
  height: 100%;
  position:absolute;    
  top: 0;
  left: 0;  
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  transition: all 600ms ease-out; 
}
.card-front, .card-back {
  width: 100%;
  height: 100%;
  background-color: #2a2b38;
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/1462889/pat.svg');
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 300%;
  position: absolute;
  border-radius: 6px;
  left: 0;
  top: 0;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -o-backface-visibility: hidden;
  backface-visibility: hidden;
}
.card-back {
  transform: rotateY(180deg);
}
.checkbox:checked ~ .card-3d-wrap .card-3d-wrapper {
  transform: rotateY(180deg);
}
.center-wrap{
  position: absolute;
  width: 100%;
  padding: 0 35px;
  top: 50%;
  left: 0;
  transform: translate3d(0, -50%, 35px) perspective(100px);
  z-index: 20;
  display: block;
}

.form-group{ 
  position: relative;
  display: block;
    margin: 0;
    padding: 0;
}
.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: #c4c3ca;
  background-color: #1f2029;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #F6BE00;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  filter: drop-shadow(0px 0px 1.5px)
}

.form-group input:-ms-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-webkit-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-ms-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-webkit-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.btn{  
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition : all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #F6BE00;
  color: #343440;
  box-shadow: 0 8px 24px 0 rgba(255,235,167,.2);
}
.btn:active,
.btn:focus{  
  background-color: #343440;
  color: #F6BE00;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.btn:hover{  
  background-color: #343440;
  color: #F6BE00;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.signupbtn {
  text-decoration: underline;
  color: #F6BE00;
  font-size: 16px;
}

</style>