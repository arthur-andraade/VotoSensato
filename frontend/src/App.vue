<template>
  <div id="app">
    <div id= "titulo">
      <h1>Voto<span>Sensato</span></h1>
    </div>

    <div v-if="!pesquisar">
        <PesquisaParametros @dadosSelecionados="recebendoParametros"/>
    </div>
    <div v-else>
      <Resultado/>
    </div>
  </div>

</template>

<script>

import PesquisaParametros from './components/Pesquisa.vue';
import Resultado from './components/Resultado';

export default {
  name: 'App',
  components: {
    PesquisaParametros,
    Resultado
  },
  data() {
    return {
      pesquisar: false,
      parametrosPesquisa: {}
    }
  },
  methods: {
    // Recebendo parâmetros para realizar buscar de deputados na A
    recebendoParametros: function(parametros){
      this.parametrosPesquisa.partido = parametros.partido;
      this.parametrosPesquisa.uf = parametros.uf;
      this.pesquisar = true;
    },
  },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  align-items: center;
}

#titulo{
  font-size: 25px;
  color: white;
  font-family: 'Racing Sans One', cursive;
}

#titulo span{
  font-size: 55px;
  text-shadow: #537EFF 2px 3px 2px;
}
</style>
