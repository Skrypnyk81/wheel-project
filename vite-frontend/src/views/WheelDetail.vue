<template>
    <div class="container">
        <div id="carouselExample" class="carousel slide">
        <div class="carousel-inner">
            <div v-for="(image, index) in wheel.images" :key="index" class="carousel-item" :class="{ 'active': index === 0 }">
                <img :src="image.image" class="d-block w-100" :alt="image.id">
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
    </div>
</template>

<script>
import { axios } from '../common/api.service';
import { endpoints } from '../common/endpoints';

    export default {
        name: "WheelDetail",
        props: {
            id: {
                type: Number,
                required: true
            }
        },
    data() {
        return {
            wheel: {}
        }
    },
    methods: {
        async getWheelDetail() {
            const endpoint = `${endpoints["detailWheel"]}${this.id}/`;
            try {
                const response = await axios.get(endpoint);
                this.wheel = response.data;
            } catch {
                console.log(error);
                alert(error.response.statusText);
            }
        }
    },
    created() {
        this.getWheelDetail()
    }
    }
    
</script>