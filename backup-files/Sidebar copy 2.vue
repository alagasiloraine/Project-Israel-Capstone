<template>
  <nav class="fixed top-2 mx-4 left-0 right-0 bg-gradient-to-r from-[#00A572] to-[#008F61] backdrop-blur-md bg-opacity-95 shadow-lg z-50 rounded-xl border border-transparent border-t-[3px] border-t-orange-400">
    <div class="max-w-[1920px] mx-auto px-4 lg:px-6 py-2.5">
      <!-- Top row with logo and profile -->
      <div class="flex items-center justify-between">
        <!-- Logo and PROJECT ISRAEL text -->
        <router-link to="/app/dashboard" class="flex items-center relative w-[180px]">
          <div class="bg-white rounded-full shadow-lg flex items-center justify-center overflow-hidden border-2 border-white/30 hover:border-white/50 transition-all duration-300" style="width: 2.8rem; height: 2.8rem;">
            <img
              src="/public/images/logo/logo-wot-text.png"
              alt="Project Israel"
              class="w-full h-full object-cover transform scale-[1.3] hover:scale-[1.8] transition-all duration-500 ease-out"
              style="transform-origin: center;"
            />
          </div>
          <div class="ml-2.5 flex flex-col">
            <span class="text-white font-bold text-sm leading-tight">PROJECT</span>
            <span class="text-orange-400 font-bold text-sm leading-tight">ISRAEL</span>
          </div>
        </router-link>

        <!-- User Profile Section with Connection Status and Notification Icons -->
        <div class="flex items-center group w-[180px] justify-end">
          <span class="text-xs text-white mr-2 hidden md:block opacity-90 group-hover:opacity-100 transition-opacity">{{ user?.email }}</span>

          <!-- WebSocket Connection Status -->
          <div class="relative mr-2">
            <button
              class="relative flex items-center justify-center h-7 w-7 rounded-full bg-white/10 hover:bg-white/20 transition-all duration-300"
              @mouseenter="showWebSocketTooltip = true"
              @mouseleave="showWebSocketTooltip = false"
            >
              <div class="flex items-center justify-center size-full rounded-full" :class="isWebSocketConnected ? 'bg-green-500/20' : ''">
                <Zap class="h-3.5 w-3.5 text-white" />
              </div>
            </button>

            <!-- WebSocket Tooltip -->
            <div
              v-show="showWebSocketTooltip"
              class="absolute right-0 top-full mt-2 w-52 bg-white/95 backdrop-blur-md rounded-lg shadow-lg overflow-hidden z-50 transition-all duration-200 border border-gray-100 transform origin-top-right"
              :class="showWebSocketTooltip ? 'scale-100 opacity-100' : 'scale-95 opacity-0'"
            >
              <!-- Tooltip content remains the same -->
            </div>
          </div>

          <!-- WiFi Connection Status -->
          <div class="relative mr-2">
            <button
              class="relative flex items-center justify-center h-7 w-7 rounded-full bg-white/10 hover:bg-white/20 transition-all duration-300"
              @mouseenter="showWifiTooltip = true"
              @mouseleave="showWifiTooltip = false"
            >
              <div class="flex items-center justify-center size-full rounded-full" :class="wifiStrength > 0 ? 'bg-green-500/20' : ''">
                <Wifi class="h-3.5 w-3.5 text-white" />
              </div>
            </button>

            <!-- WiFi Tooltip -->
            <div
              v-show="showWifiTooltip"
              class="absolute right-0 top-full mt-2 w-52 bg-white/95 backdrop-blur-md rounded-lg shadow-lg overflow-hidden z-50 transition-all duration-200 border border-gray-100 transform origin-top-right"
              :class="showWifiTooltip ? 'scale-100 opacity-100' : 'scale-95 opacity-0'"
            >
              <!-- Tooltip content remains the same -->
            </div>
          </div>

          <!-- Notification Icon -->
          <div class="relative">
            <router-link
              to="/app/notifications"
              class="relative flex items-center justify-center h-8 w-8 rounded-full bg-white/10 hover:bg-white/20 transition-all duration-300 text-white group/bell"
              :class="{ 'bg-white/30': $route.path === '/app/notifications' }"
              @mouseenter="showNotificationTooltip = true"
              @mouseleave="showNotificationTooltip = false"
            >
              <Bell class="h-4 w-4 transition-transform duration-200 group-hover/bell:scale-110" />
              <div
                v-if="unreadNotificationCount > 0"
                class="notification-badge-static absolute -top-1 -right-1 min-w-[16px] h-4 flex items-center justify-center rounded-full bg-red-500 text-white shadow-md border border-white/30"
              >
                <span class="text-[9px] font-semibold leading-none px-0.5">
                  {{ unreadNotificationCount > 99 ? '99+' : unreadNotificationCount }}
                </span>
              </div>
            </router-link>

            <!-- Notification Tooltip -->
            <div
              v-show="showNotificationTooltip"
              class="absolute top-full left-1/2 transform -translate-x-1/2 mt-1 px-2 py-0.5 bg-green-100 text-green-900 font-medium text-[10px] rounded-md whitespace-nowrap z-50 transition-all duration-200 shadow-sm"
              :class="showNotificationTooltip ? 'opacity-100' : 'opacity-0'"
            >
              Notifications
              <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-green-100"></div>
            </div>
          </div>

          <!-- Profile Section -->
          <div
            class="relative ml-4 cursor-pointer group/profile"
            @click="goToProfile"
            @mouseenter="showProfileTooltip = true"
            @mouseleave="showProfileTooltip = false"
          >
            <!-- Profile Image -->
            <div class="relative">
              <div
                class="w-8 h-8 rounded-full overflow-hidden transition-all duration-300 ease-out group-hover/profile:scale-[1.02]"
                :class="[
                  isOnProfilePage
                    ? 'ring-1 ring-green-400/60 ring-offset-1 ring-offset-white/20'
                    : 'ring-1 ring-white/15 hover:ring-white/25',
                  user?.avatar?.icon ? 'bg-white flex items-center justify-center' : ''
                ]"
              >
                <span v-if="user?.avatar?.icon" class="text-lg leading-none select-none">{{ user.avatar.icon }}</span>
                <img v-else-if="user?.profilePicture"
                     :src="user.profilePicture"
                     class="w-full h-full object-cover transition-all duration-300"
                     :class="isOnProfilePage ? 'brightness-[1.02] saturate-[1.05]' : ''"
                     alt="Profile"/>
                <img v-else
                     src="/public/images/profile.jpg"
                     class="w-full h-full object-cover transition-all duration-300"
                     alt="Profile"/>
              </div>
              <div
                v-if="isOnProfilePage"
                class="absolute -bottom-px -right-px w-2 h-2 bg-green-400 rounded-full border border-white/40 shadow-sm"
              ></div>
            </div>

            <!-- Profile Tooltip -->
            <div
              v-show="showProfileTooltip"
              class="absolute top-full left-1/2 transform -translate-x-1/2 mt-1 px-2 py-0.5 bg-green-100 text-green-800 text-[10px] font-medium rounded-md whitespace-nowrap z-50 transition-all duration-200 shadow-sm"
              :class="showProfileTooltip ? 'opacity-100' : 'opacity-0'"
            >
              Profile
              <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-green-100"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Navigation items centered -->
      <div class="flex items-center justify-center mt-1.5">
        <div class="flex items-center space-x-1 sm:space-x-2 md:space-x-3 flex-wrap gap-y-1">
          <router-link
            v-for="item in menuItems"
            :key="item.name"
            :to="item.href"
            :class="[
              'flex items-center px-2.5 sm:px-3 py-1.5 text-xs sm:text-sm font-medium rounded-lg transition-all duration-300 hover:scale-105',
              isCurrentRoute(item.href)
                ? 'bg-white text-[#00A572] shadow-md'
                : 'text-white hover:bg-white/10 hover:shadow-sm'
            ]"
          >
            <component
              :is="item.icon"
              class="h-3.5 w-3.5 mr-1.5 transition-transform duration-300 group-hover:rotate-12"
            />
            <span class="whitespace-nowrap">{{ item.name }}</span>
          </router-link>

          <div class="relative group">
            <button
              @click="toggleSensorDropdown"
              :class="[
                'flex items-center px-2.5 sm:px-3 py-1.5 text-xs sm:text-sm font-medium rounded-lg transition-all duration-300 hover:scale-105',
                isSensorDropdownOpen || isInSensorRoutes
                  ? 'bg-white text-[#00A572] shadow-md'
                  : 'text-white hover:bg-white/10 hover:shadow-sm'
              ]"
            >
              <Database class="h-3.5 w-3.5 mr-1.5" />
              <span class="whitespace-nowrap">Sensor Data</span>
              <ChevronDown
                :class="['ml-1.5 h-3 w-3 transition-transform duration-300',
                  isSensorDropdownOpen ? 'transform rotate-180' : ''
                ]"
              />
            </button>

            <div
              v-show="isSensorDropdownOpen"
              class="absolute top-full left-0 mt-1 w-52 bg-white/95 backdrop-blur-md rounded-lg shadow-lg py-1.5 z-50 border border-white/20 transform transition-all duration-300"
            >
              <router-link
                v-for="sensor in sensorTypes"
                :key="sensor.name"
                :to="sensor.href"
                :class="[
                  'flex items-center px-3 py-1.5 text-sm transition-all duration-200 hover:scale-[1.02]',
                  isCurrentRoute(sensor.href)
                    ? 'bg-[#E8F5E9] text-[#00A572] font-medium'
                    : 'text-gray-700 hover:bg-[#E8F5E9] hover:text-[#00A572]'
                ]"
              >
                <component :is="sensor.icon" class="h-3.5 w-3.5 mr-2" />
                {{ sensor.name }}
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <!-- Spacer for content below navbar -->
  <div class="h-20"></div>

  <!-- Toast notification -->
  <Transition name="toast">
    <div
      v-if="showToast"
      :class="[
        'fixed bottom-4 right-4 rounded-lg shadow-lg border p-4 flex items-center gap-3 z-[10001] max-w-md',
        toastStyles.bg,
        toastStyles.border
      ]"
    >
      <div :class="[toastStyles.iconBg, 'p-2 rounded-full']">
        <component :is="toastStyles.icon" class="w-5 h-5" :class="toastStyles.iconColor" />
      </div>
      <div>
        <p class="text-sm font-medium text-gray-800">{{ toastMessage }}</p>
      </div>
      <button
        @click="showToast = false"
        class="ml-auto text-gray-400 hover:text-gray-600"
      >
        <X class="w-4 h-4" />
      </button>
    </div>
  </Transition>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  LayoutDashboard,
  Brain,
  Cpu,
  Database,
  Sprout,
  ChevronDown,
  Droplets,
  Thermometer,
  Gauge,
  Power,
  Cloud,
  Bell,
  Wifi,
  Zap,
  X,
  CheckCircle,
  Info,
  AlertTriangle,
  XCircle,
  Beaker
} from 'lucide-vue-next'
import { auth } from '../../api/firebase.js'
import { onAuthStateChanged } from 'firebase/auth'

const route = useRoute()
const router = useRouter()

// User state
const user = ref(null)

// Navigation items - updated to use /app prefix
const menuItems = [
  { name: 'Overview', href: '/app/dashboard', icon: LayoutDashboard },
  { name: 'Crop Prediction', href: '/app/prediction', icon: Brain },
  { name: 'Weather', href: '/app/weather', icon: Cloud },
  { name: 'Device Control', href: '/app/control', icon: Cpu },
  { name: 'Soil Analysis', href: '/app/soil', icon: Sprout }
]

const sensorTypes = [
  { name: 'NPK Data', href: '/app/npkData', icon: Sprout },
  { name: 'Soil pH', href: '/app/soilph', icon: Beaker },
  { name: 'Soil Moisture', href: '/app/soil-moisture', icon: Droplets },
  { name: 'Temp/Humid', href: '/app/temperature-humidity', icon: Thermometer },
  { name: 'Water Level', href: '/app/water-level', icon: Gauge },
  { name: 'Motor Control', href: '/app/motor-control', icon: Power }
]

// UI state
const isSensorDropdownOpen = ref(false)
const showWifiTooltip = ref(false)
const showWebSocketTooltip = ref(false)
const showNotificationTooltip = ref(false)
const showProfileTooltip = ref(false)

// Functional state
const isWebSocketConnected = ref(false)
const wifiStrength = ref(100)
const wifiNetwork = ref('Unknown')
const ipAddress = ref('')
const notifications = ref([])
const unreadNotificationCount = computed(() => notifications.value.filter(n => n && !n.read).length)

// Toast system
const showToast = ref(false)
const toastMessage = ref('')
const toastSeverity = ref('info')
const toastQueue = ref([])
const isToastActive = ref(false)

const toastStyles = computed(() => {
  switch (toastSeverity.value) {
    case 'success': return { icon: CheckCircle, iconColor: 'text-green-600', iconBg: 'bg-green-100', bg: 'bg-white', border: 'border-green-200' }
    case 'info': return { icon: Info, iconColor: 'text-blue-600', iconBg: 'bg-blue-100', bg: 'bg-white', border: 'border-blue-200' }
    case 'warning': return { icon: AlertTriangle, iconColor: 'text-yellow-600', iconBg: 'bg-yellow-100', bg: 'bg-white', border: 'border-yellow-200' }
    case 'critical': return { icon: XCircle, iconColor: 'text-red-600', iconBg: 'bg-red-100', bg: 'bg-white', border: 'border-red-200' }
    default: return { icon: Info, iconColor: 'text-gray-600', iconBg: 'bg-gray-100', bg: 'bg-white', border: 'border-gray-300' }
  }
})

// Route helpers
const isCurrentRoute = (path) => route.path === path
const isInSensorRoutes = computed(() => sensorTypes.some(sensor => route.path === sensor.href))
const isOnProfilePage = computed(() => route.path === '/app/profile')

// Navigation methods
const toggleSensorDropdown = () => isSensorDropdownOpen.value = !isSensorDropdownOpen.value
const goToProfile = () => router.push('/app/profile')
const closeDropdown = (e) => {
  if (!e.target.closest('.relative.group')) {
    isSensorDropdownOpen.value = false
  }
}

// Toast system methods
const processToastQueue = () => {
  if (toastQueue.value.length === 0 || isToastActive.value) return;
  
  isToastActive.value = true
  const nextToast = toastQueue.value.shift()
  toastMessage.value = nextToast.message
  toastSeverity.value = nextToast.severity
  showToast.value = true

  setTimeout(() => {
    showToast.value = false
    setTimeout(() => {
      isToastActive.value = false
      processToastQueue()
    }, 300)
  }, 5000)
}

const showToastMessage = (message, severity = 'info') => {
  toastQueue.value.push({ message, severity })
  if (!isToastActive.value) processToastQueue()
}

// Initialize
onMounted(() => {
  onAuthStateChanged(auth, (currentUser) => {
    user.value = currentUser
  })

  document.addEventListener('click', closeDropdown)
  
  // Initialize network info
  if ('connection' in navigator) {
    const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection
    const updateWifiInfo = () => {
      wifiStrength.value = conn.downlinkMax ? Math.min(conn.downlinkMax * 10, 100) : 70
      wifiNetwork.value = conn.effectiveType || 'WiFi'
    }
    updateWifiInfo()
    if (conn.addEventListener) conn.addEventListener('change', updateWifiInfo)
  }

  // Get IP address
  fetch('https://api.ipify.org?format=json')
    .then(res => res.json())
    .then(ipData => ipAddress.value = ipData.ip)
    .catch(() => ipAddress.value = 'Unknown')
})

onBeforeUnmount(() => {
  document.removeEventListener('click', closeDropdown)
})

// Close dropdowns on route change
watch(() => route.path, () => {
  isSensorDropdownOpen.value = false
  showWifiTooltip.value = false
  showWebSocketTooltip.value = false
  showNotificationTooltip.value = false
  showProfileTooltip.value = false
})
</script>

<style scoped>
/* Your existing styles remain the same */
.router-link-active {
  position: relative;
  transform: translateZ(0);
}

.router-link-active::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: 1px;
  background: linear-gradient(to right, white, transparent);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.router-link-active:hover::after {
  transform: scaleX(1);
}

.notification-badge-static {
  min-width: 16px !important;
  height: 16px !important;
  background-color: #ef4444 !important;
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
  animation: none !important;
  transition: none !important;
  transform: none !important;
}

@media (max-width: 1024px) {
  nav {
    top: 3px;
    margin-left: 1rem;
    margin-right: 1rem;
  }
}

@media (max-width: 768px) {
  nav {
    top: 2px;
    margin-left: 0.5rem;
    margin-right: 0.5rem;
  }
}

@media (max-width: 640px) {
  nav {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
  }
}

.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  opacity: 0;
  transform: translateX(100%);
}

.toast-leave-to {
  opacity: 0;
  transform: translateX(100%);
}
</style>