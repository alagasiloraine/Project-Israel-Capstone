import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/users/LandingPage.vue'

const routes = [
  {
    path: '/',
    name: 'landing',
    component: LandingPage
  }
  // Other routes can be added here
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

