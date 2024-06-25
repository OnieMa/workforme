<script>
export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: "News",
	data() {
		return {
			opacity: 0.5
		}
	},

	// 只有在keep-alive的时候才会生效
	activated() {
		console.log('active')
		this.timer = setInterval(() => {
			this.opacity -= 0.01
			if (this.opacity <= 0) {
				this.opacity = 1
			}
		}, 16);
	},
	deactivated() {
		console.log('deactived ...')
		clearInterval(this.timer)
	}
}
</script>

<template>
	<div>
		<ul>
			<li :style="{opacity}"> Welcome</li>
			<li>News1
				<input type="text" placeholder="输入news">
			</li>
			<li>News2</li>
			<li>News3</li>
		</ul>
	</div>
</template>

<style scoped>

</style>