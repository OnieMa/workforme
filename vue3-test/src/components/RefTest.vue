<script>
import {reactive, toRef, toRefs} from "vue";

export default {
	setup() {
		let person = reactive({
			name: '战三',
			age: 19,
			job: {
				j1: {
					type: "程序员"
				}
			}
		});
		let person1 = reactive({
			name: '战三',
			age: 19,
			job: {
				j1: {
					type: "程序员"
				}
			}
		});

		let p2 = toRefs(person1);
		console.log("@@@@",p2)



		let name = toRef(person, 'name')

		function modifyName() {
			name.value = name.value + '-'
		}

		return {
			... toRefs(person1.job.j1),
			person,
			name,
			modifyName,
			age: toRef(person, 'age')
		}
	}
}

</script>

<template>
	<h3>Test toRefs</h3>
	<h3>{{ name }}</h3>
	<h3>{{ age }}</h3>
	<h3>{{ person.job.j1.type }}</h3>

	<button @click="person.name += '!'">改名字</button>
	<button @click="person.age += 1">改age</button>
	<button @click="person.job.j1.type += '@'">改工作</button>

	<button @click="modifyName">使用方法修改名字</button>
	<h3>{{type}}</h3>


</template>

<style scoped>

</style>