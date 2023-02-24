import { pinia } from '@/main'
import { useAuthStore } from '@/stores/auth-store'
import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginViewVue from '../views/LoginView.vue'


Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: import.meta.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginViewVue
    }
  ]
})

router.beforeEach (async (to, from, next) => {

  const authContext = useAuthStore(pinia)

  await authContext.checkAuth()

  if(!authContext.isLogged){

    if(from?.name !== 'login' && to?.name !== 'login'){
      return next('/login')
    }
    return next()
  }

  if(to?.name === 'login'){
    
    return next('/')
    
  }

  return next()
})

export default router
