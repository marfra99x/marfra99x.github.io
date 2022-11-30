<template>
    <div>
        <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-flex xs12 sm12 md12 lg9 xl9 class="mt-4 pt-4">
                <div>
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                    et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                    aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
                    culpa qui officia deserunt mollit anim id est laborum."
                </div>
            </v-flex>
            <v-flex justify-end align-end xs12 sm12 md12 lg3 xl3 class="mt-4 pt-2">
                <v-card class="d-flex flex-column" max-width="300">
                    <v-card-text>
                        <div class="text-center display-1 primary--text">
                            Summary
                        </div>
                        <span class="primary--text">Publications:</span>
                        <span class=""> {{ number_of_articles }}</span>
                        <br>
                        <span class="primary--text">Citation:</span>
                        <span class=""> {{ number_of_citations }}</span>
                        <br>
                        <span class="primary--text">H-index:</span>
                        <span class=""> {{ h_index }}</span>
                        <br>
                        <span class="primary--text">Co-authored:</span>
                        <span class=""> 4</span>
                        <br>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        document.title = "Research | Francesco Marino"
        return {
            number_of_articles: null,
            number_of_citations: null,
            h_index: null,
        }
    },
    created() {
        this.get_info()
    },
    methods: {
        async get_info() {
            axios.defaults.baseURL = 'http://localhost:5000/';
            await axios.get(
                "/research_info"
            ).then((result) => {
                this.number_of_articles = result.data["number_of_articles"]
                this.number_of_citations = result.data["number_of_citations"]
                this.h_index = result.data["h_index"]
            })
        }
    }
}

</script>
