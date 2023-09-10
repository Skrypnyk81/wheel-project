<template>
    <h1>Ruota singola</h1>
    {{ wheel }}
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