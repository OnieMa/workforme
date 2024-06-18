export default {
    install(Vue, x, y, z) {

        console.log(x, y, z)
        Vue.filter('mySlice', function (value) {
            return value.slice(0, 4)
        });

        Vue.mixin({
            data() {
                return {
                    x: 1090,
                    y: 2000
                }
            }
        })

        Vue.directive('fbind', {
            bind(element, binding) {
                element.value = binding.value;
            },
        })

        Vue.prototype.hello = () => {
            alert("hello!")
        }

        console.log("@@@", Vue)
    }
}
