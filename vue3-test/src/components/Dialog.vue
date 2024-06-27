<script>
import {ref} from "vue";

export default {
	name: 'DialogVue',
	setup() {
		let isShow = ref(false)

		return {
			isShow
		}
	}
}
</script>

<template>
	<div>
		<button @click="isShow = true">点我弹窗</button>
<!--		<teleport to="body">  下面也可以去一个css选择器  注意是Html 里面的 id选择器-->
		<teleport to="#navigation">
			<div class="mask" v-if="isShow">
				<div class="log">
					<h3>我是一个弹窗</h3>
					<h4>一些内容</h4>
					<button @click="isShow = false">关闭弹窗</button>
				</div>
			</div>
		</teleport>

	</div>
</template>

<style scoped>
.log {
	width: 300px;
	height: 300px;
	background: blue;
	position: absolute;
	text-align: center;
	top: 50%;
	left: 50%;
}

.mask {
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	background-color: rgba(0, 0, 0, 0.5);
}
</style>