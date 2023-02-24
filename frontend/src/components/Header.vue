<script setup lang="ts">
import router from '@/router';
import Logo from '../assets/logo-dark.png'
import ExitIcon from '../assets/right-from-bracket-solid.svg'
import UserAvatar from '../assets/user.png'
import { useAuthStore } from '../stores/auth-store'

defineProps<{
  name: string
}>()

const authContext = useAuthStore()

const logout = () => {
    
    authContext.logout()
    router.push('/login')
}

</script>

<template>
    <header name="header" class="header-wrapper">
        <div class="header">
            <div class="header-logo">
                <img :src="Logo" alt="Logo dark">
            </div>
            <div class="header-nav">
                <div class="avatar">
                    <img :src="UserAvatar" alt="user avatar">
                    <span> {{ name }}</span>
                </div>
                
                <ul class="header-nav-list">
                    <li  @click="logout" >
                        <img :src="ExitIcon" alt="logout">
                        <span>Logout</span>
                    </li>
                </ul>
            </div>
        </div>
    </header>
</template>

<style scoped>

    header {
        background: var(--header-footer);
        color: #EFEFEF
    }
    div.header {
        margin: 0 auto;
        max-width: 85%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
    }

    .header-logo {
        height: 60px;
    }

    .header-logo img {
        width: 120px;
    }
    .header-nav {
        padding: 1rem;
        position: relative;
    }

    .header-nav .avatar {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
    }

    .header-nav .avatar img {
        max-width: 2rem;
    }
    
    .header-nav:hover {
        cursor: pointer;
    }

    .header-nav:hover .header-nav-list {
        display: block;
    }

    .header-nav-list{
        position: absolute;
        cursor: pointer;
        background: #ffffff;
        color: #000000;
        display: none;

        -webkit-box-shadow: 0px 0px 28px -8px rgba(0,0,0,0.75);
        -moz-box-shadow: 0px 0px 28px -8px rgba(0,0,0,0.75);
        box-shadow: 0px 0px 28px -8px rgba(0,0,0,0.75);
        list-style-type: none;
        border-radius: 1rem;
        margin-top: 0.5rem;
        padding: 0.5rem 1rem;
    }
    
    .header-nav-list li {
        display: flex;
        padding-right: 1rem;
        gap: 0.5rem;
    }

    .header-nav-list li img  {
        max-width: 16px;
    }

</style>
