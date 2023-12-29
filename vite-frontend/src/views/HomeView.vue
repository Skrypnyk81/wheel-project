<template>
  <div class="container">
    <form @submit="navigateToSearch" class="row gy-2 gx-3 align-items-center">
      <div class="col-auto">
        <input type="text" v-model="formData.width" class="form-control" placeholder="Larghezza" aria-label="width" required>
      </div>
      <div class="col-auto">
        <input type="text" v-model="formData.ratio" class="form-control" placeholder="Altezza" aria-label="ratio" required>
      </div>
      <div class="col-auto">
        <input type="text" v-model="formData.diameter" class="form-control" placeholder="Diametro" aria-label="diameter" required>
      </div>
      <div class="col-auto">
        <select v-model="formData.season" id="season" class="form-control" required>
          <option disabled value="">Stagione</option>
          <option value="Estivi">Estivi</option>
          <option value="Invernali">Invernali</option>
          <option value="4 stagioni">4 stagioni</option>
        </select>
      </div>

      <div class="col-auto">
        <button class="btn btn-primary mb-1">Cerca <i class="bi bi-search"></i></button>
      </div>
    </form>
    <div class="container mt-4">
        <div v-for="diameter in diameters" :key="diameter">
          <h3 class="mb-3">Diametro: {{ diameter }}</h3>
          <div class="row">
            <div class="col-md-4 mb-4" v-for="wheel in filteredWheels(diameter)" :key="wheel.brand">
              <div class="card-body shadow rounded">
                <img :src="wheel.images[0]?.image" class="img-thumbnail" :alt="wheel.brand" />
                <div class="card-body ms-1">
                  <h5 class="card-title">{{ wheel.brand }}</h5>
                  <br>
                  <p class="card-text">Misura: {{ wheel.width }}/{{ wheel.ratio }}/{{ wheel.diameter }}</p>
                  <p class="card-text">Stagione: {{ wheel.season }}</p>
                  <p class="card-text">Prezzo: {{ wheel.price }} €</p>
                  <router-link :to="`/wheel/${wheel.id}`" class="btn btn-primary mb-1">Dettagli</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { axios } from '../common/api.service';
import { endpoints } from '../common/endpoints';

export default {
  name: "HomeView",
  data() {
    return {
      wheels: [],
      formData: {
      width: "",
      ratio: "",
      diameter: "",
      season: ""
      }
    }
  },
  methods: {
    async getWheels() {
      let endpoint = endpoints["listWheel"];
      try {
        const response = await axios.get(endpoint);
        this.wheels = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
        alert(error.response.statusText);
      }
    },
    filteredWheels(diameter) {
      return this.wheels.filter(wheel => wheel.diameter === diameter);
    },
    navigateToSearch(event) {
      event.preventDefault();
      this.$router.push(this.searchRoute);
    }
  },
  computed: {
    diameters() {
      const diameters = this.wheels.map(wheel => wheel.diameter);
      return [...new Set(diameters)].sort((a, b) => a - b);
    },
    searchRoute() {
        const jsonData = JSON.stringify(this.formData);
        console.log(jsonData)
        return `/search?data=${encodeURIComponent(jsonData)}`;
    }
  },
  created() {
    document.title = "Ruote";
    this.getWheels();
  }
}
</script>
