
import { RestClient } from '../utils/auth'

export const getChargeSessions = async (page?: string) => {

    const params = page ? `?page=${page}` : ''

    try {
        const response = await RestClient.get(`/api/chargesession${params}`)
        return response
    } catch (error) {
        console.warn('Error', error)
        throw new Error('Could not login')
    }
}
