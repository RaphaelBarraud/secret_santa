import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

// import axios
import axios from 'axios';

const app = createApp(App);
app.config.globalProperties.$http = axios;