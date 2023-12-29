<template>
  <nav class="navbar navbar-dark bg-primary">
    <div class="container">
      <router-link :to="{name: 'home'}" class="navbar-brand">
        Home
      </router-link>
      <router-link :to="{name: 'contacts'}">
        <button class="btn btn-outline-warning" type="submit">Contatti</button>
      </router-link>
    </div>
  </nav>
</template>

<script>
export default {
    name: "NavbarComponent",
};
</script>

<style>
.my-class{
    color: red;
}
</style>
