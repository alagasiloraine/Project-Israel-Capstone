import LandingPage from '../views/users/LandingPage.vue'
import Dashboard from '../views/users/Dashboard.vue'
import CropPrediction from '../views/users/CropPrediction.vue'

export const userRoutes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/prediction',
    name: 'CropPrediction',
    component: CropPrediction
  }
]