import acessandoApi from './config';

const api = {
    
    parametrosIniciais: async () => {
        const parametrosIniciais = await acessandoApi.get('/').then(
            res => res.data
        );
        return parametrosIniciais;
    }
}

export default api;