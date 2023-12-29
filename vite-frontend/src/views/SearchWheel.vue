<template>
    <div class="container">
        <form @submit="handleSubmit" class="row gy-2 gx-3 align-items-center">
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
        <button type="submit" class="btn btn-primary pb-1">Cerca <i class="bi bi-search"></i></button>
      </div>
    </form>
    <div class="container mt-4">
          <div class="row">
            <div class="col-md-4 mb-4" v-for="wheel in wheels" :key="wheel.brand">
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
</template>

<script>
import { axios } from '../common/api.service';
import { endpoints } from '../common/endpoints';

export default {
  name: "SearchWheelView",
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
    async handleSubmit(event) {
        if (event) {
            event.preventDefault();
        }
        
        let endpoint = endpoints["filterWheel"]; 
        try {
            const response = await axios.post(endpoint, this.formData);
            this.wheels = response.data;
            console.log(response);
        } catch (error) {
            console.log(error);
            alert(error.response.statusText);
        }
    },
  },
  created() {
    document.title = "Ricerca";
    if (this.$route.query.data) {
        // If data is passed in the URL, set it to formData and perform a search
        this.formData = JSON.parse(decodeURIComponent(this.$route.query.data));
        this.handleSubmit();
    }
  }
  }
</script>