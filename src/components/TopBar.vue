<template>
    <div>
        <v-navigation-drawer v-model="drawer" absolute temporary app width="150" height="340">
            <v-list class="pt-4">
                <v-list-item active-class="green--text" to="/">
                    <v-list-item-content>
                        <v-list-item-title>HOME</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="green--text" to="/resume">
                    <v-list-item-content>
                        <v-list-item-title>RESUME</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="green--text" to="/services">
                    <v-list-item-content>
                        <v-list-item-title>SERVICES</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="green--text" to="/portfolio">
                    <v-list-item-content>
                        <v-list-item-title>PORTFOLIO</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="green--text" to="/blog">
                    <v-list-item-content>
                        <v-list-item-title>BLOG</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="green--text" to="/contact">
                    <v-list-item-content>
                        <v-list-item-title>CONTACT</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar flat color="transparent">
            <v-app-bar-nav-icon class="hidden-md-and-up" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <v-app-bar-title class="headline">
                <span class="red--text">Francesco</span>
                <span class="black--text">Marino</span>
            </v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn @click="changeTheme" depressed small icon class="hidden-md-and-up">
                <v-icon v-if="goDark == true">mdi-weather-sunny</v-icon>
                <v-icon v-else>mdi-moon-waning-crescent</v-icon>
            </v-btn>
            <v-app-bar-title class="hidden-sm-and-down">
                <v-btn plain to="/" active-class="green--text headline">Home</v-btn>
                <v-btn plain to="/resume" active-class="green--text headline">Resume</v-btn>
                <v-btn plain to="/services" active-class="green--text headline">Services</v-btn>
                <v-btn plain to="/portfolio" active-class="green--text headline">Portfolio</v-btn>
                <v-btn plain to="/blog" active-class="green--text headline">Blog</v-btn>
                <v-btn plain to="/contact" active-class="green--text headline">Contact</v-btn>
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