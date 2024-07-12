<template>
	<div id="app">
		<div class="row">
			<div class="col-xs-offset-2 col-xs-8">
				<div class="page-header">
					<Banner></Banner>
				</div>
			</div>
		</div>

		<el-row>
			<el-button>哈哈</el-button>
		</el-row>

		<div class="row">
			<div class="col-xs-2 col-xs-offset-2">
				<div class="list-group">
					<router-link class="list-group-item" to="/About" active-class="active">about</router-link>
					<router-link class="list-group-item" to="/Home" active-class="active">home</router-link>
				</div>
			</div>
		</div>
		<div class="col-xs-6">
			<div class="panel-body">
				<router-view></router-view>
			</div>
		</div>
	</div>
</template>

<script>


import Banner from "@/components/Banner.vue";

export default {
	name: 'App',
	components: {Banner},
	mounted() {

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
}
</style>
