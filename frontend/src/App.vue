<template>
  <div v-if="this.$store.state.user && this.$route.path !== '/'">
    <Navbar />
  </div>
  <div class="bg-neutral-900">
    <router-view></router-view>
  </div>
</template>

<script >
import Navbar from './components/Navbar.vue'
export default {
  components: { Navbar },
}
</script>
