<template>
    <div id="grupo-caixa">
        <div class="caixa"> </div>
        <div class="caixa"> </div>
        <div class="caixa"> </div>
        <div class="caixa"> </div>
        <div class="caixa"> </div>
        <div class="caixa"> </div>
        <div class="caixa"> </div>
    </div>
</template>

<script>
export default {
    name: "ResultadoCaixa"
}
</script>

<style scoped>
#grupo-caixa{
    display: flex;
    flex-wrap: wrap;
    width: 800px;
}
.caixa{
    margin: 0px 15px;
    width: 300px;
    height: 300px;
    background-color: aquamarine;
}
.caixa:nth-child(n+3){
    margin-top: 15px;
}
</style>