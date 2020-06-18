<template>
        <div class="caixa"> 
            
            <div class="principal-info">
                <img :src="image">
                <div>
                    <h3>Nome: {{ nome }}</h3>
                    <h3>UF:{{ uf }}</h3>
                </div>
            </div>
            <h3>Email: {{ email }}</h3>
            <button> Saber mais</button>
        </div>
</template>

<script>
export default {
    name: "ResultadoCaixa",
    props: ['nome','image','uf','email']
}
</script>

<style scoped>

.caixa{
    border: white solid 3px;
    margin: 0px 15px;
    width: 400px;
    height: 300px;
    background-color: #537EFF;
    box-shadow: #5294F7 2px 4px 2px;
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
    width: 100px;
}

.principal-info div{
    margin-left: 10px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-wrap: wrap;
}

.caixa button{
    height: 50px;
}
</style>