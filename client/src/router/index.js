import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignIn from '../views/SignIn.vue'
import Upload from '../views/Upload.vue'
import Image from '../views/Image.vue'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path:'/post/:postId/image/:imageOrder',
    name: 'image',
    component: Image
  },
  {
    path: '/signin',
    name: 'signin',
    component: SignIn
  },
  {
    path: '/upload',
    name: 'upload',
    component: Upload,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/authenticated']) {
        console.log("Not signed in")
        next({
          'name': 'signin'
        })
      }

      next()
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
