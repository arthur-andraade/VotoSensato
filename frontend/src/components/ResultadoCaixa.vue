<template>
        <div class="caixa"> 
            
            <div class="principal-info">
                <img :src="image">
                <div>
                    <h3>Nome: {{ nome }}</h3>
                    <h3>UF: {{ uf }}</h3>
                    <h3>Email: {{ email }}</h3>
                </div>
            </div>
            <div>
                <button> Saber mais</button>
            </div>
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
    border: white none 3px;
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
    width: 100px;
}

.principal-info div{
    margin-left: 10px;
}
.principal-info div h3{
    color: white;
    word-break: break-word;
    text-align: initial;
}

.caixa div button{
    margin-top: 25px;
    height: 50px;
    width: 150px;
    background-color: #0537CC;
    color: white;
    border-style: none;
    border-radius: 10px;
}

.caixa div button:hover{
    background-color: #0645FF;
}
</style>