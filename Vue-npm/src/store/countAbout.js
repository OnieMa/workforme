export default {
	namespaced: true,
	state: {
		sum: 0, addr: 'hangzhou', comp: 'dahua',
	},
	actions: {
		operationData: function (context, value) {
			context.commit(value.med.toUpperCase(), value.numb)
		}, add(context, value) {
			context.commit('ADD', value)
		}, addWait(context, value) {
			setTimeout(() => {
				context.commit('ADD', value)
			}, 500)
		}
	},
	mutations: {
		ADD(state, value) {
			state.sum += value
		}, JIAN(state, value) {
			state.sum -= value
		}, ADDJS(state, value) {
			if (state.sum % 2) {
				state.sum += value;
			}
		},

	},
	getters: {
		bigsum(state) {
			return state.sum * 10;
		}
	}
}