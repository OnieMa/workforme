const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
	transpileDependencies: true,
	lintOnSave: false,
	/*  pages:{
		index:{
		  entry:'src-消息订阅和事件总线/main.js'
		}
	  }*/

	// 第一种代理
	// devServer:{
	//   proxy:'http://localhost:9000'
	// }

	// 方式二
	devServer: {
		proxy: {
			'/api': {
				target: 'http://localhost:9000/',
				pathRewrite: {'^/api':''},
				ws: true,
				changeOrigin: true
			},
			'/fornt':{
				target:'http://localhost:9000/'
			}
		}
	}


})
