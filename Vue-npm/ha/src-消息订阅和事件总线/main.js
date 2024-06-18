import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

//
// const demo = Vue.extend({})
// const d= new demo()
// Vue.prototype = d

/*全局的事件组件*/
// Vue.prototype.x = {
//     a: 1,
//     b: 2
// }


new Vue({
    el: '#app',
    render(createElement) {
        return createElement(App)
    },
    beforeMount() {
        Vue.prototype.$bus = this
    }
})


