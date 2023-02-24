
import { RestClient } from '../utils/auth'

export const authenticate = async (email: string, password: string) => {

    try {
        const response = await RestClient.post(`/api/auth/token`,  {email, password})
        return response
    } catch (error) {
        console.warn('Error', error)
        throw new Error('Could not login')
    }
}


export const requestNewToken = async (refresh: string) => {

    try {
        const response = await RestClient.post(`/api/auth/token/refresh`,  { refresh })
        return response
    } catch (error) {
        console.warn('Error', error)
        throw new Error('Could not Refresh token')
    }
}
