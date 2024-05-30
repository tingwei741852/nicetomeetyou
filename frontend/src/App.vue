<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    <router-link :to="'/'">
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="	https://s.udn.com.tw/static/img/logo_mark.svg"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="70"
          src="https://tw-nba.udn.com/img/logo_name.svg"
          width="70"
        />
      </div>
    </router-link >
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>

     <!-- <v-footer
    color="primary"
    
  >
  <p class="d-flex justify-center white--text">此網站僅作為練習使用，內容皆來源於聯合新聞網</p>
  </v-footer> -->
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
