<template>
    <div>
        <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-flex justify-center align-end xs12 sm12 md4 lg5 l3 class="mx-2 pt-4">
                <v-img class="mx-auto" src="/picture.png" max-width="20vw" />
                <div class="text-center primary--text">Francesco Pio Marino</div>
                <div class="text-center secondary--text">Full-Stack Engineer</div>
            </v-flex>

            <v-flex justify-end align-end xs12 sm12 md6 lg6 xl6 class="ml-8 pl-8">
                <div class="text-center py-4 subheading font-weight-bold">

                    <v-icon large color="primary" left>fa-solid fa-map-pin</v-icon>
                    <span>Catania,&nbsp;</span>
                    <span class="primary--text">Italy</span>
                </div>
                <div class="text-center py-4 subheading font-weight-bold">
                    <v-icon large color="primary" left>fa-solid fa-location-dot</v-icon>
                    <span>Angers,&nbsp;</span>
                    <span class="primary--text">France</span>
                </div>
                <div class="text-center py-4 subheading font-weight-bold">
                    <v-icon large color="primary" left>fa-solid fa-envelope</v-icon>
                    <span>marfra99x</span>
                    <span class="primary--text">@gmail.com</span>
                </div>

                <v-card-actions class="justify-center hidden-sm-and-down">
                    <v-btn v-for="icon in icons" :key="icon.icon" fab dark outlined color="green" :href="icon.href"
                        target="_blank">
                        <v-icon dark>{{ icon.icon }}</v-icon>
                    </v-btn>
                </v-card-actions>
            </v-flex>
        </v-layout>
        <v-flex justify-center align-center xs12 sm12 md4 lg12 xl5 class="mt-4 pt-4 pr-16 pl-16">
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
            ],
            myDescription: "I have recently finished my master degree in Computer Science at the University of Catania. I have always been passionate by programming and the software life cycle, and I have a strong personal background acquired during my studies during both high school and university focused on Computer Science. I like to expand my knowledge as much as possible, both in practical and theoretical. During my studies I have also been part of a research group focused on the topic of 'String Matching' that allowed me to publish several papers in journals and to attend several conferences as speaker. During and after my studies, I gained work and projects experience, which allowed me to also develop team-working and problem-solving skills that I intend to use in my role. I am very committed to succeeding in my career and I am extremely driven in achieving my goals. (WIP)"
        }
    }

}
</script>
