<script>
import {reactive, ref, watch , watchEffect} from "vue";

export default {
	name: 'WatchTest',
	setup() {
		let num = ref(0)
		let msg = ref('Hi好');
		let person = reactive({
			name: 'zhansan',
			age: 18,
			job: {
				j1: {
					salary: 30
				}
			}
		})
		let personRef = ref({
			name: 'zhansan',
			age: 18,
			job: {
				j1: {
					salary: 30
				}
			}
		})
		// 这里的value 是指监视到ref被reactive改写后的对象的数据 如果用ref定义 就得这样子监视
		watch(personRef.value,()=>{
			console.log()
		})

		function add() {
			num.value += 1
		}

		/*		// 监视ref定义的响应式数据
				watch(num, (newv, oldv) => {
					console.log(newv, oldv)
				})

				// 监视ref定义的多个数据
				watch(msg, (newv, oldv) => {
					console.log(newv, oldv)
				})*/

		// 1. 监视ref定义的多个数据
		// watch([num, msg], (newv, oldv) => {
		// 	console.log(newv, oldv)
		// }, {immediate: true})

		// watch 监视reactive
		// 2. 此处无法获取到oldValue 这是vue3存在的问题
		// 3. 且强制开启了深度监视
/*
		// 4. 监视一个值的时候  需要按照函数返回
		watch(() => person.age, (newv, oldv) => {
			console.log(newv, oldv)
		})
		// 5. 监视某些属性的时候得
		watch([() => person.age, () => person.name], (newv, oldv) => {
			console.log(newv, oldv)
		})

		// 6. 监视person 的一个属性  下的一级内的值的时候  还是得加上deep  否则就直接监视person
		watch(() => person.job, (newv, oldv) => {
			console.log(newv, oldv)
		}, {deep : true})*/


		// 会查看下面绿色的函数中使用了谁  有谁就监视谁 哪些依赖的数据被修改了  就会被监视到
		watchEffect(()=>{
			console.log('watchEffect 开启了 ...' , num.value)
			console.log('watchEffect 开启了 ...' , person.name)
		})
		return {num, msg, person, personRef,add}
	},


}
</script>

<template>
	<h3> 当前的num: {{ num }}</h3>
	<button @click="add">+1</button>
	<h3>当前的信息 {{ msg }}</h3>
	<button @click="msg += '!'">加叹号</button>
	<hr>
	<h3> {{ person.name }} {{ person.age }}</h3>
	<button @click="person.name += '!'">修改姓名</button>
	<button @click="person.age += 1">修改年龄</button>
</template>

<style scoped>

</style>