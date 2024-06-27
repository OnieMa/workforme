<template>
	<!--  <img alt="Vue logo" src="./assets/logo.png">-->
	<!--	<Hello>
			<template v-slot:sss>
				<h4>Test slot</h4>
			</template>
		</Hello>-->

	<!--	<WatchTest></WatchTest>-->
	<!--	<LifeTest v-if="isShow"></LifeTest>-->
	<!--	<button @click="isShow = !isShow">展示/消失</button>-->
	<!--	<MouseClick v-if="isShow"></MouseClick>-->


	<!--	<hr>-->
	<!--	<RefTest></RefTest>-->

	<hr>
	<!--	<ShallowVue></ShallowVue>-->
	<!--	<CustomRef></CustomRef>-->

	<Suspense>
		<template v-slot:fallback>
			<h3>loading for component ....</h3>
		</template>
		<template v-slot:default>
			<SonVue></SonVue>
		</template>
	</Suspense>
	<h3>hello</h3>
</template>

<script>
import {defineAsyncComponent, provide, reactive, ref} from "vue";
// import SonVue from "@/components/SonVue.vue";

//下面是异步的引入
const SonVue = defineAsyncComponent(() => import('@/components/SonVue.vue'))
export default {
	name: 'App',
	components: {
		SonVue,
		// CustomRef
		// ShallowVue,
		// RefTest,
		// MouseClick
		// LifeTest,
		// WatchTest,
		// Hello
	},
	setup() {
		let isShow = ref(true)

		let car = reactive({
			name: '大众',
			price: '15w'
		})
		provide('car', car)

		return {
			isShow, car
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
	background: gray;
}
</style>
