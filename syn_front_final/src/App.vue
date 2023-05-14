<template>
  <v-app>
    <v-main>
      <AppTitle/>
    </v-main>
  </v-app>
</template>


<script>

import AppTitle from './components/AppTitle';

export default {
  name: 'App',

  components: {
    AppTitle,
  },

  data: () => ({
    //
  }),
};
</script>
