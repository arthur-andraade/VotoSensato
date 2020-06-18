<template>
  <div class="pesquisa" :class="{loading: carregando}">
    
    <div v-if="!carregando">
      <h2> Como deseja fazer sua pesquisa ? </h2>
        <div class="form-group">
          <label for="partido">Partido</label>
          <select id = "partido" v-model="partidoSelecionado">
            <option 
              v-for="partido in partidos" 
              :key="partido" 
              :value="partido"
            >
              {{ partido }}            
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="estado">Estado</label>
          <select id = "estado" v-model="ufSelecionado">
            <option 
              v-for="uf in ufs" 
              :key="uf" 
              :value="uf"
            >
              {{ uf }}
            </option>
          </select>
        </div>        
        <button @click="dadosSelecionados">Pesquisar</button>
    </div>
    
    <div v-else class="loading">
      <ProgressCircle 
        :carregando="carregando"
        msg="Carregando dados"
      />
    </div>

  </div>
</template>

<script>
import ProgressCircle from './ProgressCircle';
import api from '../service/api'

export default {
  async mounted() {
    const parametros = await api.parametrosIniciais();
    this.partidos = parametros.partidos;
    this.ufs = parametros.ufs;
    this.progressBar = null;
    this.carregando = false;
  },
  name: 'PesquisaParametros',
  components: {
    ProgressCircle
  },
  data() {
    return {
      partidos: [],
      ufs: [],
      partidoSelecionado: null,
      ufSelecionado: null,
      carregando: true,
    }
  },
  methods: {
    dadosSelecionados: function (){
        this.$emit("dadosSelecionados", 
          {
            partido: this.partidoSelecionado,
            uf: this.ufSelecionado
          }
        );
    }
  }
}
</script>


<style scoped>

.pesquisa{
  border-radius: 10px;
  padding: 10px 20px;
  color: aliceblue;
  display: flex;
  flex-direction: column;
  width: 400px;
  height: 250px;
  background-color: #537EFF;
  align-items: center;
}


.form-group{
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.form-group label{
  margin-right: 10px;
  font-size: 22px;
}

.form-group select{
  width: 120px;
}

button{
  border-radius: 10px;
  border: white solid 2px;
  color: white;
  background-color: #0537CC;
  margin-top: 30px;
  width: 150px;
  text-align: center;
  height: 40px;
  font-size: 20px;
}

.loading{
  background-color: transparent;
}
</style>
