import Login from '../views/auth/Login.vue'
import Register from '../views/auth/Register.vue'

export const authRoutes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  }
]