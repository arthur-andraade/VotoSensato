<template>
    <div id="resultado">
        <div 
            id="carregado"
            v-if="!carregar"
        >             
            <!--Box com informações do PARTIDO em relação há camara -->
            <div class="resultado-info">
                <img :src="dadosPartido.logo">
                <div>
                    <h3>Sigla: {{ dadosPartido.sigla }} </h3>
                    <h3>Nome: {{ dadosPartido.nome }} </h3>
                    <h3>Numero deputados na camara: {{ dadosPartido.totalMembros}}</h3>
                    <h3>Situação: {{ dadosPartido.situacao }} </h3>
                    <div class="resultado-filtros">
                        <h3>Selecione um estado para filtrar deputados:</h3>
                        <select id="ufs" v-model="ufSelecionado">
                            <option
                                v-for="uf in ufs"
                                :key="uf"
                                :value="uf"
                            >
                                {{ uf }}
                            </option>
                        </select>
                    </div>
                </div>

            </div>
            <!--Box com cada deputado pertencente ao PARTIDO -->
            <div class="resultado-caixas">
                <ResultadoCaixa
                    v-for="deputado in dadosPartido.membros"
                    :key="deputado.id"
                    :nome="deputado.nome"
                    :image="deputado.image"
                    :uf="deputado.uf"
                    :email="deputado.email"
                />
            </div>
        </div>
        <div 
            class="carregando"
            v-else
        >
            <ProgressCircle
                :msg="msg"
                :carregando="carregar"
            />
        </div>

    </div>
</template>

<script>
import ResultadoCaixa from './ResultadoCaixa';
import ProgressCircle from './ProgressCircle';
import acessandoApi from '../service/api';

export default {
    name: "Resultado",
    props: {
        partido: {
            type: Object,
            required: true,
        },
    },
    components: {
        ProgressCircle,
        ResultadoCaixa
    },
    data(){
        return {
            msg: "Carregando dados do partido ...",
            carregar: true,
            dadosPartido: {},
            ufs: null,
            ufSelecionado: null
        }
    },
    async mounted() {
        // Pegando dados referente ao PARTIDO pela API
        const infPartido = await acessandoApi.dadosPartido(this.partido.id);
        this.ufs = await acessandoApi.recebendoUfs();
        this.dadosPartido = infPartido.dados
        this.carregar = false
    },
    watch: {
        async ufSelecionado(newValue){
            this.carregar = true;
            this.msg = "Aplicando filtro para busca de deputado...";
            const dadosFiltrado = await acessandoApi.dadosFiltrados(
                this.dadosPartido.sigla,
                newValue
            )
            if(dadosFiltrado != null ){
                this.carregar = false
            }
            this.dadosPartido.membros = dadosFiltrado
        }
    },
}
</script>

<style scoped>

#resultado{
    margin-bottom: 50px;
}
#carregado{
    margin-top: 30px;
    display: flex;
}
.resultado-info{
    color: white;
    border: white solid 3px;
    box-shadow: #5294F7 2px 4px 2px;
    padding: 15px 15px;
    margin-right: 15px;
    width: 350px;
    height: 350px;
    background-color: #537EFF;
    border-radius: 10px;
}
.resultado-info img{
    width: 150px;
    height: 75px;
}

.resultado-caixas{
    display: flex;
    flex-wrap: wrap;
    width: 900px;
}
#carregar {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.resultado-filtros{
    width: 100%;
}

</style>