<template>
	<!--  <img alt="Vue logo" src="./assets/logo.png">-->
	<!--	<Hello>
			<template v-slot:sss>
				<h4>Test slot</h4>
			</template>
		</Hello>-->

	<!--	<WatchTest></WatchTest>-->
	<!--	<LifeTest v-if="isShow"></LifeTest>-->
	<button @click="isShow = !isShow">展示/消失</button>
	<MouseClick v-if="isShow"></MouseClick>


	<hr>
	<RefTest></RefTest>

</template>

<script>
import {ref} from "vue";
import MouseClick from "@/components/MouseClick.vue";
import RefTest from "@/components/RefTest.vue";

export default {
	name: 'App',
	components: {
		RefTest,
		MouseClick
		// LifeTest,
		// WatchTest,
		// Hello
	},
	setup() {
		let isShow = ref(true)

		return {
			isShow,
		}
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
