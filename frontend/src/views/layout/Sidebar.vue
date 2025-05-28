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
          
          <!-- Notification Icon -->
          <div class="relative">
            <a 
            
              href="/notifications"
              class="relative flex items-center justify-center h-8 w-8 rounded-full bg-white/10 hover:bg-white/20 transition-all duration-300 text-white"
              :class="{ 'bg-white/30': showNotifications }"
            >
              <Bell class="h-4 w-4" />
              <!-- Notification Badge -->
              <span class="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-orange-500 text-[10px] font-bold text-white">
                {{ notifications.filter(n => n && !n.read).length }}
              </span>
            </a>
            
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

          
          <div class="relative ml-4">
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
import { ref, computed, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
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
  Droplet,
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

const currentTime = ref(Date.now())
const savedSchedules = ref([])

const notifiedStartIds = new Set()
const notifiedEndIds = new Set()

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
  showToastMessage(message, severity)

  if (severity === 'critical') {
    const today = new Date().toISOString().split('T')[0] // e.g., '2025-05-28'

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
        return
      } else {
        console.log('[DEBUG] No critical water notification found for today')
      }
    } catch (error) {
      console.error('❌ Error checking for existing notification:', error)
    }
  }

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
      await sendSMS(phone, `${title}: ${message}`)
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

const sendScheduleNotification = async (schedule, status) => {
  try {
    const dateTimeFormatted = new Date(schedule.scheduledTime).toLocaleString('en-US', {
      weekday: 'short',
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });

    const message =
      status === 'started'
        ? `The watering scheduled at ${dateTimeFormatted} is now starting.`
        : `The watering scheduled at ${dateTimeFormatted} has ended.`;

    const notification = {
      title: 'Scheduled Watering',
      message,
      severity: 'info',
      type: 'motor',
      read: false,
      timestamp: serverTimestamp()
    };

    await addDoc(collection(db, 'notifications'), notification);
    showToastMessage(`Schedule ${status}: ${dateTimeFormatted}`);
  } catch (error) {
    console.error('Notification error:', error);
  }
};

onMounted(() => {
  const waterLevelQuery = query(
    collection(db, 'water_level_readings'),
    orderBy('timestamp', 'desc'),
    limit(1)
  );

  console.log(waterLevelQuery)

  onSnapshot(waterLevelQuery, (snapshot) => {
    if (!snapshot.empty) {
      const data = snapshot.docs[0].data();
      evaluateWaterLevel(data.waterLevel);
    }
  });

  fetchWateringSchedules();

  setInterval(() => {
    currentTime.value = Date.now();
    const now = Date.now();

    savedSchedules.value.forEach(schedule => {
      if (!schedule.notifyWatering || !schedule.scheduledTime) return;

      const start = schedule.scheduledTime;
      const durationMs = (schedule.duration || 0) * 60000;
      const end = start + durationMs;

      // Trigger start toast at exact scheduled time ±1 sec
      const isStarting = Math.abs(now - start) <= 1000;
      if (isStarting && !notifiedStartIds.has(schedule.id)) {
        sendScheduleNotification(schedule, 'started');
        notifiedStartIds.add(schedule.id);
      }

      // Trigger end toast at exact end time ±1 sec
      const isEnding = Math.abs(now - end) <= 1000;
      if (isEnding && !notifiedEndIds.has(schedule.id)) {
        sendScheduleNotification(schedule, 'ended');
        notifiedEndIds.add(schedule.id);
      }
    });
  }, 1000);

  onSnapshot(collection(db, 'watering_schedules'), async (snapshot) => {
    const now = Date.now();
    const schedules = [];

    for (const doc of snapshot.docs) {
      const data = doc.data();

      // Normalize scheduledTime if needed
      if (data.scheduledTime && data.scheduledTime < 1e12) {
        data.scheduledTime *= 1000;
      }

      const pastDue = data.scheduledTime && data.scheduledTime <= now;

      if (pastDue && data.completed === false) {
        await updateDoc(doc.ref, { completed: true });
        data.completed = true;
      }

      schedules.push({ id: doc.id, ...data });
    }

    savedSchedules.value = schedules;
  });
});

const fetchWateringSchedules = async () => {
  try {
    console.log('Fetching watering schedules from Firebase...');

    const schedulesRef = collection(db, 'watering_schedules');
    const schedulesQuery = query(schedulesRef, orderBy('dateTime', 'desc'));
    const schedulesSnapshot = await getDocs(schedulesQuery);

    const now = Date.now();
    const schedules = [];

    for (const doc of schedulesSnapshot.docs) {
      const data = doc.data();

      // Normalize scheduledTime to ms if needed
      if (data.scheduledTime && data.scheduledTime < 1e12) {
        data.scheduledTime *= 1000;
      }

      schedules.push({ id: doc.id, ...data });
    }

    savedSchedules.value = schedules;
    console.log('Fetched watering schedules:', schedules.length);
  } catch (error) {
    console.error('Error fetching watering schedules:', error);
    showToastMessage('Error loading schedules. Please try again.');
  }
};


const saveToLocalStorage = (notification) => {
  const existing = JSON.parse(localStorage.removeItem('notifications') || '[]')
  // Prevent duplicates based on ID
  const exists = existing.find(n => n.id === notification.id)
  if (!exists) {
    existing.push(notification)
    localStorage.setItem('notifications', JSON.stringify(existing))
  }
}

onMounted(async () => {
  // const protocol = location.protocol === 'https:' ? 'wss' : 'ws'
  // const host = location.hostname + ':800'
  // const ws = new WebSocket(`${protocol}://${host}/api/weather/ws/weather`)


  // ws.onopen = () => {
  //   isWebSocketConnected.value = true
  //   wsStartTime = Date.now()
  //   setInterval(() => {
  //     const elapsed = Date.now() - wsStartTime
  //     const mins = Math.floor(elapsed / 60000)
  //     const hours = Math.floor(mins / 60)
  //     wsUptime.value = `${hours}h ${mins % 60}m`
  //   }, 60000)
  // }

  // ws.onclose = () => {
  //   isWebSocketConnected.value = false
  //   wsUptime.value = '0m'
  // }

  // ws.onerror = () => {
  //   isWebSocketConnected.value = false
  // }

  // // Optional: latency ping-pong logic (if supported by backend)
  // ws.onmessage = (e) => {
  // const timeSent = Date.now()
  //   wsLatency.value = timeSent - JSON.parse(e.data)?.timestamp || 30
  // }


  const res = await fetch('https://api.ipify.org?format=json');
  const ipData = await res.json();
  ipAddress.value = ipData.ip;

  if ('connection' in navigator) {
    const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;

    const updateWifiInfo = () => {
      wifiStrength.value = conn.downlinkMax ? Math.min(conn.downlinkMax * 10, 100) : 70;
      wifiNetwork.value = conn.effectiveType || 'WiFi';
    };

    // Initial set
    updateWifiInfo();

    // Watch for network changes (like switching Wi-Fi)
    if (conn.addEventListener) {
      conn.addEventListener('change', updateWifiInfo);
    }
  }

  const saved = localStorage.getItem('notifications')
  if (saved) {
    notifications.value = JSON.parse(saved)
  }

  try {
    const querySnapshot = await getDocs(collection(db, "notifications"));
    notifications.value = querySnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
  } catch (err) {
    console.error("Error fetching notifications from Firebase:", err);
  }

})


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
  { name: 'NPK Calibration', href: '/npk-calibration', icon: Beaker },
  { name: 'Soil Analysis', href: '/soil', icon: Sprout }
]

const sensorTypes = [
  { name: 'Soil Moisture', href: '/soil-moisture', icon: Droplets },
  { name: 'Water Level', href: '/water-level', icon: Gauge },
  { name: 'Temp/Humid', href: '/temperature-humidity', icon: Thermometer },
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
      showNotifications.value = false
      showWifiTooltip.value = false
      showWebSocketTooltip.value = false
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
  // simulateConnectionChanges() // Start the connection status simulation
})

onBeforeUnmount(() => {
  document.removeEventListener('click', closeDropdown)
  window.removeEventListener('resize', handleResize)
  clearTimeout(resizeTimeout)
})

watch(() => route.path, () => {
  isSensorDropdownOpen.value = false
  showNotifications.value = false
  showWifiTooltip.value = false
  showWebSocketTooltip.value = false
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


