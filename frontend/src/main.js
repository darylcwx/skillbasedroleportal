import { createApp } from "vue";
import { createRouter, createWebHashHistory } from "vue-router";

import "./style.css";
import App from "./App.vue";
import Home from "./views/Home.vue";
import Skills from "./views/Skills.vue";

const routes = [
	{ path: "/", component: Home },
	{ path: "/skills", component: Skills },
];

const router = createRouter({
	history: createWebHashHistory(),
	routes: routes,
});

createApp(App).use(router).mount("#app");
