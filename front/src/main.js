import Vue from 'vue'
import App from './App.vue'
// import axios from 'axios'

/* ここから */
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
/* ここまで */

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')



  


  


import router from "./router";

import axios from 'axios'
import VueAxios from 'vue-axios'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)

Vue.config.productionTip = false

Vue.use(VueAxios, axios)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
