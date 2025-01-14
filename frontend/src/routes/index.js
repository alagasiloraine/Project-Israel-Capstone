import { createRouter, createWebHistory } from 'vue-router'
import { authRoutes } from './auth.js'
import { userRoutes } from './users.js'

const routes = [
  ...authRoutes,
  ...userRoutes,
//   ...adminRoutes
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router