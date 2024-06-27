<script>
import {customRef, ref} from "vue";

export default {
	setup: function () {
		// 自定义一个ref
		function myRef(value) {
			let tiemoutId //定时器的id
			console.log(value)
			return customRef((track, trigger) => {
				return {
					get() {
						console.log(`有人读取了数据${value}`)
						track() // 让get去追踪一下数据变化   . 没有这个的话 只会在第一次初始化的时候调用一下
						return value
					},
					set(newValue) {
						console.log(`有人修改${value}`, `变成了${newValue}`)
						if (tiemoutId) {
							clearTimeout(tiemoutId)
						}
						tiemoutId = setTimeout(() => {
							value = newValue
							trigger() //通知vue解析模板
						}, 500);
					}
				}
			})
		}
		let keyword = ref('hello')
		let myKey = myRef('myHello')


		return {
			keyword, myKey
		}
	}
}
</script>

<template>
	<input type="text" v-model="keyword">
	<h3>keyword : {{ keyword }}</h3>
	<input type="text" v-model="myKey">
	<h3>myKey : {{ myKey }}</h3>
</template>

<style scoped>

</style>