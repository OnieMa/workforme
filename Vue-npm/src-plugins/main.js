import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false
// 引入插件
import plugins from "@/components/plugins";
Vue.use(plugins ,1,2,3)
/*
new Vue({
  render: h => h(App),
}).$mount('#app')
*/


new Vue({
  el: '#app',
  render(createElement){
    return createElement(App)
  }
})
