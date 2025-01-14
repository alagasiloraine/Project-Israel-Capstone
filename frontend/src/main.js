import { createApp } from 'vue'
import App from './App.vue'
import router from './routes'
import './style.css'  // Make sure this import exists

createApp(App).use(router).mount('#app')