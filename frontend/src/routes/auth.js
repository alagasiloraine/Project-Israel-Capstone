import Login from '../views/auth/Login.vue'
import Register from '../views/auth/Register.vue'
import Verification from '../views/auth/Verification.vue'
import ForgotPassword from '../views/auth/ForgotPassword.vue'

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
  },
  {
    path: '/login/verification',
    name: 'Verification',
    component: Verification
  },
  {
    path: '/forgotpassword',
    name: 'ForgotPassword',
    component: ForgotPassword
  }
]

