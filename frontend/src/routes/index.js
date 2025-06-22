import { createRouter, createWebHistory } from 'vue-router'
import { authRoutes } from './auth.js'
import { userRoutes } from './users.js'
import NotFound from '../views/error/NotFound.vue'
import { useUserStore } from '../utils/user'

// Combine all routes
const routes = [
  ...authRoutes,
  ...userRoutes,
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

// Define which routes are public (accessible without auth)
const publicPaths = ['/', '/about', '/organicsection', '/login', '/register', '/verify-otp', '/forgotpassword']

// Global middleware (navigation guard)
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  userStore.loadUser() // Restore session from localStorage if needed

  const isPublic = publicPaths.includes(to.path)
  const isLoggedIn = !!userStore.user
  const isVerified = userStore.user?.verified === true

  if (!isPublic && (!isLoggedIn || !isVerified)) {
    // Not public and not allowed → redirect to login
    return next('/login')
  }

  // All good → proceed
  next()
})

export default router
