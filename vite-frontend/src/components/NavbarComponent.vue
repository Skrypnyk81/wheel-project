<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container">
    <router-link :to="{name: 'home'}" class="navbar-brand">
      Gomme usate
    </router-link>
    
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
            <button type="button" class="btn btn-info">Contatti</button>
        </li>
       
      </ul>
    </div>
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
