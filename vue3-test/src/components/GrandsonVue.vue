<script>
import {inject, isReactive, isRef} from "vue";
import Dialog from "@/components/Dialog.vue";
export default {
	components: {Dialog},
	setup() {
		let car = inject('car')
		console.log('isRef',isRef(car))
		console.log('isReactive',isReactive(car))
		return {
			car
		}
	}
}
</script>

<template>
	<div id="sun">
		<h3>孙组件</h3>
		<h3>{{car}}</h3>
		<Dialog></Dialog>
	</div>
</template>

<style scoped>
#sun {
	background: aqua;
	padding: 10px;
}
</style>