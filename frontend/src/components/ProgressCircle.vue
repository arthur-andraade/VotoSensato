<template>
    <div>
        <radial-progress-bar 
        :diameter="250"
        :completed-steps="completedSteps"
        :total-steps="totalSteps"
        :startColor="primaryColor"
        :stopColor="stopColor"
        >
            <p id="msg">{{ msg }}</p>
        </radial-progress-bar>
    </div>
</template>

<script>
import RadialProgressBar from 'vue-radial-progress'

export default {

    name: "ProgressCircle",
    props: {
        carregando: {
            type: Boolean,
            required: true
        },
        msg:{
            type: String,
            required: true
        }
    },

    components: {
        RadialProgressBar
    },

    data() {
        return {
            carregar: this.carregando,
            completedSteps: 5,
            totalSteps: 10,
            primaryColor: "#537EFF",
            stopColor: "#00B7FF",
            progress: null
        }
    },

    mounted() {
        this.iniciandoProgress();
    },
    
    methods: {
        iniciandoProgress: function() {
            if(this.carregar){
                this.progress = setInterval(
                    () => {
                        this.completedSteps++;
                    }, 200);
            }else{
                this.progress = null;
            }
        }
    },
    
}
</script>

<style scoped>

#msg{
    color: white;
    font-size: 18px;
}
</style>