<template>
    <div>
        <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-flex xs10 sm10 md10 lg6 xl6 class="mt-4 pt-4">
                <h2 class="mb-4 pl-4">{{$t("Education")}}</h2>
                <v-card-text class="py-0">
                    <v-timeline align-top dense>
                        <v-timeline-item color="primary" small>
                            <v-layout pt-3>
                                <v-flex xs4>
                                    <div class="caption font-weight-bold primary--text">{{$t("SEP")}} 2020 -</div>
                                    <div class="caption font-weight-bold primary--text">{{$t("JUL")}} 2022</div>
                                </v-flex>
                                <v-flex class="pl-2">
                                    <strong> {{$t("M.S.")}} {{$t("Computer Science")}}  </strong>
                                    <span class="caption mb-2"> - {{$t("University of Catania")}}</span>
                                    <div class="caption mb-2">{{$t("master_score")}}</div>
                                </v-flex>
                            </v-layout>
                        </v-timeline-item>


                        <v-timeline-item color="primary" small>
                            <v-layout pt-3>
                                <v-flex xs4>
                                    <div class="caption font-weight-bold primary--text">{{$t("AUG")}} 2021 -</div>
                                    <div class="caption font-weight-bold primary--text">{{$t("FEB")}} 2022</div>
                                </v-flex>
                                <v-flex class="pl-2">
                                    <strong>Erasmus</strong>
                                    <span class="caption mb-2"> - Kaunas Technology University</span>
                                </v-flex>
                            </v-layout>
                        </v-timeline-item>

                        <v-timeline-item color="primary" small>
                            <v-layout pt-3>
                                <v-flex xs4>
                                    <div class="caption font-weight-bold primary--text">{{$t("SEP")}} 2017 -</div>
                                    <div class="caption font-weight-bold primary--text">{{$t("JUL")}} 2020</div>
                                </v-flex>
                                <v-flex class="pl-2">
                                    <strong>{{$t("B.S.")}} {{$t("Computer Science")}}</strong>
                                    <span class="caption mb-2"> - {{$t("University of Catania")}}</span>
                                    <div class="caption mb-2">105/110</div>
                                </v-flex>
                            </v-layout>
                        </v-timeline-item>
                    </v-timeline>
                </v-card-text>
            </v-flex>
            <v-flex xs10 sm10 md10 lg6 xl6 class="mt-4 pt-4">
                <h2 class="mb-4 pl-4">{{$t("Experience")}}</h2>
                <v-card-text class="py-0">
                    <v-timeline align-top dense>
                        <v-timeline-item color="primary" small>
                            <v-layout pt-3>
                                <v-flex xs4>
                                    <div class="caption font-weight-bold primary--text">{{$t("JUN")}} 2022 -</div>
                                    <div class="caption font-weight-bold primary--text">{{$t("PRESENT")}}</div>
                                </v-flex>
                                <v-flex class="pl-2">
                                    <strong>Full-Stack Engineer</strong>
                                    <span class="caption mb-2"> - Skillbill</span>
                                    <div class="caption mb-2">{{$t("Remote")}}</div>
                                </v-flex>
                            </v-layout>
                        </v-timeline-item>

                        <v-timeline-item color="primary" small>
                            <v-layout pt-3>
                                <v-flex xs4>
                                    <div class="caption font-weight-bold primary--text">{{$t("FEB")}} 2020 -</div>
                                    <div class="caption font-weight-bold primary--text">{{$t("MAY")}} 2022</div>
                                </v-flex>
                                <v-flex class="pl-2">
                                    <strong>{{$t("Teaching Assistant")}}</strong>
                                    <span class="caption mb-2"> - {{$t("University of Catania")}}</span>
                                    <div class="caption mb-2">Catania</div>
                                </v-flex>
                            </v-layout>
                        </v-timeline-item>

                        <v-timeline-item color="primary" small>
                            <v-layout pt-3>
                                <v-flex xs4>
                                    <div class="caption font-weight-bold primary--text">{{$t("JUL")}} 2019 -</div>
                                    <div class="caption font-weight-bold primary--text">{{$t("SEP")}} 2019</div>
                                </v-flex>
                                <v-flex class="pl-2">
                                    <strong>{{$t("Data Manipulation")}}</strong>
                                    <span class="caption mb-2"> - Compunet Cards</span>
                                    <div class="caption mb-2">Catania</div>
                                </v-flex>
                            </v-layout>
                        </v-timeline-item>

                    </v-timeline>
                </v-card-text>
            </v-flex>
        </v-layout>


        <v-layout justify-center align-center wrap class="mt-4 pt-4 mb-0 pb-0">
            <h2>
                <span>Coding</span>
                <span class="primary--text">Skills</span>
            </h2>
        </v-layout>

        <v-layout row justify-center align-center wrap class="mt-0 pt-0 mb-4 pb-4 mx-0">
            <v-layout row justify-center align-center wrap class="mt-4 pt-2 mx-0">
                <v-flex xs10 sm10 md10 lg5 xl5 class="pt-4 pr-lg-2 pr-xl-2">
                    <strong>Algorithms</strong>
                    <v-progress-linear v-model="bufferAlgorithm" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>Python</strong>
                    <v-progress-linear v-model="bufferPython" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>SQL</strong>
                    <v-progress-linear v-model="bufferSQL" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>C/C++</strong>
                    <v-progress-linear v-model="bufferC" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>Back-End Development</strong>
                    <v-progress-linear v-model="bufferBackend" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>Java</strong>
                    <v-progress-linear v-model="bufferJava" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                </v-flex>
                <v-flex xs10 sm10 md10 lg5 xl5 class="pt-4 pl-lg-2 pr-xl-2">
                    <strong>String Matching</strong>
                    <v-progress-linear v-model="bufferSM" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>Pandas</strong>
                    <v-progress-linear v-model="bufferPandas" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>Git</strong>
                    <v-progress-linear v-model="bufferGit" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>Vue</strong>
                    <v-progress-linear v-model="bufferVue" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>JavaScript</strong>
                    <v-progress-linear v-model="bufferJS" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                    <strong>Front-End Development</strong>
                    <v-progress-linear v-model="bufferFrontend" :buffer-value="bufferValue" color="primary" height="16">
                    </v-progress-linear>
                </v-flex>
            </v-layout>
        </v-layout>

        <v-layout justify-center align-center wrap class="mt-4 pt-2 mb-0 pb-0">
            <h2>
                <span>Language</span>
                <span class="primary--text">Skills</span>
            </h2>
        </v-layout>
        <v-layout row justify-center align-center wrap class="mt-0 pt-0 mx-0">
            <v-flex xs10 sm10 md10 lg5 xl5 class="mpt-4">
                <strong>{{$t("Italian")}}</strong>
                <v-progress-linear v-model="bufferItalian" :buffer-value="bufferValue" color="primary" height="16">
                </v-progress-linear>
                <strong>{{$t("English")}}</strong>
                <v-progress-linear v-model="bufferEnglish" :buffer-value="bufferValue" color="primary" height="16">
                </v-progress-linear>
                <strong>{{$t("French")}}</strong>
                <v-progress-linear v-model="bufferFrench" :buffer-value="bufferValue" color="primary" height="16">
                </v-progress-linear>
            </v-flex>
        </v-layout>

        <v-layout row justify-center align-center wrap class="mt-4 pt-4 pb-4 mb-4">
            <div class="mt-4 pt-2">
                <v-btn href="FrancescoPioMarinoResume.pdf" target="_blank" color="primary" dark large>
                    {{$t("Download Resume")}}
                    <v-icon right dark>mdi-download-circle</v-icon>
                </v-btn>
            </div>
        </v-layout>


    </div>
</template>
  
<script>
export default {
    data() {
        document.title = "Resume | Francesco Marino"
        return {
            bufferPython: 0,
            bufferSQL: 0,
            bufferC: 0,
            bufferVue: 0,
            bufferPandas: 0,
            bufferJS: 0,
            bufferBackend: 0,
            bufferFrontend: 0,
            bufferGit: 0,
            bufferJava: 0,
            bufferAlgorithm: 0,
            bufferSM: 0,
            bufferValue: 100,
            interval: 0,
            bufferItalian: 0,
            bufferEnglish: 0,
            bufferFrench: 0,
        };
    },
    mounted() {
        this.startBuffer();
    },

    beforeDestroy() {
        clearInterval(this.interval);
    },

    methods: {
        startBuffer() {
            this.interval = setInterval(() => {
                this.bufferPython = 95
                this.bufferSQL = 95
                this.bufferC = 95
                this.bufferVue = 80
                this.bufferPandas = 90
                this.bufferJS = 80
                this.bufferBackend = 80
                this.bufferFrontend = 75
                this.bufferGit = 80
                this.bufferJava = 80
                this.bufferSM = 100
                this.bufferAlgorithm = 95
                this.bufferItalian = 100
                this.bufferEnglish = 90
                this.bufferFrench = 55
            }, 800);
        }
    }
};
</script>