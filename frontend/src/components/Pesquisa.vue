<template>
  <div class="pesquisa">
    <form>
        <h2> Como deseja fazer sua pesquisa ? </h2>
        
        <div class="form-group">
          <label for="partido">Partido</label>
          <select id = "partido">
            <option v-for="partido in partidos" :key="partido" >{{partido}}</option>
          </select>
        </div>

        <div class="form-group">
          <label for="estado">Estado</label>
          <select id = "estado">
            <option v-for="uf in ufs" :key="uf">{{uf}}</option>
          </select>
        </div>
        <button>Pesquisar</button>
    </form>
  </div>
</template>

<script>
import api from '../service/api'

export default {
  
  async mounted() {
    const parametros = await api.parametrosIniciais()
    this.partidos = parametros.partidos
    this.ufs = parametros.ufs
  },


  name: 'Pesquisa',
  data() {
    return {
      partidos: [],
      ufs: []
    }
  },
}
</script>


<style scoped>

.pesquisa{
  padding: 10px 20px;
  color: aliceblue;
  display: flex;
  flex-direction: column;
  width: 400px;
  height: 250px;
  background-color: black;
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

form button{
  margin-top: 30px;
  width: 150px;
  text-align: center;
  height: 40px;
  font-size: 20px;
}
</style>
