<script>
import nprogress from "nprogress";
// 配置 NProgress
nprogress.configure({ speed: 500, showSpinner: false })
export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: "About",
	destroyed() {
		console.log('About destroy');
	},
	// 组件内的路由守卫
	beforeRouteEnter(to, from, next) {
		console.log("beforeEnter", this)

		if (to.meta.isAuth) {
			if (localStorage.getItem("school") === 'dahua') {
				next();
			} else {
				alert("无权限")
			}
		} else {
			next()
		}
		// next(vm => {${1:}
		// });
	},
	beforeRouteLeave(to, from, next) {
		console.log("beforeRouteLeave", this)

		next();
	},
}
</script>

<template>
	<div>
		<h3>About</h3>
	</div>
</template>

<style scoped>

</style>