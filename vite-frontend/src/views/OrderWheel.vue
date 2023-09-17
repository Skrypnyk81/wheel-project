<template>
  <div class="container mt-5">
    <form @submit.prevent="submitForm">

      <!-- First Name Input -->
      <div class="mb-3">
        <label for="first_name" class="form-label">Cognome</label>
        <input v-model="formData.first_name" type="text" class="form-control" id="first_name" required>
      </div>

      <!-- Second Name Input -->
      <div class="mb-3">
        <label for="second_name" class="form-label">Nome</label>
        <input v-model="formData.second_name" type="text" class="form-control" id="second_name" required>
      </div>

      <!-- Phone Input -->
      <div class="mb-3">
        <label for="phone" class="form-label">Telefono</label>
        <input v-model="formData.phone" type="tel" class="form-control" id="phone" required>
      </div>

      <!-- Street Input -->
      <div class="mb-3">
        <label for="street" class="form-label">Via</label>
        <input v-model="formData.street" type="text" class="form-control" id="street" required>
      </div>

      <!-- City Input -->
      <div class="mb-3">
        <label for="city" class="form-label">Città</label>
        <input v-model="formData.city" type="text" class="form-control" id="city" required>
      </div>

      <!-- Postal Code Input -->
      <div class="mb-3">
        <label for="postal_code" class="form-label">Codice postale</label>
        <input v-model="formData.postal_code" type="text" class="form-control" id="postal_code" required>
      </div>

      <!-- State Input -->
      <div class="mb-3">
        <label for="state" class="form-label">Provincia</label>
        <input v-model="formData.state" type="text" class="form-control" id="state" required>
      </div>

      <!-- Email Input -->
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input v-model="formData.email" type="text" class="form-control" id="email" required>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">Invia ordine</button>

    </form>
  </div>
</template>

<script>
import { axios } from '../common/api.service';
import { endpoints } from '../common/endpoints';

export default {
  name: "OrderView",
  props: {
    id: {
      type: Number, 
      default: null
    }
  },
  data() {
    return {
        formData: {
        wheel: this.id,
        first_name: '',
        second_name: '',
        phone: '',
        street: '',
        city: '',
        state: '',
        postal_code: '',
        email: ''
      }
    }
  },
  methods: {
    async submitForm() {
      let endpoint = endpoints["createOrder"];
      try {
        const response = await axios.post(endpoint, this.formData);
        // Show a popup message
         window.alert("Il tuo ordine è stato inviato!");
    
        // Redirect to the home URL
        this.$router.push('/');
      } catch (error) {
        console.log(error);
        alert(error.response.statusText);
      }
    }
  },
  created() {
    document.title = "Ordine";
  }
}
</script>