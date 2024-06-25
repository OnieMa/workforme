import Vue from 'vue'
import App from './App.vue'
import vueResource from 'vue-resource'

Vue.config.productionTip = false

Vue.use(vueResource)
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
	beforeMount() {
		Vue.prototype.$bus = this
	}
})
