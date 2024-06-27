<template>
	<h3>Shallow Vue Test</h3>
	<h3> {{ person.name }} {{ person.age }}</h3>
	<h3>{{ person.job }}</h3>
	<h3>x:{{ x }} y: {{ z.y }}</h3>
	<h3>汽车: {{ person.car }}</h3>
	<button @click="person.name += '!'">修改姓名</button>
	<button @click="person.age += 1">修改年龄</button>
	<button @click="person.job.xian += '@'">修改job</button>
	<button @click="x+=1">点我x+1</button>
	<button @click="z.y+=1">点我y+1</button>

	<button @click="showRaw">输出原始person</button>
	<button @click="addCar">添加一个车的信息</button>
	<button @click="modifyCarName">换车</button>

</template>
<script>
import {markRaw, reactive, readonly, shallowRef, toRaw, toRefs} from "vue";

export default {
	setup() {
		// 只能检测第一层的数据变化
		// let person = shallowReactive({

		// shallowRef 只会对普通的数据进行响应式
		let x = shallowRef(0)

		// 不会对对象的属性进行响应式  就是说检测不到y的变化  但是整体替换z可以实现响应式
		let z = shallowRef({
			y: 0
		})


		let person = reactive({
			name: '張三',
			age: 20,
			job: {
				xian: 'xust',
				hz: {
					name: 'dahua',
					type: 'computer'
				}
			}
		});
		x = readonly(x) // x将不会被修改
		// let person = shallowReadonly(person) // person 第一层也不会被修改  更深的层可以修改


		function showRaw() {
			let rawPerson = toRaw(person); // 只能修改reactive定义的数据  ref的不可以
			rawPerson.age += 10;  // 数据会修改  但是不是响应式
			console.log(rawPerson)
		}

		function addCar() {
			let car = {name: '宝马', price: 30}
			person.car = markRaw(car); // 原始的数据 将不会被响应式修改
		}

		function modifyCarName(){
			person.car.name = 'tesla';
			console.log(person.car)
		}

		return {
			person, x, z, showRaw, addCar, ...toRefs(person), modifyCarName
		}
	}
}
</script>


<style scoped>

</style>