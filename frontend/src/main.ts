import Vue from 'vue'

import App from './App.vue'
import router from './router'
import { createPinia, PiniaVuePlugin  } from "pinia";

import './assets/main.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUser } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon, FontAwesomeLayers } from '@fortawesome/vue-fontawesome'

Vue.component('font-awesome-icon', FontAwesomeIcon)
library.add(faUser)

Vue.use(PiniaVuePlugin)

export const pinia = createPinia()

new Vue({
  render: (h) => h(App),
  pinia,
  router
}).$mount('#app')

