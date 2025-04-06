import { createApp } from 'vue'
import App from './App.vue'
import router from './routes'
import './style.css'  // Make sure this import exists
import "toastr/build/toastr.min.css";
import { createVuetify } from 'vuetify';
import 'vuetify/styles'; 


// createApp(App).use(router).mount('#app')
const vuetify = createVuetify();
const app = createApp(App);
app.use(router);
app.use(vuetify);
app.mount('#app');