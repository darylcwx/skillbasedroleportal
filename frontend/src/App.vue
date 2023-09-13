<script >
//import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/Navbar.vue'
export default { components: { Navbar } }
</script>

<template>
  <!-- <Navbar /> -->
  <div class="bg-neutral-800">
    <div class="container mx-auto px-4">
      <router-view></router-view>
    </div>
  </div>
</template>
