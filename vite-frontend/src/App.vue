<template>
  <header>
    <NavbarComponent />
  </header>

  <RouterView />
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import NavbarComponent from './components/NavbarComponent.vue';
export default {
    name: "app",
    components: { NavbarComponent }
}
</script>
