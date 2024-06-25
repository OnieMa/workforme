<template>
	<div>
		<h3>person 组件中的 {{ sum }}</h3>
		<h3>列表第一个人名是 {{firstListName}}</h3>
		<button @click="add">添加人员</button>
		<button @click="addWang">添加姓王的人员</button>
		<ul>
			<li v-for="item in persons"> {{ item.name }} {{ item.age }}</li>
		</ul>

		<input type="text" placeholder="输入名字" v-model="name">
		<input type="text" placeholder="输入年纪" v-model="age">
	</div>

</template>

<script>
import store from "@/store";

export default {
	name: "Person",
	computed: {
		persons() {
			return this.$store.state.personAbout.persons;
		},
		sum() {
			return this.$store.state.countAbout.sum
		},
		firstListName(){
			return this.$store.getters["personAbout/firstListName"]
		}
	},
	data() {
		return {
			name: '',
			age: 0
		}
	},
	methods: {
		add() {
			const persons = {
				name: this.name,
				age: this.age,
			}
			this.$store.commit('personAbout/ADDPERSON', persons);
		},
		addWang(){
			const persons = {
				name: this.name,
				age: this.age,
			}
			this.$store.dispatch('personAbout/addPersonWang',persons)
		}

	},
}
</script>


<style scoped>
input {
	margin-left: 10px;
}
</style>