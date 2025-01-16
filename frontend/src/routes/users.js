import LandingPage from '../views/users/LandingPage.vue'
import Dashboard from '../views/users/Dashboard.vue'
import CropPrediction from '../views/users/CropPrediction.vue'
import DeviceControl from '../views/users/DeviceControl.vue'
import SoilMoisture from '../views/users/SoilMoisture.vue'
import WaterLevel from '../views/users/WaterLevel.vue'
import Humidity from '../views/users/Humidity.vue'
import Temperature from '../views/users/Temperature.vue'
import MotorControl from '../views/users/MotorControl.vue'
import SoilAnalysis from '../views/users/SoilAnalysis.vue'

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
    path: '/humidity',
    name: 'Humidity',
    component: Humidity
  },
  {
    path: '/temperature',
    name: 'Temperature',
    component: Temperature
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
]