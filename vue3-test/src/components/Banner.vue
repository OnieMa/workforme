<script>
export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: "Banner",
	methods: {
		back() {
			this.$router.back();
			// this.$router.forward();
		},
		go(){
			this.$router.go(-1);
		}
	},
}
</script>

<template>
	<div>
		<h2>Vue Router Demo</h2>
		<button @click="back">back</button>
		<button @click="go">go</button>
	</div>
</template>

<style scoped>

</style>