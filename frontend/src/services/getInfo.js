import api from '@/services/api.js'

export default {
    
    status() {
        return api().get('/')
    }

}