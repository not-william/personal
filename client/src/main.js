import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import '@/assets/styles/app.css'

require('@/store/subscriber.js')

axios.defaults.baseURL = 'http://143.110.170.163:8000/api/'

Vue.config.productionTip = false

store.dispatch('auth/attempt', localStorage.getItem('token')).then(
  new Vue({
    router,
    store,
    render: h => h(App)
  }).$mount('#app')
)
