<template>
  <div id="app">
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
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
