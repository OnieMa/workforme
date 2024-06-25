<script>
export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: "Home",
	destroyed() {
		console.log('Home destroy');
	},
}
</script>

<template>
	<div>
		<h3>Home</h3>
		<div>
			<ul class="nav nav-tabs">
				<li>
					<router-link class="list-group-item" active-class="active" to="/Home/News">News</router-link>
				</li>
				<li>
					<router-link class="list-group-item" active-class="active" to="/Home/Message">Message</router-link>
				</li>
			</ul>
		</div>


		<div class="panel-body">
			<!--不写的话 全部缓存-->
<!--			<keep-alive include="Message">-->
			<keep-alive>
				<router-view></router-view>
			</keep-alive>
		</div>

	</div>

</template>

<style scoped>

</style>