import vueRouter from 'vue-router'
import About from "@/pages/About.vue";
import Home from "@/pages/Home.vue";
import News from "@/pages/News.vue";
import Message from "@/pages/Message.vue";
import Detail from "@/pages/Detail.vue";
import NProgress from 'nprogress'


const router = new vueRouter({
	mode: "history",
	routes: [
		{
			name: 'guanyu',
			path: '/About',
			component: About,
			meta: {
				isAuth: true,
				title:'关于'
			},
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
					meta: {
						isAuth: true,
						title:'新闻'
					},
					// 独享的路由守卫
					// beforeEnter: ()=>{}
					beforeEnter(to,from,next){
						if (to.meta.isAuth) {
							if (localStorage.getItem("school") === 'dahua') {
								next();
							} else {
								alert("无权限")
							}
						} else {
							next()
						}
						console.log('beforeEnter',this)
					}
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

// 配置 NProgress，禁用自动 trickle 并设置 trickleSpeed
NProgress.configure({ trickle: false })

let timer

router.beforeEach((to, from, next) => {
	NProgress.start()
	// 每次路由开始时启动定时器，模拟匀速加载
	timer = setInterval(() => {
		NProgress.inc()
	}, 100)
	next()
})

router.afterEach(() => {
	// 路由结束时完成进度条并清除定时器
	clearInterval(timer)
	NProgress.done()
})


// 在这里加上路由守卫 每次路由切换之前 和 初始化的时候被调用
// router.beforeEach((to, from, next) => {
// 	if (to.path === '/Home/News') {
// 		if (localStorage.getItem("school") === 'dahua') {
// 			next();
// 		}
// 		alert("无权限")
// 	}else {
// 		next()
// 	}
// })


// 使用meta元信息进行权限的校验
// router.beforeEach((to, from, next) => {
// 	if (to.meta.isAuth) {
// 		if (localStorage.getItem("school") === 'dahua') {
// 			next();
// 		} else {
// 			alert("无权限")
// 		}
// 	} else {
// 		next()
// 	}
// })

// 后置的守卫 一般是用于做title的展示
// router.afterEach((to, from) => {
// 	document.title = to.meta.title || 'vueRouter'
// 	console.log('to',to)
// 	console.log('from',from)
// })

export default router