import acessandoApi from './config';

const api = {
    
    // Pegando parâmetros na API para realizar pesquisa
    parametrosIniciais: async () => {
        const parametrosIniciais = await acessandoApi.get('/').then(
            res => res.data
        );
        return parametrosIniciais;
    },

    // Pegando dados específico de PARTIDO
    dadosPartido: async (idPartido) =>{
        const dados = await acessandoApi.get(`/partido/${idPartido}`).then(
            res => res.data
        )
        return dados;
    }   
}

export default api;