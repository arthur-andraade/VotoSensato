<template>
    <div id="resultado">

        <!--Box com informações do Patido em relação há camara -->
        <div class="resultado-info">
            <img src="data:image/png;base64,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" alt="Imagem do partido">

            <div>
                <h3>Sigla: </h3>
                <h3>Nome: </h3>
                <h3>Numero deputados na camara: </h3>
                <h3>Situação: </h3>
            </div>

        </div>
        
        <!--Box com informações do Patido em relação há camara -->
        <div class="resultado-caixas">
            <ResultadoCaixa/>
            <ResultadoCaixa/>
            <ResultadoCaixa/>
            <ResultadoCaixa/>
            <ResultadoCaixa/>
        </div>

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
    padding: 15px 15px;
    margin-right: 15px;
    width: 350px;
    height: 280px;
    background-color: #537EFF;
    border-radius: 10px;
}
.resultado-info img{
    width: 150px;
    height: 75px;
}

.resultado-caixas{
    display: flex;
    flex-wrap: wrap;
    width: 900px;
}
</style>