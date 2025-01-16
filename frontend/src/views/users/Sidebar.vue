<template>
  <div class="hidden md:flex md:flex-shrink-0 relative z-50">
    <div :class="[
      'flex flex-col bg-[#002B1D] transition-all duration-300 ease-in-out rounded-tr-3xl rounded-br-3xl relative',
      isCollapsed ? 'w-20' : 'w-[280px]'
    ]">
      <!-- Logo Section -->
      <div class="flex flex-col items-center px-6 py-4 border-b border-[#1a4d4f]">
        <div :class="['flex items-center justify-center transition-all duration-300', isCollapsed ? 'w-16 h-16' : 'w-24 h-24']">
          <img 
            src="/images/project-israel-logo-removebg-preview.png" 
            alt="Project Israel" 
            class="w-full h-full object-contain"
          />
        </div>
        <span class="text-white text-2xl font-semibold mt-4" :class="[isCollapsed ? 'hidden' : 'block']">
          Project Israel
        </span>
      </div>

      <!-- Toggle Button - Outside Sidebar -->
      <button 
        @click="toggleSidebar"
        class="absolute -right-12 top-12 px-4 py-3 rounded-lg bg-[#002B1D] hover:bg-[#1a4d4f] text-gray-300 hover:text-[#8FE3CF] transition-colors shadow-lg z-50"
      >
        <Menu v-if="isCollapsed" class="h-5 w-5" />
        <PanelLeftClose v-else class="h-5 w-5" />
      </button>

      <!-- Navigation -->
      <nav class="flex-1 px-6 py-8">
        <div v-show="!isCollapsed" class="mb-8">
          <h3 class="text-sm font-semibold text-gray-400 uppercase tracking-wider">
            MENU
          </h3>
        </div>
        
        <div class="space-y-6">
          <router-link 
            v-for="item in menuItems" 
            :key="item.name"
            :to="item.href"
            :class="[
              'flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-colors duration-150',
              isCollapsed ? 'justify-center' : '',
              isCurrentRoute(item.href) ? 'bg-[#1a4d4f] text-white' : 'text-gray-300 hover:bg-[#1a4d4f] hover:text-white'
            ]"
          >
            <component 
              :is="item.icon" 
              :class="[
                'flex-shrink-0 h-5 w-5',
                isCurrentRoute(item.href) ? 'text-[#8FE3CF]' : 'text-gray-400 group-hover:text-[#8FE3CF]'
              ]"
            />
            <span 
              :class="['ml-4 transition-opacity duration-300', isCollapsed ? 'hidden' : 'block']"
            >
              {{ item.name }}
            </span>
          </router-link>

          <!-- Sensor Data Dropdown -->
          <div class="relative" v-if="!isCollapsed">
            <button 
              @click="toggleSensorDropdown"
              :class="[
                'flex items-center w-full px-4 py-3 text-sm font-medium rounded-lg transition-colors duration-150',
                isSensorDropdownOpen || isCurrentRoute('/sensors') ? 'bg-[#1a4d4f] text-white' : 'text-gray-300 hover:bg-[#1a4d4f] hover:text-white'
              ]"
            >
              <Database class="flex-shrink-0 h-5 w-5 text-gray-400 group-hover:text-[#8FE3CF]" />
              <span class="ml-4">Sensor Data</span>
              <ChevronDown 
                :class="['ml-auto h-5 w-5 transition-transform', isSensorDropdownOpen ? 'transform rotate-180' : '']"
              />
            </button>
            <div 
              v-show="isSensorDropdownOpen"
              class="mt-2 space-y-2 px-4"
            >
              <router-link 
                v-for="sensor in sensorTypes" 
                :key="sensor.name"
                :to="sensor.href"
                class="block px-4 py-2 text-sm text-gray-300 hover:bg-[#1a4d4f] hover:text-white rounded-lg transition-colors duration-150"
              >
                {{ sensor.name }}
              </router-link>
            </div>
          </div>
        </div>
      </nav>

      <!-- Profile Section -->
      <div class="border-t border-[#1a4d4f] p-6">
        <div class="flex items-center" :class="{ 'justify-center': isCollapsed }">
          <div :class="['flex items-center justify-center transition-all duration-300', isCollapsed ? 'w-16 h-16' : 'w-12 h-12']">
            <img 
              src="/images/profile-example.jpg" 
              class="w-full h-full rounded-full object-cover border-2 border-[#1a4d4f]" 
              alt="Profile" 
            />
          </div>
          <div v-if="!isCollapsed" class="ml-3">
            <p class="text-sm font-medium text-white">John Doe</p>
            <p class="text-xs text-gray-400">Farmer</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { 
  LayoutDashboard,
  Brain,
  BarChart2,
  Cpu,
  Database,
  Sprout,
  Menu,
  PanelLeftClose,
  ChevronDown
} from 'lucide-vue-next'

const isCollapsed = ref(false)
const isSensorDropdownOpen = ref(false)
const route = useRoute()

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
  if (isCollapsed.value) {
    isSensorDropdownOpen.value = false
  }
}

const toggleSensorDropdown = () => {
  isSensorDropdownOpen.value = !isSensorDropdownOpen.value
}

const isCurrentRoute = (path) => {
  return route.path === path
}

const menuItems = [
  { name: 'Overview', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Crop Prediction', href: '/prediction', icon: Brain },
  { name: 'Device Control', href: '/control', icon: Cpu },
  { name: 'Soil Analysis', href: '/soil', icon: Sprout },
]

const sensorTypes = [
  { name: 'Soil Moisture', href: '/soil-moisture' },
  { name: 'Water Level', href: '/water-level' },
  { name: 'Humidity', href: '/humidity' },
  { name: 'Temperature', href: '/temperature' },
  { name: 'Motor Control', href: '/motor-control' },
]
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Add styles to ensure sidebar and button are always visible */
.sidebar-wrapper {
  position: relative;
  z-index: 50;
}
</style>

