<template>
	<div
		v-if="this.$store.state.user && this.$route.path !== '/'"
		class="fixed top-0 w-full z-10">
		<Navbar />
	</div>
	<div class="bg-background">
		<router-view></router-view>
	</div>
	<Footer />
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
export default {
	components: { Navbar, Footer },
};
</script>
