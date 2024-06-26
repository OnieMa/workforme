<script>
import usePoint from "@/hooks/usePoint";

export default {
	setup() {
		let position = usePoint();

		return {
			position
		}
	}
}
</script>

<template>
	<h3>Chile Mouse </h3>
	<h3>当前鼠标点击的坐标是 {{ position.x }} {{ position.y }}</h3>
</template>

<style scoped>

</style>