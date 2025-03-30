<template>
  <nav class="fixed top-2 mx-4 left-0 right-0 bg-gradient-to-r from-[#00A572] to-[#008F61] backdrop-blur-md bg-opacity-95 shadow-lg z-50 rounded-xl border border-transparent border-t-[3px] border-t-orange-400">
    <div class="max-w-[1920px] mx-auto px-4 lg:px-6 py-2.5">
      <!-- Top row with logo and profile -->
      <div class="flex items-center justify-between">
        <!-- Logo and PROJECT ISRAEL text - positioned with padding-top -->
        <div class="flex items-center relative w-[180px]" style="padding-top: 4px;">
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
        </div>

        <!-- User Profile Section with Notification Icon - balanced spacing -->
        <div class="flex items-center group justify-end">
          <span class="text-xs text-white mr-2 hidden md:block opacity-90 group-hover:opacity-100 transition-opacity">{{ user?.email }}</span>
          
          <!-- Notification Icon - with balanced spacing -->
          <div class="relative group/notification mr-4">
            <button class="relative flex items-center justify-center h-8 w-8 rounded-full bg-white/10 hover:bg-white/20 transition-all duration-300 text-white">
              <Bell class="h-4 w-4" />
              <!-- Notification Badge -->
              <span class="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-orange-500 text-[10px] font-bold text-white">3</span>
            </button>
            
            <!-- Notification Tooltip -->
            <div class="absolute right-0 top-full mt-1 w-64 origin-top-right scale-95 opacity-0 pointer-events-none group-hover/notification:scale-100 group-hover/notification:opacity-100 group-hover/notification:pointer-events-auto transition-all duration-200 z-50">
              <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                <div class="p-2 bg-[#00A572] text-white font-medium text-sm flex items-center justify-between">
                  <span>Notifications</span>
                  <span class="text-xs px-1.5 py-0.5 bg-white/20 rounded-full">3 new</span>
                </div>
                <div class="max-h-[250px] overflow-y-auto">
                  <div class="p-2 hover:bg-gray-50 border-b border-gray-100">
                    <div class="flex items-start gap-2">
                      <div class="h-2 w-2 rounded-full bg-orange-500 mt-1.5 flex-shrink-0"></div>
                      <div>
                        <p class="text-xs font-medium text-gray-800">Soil moisture level is low</p>
                        <p class="text-xs text-gray-500">10 minutes ago</p>
                      </div>
                    </div>
                  </div>
                  <div class="p-2 hover:bg-gray-50 border-b border-gray-100">
                    <div class="flex items-start gap-2">
                      <div class="h-2 w-2 rounded-full bg-orange-500 mt-1.5 flex-shrink-0"></div>
                      <div>
                        <p class="text-xs font-medium text-gray-800">Weather alert: Rain expected</p>
                        <p class="text-xs text-gray-500">1 hour ago</p>
                      </div>
                    </div>
                  </div>
                  <div class="p-2 hover:bg-gray-50">
                    <div class="flex items-start gap-2">
                      <div class="h-2 w-2 rounded-full bg-orange-500 mt-1.5 flex-shrink-0"></div>
                      <div>
                        <p class="text-xs font-medium text-gray-800">Motor control activated</p>
                        <p class="text-xs text-gray-500">3 hours ago</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="p-2 bg-gray-50 text-center">
                  <button class="text-xs text-[#00A572] font-medium hover:underline">View all notifications</button>
                </div>
              </div>
            </div>
          </div>
          
          <div class="relative">
            <div class="absolute inset-0 bg-gradient-to-r from-[#00A572] to-[#008F61] rounded-full blur-md opacity-0 group-hover:opacity-50 transition-opacity"></div>
            <img 
              :src="user?.profilePicture || '/public/images/profile.jpg'"
              class="w-8 h-8 rounded-full border-2 border-white/30 hover:border-white/60 transition-all duration-300 relative z-10 object-cover"
              alt="Profile"
            />
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
  Bell
} from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const user = ref(null)
const isSensorDropdownOpen = ref(false)

const menuItems = [
  { name: 'Overview', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Crop Prediction', href: '/prediction', icon: Brain },
  { name: 'Weather', href: '/weather', icon: Cloud },
  { name: 'Device Control', href: '/control', icon: Cpu },
  { name: 'Soil Analysis', href: '/soil', icon: Sprout }
]

const sensorTypes = [
  { name: 'Soil Moisture', href: '/soil-moisture', icon: Droplets },
  { name: 'Water Level', href: '/water-level', icon: Gauge },
  { name: 'Humidity', href: '/humidity', icon: Droplets },
  { name: 'Temperature', href: '/temperature', icon: Thermometer },
  { name: 'Motor Control', href: '/motor-control', icon: Power },
]

const toggleSensorDropdown = () => {
  isSensorDropdownOpen.value = !isSensorDropdownOpen.value
}

const isCurrentRoute = (path) => {
  return route.path === path
}

const isInSensorRoutes = computed(() => {
  return sensorTypes.some(sensor => route.path === sensor.href)
})

const closeDropdown = (e) => {
  if (!e.target.closest('.relative')) {
    isSensorDropdownOpen.value = false
  }
}

let resizeTimeout
const handleResize = () => {
  clearTimeout(resizeTimeout)
  resizeTimeout = setTimeout(() => {
    if (window.innerWidth < 640) {
      isSensorDropdownOpen.value = false
    }
  }, 150)
}

onMounted(() => {
  const storedUser = localStorage.getItem("user") || sessionStorage.getItem("user")
  if (storedUser) {
    try {
      user.value = JSON.parse(storedUser)
    } catch (e) {
      console.error('Error parsing user data:', e)
    }
  }
  
  document.addEventListener('click', closeDropdown)
  window.addEventListener('resize', handleResize)
  
  handleResize()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', closeDropdown)
  window.removeEventListener('resize', handleResize)
  clearTimeout(resizeTimeout)
})

watch(() => route.path, () => {
  isSensorDropdownOpen.value = false
})
</script>

<style scoped>
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

nav {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

@supports (-webkit-backdrop-filter: none) or (backdrop-filter: none) {
  nav {
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
  }
}

html {
  scroll-behavior: smooth;
}

@supports (-webkit-touch-callout: none) {
  nav {
    transform: translateZ(0);
    -webkit-font-smoothing: antialiased;
  }
}

@-moz-document url-prefix() {
  nav {
    will-change: transform;
    backface-visibility: hidden;
  }
}

* {
  -webkit-tap-highlight-color: transparent;
}

:focus-visible {
  outline: 2px solid white;
  outline-offset: 2px;
}

@media print {
  nav {
    display: none;
  }
}
</style>