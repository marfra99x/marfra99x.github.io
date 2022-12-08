<template>
    <div>
        <v-navigation-drawer v-model="drawer" absolute temporary app width="150" height="340">
            <v-list class="pt-4">
                <v-list-item active-class="primary--text" to="/">
                    <v-list-item-content>
                        <v-list-item-title>Home</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="primary--text" to="/resume">
                    <v-list-item-content>
                        <v-list-item-title>{{$t("Resume")}}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item active-class="primary--text" to="/research">
                    <v-list-item-content>
                        <v-list-item-title>{{$t("Research")}}</v-list-item-title>
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
                <v-btn plain to="/resume" active-class="primary--text headline">{{$t("Resume")}}</v-btn>
                <v-btn plain to="/research" active-class="primary--text headline">{{$t("Research")}}</v-btn>
                <v-menu left bottom>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn icon v-bind="attrs" v-on="on">
                                <v-img contain width="24" height="24" :src="`/${current}.png`"></v-img>
                        </v-btn>
                    </template>
                    <v-list>
                        <v-list-item v-for="l in language" :key="l" @click="changeLanguage(l)">
                            <v-list-item-title> <v-img contain width="24" height="24" :src="`/${l}.png`"></v-img></v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
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
            drawer: null,
            language: [
                "english_icon", "italy_icon", "french_icon"
            ],
            current: "english_icon",
        };
    },
    methods: {
        changeTheme() {
            this.$emit("changeTheme", this.goDark)
        },
        changeLanguage(l){
            this.$root.$i18n.locale = l.substring(0,2)
            this.current = l
        }
    }
};
</script>

<style >

</style>