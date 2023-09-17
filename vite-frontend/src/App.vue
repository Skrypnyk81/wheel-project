<template>
  <div>
    <NavbarComponent />
  </div>
  <div class="container">
    <p>Denys Gomme usate di qualità</p>
    <p>Spedizione in tutta Italia, con il corriere BRT, <span class="bolded">PAGAMENTO ALLA CONSEGNA</span></p>
  </div>
  <router-view />
  <footer class="text-black text-center py-3">
    <div class="container">
        <p>© 2023 La Mia Azienda. Tutti i diritti riservati.</p>
    </div>
</footer>
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

<style>
.bolded {
  color: red;
  text-align: center;
}
</style>