<template>
  <nav class="fixed top-2 mx-4 left-0 right-0 bg-gradient-to-r from-[#00A572] to-[#008F61] backdrop-blur-md bg-opacity-95 shadow-lg z-50 rounded-xl border border-transparent border-t-[3px] border-t-orange-400">
    <div class="max-w-[1920px] mx-auto px-4 lg:px-6 py-2.5">
      <!-- Top row with logo and profile -->
      <div class="flex items-center justify-between">
        <!-- Logo and PROJECT ISRAEL text - positioned with padding-top -->
        <div class="flex items-center relative w-[180px]">
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
            
            <!-- Enhanced WebSocket Tooltip - Minimalist Design -->
            <div 
              v-show="showWebSocketTooltip"
              class="absolute right-0 top-full mt-2 w-52 bg-white/95 backdrop-blur-md rounded-lg shadow-lg overflow-hidden z-50 transition-all duration-200 border border-gray-100 transform origin-top-right"
              :class="showWebSocketTooltip ? 'scale-100 opacity-100' : 'scale-95 opacity-0'"
            >
              <div class="p-3">
                <div class="flex items-center justify-between mb-3">
                  <div class="flex items-center">
                    <div class="w-2 h-2 rounded-full mr-2" :class="isWebSocketConnected ? 'bg-green-500' : 'bg-red-500'"></div>
                    <h3 class="font-medium text-sm text-gray-800">WebSocket</h3>
                  </div>
                  <Zap class="h-4 w-4 text-[#00A572]" />
                </div>
                
                <div v-if="isWebSocketConnected" class="space-y-2.5">
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-gray-500">Status</span>
                    <span class="font-medium text-gray-800">Connected</span>
                  </div>
                  
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-gray-500">Latency</span>
                    <span class="font-medium text-gray-800">{{ wsLatency }}ms</span>
                  </div>
                  
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-gray-500">Uptime</span>
                    <span class="font-medium text-gray-800">{{ wsUptime }}</span>
                  </div>
                  
                </div>
                
                <div v-else class="flex items-center justify-center py-2">
                  <span class="text-xs text-red-500 font-medium">Disconnected</span>
                </div>
              </div>
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
            
            <!-- Enhanced WiFi Tooltip - Minimalist Design -->
            <div 
              v-show="showWifiTooltip"
              class="absolute right-0 top-full mt-2 w-52 bg-white/95 backdrop-blur-md rounded-lg shadow-lg overflow-hidden z-50 transition-all duration-200 border border-gray-100 transform origin-top-right"
              :class="showWifiTooltip ? 'scale-100 opacity-100' : 'scale-95 opacity-0'"
            >
              <div class="p-3">
                <div class="flex items-center justify-between mb-3">
                  <div class="flex items-center">
                    <div class="w-2 h-2 rounded-full mr-2" :class="wifiStrength > 0 ? 'bg-green-500' : 'bg-red-500'"></div>
                    <h3 class="font-medium text-sm text-gray-800">WiFi Status</h3>
                  </div>
                  <Wifi class="h-4 w-4 text-[#00A572]" />
                </div>
                
                <div v-if="wifiStrength > 0" class="space-y-2.5">
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-gray-500">Network</span>
                    <span class="font-medium text-gray-800">{{ wifiNetwork }}</span>
                  </div>
                  
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-gray-500">IP Address</span>
                    <span class="font-medium text-gray-800">{{ ipAddress }}</span>
                  </div>
                  
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-gray-500">Signal</span>
                    <span class="font-medium text-gray-800">{{ wifiStrength }}%</span>
                  </div>
                  
                  <!-- Signal Strength Bar -->
                  <div class="mt-1.5">
                    <div class="w-full h-1 bg-gray-100 rounded-full overflow-hidden">
                      <div 
                        class="h-full rounded-full transition-all duration-500 ease-out"
                        :class="getSignalStrengthClass(wifiStrength)"
                        :style="{ width: `${wifiStrength}%` }"
                      ></div>
                    </div>
                  </div>
                </div>
                
                <div v-else class="flex items-center justify-center py-2">
                  <span class="text-xs text-red-500 font-medium">Disconnected</span>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Notification Icon with Enhanced Minimalist Badge -->
          <div class="relative">
            <router-link 
              to="/notifications"
              class="relative flex items-center justify-center h-8 w-8 rounded-full bg-white/10 hover:bg-white/20 transition-all duration-300 text-white group/bell"
              :class="{ 'bg-white/30': $route.path === '/notifications' }"
              @mouseenter="showNotificationTooltip = true"
              @mouseleave="showNotificationTooltip = false"
            >
              <Bell class="h-4 w-4 transition-transform duration-200 group-hover/bell:scale-110" />
              
              <!-- Enhanced Minimalist Notification Badge - Completely Static -->
              <div 
                v-if="unreadNotificationCount > 0"
                class="notification-badge-static absolute -top-1 -right-1 min-w-[16px] h-4 flex items-center justify-center rounded-full bg-red-500 text-white shadow-md border border-white/30"
              >
                <span class="text-[9px] font-semibold leading-none px-0.5">
                  {{ unreadNotificationCount > 99 ? '99+' : unreadNotificationCount }}
                </span>
              </div>
            </router-link>
            
            <!-- Ultra Small Notification Tooltip - Compact and Readable -->
            <!-- Custom Small Notification Tooltip -->
            <div 
              v-show="showNotificationTooltip"
              class="absolute top-full left-1/2 transform -translate-x-1/2 mt-1 px-2 py-0.5 bg-green-100 text-green-900 font-medium text-[10px] rounded-md whitespace-nowrap z-50 transition-all duration-200 shadow-sm"
              :class="showNotificationTooltip ? 'opacity-100' : 'opacity-0'"
            >
              Notifications
              <!-- Custom small tooltip arrow -->
              <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-green-100"></div>
            </div>
            
            <!-- Notification Panel -->
            <!-- <div 
              v-show="showNotifications"
              class="absolute right-0 top-full mt-2 w-80 origin-top-right bg-white rounded-lg shadow-lg overflow-hidden z-50 border border-gray-100 transform transition-all duration-200"
              :class="notificationAnimation"
            >
              <div class="p-3 bg-gradient-to-r from-[#00A572] to-[#008F61] text-white">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-2">
                    <Bell class="h-4 w-4" />
                    <h3 class="font-medium">Notifications</h3>
                  </div>
                  <div class="flex items-center gap-2">
                    <span 
                      v-if="notifications && notifications.length"
                      class="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-orange-500 text-[10px] font-bold text-white"
                    >
                      {{ notifications.filter(n => n && !n.read).length }}
                    </span>

                    <button 
                      @click.stop="markAllAsRead"
                      class="text-xs px-1.5 py-0.5 bg-white/10 hover:bg-white/20 rounded-md transition-colors"
                      title="Mark all as read"
                    >
                      <Check class="h-3 w-3" />
                    </button>
                  </div>
                </div>
              </div>

              <div class="max-h-[350px] overflow-y-auto">
                <div v-if="notifications.filter(n => n).length === 0" class="p-4 text-center text-gray-500">
                  <BellOff class="h-6 w-6 mx-auto mb-2 text-gray-400" />
                  <p class="text-sm">No notifications</p>
                </div>
                
                <div v-else>
                  <div v-if="todayNotifications.filter(n => n).length > 0">
                    <div class="px-3 py-1.5 bg-gray-50 border-y border-gray-100">
                      <span class="text-xs font-medium text-gray-500">Today</span>
                    </div>
                    <div 
                      v-for="notification in todayNotifications.filter(n => n)" 
                      :key="notification.id"
                      class="p-3 border-b border-gray-100 hover:bg-gray-50 transition-colors cursor-pointer"
                      :class="{ 'bg-blue-50/50': notification && !notification.read }"
                      @click="markAsRead(notification.id)"
                    >
                      <div class="flex items-start gap-3">
                        <div 
                          class="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center"
                          :class="getNotificationTypeClass(notification.type).bgColor"
                        >
                          <component 
                            :is="getNotificationTypeClass(notification.type).icon" 
                            class="h-4 w-4 text-white" 
                          />
                        </div>
                        <div class="flex-1 min-w-0">
                          <p class="text-sm font-medium text-gray-900 mb-0.5">{{ notification.title }}</p>
                          <p class="text-xs text-gray-500 mb-1">{{ notification.message }}</p>
                          <div class="flex items-center justify-between">
                            <span class="text-xs text-gray-400">{{ formatTime(notification.time) }}</span>
                            <div v-if="notification && !notification.read" class="h-2 w-2 rounded-full bg-blue-500"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <div v-if="earlierNotifications.filter(n => n).length > 0">
                    <div class="px-3 py-1.5 bg-gray-50 border-y border-gray-100">
                      <span class="text-xs font-medium text-gray-500">Earlier</span>
                    </div>
                    <div 
                      v-for="notification in earlierNotifications.filter(n => n)" 
                      :key="notification.id"
                      class="p-3 border-b border-gray-100 hover:bg-gray-50 transition-colors cursor-pointer"
                      :class="{ 'bg-blue-50/50': notification && !notification.read }"
                      @click="markAsRead(notification.id)"
                    >
                      <div class="flex items-start gap-3">
                        <div 
                          class="flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center"
                          :class="getNotificationTypeClass(notification.type).bgColor"
                        >
                          <component 
                            :is="getNotificationTypeClass(notification.type).icon" 
                            class="h-4 w-4 text-white" 
                          />
                        </div>
                        <div class="flex-1 min-w-0">
                          <p class="text-sm font-medium text-gray-900 mb-0.5">{{ notification.title }}</p>
                          <p class="text-xs text-gray-500 mb-1">{{ notification.message }}</p>
                          <div class="flex items-center justify-between">
                            <span class="text-xs text-gray-400">{{ formatTime(notification.time) }}</span>
                            <div v-if="notification && !notification.read" class="h-2 w-2 rounded-full bg-blue-500"></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="p-2 bg-gray-50 border-t border-gray-100 flex justify-between items-center">
                <a href="/notifications" class="text-xs text-[#00A572] font-medium hover:underline">
                  View all notifications
                </a>
                <button 
                  @click.stop="showNotifications = false"
                  class="text-xs px-2 py-1 text-gray-500 hover:bg-gray-200 rounded transition-colors"
                >
                  Close
                </button>
              </div>
            </div> -->
          </div>

          <!-- Pure Minimalist Profile with Subtle Active State -->
          <div 
            class="relative ml-4 cursor-pointer group/profile" 
            @click="goToProfile"
            @mouseenter="showProfileTooltip = true"
            @mouseleave="showProfileTooltip = false"
          >
            <!-- Profile Image with Ultra Clean Design -->
            <div class="relative">
              <div 
                class="w-8 h-8 rounded-full overflow-hidden transition-all duration-300 ease-out group-hover/profile:scale-[1.02]"
                :class="isOnProfilePage 
                  ? 'ring-1 ring-green-400/60 ring-offset-1 ring-offset-white/20' 
                  : 'ring-1 ring-white/15 hover:ring-white/25'"
              >
                <img 
                  :src="user?.profilePicture || '/public/images/profile.jpg'"
                  class="w-full h-full object-cover transition-all duration-300"
                  :class="isOnProfilePage ? 'brightness-[1.02] saturate-[1.05]' : ''"
                  alt="Profile"
                />
                
                <!-- Ultra Subtle Active Overlay -->
                <div 
                  v-if="isOnProfilePage"
                  class="absolute inset-0 bg-gradient-to-br from-green-400/8 via-transparent to-transparent"
                ></div>
              </div>
              
              <!-- Micro Active Indicator -->
              <div 
                v-if="isOnProfilePage"
                class="absolute -bottom-px -right-px w-2 h-2 bg-green-400 rounded-full border border-white/40 shadow-sm"
              ></div>
            </div>
            
            <!-- Ultra Small Profile Tooltip - Compact and Readable -->
            <!-- Custom Small Profile Tooltip -->
            <div 
              v-show="showProfileTooltip"
              class="absolute top-full left-1/2 transform -translate-x-1/2 mt-1 px-2 py-0.5 bg-green-100 text-green-800 text-[10px] font-medium rounded-md whitespace-nowrap z-50 transition-all duration-200 shadow-sm"
              :class="showProfileTooltip ? 'opacity-100' : 'opacity-0'"
            >
              Profile
              <!-- Custom small tooltip arrow -->
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
  
  <!-- Click outside handler for notifications -->
  <div 
    v-if="showNotifications" 
    class="fixed inset-0 z-40"
    @click="showNotifications = false"
  ></div>
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
import { ref, computed, onMounted, onBeforeUnmount, watch, nextTick, provide } from 'vue'
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
  BellOff,
  Wifi,
  Zap,
  Check,
  AlertCircle,
  // Droplet, // Already imported
  Leaf,
  BarChart,
  Cog,
  Beaker,
  CheckCircle,
  Info,
  AlertTriangle,
  XCircle,
  X 
} from 'lucide-vue-next'
import axios from 'axios'
import { eventBus } from '../../eventBus'
import { sendPushNotification } from '../../utils/notify.js'
import { initWaterStream, onWaterLevelUpdate } from '../../utils/water.js'
import api from '../../api/index.js'
import {
  getFirestore,
  collection,
  addDoc,
  getDocs,
  query,
  orderBy,
  limit,
  doc,
  setDoc,
  Timestamp,
  serverTimestamp,
  getDoc,
  updateDoc,
  deleteDoc,
  where,
  getDocsFromServer,
  onSnapshot 
} from 'firebase/firestore'

const db = getFirestore()

const route = useRoute()
const router = useRouter()
const user = ref(null)
const isSensorDropdownOpen = ref(false)  
// Tooltip visibility states
const showWifiTooltip = ref(false)
const showWebSocketTooltip = ref(false)
const showNotificationTooltip = ref(false)
const showProfileTooltip = ref(false)

// Notifications
const showNotifications = ref(false)
const notificationAnimation = ref('scale-95 opacity-0')

const isWebSocketConnected = ref(false)
const wsLatency = ref(0)
const wsUptime = ref('0m')
let wsStartTime = null
const wifiStrength = ref(100)
const wifiNetwork = ref('Unknown')
const ipAddress = ref('')

// Sample notifications data
const notifications = ref([])
const waterLevel = ref(0);
const sensorReadings = ref([]);

// Computed property for checking if user is on profile page
const isOnProfilePage = computed(() => {
  return route.name === 'UserProfile' || route.path === '/profile' || route.path.includes('/user-profile')
})

// Computed property for unread notification count
const unreadNotificationCount = computed(() => {
  return notifications.value.filter(n => n && !n.read).length;
});

// Provide the unread count to any child components that need it
provide('unreadNotificationCount', unreadNotificationCount);

const currentTime = ref(Date.now())
const savedSchedules = ref([])

const notifiedStartIds = new Set()
const notifiedEndIds = new Set()

// Keep track of previous states of schedules to detect changes for end notifications
const previousSchedulesMap = new Map();

// Toast handling
const showToast = ref(false)
const toastMessage = ref('')
const toastSeverity = ref('info')
const toastTimeout = ref(null)

// const sendSMS = async (phone, message) => {
//   try {
//     const response = await axios.post('http://127.0.0.1:8000/send-sms', {
//       phone,
//       message
//     })
//     console.log('✅ SMS sent:', response.data)
//   } catch (error) {
//     if (error.response) {
//       console.error('❌ SMS send error:', error.response.data)
//     } else {
//       console.error('❌ SMS send error:', error)
//     }
//   }
// }

const showToastMessage = (message, severity = 'info') => {
  if (toastTimeout.value) clearTimeout(toastTimeout.value)

  toastMessage.value = message
  toastSeverity.value = severity
  showToast.value = true

  toastTimeout.value = setTimeout(() => {
    showToast.value = false
  }, 10000)
}

const toastStyles = computed(() => {
  switch (toastSeverity.value) {
    case 'success':
      return {
        icon: CheckCircle,
        iconColor: 'text-green-600',
        iconBg: 'bg-green-100',
        bg: 'bg-white',
        border: 'border-green-200'
      }
    case 'info':
      return {
        icon: Info,
        iconColor: 'text-blue-600',
        iconBg: 'bg-blue-100',
        bg: 'bg-white',
        border: 'border-blue-200'
      }
    case 'warning':
      return {
        icon: AlertTriangle,
        iconColor: 'text-yellow-600',
        iconBg: 'bg-yellow-100',
        bg: 'bg-white',
        border: 'border-yellow-200'
      }
    case 'critical':
      return {
        icon: XCircle,
        iconColor: 'text-red-600',
        iconBg: 'bg-red-100',
        bg: 'bg-white',
        border: 'border-red-200'
      }
    case 'failed':
      return {
        icon: XCircle,
        iconColor: 'text-gray-600',
        iconBg: 'bg-gray-100',
        bg: 'bg-white',
        border: 'border-gray-300'
      }
    default:
      return {
        icon: Info,
        iconColor: 'text-gray-600',
        iconBg: 'bg-gray-100',
        bg: 'bg-white',
        border: 'border-gray-300'
      }
  }
})

defineExpose({ showToastMessage })

const localNotifiedCache = {
  critical: null,
  warning: null,
  info: null,
}

const isSameDay = (d1, d2) =>
  d1.getFullYear() === d2.getFullYear() &&
  d1.getMonth() === d2.getMonth() &&
  d1.getDate() === d2.getDate()

const sendNotification = async (message, title, severity = 'info') => {
  // Default: show toast for non-critical notifications
  if (severity !== 'critical') {
    showToastMessage(message, severity)
  }

  let shouldSend = true

  if (severity === 'critical') {
    const today = new Date().toISOString().split('T')[0]

    const q = query(
      collection(db, 'notifications'),
      where('severity', '==', 'critical'),
      where('type', '==', 'water'),
      where('date', '==', today)
    )

    try {
      const snapshot = await getDocsFromServer(q)

      if (!snapshot.empty) {
        console.log('[DEBUG] Critical water notification already exists for today:', snapshot.docs[0].data())
        shouldSend = false
      } else {
        console.log('[DEBUG] No critical water notification found for today')
      }
    } catch (error) {
      console.error('❌ Error checking for existing notification:', error)
      shouldSend = false // Prevent duplicate on query error
    }
  }

  if (!shouldSend) return

  // Show toast only if allowed to send
  showToastMessage(message, severity)

  const notification = {
    id: Date.now().toString(),
    message,
    title,
    type: 'water',
    severity,
    read: false,
    date: new Date().toISOString().split('T')[0],
    timestamp: serverTimestamp(),
  }

  try {
    const docRef = await addDoc(collection(db, 'notifications'), notification)
    console.log('✅ Notification saved to Firestore:', docRef.id)

    const savedDoc = await getDoc(docRef)
    console.log('[DEBUG] Saved notification:', savedDoc.data())

    if (severity === 'critical') {
      const phone = '+639627080157'
      // await sendSMS(phone, `${title}: ${message}`) // Assuming sendSMS is defined elsewhere or re-added
    }
  } catch (error) {
    console.error('❌ Error saving notification:', error)
  }
}

const evaluateWaterLevel = (level) => {
  if (level <= 15) {
    sendNotification(
      'Water level is critically low! Immediate action required.',
      'Critical Water Level',
      'critical'
    )
  } else if (level <= 30 && level > 15) {
    sendNotification(
      'Water level is low (20–30%). Consider refilling soon.',
      'Low Water Level',
      'warning'
    )
  } else if (level === 50) {
    sendNotification(
      'Water level is at 50%. Monitoring status.',
      'Water Level Update',
      'info'
    )
  }
}

const sendScheduleNotification = async (schedule, status) => { // `status` is 'started' or 'ended'
  try {
    const dateTimeFormatted = new Date(schedule.scheduledTime).toLocaleString('en-US', {
      weekday: 'short',
      // year: 'numeric', // Year might be too verbose for a quick notification
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });

    const eventType = status === 'started' ? 'watering_start' : 'watering_end';

    const message =
      status === 'started'
        ? `The watering scheduled at ${dateTimeFormatted} is now starting.`
        : `The watering scheduled at ${dateTimeFormatted} has ended.`;

    // --- Duplicate Check ---
    const notificationsRef = collection(db, 'notifications');
    const q = query(notificationsRef,
      where('scheduleId', '==', schedule.id),
      where('eventType', '==', eventType)
    );

    const querySnapshot = await getDocs(q);
    if (!querySnapshot.empty) {
      console.log(`Notification for schedule ${schedule.id} (${eventType}) already exists. Skipping.`);
      // Ensure local cache is also up-to-date if somehow missed
      if (status === 'started') notifiedStartIds.add(schedule.id);
      else notifiedEndIds.add(schedule.id);
      return; // Exit if duplicate
    }
    // --- End Duplicate Check ---

    const notification = {
      title: 'Scheduled Watering',
      message,
      severity: 'info',
      type: 'watering_schedule', // More specific type for this category of notification
      scheduleId: schedule.id,   // Store the ID of the schedule this notification relates to
      eventType: eventType,      // Store 'watering_start' or 'watering_end'
      read: false,
      timestamp: serverTimestamp()
    };

    await addDoc(collection(db, 'notifications'), notification);
    showToastMessage(`Schedule ${status}: ${dateTimeFormatted}`);

    // Update local notification caches after successful send
    if (status === 'started') notifiedStartIds.add(schedule.id);
    else notifiedEndIds.add(schedule.id);

  } catch (error) {
    console.error('Notification error:', error);
  }
};

// Function to fetch notifications from Firestore
const fetchNotifications = async () => {
  try {
    const querySnapshot = await getDocs(collection(db, "notifications"));
    notifications.value = querySnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
    console.log('Fetched notifications:', notifications.value.length);
  } catch (err) {
    console.error("Error fetching notifications from Firebase:", err);
  }
};

// Set up real-time listener for notifications
const setupNotificationsListener = () => {
  const notificationsRef = collection(db, 'notifications');
  const q = query(notificationsRef, orderBy('timestamp', 'desc'));
  
  return onSnapshot(q, (snapshot) => {
    const notificationsList = [];
    snapshot.forEach((doc) => {
      notificationsList.push({
        id: doc.id,
        ...doc.data()
      });
    });
    notifications.value = notificationsList;
    console.log('Notifications updated:', notifications.value.length);
  }, (error) => {
    console.error('Error in notifications listener:', error);
  });
};

let unsubscribeNotifications = null;
let unsubscribeSchedules = null;

const fetchWateringSchedules = () => {
  const schedulesRef = collection(db, 'watering_schedules');
  const schedulesQuery = query(schedulesRef, orderBy('dateTime', 'desc')); // Consider ordering by scheduledTime for consistency

  if (unsubscribeSchedules) unsubscribeSchedules();

  unsubscribeSchedules = onSnapshot(
    schedulesQuery,
    (snapshot) => {
      const now = Date.now();
      const schedules = [];

      snapshot.forEach((doc) => {
        const data = doc.data();
        const scheduleId = doc.id;
        const currentScheduleData = { id: scheduleId, ...data };

        // Normalize scheduledTime to ms
        if (currentScheduleData.scheduledTime && currentScheduleData.scheduledTime < 1e12) {
          currentScheduleData.scheduledTime *= 1000;
        }

        const previousScheduleState = previousSchedulesMap.get(scheduleId);

        // Auto-mark as completed if past and not recurring
        if (currentScheduleData.mode === 'one-time' && currentScheduleData.scheduledTime < now && currentScheduleData.completed === false) {
          updateDoc(doc(db, 'watering_schedules', scheduleId), { completed: true, updatedAt: serverTimestamp() })
            .then(() => console.log(`Auto-marked schedule ${scheduleId} as completed.`))
            .catch(err => console.error("Error auto-updating schedule:", err));
          // The onSnapshot will pick this change up again, and currentScheduleData.completed will be true in a subsequent callback.
        }

        // Check for 'completed' transition for END notification
        if (previousScheduleState && previousScheduleState.completed === false && currentScheduleData.completed === true) {
          if (!notifiedEndIds.has(scheduleId)) {
            // Check if the schedule's end time was relatively recent to avoid old notifications
            const scheduleEndTime = currentScheduleData.scheduledTime + (currentScheduleData.duration || 0) * 60000;
            if (Math.abs(now - scheduleEndTime) < 5 * 60 * 1000) { // e.g., within last 5 minutes
              sendScheduleNotification(currentScheduleData, 'ended'); // sendScheduleNotification now handles notifiedEndIds
            } else {
              console.log(`Schedule ${scheduleId} completed, but end time was not recent. Not sending 'ended' notification.`);
              notifiedEndIds.add(scheduleId); // Still mark to prevent future attempts if logic changes
            }
          }
        }
        schedules.push(currentScheduleData);
        previousSchedulesMap.set(scheduleId, { ...currentScheduleData }); // Store a copy for next comparison
      });

      savedSchedules.value = schedules;
    },
    (error) => {
      console.error('Error listening to watering schedules:', error);
    }
  );
};

const saveToLocalStorage = (notification) => {
  const existing = JSON.parse(localStorage.getItem('notifications') || '[]') // Corrected: localStorage.getItem
  // Prevent duplicates based on ID
  const exists = existing.find(n => n.id === notification.id)
  if (!exists) {
    existing.push(notification)
    localStorage.setItem('notifications', JSON.stringify(existing))
  }
}

const getSignalStrengthClass = (strength) => {
  if (strength >= 70) return 'bg-green-500'
  if (strength >= 40) return 'bg-yellow-500'
  return 'bg-red-500'
}

const menuItems = [
  { name: 'Overview', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Crop Prediction', href: '/prediction', icon: Brain },
  { name: 'Weather', href: '/weather', icon: Cloud },
  { name: 'Device Control', href: '/control', icon: Cpu },
  { name: 'Soil Analysis', href: '/soil', icon: Sprout }
]

const sensorTypes = [
  { name: 'NPK Data', href: '/npkData', icon: Sprout },
  { name: 'Soil pH', href: '/soilph', icon: Beaker },
  { name: 'Soil Moisture', href: '/soil-moisture', icon: Droplets },
  { name: 'Temp/Humid', href: '/temperature-humidity', icon: Thermometer },
  { name: 'Water Level', href: '/water-level', icon: Gauge },
  { name: 'Motor Control', href: '/motor-control', icon: Power }
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
  if (!e.target.closest('.relative.group')) { // More specific selector for sensor dropdown
    isSensorDropdownOpen.value = false
  }
}

const goToProfile = () => {
  router.push({ name: 'UserProfile' })
}

let resizeTimeout
const handleResize = () => {
  clearTimeout(resizeTimeout)
  resizeTimeout = setTimeout(() => {
    if (window.innerWidth < 640) {
      isSensorDropdownOpen.value = false
      showNotifications.value = false
      showWifiTooltip.value = false
      showWebSocketTooltip.value = false
      showNotificationTooltip.value = false
      showProfileTooltip.value = false
    }
  }, 150)
}

onMounted(async () => {
  // Get user data from storage
  const storedUser = localStorage.getItem("user") || sessionStorage.getItem("user")
  if (storedUser) {
    try {
      user.value = JSON.parse(storedUser)
    } catch (e) {
      console.error('Error parsing user data:', e)
    }
  }
  
  // Set up event listeners
  document.addEventListener('click', closeDropdown)
  window.addEventListener('resize', handleResize)
  
  // Handle responsive behavior
  handleResize()
  
  // Fetch IP and network info
  try {
    const res = await fetch('https://api.ipify.org?format=json');
    const ipData = await res.json();
    ipAddress.value = ipData.ip;
  } catch (error) {
    console.error('Error fetching IP:', error);
    ipAddress.value = 'Unknown';
  }

  // Set up network info
  if ('connection' in navigator) {
    const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;

    const updateWifiInfo = () => {
      wifiStrength.value = conn.downlinkMax ? Math.min(conn.downlinkMax * 10, 100) : 70;
      wifiNetwork.value = conn.effectiveType || 'WiFi';
    };

    // Initial set
    updateWifiInfo();

    // Watch for network changes
    if (conn.addEventListener) {
      conn.addEventListener('change', updateWifiInfo);
    }
  }

  // Load notifications from localStorage first for immediate display
  const saved = localStorage.getItem('notifications')
  if (saved) {
    notifications.value = JSON.parse(saved)
  }

  // Then fetch from Firestore and set up real-time listener
  await fetchNotifications();
  unsubscribeNotifications = setupNotificationsListener();
  
  // Set up watering schedules listener
  fetchWateringSchedules();
  
  // Set up interval for checking scheduled notifications
  setInterval(() => {
    currentTime.value = Date.now();
    const now = Date.now();
    savedSchedules.value.forEach((schedule) => {
      // Skip if no notification needed, no scheduled time, or already completed (for start)
      if (!schedule.notifyWatering || !schedule.scheduledTime || schedule.completed) return;

      const start = schedule.scheduledTime;

      // START notification
      const isStarting = Math.abs(now - start) <= 2000; // Check if current time is within 2s of start
      if (isStarting && !notifiedStartIds.has(schedule.id)) {
        sendScheduleNotification(schedule, 'started');
      }
    });
  }, 1000);
})

onBeforeUnmount(() => {
  // Clean up event listeners
  document.removeEventListener('click', closeDropdown)
  window.removeEventListener('resize', handleResize)
  clearTimeout(resizeTimeout)
  
  // Clean up Firestore listeners
  if (unsubscribeSchedules) unsubscribeSchedules();
  if (unsubscribeNotifications) unsubscribeNotifications();
})

// Watch for route changes to close dropdowns
watch(() => route.path, () => {
  isSensorDropdownOpen.value = false
  showNotifications.value = false
  showWifiTooltip.value = false
  showWebSocketTooltip.value = false
  showNotificationTooltip.value = false
  showProfileTooltip.value = false
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

/* Ensure notification badge styling is consistent */
.notification-badge {
  /* These styles will override any inline styles */
  min-width: 16px !important;
  height: 16px !important;
  background-color: #ef4444 !important; /* Tailwind red-500 */
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
}

/* Completely static notification badge - no animations */
.notification-badge-static {
  min-width: 16px !important;
  height: 16px !important;
  background-color: #ef4444 !important; /* Tailwind red-500 */
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
  /* Explicitly disable all animations and transitions */
  animation: none !important;
  transition: none !important;
  transform: none !important;
}

.notification-badge-static:hover {
  /* Remove hover effects that might cause movement */
  transform: none !important;
  animation: none !important;
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

/* Toast animation styles */
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