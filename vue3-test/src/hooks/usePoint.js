import {onBeforeUnmount, onMounted, reactive} from "vue";

export default function () {
	let position = reactive({
		x: 0,
		y: 0
	})

	function savePoint(event) {
		position.x = event.pageX
		position.y = event.pageY
		console.log(event.pageX, event.pageY)
	}

	onMounted(() => {
		window.addEventListener('click', savePoint);
	})

	onBeforeUnmount(() => {
		window.removeEventListener('click', savePoint)
	})

	return position;

}