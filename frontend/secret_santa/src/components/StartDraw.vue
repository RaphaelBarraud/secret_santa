<template>
    <div class="start_container">
        <!-- Part of the interface to add a new draw -->
        <div class="start_draw">
            <h1>Start Draw</h1>
            <form v-on:submit.prevent="postDraw">
                <div class="form-group">
                    <label for="name">Draw Name&nbsp;</label>
                    <textarea class="form-control" id="name" v-model="name"></textarea>
                </div>
                <br>
                <div class="form-group">
                    <button type="submit" class="bigButton">Start Draw</button>
                </div>
            </form>
        </div>
        <br>
        <h2 v-if="this.statusMessage !== ''">{{this.statusMessage}}</h2>
        <hr>
        <!-- Part of the interface to see the participant list -->
        <div v-if="this.statusMessage !== 'Draw successfully Created'" class="partipants_content">
            <h2>Participant list</h2>
            <ul class="partipants_list">
                <div v-for="participant in participants" :key="participant.id">
                    <!-- Dislay the Participant and the blacklist associated -->
                    <h3>{{ participant.first_name }} {{ participant.last_name }} / Blacklist: {{ participant.blacklist }}</h3>
                </div>
            </ul>
        </div>
        <!-- Part of the interface to display the draw result -->
        <div v-else class="result_content">
            <h2>Draw Result</h2>
            <ul class="result_list">
                <div v-for="result in this.draw_result" :key="result.id">
                    <h3>{{result}}</h3>
                </div>
            </ul>
        </div>
        
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                // participants
                participants: [''],
                name: '',
                draw_result: [''],
                result_name: '',
                statusMessage: ''
            }
        },
        methods: {
            // Method to get the list of all participants
            getParticipants () {
                axios.get(   
                    'http://127.0.0.1:8000/participants/'
                )
                .then((response) => {
                    // Set the returned data in the participants array
                    this.participants = response.data
                })
                .catch((err) => {
                    console.log('Error', err)
                })
            },
            // Method to create a new participant
            postDraw(){
                axios.post(   
                    'http://127.0.0.1:8000/draws/',{
                    name: this.name,
                    draw_result: []

                })
                .then((response) => {
                    // Set the draw_result into the variable
                    this.draw_result = response.data["draw_result"]
                    this.result_name = response.data["name"]
                    // Reset the name field value.
                    this.name = '';
                    this.statusMessage = "Draw successfully Created"
                })
                .catch((err) => {
                    console.log('Error', err)
                    this.statusMessage = err
                })
            }
        },created() {
            // Fetch participants on page load
            this.getParticipants();
        }
    }
</script>