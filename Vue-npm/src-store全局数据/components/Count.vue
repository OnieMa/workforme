<template>
	<div>
		<h3>当前的bigSum 为 {{ bigsum }}</h3>
		<h3>当前的就和为 {{ sum }}</h3>
		<h3>I'm in {{ addr }} {{ comp }}</h3>


		<select v-model.number="n">
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
		</select>
		<button @click="add(n)">+</button>
		<button @click="JIAN(n)">-</button>
		<button @click="ADDJS(n)">奇数加一</button>
		<button @click="addWait(n)">一会儿再加</button>

		<hr>
		<h3>当前人员得总人数是{{ persons.length }}</h3>

	</div>

</template>
<script>
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";

export default {
	name: "Count",
	data() {
		return {
			n: 1
		}
	},
	computed: {
		...mapState('countAbout', ['sum', 'addr', 'comp']),
		...mapState('personAbout', ['persons']),
		...mapGetters('countAbout', ['bigsum'])
	},

	methods: {
		...mapActions('countAbout', ['add','addWait']),
		...mapMutations('countAbout', ['JIAN','ADDJS']),


	},
}
</script>


<style scoped>
button {
	margin: 5px;
}
</style>