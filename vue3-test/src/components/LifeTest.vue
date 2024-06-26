<script>
import {onBeforeMount, onBeforeUnmount, onBeforeUpdate, onMounted, onUnmounted, onUpdated, ref} from "vue";

export default {
	setup() {
		// 通过组合api的形式操作
		onBeforeMount(()=>{
			console.log('onBeforeMount')
		})
		onMounted(()=>{
			console.log('onMounted')
		})
		onBeforeUpdate(()=>{
			console.log('onBeforeUpdate')
		})
		onUpdated(()=>{
			console.log('onUpdated')
		})
		onBeforeUnmount(()=>{
			console.log('onBeforeUnmount')
		})
		onUnmounted(()=>{
			console.log('onUnmounted')
		})

		let count = ref(0);
		return {count}
	},
	// 通过配置项的形式进行操作
	beforeMount() {
		console.log("life beforeMount");
	},
	beforeUnmount() {
		console.log("life beforeUnmount");
	}
}
</script>

<template>
	<h3> {{ count }}</h3>
	<button @click="count += 1">点击加1</button>
</template>

<style scoped>

</style>