<template>
    <div class="container mt-4">
        <div v-if="wheel">
            <div class="col-md">
            <div class="card-body shadow rounded">
              <h5 class="card-title">{{ wheel.brand }}</h5>
              <p class="card-text">Misura: {{ wheel.width }}/{{ wheel.ratio }}/{{ wheel.diameter }} {{ wheel.load }}{{ wheel.speed }} {{ wheel.season }}</p>
              <p class="card-text">Battistrada: {{ wheel.tread }}%</p>
              <p class="card-text">Marca: {{ wheel.brand }} {{ wheel.quantity }} {{ wheel.dot }}</p>
              <p class="card-text">Prezzo: {{ wheel.price }} €</p>
              <router-link :to="`/order/${wheel.id}`" class="btn btn-primary">Ordina</router-link>
            </div>
          </div>
            <!-- Elenco di immagini in fila -->
            <Carousel id="WheelDetail" :items-to-show="1" :wrap-around="false" v-model="currentSlide">
                <slide v-for="(image, index) in wheel.images" :key="index" class="me-2 mb-2">
                    <div class="carousel__item">
                        <img  class="zoon-image"
                        :src="image.image"
                        :alt="index">
                    </div>
                </slide>
            </carousel>
            <Carousel
                id="thumbnails"
                :items-to-show="3"
                :wrap-around="true"
                v-model="currentSlide"
                ref="carousel"
            >
                <Slide v-for="(image, index) in wheel.images" :key="index" class="me-2 mb-2">
                    <div class="carousel__item"  @click="slideTo(index)">
                        <img :src="image.image" :alt="index" class="img-ridimensionata">
                    </div>
                </Slide>
            </Carousel>
        </div>
        <div v-else>
            <h1 class="text-danger text-center">Le ruote non ci sono!</h1>
        </div>
    </div>
</template>

<script>
import { axios } from '../common/api.service';
import { endpoints } from '../common/endpoints';
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide } from 'vue3-carousel';

export default {
        name: "WheelDetail",
        components: {
            Carousel,
            Slide,
        },
        props: {
            id: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                wheel: {},
                currentSlide: 0,
            }
        },
        methods: {
            setPageTitle(title) {
                document.title = title;
            },
            async getWheelDetail() {
                const endpoint = `${endpoints["detailWheel"]}${this.id}/`;
                try {
                    const response = await axios.get(endpoint);
                    this.wheel = response.data;
                    this.setPageTitle(response.data.slug);
                } catch (error) {
                    console.log(error);
                    this.wheel = null;
                }
            },
            slideTo(val) {
                this.currentSlide = val
                },
        },
        created() {
            this.getWheelDetail()
        }
}  
</script>
<style>
.carousel__item {
  min-height: 200px;
  width: 100%;
  background-color: white;
  color: var(--vc-clr-white);
  font-size: 20px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.img-ridimensionata {
  max-width: 100%; /* L'immagine può essere larga al massimo il 100% del suo contenitore */
  max-height: 300px; /* L'immagine può essere alta al massimo 500px */
  display: block; /* Facoltativo: per centrare l'immagine se è più piccola del suo contenitore */
  margin: 0 auto; /* Facoltativo: per centrare l'immagine se è più piccola del suo contenitore */
}
.zoon-image {
    max-width: 100%;
    max-height: 500px;
    display: block; /* Facoltativo: per centrare l'immagine se è più piccola del suo contenitore */
    margin: 0 auto; /* Facoltativo: per centrare l'immagine se è più piccola del suo contenitore */

}
</style>