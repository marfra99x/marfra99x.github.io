<template>
    <v-app :dark="goDark">
        <v-main>
            <v-container align-center>
                <TopBar :goDark="goDark" @changeTheme="updateTheme($event)" />
                <router-view/>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
import TopBar from './components/TopBar.vue';

export default {
    name: 'App',

    components: {
        TopBar: TopBar,
    },

    methods: {
        updateTheme(updatedTheme) {
            this.goDark = !updatedTheme;
            this.$vuetify.theme.dark = this.goDark
            console.log(this.goDark)
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