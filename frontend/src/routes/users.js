import LandingPage from '../views/users/LandingPage.vue'
import Dashboard from '../views/users/Dashboard.vue'
import CropPrediction from '../views/users/CropPrediction.vue'
import DeviceControl from '../views/users/DeviceControl.vue'
import SoilMoisture from '../views/users/SoilMoisture.vue'
import WaterLevel from '../views/users/WaterLevel.vue'
import TemperatureHumidity from '../views/users/TemperatureHumidity.vue'
import MotorControl from '../views/users/MotorControl.vue'
import SoilAnalysis from '../views/users/SoilAnalysis.vue'
import UserProfile from '../views/users/UserProfile.vue'
import About from '../views/users/About.vue'
import OrganicSection from '../views/users/OrganicSection.vue'
import WeatherForecast from '../views/users/WeatherForecast.vue'
import Notifications from '../views/users/Notifications.vue'

export const userRoutes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/organicsection',
    name: 'OrganicSection',
    component: OrganicSection
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/prediction',
    name: 'CropPrediction',
    component: CropPrediction,
    meta: { requiresAuth: true }
  },
  {
    path: '/control',
    name: 'DeviceControl',
    component: DeviceControl,
    meta: { requiresAuth: true }
  },
  {
    path: '/soil-moisture',
    name: 'SoilMoisture',
    component: SoilMoisture,
    meta: { requiresAuth: true }
  },
  {
    path: '/water-level',
    name: 'WaterLevel',
    component: WaterLevel,
    meta: { requiresAuth: true }
  },
  {
    path: '/temperature-humidity',
    name: 'TemperatureHumidity',
    component: TemperatureHumidity,
    meta: { requiresAuth: true }
  },
  {
    path: '/motor-control',
    name: 'MotorControl',
    component: MotorControl,
    meta: { requiresAuth: true }
  },
  {
    path: '/soil',
    name: 'SoilAnalysis',
    component: SoilAnalysis,
    meta: { requiresAuth: true }
  },
  {
    path: '/profile',
    name: 'UserProfile',
    component: UserProfile,
    meta: { requiresAuth: true }
  },
  {
    path: '/weather',
    name: 'WeatherForecast',
    component: WeatherForecast,
    meta: { requiresAuth: true }
  },
  {
    path: '/notifications',
    name: 'Notifications',
    component: Notifications,
    meta: { requiresAuth: true }
  }
]
