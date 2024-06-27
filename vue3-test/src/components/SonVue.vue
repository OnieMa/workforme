<script>
import {ref} from "vue";

export default {
	async setup() {
		let count = ref(30);
		let p = new Promise((resolve, reject) => {
			setTimeout(() => {
				resolve({count});
			}, 1000)
		})
		//  可以返回一个Promise实例  但是得使用异步的组件包裹引入
		return await p
	}
}
</script>

<template>
	<div id="son"><h3>子组件</h3>
		<grandson-vue></grandson-vue>
	</div>
</template>

<style scoped>
#son {
	padding: 10px;
	background: green;
}
</style>