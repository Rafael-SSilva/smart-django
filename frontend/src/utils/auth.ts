import axios, { type AxiosInstance, type InternalAxiosRequestConfig } from 'axios'

export const BASE_URL = import.meta.env.VITE_BACKEND_BASE_URL

export const RestClient : AxiosInstance = axios.create({
    baseURL: BASE_URL
})


RestClient.interceptors.request.use((config: InternalAxiosRequestConfig) => {
    const token = localStorage.getItem("access");
    config.headers.Authorization = `Bearer ${token}`;
    return config;
  });
  
RestClient.interceptors.response.use(
(response) => response,
    ({ response }) => {
    if (response.status === 401) {
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')

        if(!window.location.href.includes("login")){

            window.location.href = "/login";
        }
    }
    return response;
}
);
