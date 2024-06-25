<script>
export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: "Detail",
	mounted() {
		console.log(this.$route);
	},
	props:['id','msg']
}
</script>

<template>
<div>
	<h3>这里是使用query展示</h3>
	<ul>
		<li>id: {{id}}</li>
		<li>msg: {{msg}} </li>
	</ul>
	<hr>
	<h3>这里是params展示</h3>
	<ul>
		<li>id: {{id}}</li>
		<li>msg: {{msg}} </li>
	</ul>
</div>
</template>

<style scoped>

</style>