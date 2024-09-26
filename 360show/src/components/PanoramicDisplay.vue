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
	width: 100vw;
	height: 100vh;
}
</style>