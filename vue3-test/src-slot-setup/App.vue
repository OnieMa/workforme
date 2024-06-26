<template>
	<!--  <img alt="Vue logo" src="./assets/logo.png">-->
	<Hello msg="nihao" school="dahua" xixi='xixi' @sayHello="sayHello">
		<template v-slot:sss>
			<h4>Test slot</h4>
		</template>
	</Hello>
</template>

<script>
import Hello from "@/components/Hello.vue";

export default {
	name: 'App',
	components: {
		Hello
	},
	setup() {
		function sayHello() {
			alert("hello 粗发了")
		}

		return {sayHello}
	}

}
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}
</style>
