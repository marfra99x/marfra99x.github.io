<template>
    <div>
        <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-img justify-center src="/picture.png" max-width="25vw" />
        </v-layout>

        <v-layout column justify-center align-center wrap class="mt-4 pt-2">
            <div class="primary--text">Francesco Pio Marino</div>
            <div class="secondary--text">Full-Stack Engineer</div>
        </v-layout>
    </div>
</template>

<script>
export default {
    mounted() {
        document.title = "Home | Francesco Marino"
    },
    data(){
        return{
        }
    }

}
</script>
