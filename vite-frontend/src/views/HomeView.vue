<template>
  <div class="container">
    <div class="row">
      <div v-for="wheel in wheels" :key="wheel.id" class="col-md-4">
      <div class="card mb-3">
        <div class="row g-0">
          <div class="col-md-4">
            <img :src="wheel.images[0].image" class="card-img-top" :alt="wheel.id">
          </div>
          <div class="col-md-8">
            <div class="card-body shadow rounded">
              <h5 class="card-title">{{ wheel.brand }}</h5>
              <p class="card-text">Largezza: {{ wheel.width }}</p>
              <p class="card-text">Prezzo: {{ wheel.price }}</p>
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
    }
  },
  created() {
    document.title = "Ruote";
    this.getWheels();
  }
}
</script>