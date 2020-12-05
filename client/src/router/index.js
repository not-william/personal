import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SignIn from '../views/SignIn.vue'
import Upload from '../views/Upload.vue'
import ImageFromPost from '../views/ImageFromPost.vue'
import ImageFromSearch from '../views/ImageFromSearch.vue'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/search/:search',
    name: 'search',
    component: Home,
  },
  {
    path:'/post/:postId/image/:imageOrder',
    name: 'image-from-post',
    component: ImageFromPost
  },
  {
    path:'/image/:imageId',
    name: 'image-from-search',
    component: ImageFromSearch
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
