<template>
    <div>
        <v-navigation-drawer v-model="drawer" absolute temporary app width="150" height="340">
            <v-list class="pt-4">
                <v-list-item active-class="primary--text" to="/">
                    <v-list-item-content>
                        <v-list-item-title>HOME</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="primary--text" to="/resume">
                    <v-list-item-content>
                        <v-list-item-title>RESUME</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="primary--text" to="/research">
                    <v-list-item-content>
                        <v-list-item-title>RESEARCH</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar flat dense color="transparent">
            <v-app-bar-nav-icon class="hidden-md-and-up" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <v-app-bar-title class="headline">
                <span class="headline text-capitalize">Francesco</span>
                <span class="primary--text headline text-capitalize">Marino</span>
            </v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn @click="changeTheme" depressed small icon class="hidden-md-and-up">
                <v-icon v-if="goDark == true">mdi-weather-sunny</v-icon>
                <v-icon v-else>mdi-moon-waning-crescent</v-icon>
            </v-btn>
            <v-app-bar-title class="hidden-sm-and-down">
                <v-btn plain to="/" active-class="primary--text headline">Home</v-btn>
                <v-btn plain to="/resume" active-class="primary--text headline">Resume</v-btn>
                <v-btn plain to="/research" active-class="primary--text headline">Research</v-btn>
                <v-btn @click="changeTheme" depressed small icon>
                    <v-icon v-if="goDark == true">mdi-weather-sunny</v-icon>
                    <v-icon v-else>mdi-moon-waning-crescent</v-icon>
                </v-btn>
            </v-app-bar-title>
        </v-app-bar>
    </div>
</template>

<script>
export default {
    props: {
        goDark: {
            type: Boolean
        },
        blue: {
            type: String,
            default: "#FF00FF"
        }
    },
    data() {
        return {
            drawer: null
        };
    },
    methods: {
        changeTheme() {

            this.$emit("changeTheme", this.goDark);
        }
    }
};
</script>

<style >

</style>