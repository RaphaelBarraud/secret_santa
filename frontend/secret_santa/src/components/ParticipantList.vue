<template>
    <div class="partipants_container">
        <!-- Part of the interface to add a new participant -->
        <div class="add_participant">
            <h1>Add Participant</h1>
            <form v-on:submit.prevent="postParticipant">
                <div class="form-group">
                    <label for="first_name">First Name&nbsp;</label>
                    <textarea class="form-control" id="first_name" v-model="first_name"></textarea>
                    <br>
                    <label for="last_name">Last Name&nbsp;</label>
                    <textarea class="form-control" id="last_name" v-model="last_name"></textarea>
                </div>
                <br>
                <div class="form-group">
                    <button type="submit" class="bigButton">Add Participant</button>
                </div>
            </form>
        </div>
        <br>
        <hr>
        <!-- Part of the interface to see the participant list -->
        <div class="partipants_content">
            <h1>Participant list</h1>
            <ul class="partipants_list">
                <div v-for="participant in participants" :key="participant.id">
                    <!-- Dislay the Participant and the blacklist associated -->
                    <h2>{{ participant.first_name }} {{ participant.last_name }}</h2>
                    <h3>Blacklisted: {{ participant.blacklist }} </h3>

                    <button @click="deleteParticipant(participant.id)" class="mediumButton">Delete</button>
                    <br><br>
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
                first_name: '',
                last_name: ''
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
            postParticipant(){
                axios.post(   
                    'http://127.0.0.1:8000/participants/',{
                    first_name: this.first_name,
                    last_name: this.last_name
                })
                .then((response) => {
                    // Append the returned data to the participants array
                    this.participants.unshift(response.data);
                    // Reset the first_name and last_name field values.
                    this.first_name = '';
                    this.last_name = '';
                })
                .catch((err) => {
                    console.log('Error', err)
                })
            },
            // Method to delete a participant
            deleteParticipant(participantID){
                // Confirm if one wants to delete the participant
                let confirmation = confirm("Do you want to delete this participant?");
                if(confirmation){
                    axios.delete(`http://127.0.0.1:8000/participants/${participantID}/`)
                    .then((response) => {
                        console.log('Resource deleted successfully:', response.data);
                        // Refresh the participants
                        this.getParticipants();
                    })
                    .catch((err) => {
                        console.log('Error', err)
                    })
                }
            }
        },created() {
            // Fetch participants on page load
            this.getParticipants();
        }
    }
</script>