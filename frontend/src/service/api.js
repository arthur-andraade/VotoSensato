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
        );
        return dados;
    },

    // Pegando ufs de estados para aplicar filtro
    recebendoUfs: async () => {
        const ufs = await acessandoApi.get('ufs').then(
            res => res.data
        );
        return ufs.siglas;
    },

    dadosFiltrados: async(partido, uf) => {
        const dadosFiltrado = await acessandoApi.get(`filtro?partido=${partido}&uf=${uf}`).then(
            res => res.data
        )
        return dadosFiltrado.membrosFiltrado
    }
    
}

export default api;