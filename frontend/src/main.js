import { createApp } from "vue";
import { createRouter, createWebHashHistory } from "vue-router";

import "bootstrap/dist/css/bootstrap.css";
import "./style.css";

import App from "./App.vue";
import Login from "./views/Login.vue";
import Home from "./views/Home.vue";

const routes = [
	{ name: "Login", path: "/", component: Login },
	{ name: "Home", path: "/:role/home", component: Home, props: true },
];

const router = createRouter({
	history: createWebHashHistory(),
	routes: routes,
});

createApp(App).use(router).mount("#app");
