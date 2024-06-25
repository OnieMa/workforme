<template>
	<div class="container">
		<Count></Count>
		<hr>
		<Person></Person>
	</div>
</template>
<script>


import Count from "@/components/Count.vue";
import Person from "@/components/Person.vue";

export default {
	name: 'App',
	components: {Person, Count},
	data() {
		return {

		}
	},
	methods: {},
	mounted() {
		console.log("App",this);
	},
}
</script>

<style>
.container {
	display: flex;
	justify-content: space-around;
}
</style>