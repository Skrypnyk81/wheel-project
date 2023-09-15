<template>
  <div>
    <NavbarComponent />
  </div>

  <router-view />
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue';
export default {
    name: "app",
    components: { 
      NavbarComponent
    }
}
</script>
