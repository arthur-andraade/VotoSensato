<template>
    <div id="resultado">
        <div class="resultado-info"></div>
        <ResultadoCaixa/>
    </div>
</template>

<script>
import ResultadoCaixa from './ResultadoCaixa';

export default {
    name: "Resultado",
    components: {
        ResultadoCaixa
    }
}
</script>

<style scoped>
#resultado{
    margin-top: 30px;
    display: flex;
}
.resultado-info{
    margin-right: 15px;
    width: 350px;
    height: 200px;
    background-color: black;
}
</style>