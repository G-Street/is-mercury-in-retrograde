import Vue from 'vue'
import App from './App.vue'
import VueKinesis from 'vue-kinesis'

Vue.use(VueKinesis)
Vue.config.productionTip=false

new Vue({
  render: h => h(App),
}).$mount('#app')
