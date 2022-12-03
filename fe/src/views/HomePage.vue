<template>
    <div>
        <v-layout row justify-start align-start wrap class="mt-4 pt-2">
            <v-flex justify-start align-end xs12 sm12 md12 lg5 l5 class="mx-2 pt-4">
                <v-img class="mx-auto" src="/picture.png" max-width="20vw" />
                <h2>
                    <div class="text-center primary--text">Francesco Pio Marino</div>
                    <div class="text-center secondary--text">Full-Stack Engineer</div>
                </h2>
            </v-flex>

            <v-flex justify-end align-end xs3 sm3 md6 lg2 xl2 class="ml-8 pl-8">
            </v-flex>
            <v-flex justify-end align-end xs8 sm8 md5 lg3 xl3 class="ml-8 pl-8 pt-4">
                <div class="text-left py-4 subheading font-weight-bold">
                    <v-icon large color="primary" left>fa-solid fa-map-pin</v-icon>
                    <span>Angers,&nbsp;</span>
                    <span class="primary--text">France</span>
                </div>
                <div class="text-left py-4 subheading font-weight-bold">
                        <v-icon large color="primary" left>fa-solid fa-cake-candles</v-icon>
                        <span>Catania,&nbsp;</span>
                        <span class="primary--text">Italy</span>
                </div>
                <div class="text-left py-4 subheading font-weight-bold">
                    <v-icon large color="primary" left>fa-solid fa-code</v-icon>
                    <span>Full&nbsp;</span>
                    <span class="primary--text">Remote</span>
                </div>
                <div class="text-left py-4 subheading font-weight-bold">
                    <v-icon large color="primary" left>fa-solid fa-question</v-icon>
                    <span>TO</span>
                    <span class="primary--text">DO</span>
                </div>
                <div class="text-left py-4 subheading font-weight-bold">
                    <v-icon large color="primary" left>fa-solid fa-envelope</v-icon>
                    <span>marfra99x</span>
                    <span class="primary--text">@gmail.com</span>
                </div>

                <v-card-actions class="justify-start hidden-sm-and-down ml-4">
                    <v-btn v-for="icon in icons" :key="icon.icon" fab dark outlined color="primary" :href="icon.href"
                        target="_blank">
                        <v-icon dark>{{ icon.icon }}</v-icon>
                    </v-btn>
                </v-card-actions>
            </v-flex>
        </v-layout>
        <v-flex justify-center align-center xs12 sm12 md4 lg12 xl5 class="mt-4 pt-4 ">
            {{ myDescription }}
        </v-flex>
    </div>
</template>

<script>
export default {
    mounted() {
        document.title = "Home | Francesco Marino"
    },
    data() {
        return {

            icons: [
                { href: "https://github.com/marfra99x", icon: "fab fa-github" },
                {
                    href: "https://www.linkedin.com/in/francescopiomarino/",
                    icon: "fab fa-linkedin-in"
                },
                {
                    href: "https://telegram.me/francesco_marino99",
                    icon: "fab fa-telegram"
                },
            ],
            myDescription: "I have recently finished my master degree in Computer Science at the University of Catania. I have always been passionate by programming and the software life cycle, and I have a strong personal background acquired during my studies during both high school and university focused on Computer Science. I like to expand my knowledge as much as possible, both in practical and theoretical. During my studies I have also been part of a research group focused on the topic of 'String Matching' that allowed me to publish several papers in journals and to attend several conferences as speaker. During and after my studies, I gained work and projects experience, which allowed me to also develop team-working and problem-solving skills that I intend to use in my role. I am very committed to succeeding in my career and I am extremely driven in achieving my goals. (WIP)"
        }
    }

}
</script>
