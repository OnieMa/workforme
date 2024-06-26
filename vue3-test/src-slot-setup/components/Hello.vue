<script>
import {reactive} from "vue";

export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: 'Hello',
	props: ['msg', 'school'],
	emits: ['sayHello'],  // vue3 的新东西 必须声明一下 否则要提示错误(不影响运行)
	mounted() {
		console.log(this)
	},
	setup(props, context) {
		console.log('this set_up ', this)
		console.log('props', props)
		console.log('attr', context.attr)
		let person = reactive({
			name: 'zhansgahn',
			age: 19
		})

		function speakHello(value) {
			context.emit('sayHello', value)
		}

		return {person, speakHello}
	},
	beforeCreate() {
		console.log('beforeCreate', this);
	},

}
</script>

<template>
	<button @click="speakHello(person)">触发hello</button>
	<h3> Hello Vue 3</h3>
	<slot name="sss"></slot>
	<h3> {{ msg }} {{ school }}</h3>
	<slot name="sss"></slot>

	<hr>
	<h3>{{ person.name }} {{ person.age }}</h3>
</template>

<style scoped>

</style>