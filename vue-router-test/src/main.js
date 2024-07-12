import Vue from 'vue';
import { Button, Row } from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import '@/assets/css/nprogress.css';

Vue.use(Button)
Vue.use(Row)

new Vue({
	el: '#app',
	render: h => h(App)
});

import VueRouter from "vue-router";
import router from "@/router";

Vue.use(VueRouter)
Vue.config.productionTip = false

new Vue({
	render: h => h(App),
	router: router
}).$mount('#app')
