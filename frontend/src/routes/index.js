import { createRouter, createWebHistory } from 'vue-router'
import { authRoutes } from './auth.js'
import { userRoutes } from './users.js'
import NotFound from '../views/error/NotFound.vue' // Add this import

const routes = [
  ...authRoutes,
  ...userRoutes,
  // Add this catch-all 404 route at the end
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router