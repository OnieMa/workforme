<script>

export default {
	name: "List",
	data() {
		return {
			users: []
		}
	},
	methods: {
		getMessage: function () {
			const infos = localStorage.getItem("users")
			this.users = JSON.parse(infos);
			console.log("@@@", this.users)
		},
		death(){
			this.$destroy()
		}
	},
	mounted() {
		// this.$bus.$on("sendUsers", (data) => {
		// 	this.users = data.items;
		// });
	},
	beforeDestroy() {
		localStorage.clear();
	}
}
</script>

<template>
	<div>
		<br>
		<button @click="getMessage">获取数据</button>
		<button @click="death">死掉</button>
		<br>
		<ul v-show="users.length">
			<li v-for="item in users">
				{{ item.login }}
				<img class="avatar" :src="item.avatar_url" alt="Dynamic Image">
			</li>
		</ul>
	</div>
</template>

<style scoped>
.avatar {
	width: 50px;
	height: 50px;
	margin-left: 50px;
}
</style>