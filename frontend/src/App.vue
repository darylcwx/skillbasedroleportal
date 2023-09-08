<script >
//import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/Navbar.vue'
export default { components: { Navbar } }
</script>

<template>
  <Navbar />
  <div className="container mx-auto px-4">
    <router-view></router-view>

  </div>
</template>
