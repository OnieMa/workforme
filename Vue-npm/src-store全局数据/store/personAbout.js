export default {
	namespaced: true,
	actions: {
		addPersonWang(context, value) {
			if (value.name.indexOf("w") === 0) {
				context.commit('ADDPERSON',value)
			}
		},
	},
	mutations: {
		ADDPERSON(state, obj) {
			console.log('mutation ADDPERSON', obj)
			state.persons.unshift(obj)
		},
	},
	state: {
		persons: [{name: 'zhangsan', age: 20}]
	},
	getters: {
		firstListName(state) {
			return state.persons[0].name
		},
	}
}