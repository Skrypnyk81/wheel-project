<template>
  <div class="container">
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
                  <p class="card-text">Battistrada: {{ wheel.tread }}%</p>
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
      wheels: []
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
  },
  computed: {
    diameters() {
      const diameters = this.wheels.map(wheel => wheel.diameter);
      return [...new Set(diameters)].sort((a, b) => a - b);
    },
  },
  created() {
    document.title = "Ruote";
    this.getWheels();
  }
}
</script>
