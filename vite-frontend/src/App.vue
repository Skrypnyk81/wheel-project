<template>
  <div>
    <NavbarComponent />
  </div>
  <div class="container">
    <p>Guida Sicuro, Risparmia con Stile: I Nostri Pneumatici Usati fanno la Differenza!</p>
    <br>
    <p>Spedizione è <span class="bolded">COMPRESA</span> nel prezzo, spediamo in tutta Italia, con il corriere BRT, <span class="bolded">PAGAMENTO ALLA CONSEGNA</span></p>
    <br>
  </div>
  <router-view />
  <footer class="text-black text-center py-3">
    <div class="container">
      <br>
        <p>© 2024 Iukhymets Denys II, via Enrico Fermi 4, Treviglio(BG) 24047. P.Iva 04356840167 Tutti i diritti riservati.</p>
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