<script>
// import {h} from 'vue'
import {reactive, ref} from "vue";

export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: 'Hello',
	setup() {
		// 普通的数据  不会被vue检测
		let name = 'zahsan';
		let age = ref(18); //使用ref加工 才会被检测到
		let job = ref({
			type: '前端工程师',
			salary: 3000
		})
		let addr = reactive({
			type: 'str',
			detail: 'hangzhou',
			hobby: ['抽烟', '喝酒'],
			game: {
				china: '王者'
			}

		})

		function addSex(){
			addr.sex = 'man';
		}
		function delType(){
			delete addr.type;
		}
		function sayHello() {
			console.log(`我是`, name, age)
		}

		function modifyName() {
			age.value = 30
			job.value.salary = 40000    // 只需要拿到第一层的时候调用.value 后面的不需要
			addr.type = 'newNumber'     // 使用reactive就不需要加上value
			addr.hobby[1] = '烫头'       // 也可以直接被操作
			addr.game.china = '英雄联盟'  // 也可以深度的检测数据的变化

			// 下面是错误写法
			// this.name = 'lisi'
			// this.age = 30
		}

		return {
			name, age, job, addr, sayHello, modifyName,addSex,delType
		}

		// 返回一个渲染函数
		// return ()=>{
		// 	console.log(h)
		// 	return h('h1','hhhhaaaa')
		// }
	}
}
</script>

<template>
	<h3>hello vue3 {{ name }} {{ age }}</h3>
	<button @click="sayHello">你好</button>
	<button @click="modifyName">修改人的信息</button>
	<button @click="addSex"> 添加一个sex属性</button>
	<button @click="delType"> 删除type</button>
	<hr>
	<h3>{{ job.type }} {{ job.salary }}</h3>
	<h3>{{ addr.type }} {{ addr.detail }}</h3>
	<h3>{{ addr.hobby }} {{ addr.game.china }}</h3>
	<h3>{{addr.sex}}</h3>

</template>

<style scoped>

</style>