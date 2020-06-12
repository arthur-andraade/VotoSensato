<template>
  <div id="app">
    <div id= "titulo">
      <h1>VotoSensato</h1>
    </div>

    <pesquisa/>
  </div>
</template>

<script>
import pesquisa from './components/Pesquisa.vue'

export default {
  name: 'App',
  components: {
    pesquisa
  }
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
  margin-top: 60px;
  align-items: center;
}
</style>
