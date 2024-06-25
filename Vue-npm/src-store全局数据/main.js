import Vue from 'vue'
import store from "@/store";

import App from './App.vue'
Vue.config.productionTip = false

/*
new Vue({
  render: h => h(App),
}).$mount('#app')
*/


new Vue({
	el: '#app',
	render(createElement) {
		return createElement(App)
	},
	store,
	beforeMount() {
		Vue.prototype.$bus = this
	}

})
console.log(this)
