<template>
    <div>

        <v-footer class="pb-0 mb-0 mx-0 hidden-sm-and-down" color="transparent">
            {{$t("Developed using")}}&nbsp;
            <v-icon small color="green">fab fa-vuejs</v-icon>
        </v-footer>
        <v-footer class="pt-0 mt-0 mx-0" color="transparent">
            <span class="hidden-sm-and-down">{{$t("Some feature have just learning purpose.")}}</span>
            <span class="hidden-md-and-up">{{$t("Developed using")}}&nbsp;</span>
            <span class="hidden-md-and-up"><v-icon small color="green">fab fa-vuejs</v-icon></span>
            <v-spacer></v-spacer>
            <div>&copy; {{ new Date().getFullYear() }}</div>
        </v-footer>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>

</style>