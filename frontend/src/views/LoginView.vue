<template>
    <main>
        <div class="content">
            <div class="login-container">
                <div class="logo" >
                    <img :src="Logo" alt="Logo" >
                </div>
            <form class="form" @submit.prevent="loginUser">
                <div class="form-input">
                    <div class="input">
                        <img :src="UserIcon" alt="user email">
                        <input type="text" name="email" id="email" placeholder="Email" v-model="email">
                    </div>
                    <div class="input">
                        <img :src="LockIcon" alt="user password">
                        <input type="password" name="password" id="password" placeholder="Password" v-model="password">
                    </div>
                </div>
                <button type="submit">LOGIN</button>
            </form>
        </div>
        <Footer />
        </div>
    </main>
</template>

<script setup lang="ts">

    import Logo from '../assets/logo.png'
    import UserIcon from '../assets/user-solid.svg'
    import LockIcon from '../assets/lock-solid.svg'
    import Footer from '../components/Footer.vue';
    import router from '@/router';
    import { ref } from 'vue';
    import { useAuthStore } from '../stores/auth-store'

    const authContext = useAuthStore()
    
    const email = ref<string>('')
    const password = ref<string>('')

    async function loginUser() {
        
      if(!email || !password){
        return
      }
      
      const response = await authContext.login(email?.value, password?.value)
      
      if(response?.status === 200){
        
          router.push('/')
      }
      

    }
</script>
  
<style scoped>

    .content {
        background-color: var(--login-background);
        display: flex;
        flex: 1;
        justify-content: center;
    }

    .content footer {
        position: absolute;
        bottom: 0;
    }

    .login-container {
        /* top: 50%;
        left: 50%;
        transform: translate(-50%, -50%); */
        width: 100%;
        max-width: 420px ;

        background: #FFFFFF;
        border-radius: 1rem;
        color: var(--login-color);
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 4rem ;
        padding: 2.5rem;

    }
    
    .logo img {
        width: 100%;
    }

    .form {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 3rem;
    }

    .form .form-input {
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }

    .form .form-input .input {
        display: flex;
    }

    .form .form-input .input img {
        max-width: 1rem;
        position: relative;
        left: 1rem;
    }

    .form input {
        border: none;
        border-bottom: 1px solid var(--login-color);
        display: block;
        padding: 0.5rem 2rem;
        width: 100%;
        font-size: 1rem;
    }

    .form input:focus {
        outline: none;
    }

    .form input::placeholder {
        position: relative;
    }

    .form button {
        background: var(--login-button);
        border: none;
        border-radius: 3rem;
        padding: 1rem;
        width: 100%;
        color: #FFFFFF;
        font-size: 1rem;


    }

    .form button:hover {
        cursor: pointer;
    }


</style>
  