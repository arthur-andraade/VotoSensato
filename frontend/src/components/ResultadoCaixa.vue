<template>
        <div class="caixa"> 
            
            <div class="principal-info">
                <img src="http://www.camara.gov.br/internet/deputado/bandep/73701.jpg">
                <div>
                    <h3>Nome:</h3>
                    <h3>Nome parlamentar:</h3>
                    <h3>Condição:</h3>
                </div>
            </div>

            <button> Saber mais</button>
        </div>
</template>

<script>
export default {
    name: "ResultadoCaixa"
}
</script>

<style scoped>

.caixa{
    margin: 0px 15px;
    width: 400px;
    height: 300px;
    background-color: #537EFF;
    border-radius: 10px;
}
.caixa:nth-child(n+3){
    margin-top: 15px;
}

.principal-info{
    padding: 10px 10px;
    height: 160px;
    display: flex;
}
.principal-info img{
    border-radius: 10%;
}

.principal-info div{
    margin-left: 10px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.caixa button{
    margin-top: 30px;
    height: 50px;
}
</style>