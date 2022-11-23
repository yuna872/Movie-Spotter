<template>
  <div class="section">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
            <h6 class="mb-0 pb-3"><span>Log In </span><span>Sign Up</span></h6>
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
                            <input type="text" id="username" v-model="username" class="form-style" placeholder="ID" autocomplete="off">
                            <i class="input-icon fas fa-user"></i>
                          </div>
                          
                          <div class="form-group mt-2">
                            <input type="password" id="password" v-model="password" class="form-style" placeholder="Password" autocomplete="off">
                            <i class="input-icon fas fa-lock"></i>
                          </div>

                          <div class="form-group mt-2">
                            <input type="password" id="password2" v-model="password2" class="form-style" placeholder="Password Confirmation" autocomplete="off">
                            <i class="input-icon fas fa-lock"></i>
                            <!-- <i class="input-icon fas fa-check fa-stack-1x" style="color:#343440"></i> -->
                          </div>

                          <div class="form-group mt-2">
                            <input type="text" id="nickname" v-model="nickname" class="form-style" placeholder="Nickname" autocomplete="off">
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
                        <router-link :to="{ name: 'signup' }">Sign Up</router-link>
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
          this.$emit('first-time')
        })
        .catch((err)=> {
          console.log(err)
        })
    }
  }
}

</script>