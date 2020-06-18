<template>
    <div id="resultado">
        <div 
            id="carregado"
            v-if="!carregar"
        >             
            <!--Box com informações do Patido em relação há camara -->
            <div class="resultado-info">
                <img :src="dadosPartido.logo">
                <div>
                    <h3>Sigla: {{ dadosPartido.sigla }} </h3>
                    <h3>Nome: {{ dadosPartido.nome }} </h3>
                    <h3>Numero deputados na camara: {{ dadosPartido.totalMembros}}</h3>
                    <h3>Situação: {{ dadosPartido.situacao }} </h3>
                </div>

            </div>
            <!--Box com informações do Patido em relação há camara -->
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
                msg="Carregando dados sobre partido..."
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
            carregar: true,
            dadosPartido: {}
        }
    },

    async mounted() {
        const infPartido = await acessandoApi.dadosPartido(this.partido.id);
        this.dadosPartido = infPartido.dados
        this.carregar = false
    },
}
</script>

<style scoped>
#carregado{
    margin-top: 30px;
    display: flex;
}
.resultado-info{
    border: white solid 3px;
    box-shadow: #5294F7 2px 4px 2px;
    padding: 15px 15px;
    margin-right: 15px;
    width: 350px;
    height: 280px;
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
</style>