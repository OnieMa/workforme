import vueRouter from 'vue-router'
import About from "@/pages/About.vue";
import Home from "@/pages/Home.vue";
import News from "@/pages/News.vue";
import Message from "@/pages/Message.vue";
import Detail from "@/pages/Detail.vue";

const Rt = new vueRouter({
	routes: [
		{
			name: 'guanyu',
			path: '/About',
			component: About
		},
		{
			name: 'jia',
			path: '/Home',
			component: Home,
			children: [
				{
					name: 'xinwen',
					path: 'News',
					component: News,
				},
				{
					name: 'xiaoxi',
					path: 'Message',
					component: Message,
					children: [
						{
							name: 'xiangqing',
							path: 'Detail',
							component: Detail,
							// props:{a:1,b:2} 对象的显示
							// props:true // 若为true 则会把所有收到的params的参数传递给对应的组件
							props({query: {id, msg}}) {
								return {id, msg}
							}// {query:{id,msg}} 结构赋值的写法
						}
					]
				},
			]
		}
	]
});

// 在这里加上路由守卫 每次路由切换之前 和 初始化的时候被调用
Rt.beforeEach((to, from, next) => {
	if (to.path === '/Home/News') {
		if (localStorage.getItem("school") === 'dahua') {
			next();
		}
		alert("无权限")
	}else {
		next()
	}



})


export default Rt