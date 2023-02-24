import { defineStore } from 'pinia'
import { authenticate, requestNewToken } from '../services/auth-service'
import VueJwtDecode from 'vue-jwt-decode'

export interface JwtResponse {
  access: string
  refresh: string
}

export interface Token {
  account_id: number | string
  exp: number
  iat: number
  alg: string
  jti: string
  username: string
  token_type: string
  typ: string
}

const saveTokenOnStorage = (data: JwtResponse ) => {
  localStorage.setItem('access', data.access)
  localStorage.setItem('refresh', data.refresh)
}

const getUsername = () => {
  const token : string  = localStorage.getItem('access') as string

  if(token){

    const { username } = (VueJwtDecode.decode(token) as any) as Token

    return username
  }

  return ''
}

export const useAuthStore = defineStore('auth', {
  state: () => {
    const username = getUsername()
    return { username: username, isLogged: false}
  },
  actions: {
    async login(email: string, password: string) {
      const response = await authenticate(email, password)

      if(response.status == 200){
        const { data } = response

        saveTokenOnStorage(data)

        const username = getUsername()
        
        this.$patch({username, isLogged: true})
      }

      return response
    },
    async checkAuth(){

      const token : string  = localStorage.getItem('access') as string

      if(token){
        const { exp, username} = (VueJwtDecode.decode(token) as any) as Token
        const currentDate : Date = new Date() 
        const expireDate : Date = new Date(exp * 1000)
        const refreshToken : string  = localStorage.getItem('refresh') as string

        if(currentDate > expireDate && refreshToken) {
          //retrieves a new token
          const response = await requestNewToken(refreshToken)

          if(response.status == 200){
            const { data } = response

            saveTokenOnStorage(data)
            
            this.$patch({username:  username || '', isLogged: true})

            return
          }  
          
        }
        
        this.$patch({username: this.username, isLogged: true})

      }

    },
    logout(){
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      this.$patch({username:  '', isLogged: false})
    }
  },
})
