<template>
   <!-- Header of the interface with 3 menu buttons -->
  <h1 id="menuItems">WELCOME TO THE SECRET SANTA</h1>
  <div class="menu-filters">
    <button @click="menuPressed('participants')" type="button" class="block">
      Participants page
    </button>
    <button @click="menuPressed('draw')" type="button" class="block">
      Start Draw page
    </button>
    <span class="tab"></span>
    <button @click="menuPressed('history')" type="button" class="block">
      Draw History page
    </button>
  </div>
  <!-- Display the component based on the compoDisplay value -->
  <div v-if="this.compoDisplay == 'participants'" id="app"><Participants /></div>
  <div v-else-if="this.compoDisplay == 'draw'" id="app"><StartDraw /></div>
  <div v-else-if="this.compoDisplay == 'history'" id="app"><DrawHistory /></div>
</template>

<script>
import Participants from './components/ParticipantList.vue'
import StartDraw from './components/StartDraw.vue'
import DrawHistory from './components/DrawHistory.vue'

export default {
  name: 'App',
  components: {
    Participants,
    StartDraw,
    DrawHistory
  },
  methods: {
      // Method called when menu buttons are pressed
      menuPressed(compo){
        this.compoDisplay= compo
        this.$forceUpdate();
      }
  },created() {
    this.compoDisplay= 'participants'
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.block {
  width: 15%;
  border: 3px solid black;
  background-color: #f32121;
  padding: 8px 16px;
  margin-right:50px;
  font-size: 20px;
  cursor: pointer;
  text-align: center;
}
.bigButton {
  width: 10%;
  border: 2px solid black;
  background-color: #c4b7b7;
  padding: 4px 8px;
  margin-right:5px;
  font-size: 17px;
  cursor: pointer;
  text-align: center;
}
.mediumButton {
  width: 7%;
  border: 2px solid black;
  background-color: #c4b7b7;
  padding: 4px 8px;
  margin-right:5px;
  font-size: 15px;
  cursor: pointer;
  text-align: center;
}

</style>
