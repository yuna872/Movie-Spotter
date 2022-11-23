import Vue from 'vue'
import VueRouter from 'vue-router'
import Movies from '@/views/Movies'
import Login from '@/views/accounts/Login'
import Signup from '@/views/accounts/Signup'
import AboutUs from '@/views/AboutUs'
import Detail from '@/views/Detail'
import UserInfo from '@/views/accounts/UserInfo'
import MyInfo from '@/views/accounts/MyInfo'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: Movies
  },
  {
    path: '/accounts/login',
    name: 'login',
    component: Login
  },
  {
    path: '/accounts/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/aboutus',
    name: 'aboutus',
    component: AboutUs
  },
  {
    path: '/:id',
    name: 'detail',
    component: Detail,

  },
  {
    path: '/accounts/myinfo',
    name: 'myinfo',
    component: MyInfo
  },
  {
    path: '/accounts/:id',
    name: 'userinfo',
    component: UserInfo
  },
]

const router = new VueRouter({
  mode: 'history',
  scrollBehavior() {
    return { x: 0, y: 0}
  },
  base: process.env.BASE_URL,
  routes
})

export default router
