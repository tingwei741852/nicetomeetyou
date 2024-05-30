import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router';
import VueNativeSock from 'vue-native-websocket'

const host = process.env.VUE_APP_API_HOST;
const port = process.env.VUE_APP_API_PORT;

Vue.use(VueNativeSock, `ws://${host}:${port}/ws/news/`, {
  reconnection: true,
  reconnectionAttempts: 5,
  reconnectionDelay: 3000,
})

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
