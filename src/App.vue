<template>
  <v-app>
    <v-main>
      <HomePage/>
    </v-main>
  </v-app>
</template>

<script>
import HomePage from './views/HomePage';

export default {
  name: 'App',

  components: {
    HomePage: HomePage,
  },

  data: () => ({
    //
  }),
};
</script>
