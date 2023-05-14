import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueKonva from 'vue-konva'
// import VueChartkick from 'vue-chartkick'
// import 'chartkick/chart.js'

// app.use(VueChartkick)
Vue.config.productionTip = false
Vue.use(VueKonva);

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')

