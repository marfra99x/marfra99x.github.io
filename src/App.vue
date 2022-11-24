<template>
    <v-app :dark="goDark" >
        <v-main>
            <TopBar :goDark="goDark" @changeTheme="updateTheme($event)"/>
            WIP
        </v-main>
    </v-app>
</template>

<script>
import TopBar from './components/TopBar';

export default {
    name: 'App',

    components: {
        TopBar: TopBar,
    },

    methods: {
        updateTheme(updatedTheme) {
            this.goDark = !updatedTheme;
        }
    },
    data() {
        return { goDark: false };
    },
}
</script>

<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css";
</style>