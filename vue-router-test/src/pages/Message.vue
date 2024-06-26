<script>
export default {
	// eslint-disable-next-line vue/multi-word-component-names
	name: "Message",
	data() {
		return {
			lists: [
				{id: '001', msg: 'msg1'},
				{id: '002', msg: 'msg2'},
				{id: '003', msg: 'msg3'}
			]
		}
	},
	methods: {
		pushShow(m) {
			this.$router.push({
				name: 'xiangqing',
				query: {
					id: m.id,
					msg: m.msg
				}
			})
		},
		replaceShow(m){
			this.$router.replace({
				name: 'xiangqing',
				query: {
					id: m.id,
					msg: m.msg
				}
			})
		}
	},

}
</script>

<template>
	<div>
		<ul>
			<li v-for="m in lists" :key="m.id">
				<!-- replace 会以替换掉当前的栈-->
				<router-link replace
					:to="{
					name:'xiangqing',
					// path:'/Home/Message/Detail',
					// params:{
					// 使用params的时候必须使用 path
					query:{
						id:m.id,
						msg:m.msg
					}
				}">{{ m.id }}
				</router-link>
<!--				<router-link :to="`/Home/Message/Detail/${m.id}/${m.msg}`">{{m.msg}}</router-link>-->
				<button @click="pushShow(m)">push查看</button>
				<button @click="replaceShow(m)">replace查看</button>

			</li>
		</ul>
		<hr/>
		<router-view></router-view>
	</div>

</template>

<style scoped>

</style>