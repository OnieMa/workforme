<script>
import {reactive, computed} from "vue";

export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: 'Hello',
	props: ['msg', 'school'],
	emits: ['sayHello'],  // vue3 的新东西 必须声明一下 否则要提示错误(不影响运行)
	setup() {
		let person = reactive({
			firstName: 'san',
			lastName: 'zhang',
			age: 19
		})

		// let fullName = computed(()=>{
		// 	return person.lastName + person.firstName
		// })

		// 简写的形式  只有读取 被修改会报错
		// person.fullName = computed(() => {
		// 	return person.lastName + '-' + person.firstName
		// })

		// 完整的形式
		person.fullName = computed({
			get() {
				return person.lastName + '-' + person.firstName
			},
			set(value) {
				const nameArr = value.split('-');
				person.lastName = nameArr[0]
				person.firstName = nameArr[1]
			}
		})


		return {person}
	},
	// computed: {
	// 	fullName() {
	// 		return this.person.lastName + this.person.firstName
	// 	}
	// },

}
</script>

<template>
	<h3>一个人的信息: {{ person.fullName }}</h3>
	姓<input type="text" v-model="person.lastName"> <br>
	名<input type="text" v-model="person.firstName">

	<br>
	全名 <input v-model="person.fullName">
</template>

<style scoped>

</style>