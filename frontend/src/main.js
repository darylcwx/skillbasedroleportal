import { createApp } from "vue";
import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";
import { createRouter, createWebHashHistory } from "vue-router";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.js";
import "./style.css";

import App from "./App.vue";
import Login from "./views/Login.vue";
import Home from "./views/Home.vue";
import Listings from "./views/Listings.vue";

const store = createStore({
	state() {
		return {
			user: null,
			reloaded: false,
		};
	},
	mutations: {
		setUser(state, user) {
			state.user = user;
		},
	},
	plugins: [createPersistedState({ storage: window.sessionStorage })],
});

const routes = [
	{ name: "Login", path: "/", component: Login },
	{ name: "Home", path: "/home", component: Home },
	{ name: "Listings", path: "/listings", component: Listings },
];

const router = createRouter({
	history: createWebHashHistory(),
	routes: routes,
});

createApp(App).use(router).use(store).mount("#app");
