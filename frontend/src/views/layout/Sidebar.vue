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
              <button 
                @click="toggleNotifications"
                class="relative flex items-center justify-center h-8 w-8 rounded-full bg-white/10 hover:bg-white/20 transition-all duration-300 text-white"
                :class="{ 'bg-white/30': showNotifications }"
              >
                <Bell class="h-4 w-4" />
                <!-- Notification Badge -->
                <span class="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-orange-500 text-[10px] font-bold text-white">{{ notifications.filter(n => !n.read).length }}</span>
              </button>
              
              <!-- Notification Panel (Shown when clicked) -->
              <div 
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
                      <span class="text-xs px-1.5 py-0.5 bg-white/20 rounded-full">{{ notifications.filter(n => !n.read).length }} new</span>
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
                  <div v-if="notifications.length === 0" class="p-4 text-center text-gray-500">
                    <BellOff class="h-6 w-6 mx-auto mb-2 text-gray-400" />
                    <p class="text-sm">No notifications</p>
                  </div>
                  
                  <div v-else>
                    <!-- Today's Notifications -->
                    <div v-if="todayNotifications.length > 0">
                      <div class="px-3 py-1.5 bg-gray-50 border-y border-gray-100">
                        <span class="text-xs font-medium text-gray-500">Today</span>
                      </div>
                      <div 
                        v-for="notification in todayNotifications" 
                        :key="notification.id"
                        class="p-3 border-b border-gray-100 hover:bg-gray-50 transition-colors cursor-pointer"
                        :class="{ 'bg-blue-50/50': !notification.read }"
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
                              <div v-if="!notification.read" class="h-2 w-2 rounded-full bg-blue-500"></div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    <!-- Earlier Notifications -->
                    <div v-if="earlierNotifications.length > 0">
                      <div class="px-3 py-1.5 bg-gray-50 border-y border-gray-100">
                        <span class="text-xs font-medium text-gray-500">Earlier</span>
                      </div>
                      <div 
                        v-for="notification in earlierNotifications" 
                        :key="notification.id"
                        class="p-3 border-b border-gray-100 hover:bg-gray-50 transition-colors cursor-pointer"
                        :class="{ 'bg-blue-50/50': !notification.read }"
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
                              <div v-if="!notification.read" class="h-2 w-2 rounded-full bg-blue-500"></div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div class="p-2 bg-gray-50 border-t border-gray-100 flex justify-between items-center">
                  <button class="text-xs text-[#00A572] font-medium hover:underline">
                    View all notifications
                  </button>
                  <button 
                    @click.stop="showNotifications = false"
                    class="text-xs px-2 py-1 text-gray-500 hover:bg-gray-200 rounded transition-colors"
                  >
                    Close
                  </button>
                </div>
              </div>
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
    BellOff,
    Wifi,
    Zap,
    Check,
    AlertTriangle,
    Info,
    AlertCircle,
    Droplet,
    Leaf,
    BarChart,
    Cog
  } from 'lucide-vue-next'
  
  
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
  
  // Sample notifications data
  const notifications = ref([
    {
      id: 1,
      type: 'alert',
      title: 'Soil Moisture Alert',
      message: 'Soil moisture level is critically low in Zone A.',
      time: new Date(Date.now() - 10 * 60 * 1000), // 10 minutes ago
      read: false
    },
    {
      id: 2,
      type: 'warning',
      title: 'Weather Alert',
      message: 'Heavy rain expected in the next 24 hours.',
      time: new Date(Date.now() - 60 * 60 * 1000), // 1 hour ago
      read: false
    },
    {
      id: 3,
      type: 'info',
      title: 'System Update',
      message: 'System successfully updated to version 2.4.0.',
      time: new Date(Date.now() - 3 * 60 * 60 * 1000), // 3 hours ago
      read: false
    },
    {
      id: 4,
      type: 'success',
      title: 'Irrigation Completed',
      message: 'Scheduled irrigation completed successfully.',
      time: new Date(Date.now() - 5 * 60 * 60 * 1000), // 5 hours ago
      read: true
    },
    {
      id: 5,
      type: 'water',
      title: 'Water Level Low',
      message: 'Water reservoir level is below 30%.',
      time: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000), // 1 day ago
      read: true
    },
    {
      id: 6,
      type: 'system',
      title: 'Maintenance Required',
      message: 'Pump system requires maintenance check.',
      time: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000), // 2 days ago
      read: true
    },
    {
      id: 7,
      type: 'data',
      title: 'Data Analysis Complete',
      message: 'Crop yield prediction analysis is ready to view.',
      time: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000), // 3 days ago
      read: true
    }
  ])
  
  const isWebSocketConnected = ref(false)
  const wsLatency = ref(0)
  const wsUptime = ref('0m')
  let wsStartTime = null
  const wifiStrength = ref(100)
  const wifiNetwork = ref('Unknown')
  const ipAddress = ref('')

  onMounted(async () => {
    const protocol = location.protocol === 'https:' ? 'wss' : 'ws'
    const host = location.hostname + ':8000'
    const ws = new WebSocket(`${protocol}://${host}/api/weather/ws/weather`)


    ws.onopen = () => {
      isWebSocketConnected.value = true
      wsStartTime = Date.now()
      setInterval(() => {
        const elapsed = Date.now() - wsStartTime
        const mins = Math.floor(elapsed / 60000)
        const hours = Math.floor(mins / 60)
        wsUptime.value = `${hours}h ${mins % 60}m`
      }, 60000)
    }

    ws.onclose = () => {
      isWebSocketConnected.value = false
      wsUptime.value = '0m'
    }

    ws.onerror = () => {
      isWebSocketConnected.value = false
    }

  // Optional: latency ping-pong logic (if supported by backend)
    ws.onmessage = (e) => {
      const timeSent = Date.now()
      wsLatency.value = timeSent - JSON.parse(e.data)?.timestamp || 30
    }


    // Get IP address
    const res = await fetch('https://api.ipify.org?format=json');
    const ipData = await res.json();
    ipAddress.value = ipData.ip;

    // Estimate WiFi type (not always accurate) and listen for changes
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

  })



  // Get signal strength class based on percentage
  const getSignalStrengthClass = (strength) => {
    if (strength >= 70) return 'bg-green-500'
    if (strength >= 40) return 'bg-yellow-500'
    return 'bg-red-500'
  }
  
  // Filter notifications by date
  const todayNotifications = computed(() => {
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    
    return notifications.value.filter(notification => {
      const notificationDate = new Date(notification.time)
      return notificationDate >= today
    })
  })
  
  const earlierNotifications = computed(() => {
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    
    return notifications.value.filter(notification => {
      const notificationDate = new Date(notification.time)
      return notificationDate < today
    })
  })
  
  // Toggle notifications panel
  const toggleNotifications = () => {
    showNotifications.value = !showNotifications.value
    
    // Add animation
    if (showNotifications.value) {
      setTimeout(() => {
        notificationAnimation.value = 'scale-100 opacity-100'
      }, 10)
    } else {
      notificationAnimation.value = 'scale-95 opacity-0'
    }
  }
  
  // Mark notification as read
  const markAsRead = (id) => {
    const notification = notifications.value.find(n => n.id === id)
    if (notification) {
      notification.read = true
    }
  }
  
  // Mark all notifications as read
  const markAllAsRead = () => {
    notifications.value.forEach(notification => {
      notification.read = true
    })
  }
  
  // Format time for notifications
  const formatTime = (time) => {
    const now = new Date()
    const notificationTime = new Date(time)
    const diffMs = now - notificationTime
    const diffMins = Math.floor(diffMs / 60000)
    const diffHours = Math.floor(diffMs / 3600000)
    const diffDays = Math.floor(diffMs / 86400000)
    
    if (diffMins < 60) {
      return `${diffMins} min${diffMins !== 1 ? 's' : ''} ago`
    } else if (diffHours < 24) {
      return `${diffHours} hour${diffHours !== 1 ? 's' : ''} ago`
    } else if (diffDays < 7) {
      return `${diffDays} day${diffDays !== 1 ? 's' : ''} ago`
    } else {
      return notificationTime.toLocaleDateString()
    }
  }
  
  // Get notification type styling
  const getNotificationTypeClass = (type) => {
    switch (type) {
      case 'alert':
        return { 
          bgColor: 'bg-red-500',
          icon: AlertCircle
        }
      case 'warning':
        return { 
          bgColor: 'bg-orange-500',
          icon: AlertTriangle
        }
      case 'info':
        return { 
          bgColor: 'bg-blue-500',
          icon: Info
        }
      case 'success':
        return { 
          bgColor: 'bg-green-500',
          icon: Check
        }
      case 'water':
        return { 
          bgColor: 'bg-cyan-500',
          icon: Droplet
        }
      case 'system':
        return { 
          bgColor: 'bg-purple-500',
          icon: Cog
        }
      case 'data':
        return { 
          bgColor: 'bg-indigo-500',
          icon: BarChart
        }
      default:
        return { 
          bgColor: 'bg-gray-500',
          icon: Bell
        }
    }
  }
  
  // Simulate connection status changes (in a real app, this would be based on actual connections)
//   const simulateConnectionChanges = () => {
//     // Randomly toggle WebSocket connection status every 30-60 seconds
//     setInterval(() => {
//       if (Math.random() > 0.8) { // 20% chance to toggle
//         isWebSocketConnected.value = !isWebSocketConnected.value
        
//         // Update WebSocket latency
//         if (isWebSocketConnected.value) {
//           wsLatency.value = Math.floor(10 + Math.random() * 50) // 10-60ms
          
//           // Calculate uptime
//           const hours = Math.floor(Math.random() * 12)
//           const minutes = Math.floor(Math.random() * 60)
//           wsUptime.value = `${hours}h ${minutes}m`
//         }
//       } else if (isWebSocketConnected.value) {
//         // Just update latency occasionally
//         wsLatency.value = Math.floor(10 + Math.random() * 50) // 10-60ms
//       }
//     }, 30000 + Math.random() * 30000)
    
//     // Randomly change WiFi strength every 15-30 seconds
//     setInterval(() => {
//       if (Math.random() > 0.7) { // 30% chance to change
//         // Random value between 0 and 100, with higher probability for good connection
//         wifiStrength.value = Math.random() > 0.2 ? 
//           Math.floor(70 + Math.random() * 30) : // 70-100% (good)
//           Math.floor(Math.random() * 70) // 0-70% (poor to moderate)
          
//         // Occasionally change network name if disconnected/reconnected
//         if (Math.random() > 0.9) {
//           const networks = ['RODA_2002', 'ProjectIsrael_5G', 'Farm_Network', 'Guest_WiFi']
//           wifiNetwork.value = networks[Math.floor(Math.random() * networks.length)]
          
//           // Generate random IP
//           const ip1 = Math.floor(Math.random() * 255)
//           const ip2 = Math.floor(Math.random() * 255)
//           ipAddress.value = `192.168.${ip1}.${ip2}`
//         }
//       }
//     }, 15000 + Math.random() * 15000)
//   }
  
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