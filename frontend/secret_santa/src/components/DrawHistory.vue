<template>
    <div class="drawHistory_container">
        <!-- Part of the interface to display last 5 draws -->
        <div class="drawHistory">
            <h1>Display last 5 draws</h1>
            <!-- Part of the interface to see the draw list -->
            <div v-for="draw in draws" :key="draw.id">
                <!-- Dislay the Name and time of the draw -->
                <hr>
                <h2>DrawName: {{ draw.name }}</h2>
                <h3>created on the {{ draw.creation_time }}</h3>
                <!-- Loop through the draw resul to display it -->
                <div v-for="result in draw.draw_result" :key="result.id">
                    <h4>{{result}}</h4>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                // draws
                draws: ['']
            }
        },
        methods: {
            // Method to get the list of all draws
            getDraws () {
                axios.get(   
                    'http://127.0.0.1:8000/draws/'
                )
                .then((response) => {
                    // Set the last 5 draws in the draws array(should be made on the backend)
                    this.draws = response.data.slice(0, 5)
                })
                .catch((err) => {
                    console.log('Error', err)
                })
            }
        },created() {
            // Fetch draws on page load
            this.getDraws();
        }
    }
</script>