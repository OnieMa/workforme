<script>
import {Viewer} from '@photo-sphere-viewer/core';


export default {
	name: "PanoramicDisplay",
	data() {
		return {
			pic: "/jinhua.jpg",
		};
	},
	mounted() {
		const viewer = new Viewer({
			container: document.querySelector('#viewer'),
			panorama: this.pic
		});
	}
}
</script>

<template>
	<div id="viewer"></div>
</template>

<style scoped>
#viewer {
	width: 100vw;  /* 设置容器宽度为视口宽度 */
	height: 100vh; /* 设置容器高度为视口高度 */
}
</style>