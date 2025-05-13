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
    component: Dashboard
  },
  {
    path: '/prediction',
    name: 'CropPrediction',
    component: CropPrediction
  },
  {
    path: '/control',
    name: 'DeviceControl',
    component: DeviceControl
  },
  {
    path: '/soil-moisture',
    name: 'SoilMoisture',
    component: SoilMoisture
  },
  {
    path: '/water-level',
    name: 'WaterLevel',
    component: WaterLevel
  },
  {
    path: '/temperature-humidity',
    name: 'temperature-humidity',
    component: TemperatureHumidity
  },
  {
    path: '/motor-control',
    name: 'MotorControl',
    component: MotorControl
  },
  {
    path: '/soil',
    name: 'SoilAnalysis',
    component: SoilAnalysis
  },
  {
    path: '/profile',
    name: 'UserProfile',
    component: UserProfile
  },
  {
    path: '/weather',
    name: 'WeatherForecast',
    component: WeatherForecast
  }
]