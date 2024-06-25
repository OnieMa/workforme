<template>
	<div>
		<span>Get from Github</span>
		<br>
		<input type="text" v-model="searchKey" @keyup.enter="getUserInfo">
		<button @click="getUserInfo">获取信息</button>
		<br>
		<List/>

	</div>
</template>
<script>

import List from "@/components/List.vue";
import axios from "axios";

export default {
	name: 'App',
	components: {List},
	data() {
		return {
			searchKey: ''
		}
	},
	methods: {
		getUserInfo() {
			console.log(this)
			// axios.get(`http://api.github.com/search/users?q=${this.searchKey}`).then(
			// 	response => {
			// 		console.log('ok', response.data)
			// 		this.$bus.$emit("sendUsers", response.data)
			// 		localStorage.setItem('users', JSON.stringify(response.data.items))
			// 	},
			// 	error => {
			// 		console.log(error.message)
			// 	}
			// )


			this.$http.get(`http://api.github.com/search/users?q=${this.searchKey}`).then(
				response => {
					console.log('ok', response.data)
					this.$bus.$emit("sendUsers", response.data)
					localStorage.setItem('users', JSON.stringify(response.data.items))
				},
				error => {
					console.log(error.message)
				}
			)
		},


	},
}
</script>

<style>

</style>