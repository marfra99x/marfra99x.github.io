<template>
    <v-app :dark="goDark" :style="{ background: $vuetify.theme.themes[theme].background }">
        <v-main>
            <v-container align-center>
                <TopBar :goDark="goDark" @changeTheme="updateTheme($event)" />
                <router-view />
            </v-container>
        </v-main>
        <FooterBar/>
    </v-app>
</template>

<script>
import TopBar from './components/TopBar.vue';
import FooterBar from './components/FooterBar.vue';

export default {
    name: 'App',

    components: {
        TopBar: TopBar,
        FooterBar: FooterBar,
    },

    methods: {
        updateTheme(updatedTheme) {
            this.goDark = !updatedTheme;
            this.$vuetify.theme.dark = this.goDark
            this.theme = (this.goDark) ? 'dark' : 'light'
        }
    },
    data() {
        return {
            goDark: false,
            theme: 'light'
        };
    },
}
</script>

<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css";
</style>