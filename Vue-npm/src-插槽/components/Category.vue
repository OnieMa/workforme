<script>
export default {
	name: "Category",
	props: ['listData', 'title'],
	data() {
		return {
			games: ['王者','爱消除']
		}
	},
}
</script>

<template>
	<div class="category">
		<h3>{{ title }}</h3>
		<ul>
			<li v-for="(item,index) in listData" :key="index">{{ item }}</li>
		</ul>

		<hr>
		<hr>
		<!--		这里是一个默认插槽-->
<!--		<slot name="head1">xxxxxxxxxxxx</slot>-->
<!--		<slot name="foot">xxxxxxxxxxxx</slot>-->
<!--		<slot name="allGame">xxxxxxxxxxxx</slot>-->
		<slot :games="games" :x="1"></slot>
	</div>
</template>

<style scoped>
.category {
	border: 1px gray solid;
}

</style>