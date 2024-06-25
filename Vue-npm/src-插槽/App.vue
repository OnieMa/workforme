<template>
	<div class="container">
		<Category title="美食" :listData="foods">
			<h4 slot="foot">test</h4>
			<h4 slot="head1">test222</h4>
			<!-- 在vue2.6之后 具名插槽的新语法替代了旧的 slot 特性，使得代码更加清晰和易读。新的具名插槽语法使用 v-slot 指令，而不是直接在元素上使用 slot 属性。-->
		</Category>


		<Category title="游戏" :listData="games">
			<template v-slot:allGame>
				<a href="http://www.baidu.com">具名插槽的实现</a>
				<a href="http://www.baidu.com">具名插槽的实现</a>
			</template>
		</Category>


		<Category title="电源">
			<!--<template scope="items">-->
			<template slot-scope="items">
				<ol>
					<li v-for="item in items.games">{{ item }}</li>
				</ol>
				{{items.x}}
			</template>
		</Category>
	</div>
</template>
<script>

import Category from "@/components/Category.vue";

export default {
	name: 'App',
	components: {Category},
	data() {
		return {
			foods: ['火锅', '奶茶', '方便面'],
			games: ['王者', 'k', 'c'],
			// films: ['李焕英', '潜伏',],

		}
	},
	methods: {},
}
</script>

<style>
.container {
	display: flex;
	justify-content: space-around;
}
</style>