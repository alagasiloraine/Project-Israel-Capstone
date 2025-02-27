<template>
  <nav class="fixed top-2 mx-4 left-0 right-0 bg-gradient-to-r from-[#00A572] to-[#008F61] backdrop-blur-md bg-opacity-95 shadow-lg z-50 rounded-xl border border-transparent border-t-[3px] border-t-orange-400">
    <!-- Logo positioning remains unchanged -->
    <div class="absolute left-1/2 -top-2.5 transform -translate-x-1/2">
      <div class="bg-white rounded-full shadow-lg flex items-center justify-center overflow-hidden border-2 border-white/30 hover:border-white/50 transition-all duration-300" style="width: 3.5rem; height: 3.5rem;">
        <img 
          src="/public/images/logo/logo-wot-text.png"
          alt="Project Israel"
          class="w-full h-full object-cover transform scale-[1.3] hover:scale-[1.8] transition-all duration-500 ease-out"
          style="transform-origin: center;"
        />
      </div>
    </div>

    <div class="max-w-[1920px] mx-auto px-6 lg:px-12 pt-6 pb-3">
      <div class="flex items-center justify-between mt-6">
        <!-- Left Navigation remains unchanged -->
        <div class="flex items-center space-x-3 md:space-x-4 flex-wrap gap-y-2 pt-1">
          <router-link 
            v-for="item in menuItems" 
            :key="item.name"
            :to="item.href"
            :class="[
              'flex items-center px-4 py-2 text-sm font-medium rounded-lg transition-all duration-300 hover:scale-105',
              isCurrentRoute(item.href) 
                ? 'bg-white text-[#00A572] shadow-md' 
                : 'text-white hover:bg-white/10 hover:shadow-sm'
            ]"
          >
            <component 
              :is="item.icon" 
              class="h-4 w-4 mr-2 transition-transform duration-300 group-hover:rotate-12"
            />
            {{ item.name }}
          </router-link>

          <div class="relative group">
            <button 
              @click="toggleSensorDropdown"
              :class="[
                'flex items-center px-4 py-2 text-sm font-medium rounded-lg transition-all duration-300 hover:scale-105', 
                isSensorDropdownOpen || isInSensorRoutes 
                  ? 'bg-white text-[#00A572] shadow-md' 
                  : 'text-white hover:bg-white/10 hover:shadow-sm'
              ]"
            >
              <Database class="h-4 w-4 mr-2" />
              Sensor Data
              <ChevronDown 
                :class="['ml-2 h-3 w-3 transition-transform duration-300',
                  isSensorDropdownOpen ? 'transform rotate-180' : ''
                ]"
              />
            </button>

            <div 
              v-show="isSensorDropdownOpen"
              class="absolute top-full left-0 mt-2 w-52 bg-white/95 backdrop-blur-md rounded-lg shadow-lg py-1.5 z-50 border border-white/20 transform transition-all duration-300" 
            >
              <router-link
                v-for="sensor in sensorTypes"
                :key="sensor.name"
                :to="sensor.href"
                :class="[
                  'flex items-center px-3 py-2 text-sm transition-all duration-200 hover:scale-[1.02]',
                  isCurrentRoute(sensor.href)
                    ? 'bg-[#E8F5E9] text-[#00A572] font-medium'
                    : 'text-gray-700 hover:bg-[#E8F5E9] hover:text-[#00A572]'
                ]"
              >
                <component :is="sensor.icon" class="h-3.5 w-3.5 mr-2.5" />
                {{ sensor.name }}
              </router-link>
            </div>
          </div>
        </div>

        <!-- Adjusted User Profile Section -->
        <div class="flex items-center pt-1 group">
          <span class="text-sm text-white mr-3 hidden sm:block opacity-90 group-hover:opacity-100 transition-opacity">{{ user?.email }}</span>
          <div class="relative">
            <div class="absolute inset-0 bg-gradient-to-r from-[#00A572] to-[#008F61] rounded-full blur-md opacity-0 group-hover:opacity-50 transition-opacity"></div>
            <img 
              :src="user?.profilePicture || '/public/images/profile.jpg'"
              class="w-10 h-10 rounded-full border-2 border-white/30 hover:border-white/60 transition-all duration-300 relative z-10 object-cover"
              alt="Profile"
            />
          </div>
        </div>
      </div>
    </div>
  </nav>

  <!-- Spacer remains unchanged -->
  <div class="h-28"></div>
</template>

<script setup>
// Script section remains unchanged
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue'
import { useRoute } from 'vue-router'
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
  Cloud
} from 'lucide-vue-next'

const route = useRoute()
const user = ref(null)
const isSensorDropdownOpen = ref(false)

const menuItems = [
  { name: 'Overview', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Crop Prediction', href: '/prediction', icon: Brain },
  { name: 'Soil Analysis', href: '/soil', icon: Sprout },
  { name: 'Weather', href: '/weather', icon: Cloud }
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
/* Styles remain unchanged */
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
  
  .nav-content {
    padding: 0.75rem;
  }
}

@media (max-width: 768px) {
  nav {
    top: 2px;
    margin-left: 0.5rem;
    margin-right: 0.5rem;
  }
  
  .nav-links {
    gap: 0.5rem;
  }
}

@media (max-width: 640px) {
  nav {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
  }

  .nav-content {
    flex-direction: column;
    align-items: stretch;
    padding: 0.5rem;
  }
  
  .profile-section {
    margin-top: 0.5rem;
    justify-content: center;
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

.nav-item, 
.dropdown-trigger {
  user-select: none;
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