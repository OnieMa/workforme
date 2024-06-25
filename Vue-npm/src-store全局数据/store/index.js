import Vue from 'vue'
import Vuex from "vuex";
import countAbout from "@/store/countAbout";
import personAbout from "@/store/personAbout";

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		countAbout,
		personAbout
	}
})