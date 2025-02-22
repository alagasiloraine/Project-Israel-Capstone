<template>
  <!-- Main navigation container with floating effect -->
  <nav class="fixed top-4 mx-6 left-0 right-0 bg-[#00A572] shadow-lg z-50 rounded-2xl border-t-4 border-t-orange-300">
    <!-- Circular logo container - Keeping original size -->
    <div class="absolute left-1/2 -top-4 transform -translate-x-1/2">
      <div class="bg-white rounded-full shadow-lg flex items-center justify-center overflow-hidden" style="width: 4rem; height: 4rem;">
        <img 
          src="/public/images/logo/logo-wot-text.png"
          alt="Project Israel"
          class="w-full h-full object-cover transform scale-[1.5] hover:scale-[2.2] transition-transform duration-300"
          style="transform-origin: center;"
        />
      </div>
    </div>

    <div class="max-w-[1920px] mx-auto px-10 pt-10 pb-3.5">
      <div class="flex items-center justify-between mt-5.3">
        <!-- Left Navigation -->
        <div class="flex items-center space-x-4 flex-wrap gap-y-2.6 pt-3.5">
          <router-link 
            v-for="item in menuItems" 
            :key="item.name"
            :to="item.href"
            :class="[
              'flex items-center px-4 py-2.5 text-sm font-medium rounded-lg transition-colors hover:bg-opacity-90',
              isCurrentRoute(item.href) 
                ? 'bg-[#008F61] text-white shadow-sm' 
                : 'text-white/90 hover:bg-[#008F61] hover:text-white'
            ]"
          >
            <component 
              :is="item.icon" 
              class="h-5 w-5 mr-2.5"
            />
            {{ item.name }}
          </router-link>

          <!-- Sensor Data Dropdown -->
          <div class="relative">
            <button 
              @click="toggleSensorDropdown"
              :class="[
                'flex items-center px-4 py-2.5 text-sm font-medium rounded-lg transition-colors hover:bg-opacity-90', 
                isSensorDropdownOpen || isInSensorRoutes 
                  ? 'bg-[#008F61] text-white shadow-sm' 
                  : 'text-white/90 hover:bg-[#008F61] hover:text-white'
              ]"
            >
              <Database class="h-5 w-5 mr-2.5" />
              Sensor Data
              <ChevronDown 
                :class="['ml-2.5 h-4 w-4 transition-transform duration-200',
                  isSensorDropdownOpen ? 'transform rotate-180' : ''
                ]"
              />
            </button>

            <!-- Dropdown Menu -->
            <div 
              v-show="isSensorDropdownOpen"
              class="absolute top-full left-0 mt-2 w-48 bg-white rounded-lg shadow-lg py-2.5 z-50" 
            >
              <router-link
                v-for="sensor in sensorTypes"
                :key="sensor.name"
                :to="sensor.href"
                :class="[
                  'flex items-center px-4 py-2.5 text-sm transition-colors hover:bg-opacity-90',
                  isCurrentRoute(sensor.href)
                    ? 'bg-[#E8F5E9] text-[#00A572] font-medium'
                    : 'text-gray-700 hover:bg-[#E8F5E9] hover:text-[#00A572]'
                ]"
              >
                <component :is="sensor.icon" class="h-4 w-4 mr-3" />
                {{ sensor.name }}
              </router-link>
            </div>
          </div>
        </div>

        <!-- Right Section - User Profile -->
        <div class="flex items-center pt-3.5">
          <span class="text-sm text-white mr-3 hidden sm:block">{{ user?.email }}</span>
          <img 
            :src="user?.profilePicture || '/public/images/default-avatar.png'"
            class="w-10 h-10 rounded-full border-2 border-white/20 hover:border-white/40 transition-colors duration-200"
            alt="Profile"
          />
        </div>
      </div>
    </div>
  </nav>

  <!-- Adjusted spacer height -->
  <div class="h-26"></div>
</template>

<script setup>
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

// Route and state management
const route = useRoute()
const user = ref(null)
const isSensorDropdownOpen = ref(false)

// Navigation menu items
const menuItems = [
  { name: 'Overview', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Crop Prediction', href: '/prediction', icon: Brain },
  { name: 'Soil Analysis', href: '/soil', icon: Sprout },
  { name: 'Weather', href: '/weather', icon: Cloud }
]

// Sensor types for dropdown
const sensorTypes = [
  { name: 'Soil Moisture', href: '/soil-moisture', icon: Droplets },
  { name: 'Water Level', href: '/water-level', icon: Gauge },
  { name: 'Humidity', href: '/humidity', icon: Droplets },
  { name: 'Temperature', href: '/temperature', icon: Thermometer },
  { name: 'Motor Control', href: '/motor-control', icon: Power },
]

// Methods
const toggleSensorDropdown = () => {
  isSensorDropdownOpen.value = !isSensorDropdownOpen.value
}

const isCurrentRoute = (path) => {
  return route.path === path
}

const isInSensorRoutes = computed(() => {
  return sensorTypes.some(sensor => route.path === sensor.href)
})

// Click outside handler
const closeDropdown = (e) => {
  if (!e.target.closest('.relative')) {
    isSensorDropdownOpen.value = false
  }
}

// Lifecycle hooks
onMounted(() => {
  // Load user data
  const storedUser = localStorage.getItem("user") || sessionStorage.getItem("user")
  if (storedUser) {
    user.value = JSON.parse(storedUser)
  }
  
  // Add click outside listener
  document.addEventListener('click', closeDropdown)
  
  // Add resize listener for responsive handling
  window.addEventListener('resize', handleResize)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', closeDropdown)
  window.removeEventListener('resize', handleResize)
})

// Watch route changes
watch(() => route.path, () => {
  isSensorDropdownOpen.value = false
})

// Responsive handling
const handleResize = () => {
  if (window.innerWidth < 640) { // sm breakpoint
    isSensorDropdownOpen.value = false
  }
}

// Initialize responsive state
handleResize()
</script>

<style scoped>
/* Active link styling */
.router-link-active {
  position: relative;
}

.router-link-active::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -2px;
  height: 2px;
  background-color: white;
  transform: scaleX(0);
  transition: transform 0.2s ease;
}

.router-link-active:hover::after {
  transform: scaleX(1);
}

/* Responsive design */
@media (max-width: 1024px) {
  nav {
    top: 3px;
    margin-left: 1rem;
    margin-right: 1rem;
  }
  
  .nav-content {
    padding: 1rem;
  }
}

@media (max-width: 768px) {
  nav {
    top: 2px;
    margin-left: 0.75rem;
    margin-right: 0.75rem;
  }
  
  .nav-links {
    gap: 0.5rem;
  }
}

@media (max-width: 640px) {
  .nav-content {
    flex-direction: column;
    align-items: stretch;
  }
  
  .profile-section {
    margin-top: 1rem;
    justify-content: center;
  }
}

/* Transitions */
nav {
  transition: all 0.3s ease;
}

.dropdown-enter-active,
.dropdown-leave-active {
  transition: opacity 0.2s, transform 0.2s;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Cross-browser compatibility */
@supports (-webkit-backdrop-filter: none) or (backdrop-filter: none) {
  nav {
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
  }
}

/* Ensure smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Fix for Safari */
@supports (-webkit-touch-callout: none) {
  nav {
    /* Specific fixes for Safari if needed */
    transform: translateZ(0);
  }
}

/* Fix for Firefox */
@-moz-document url-prefix() {
  nav {
    /* Specific fixes for Firefox if needed */
    will-change: transform;
  }
}
</style>