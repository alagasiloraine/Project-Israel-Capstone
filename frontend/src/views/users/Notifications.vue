<template>
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen pt-32">
      <!-- Container Wrapper with proper spacing -->
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Main Container with adjusted width -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] overflow-hidden transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Content Wrapper - Flex column to separate fixed header from scrollable content -->
          <div class="flex flex-col h-full">
            <!-- Fixed Header Section -->
            <div class="p-6 pb-0">
              <!-- Simple Header -->
              <div class="flex items-center justify-between mb-6">
                <div class="flex items-center">
                  <Bell class="h-6 w-6 text-gray-700 mr-3" />
                  <h1 class="text-xl font-semibold text-gray-800">Notifications</h1>
                </div>
                <div class="flex items-center space-x-3">
                  <button 
                    @click="markAllAsRead"
                    class="flex items-center px-3 py-1.5 bg-gray-100 hover:bg-gray-200 rounded-lg text-gray-700 text-sm transition-colors"
                  >
                    <Check class="h-4 w-4 mr-1.5" />
                    <span>Mark all as read</span>
                  </button>
                  <button 
                    @click="$router.push('/dashboard')"
                    class="flex items-center px-3 py-1.5 bg-gray-100 hover:bg-gray-200 rounded-lg text-gray-700 text-sm transition-colors"
                  >
                    <ArrowLeft class="h-4 w-4 mr-1.5" />
                    <span>Back</span>
                  </button>
                </div>
              </div>

              <!-- Filters and Search -->
              <div class="mb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <div class="flex flex-wrap items-center gap-2">
                  <button 
                    v-for="filter in filters" 
                    :key="filter.value"
                    @click="activeFilter = filter.value"
                    :class="[
                      'px-3 py-1.5 text-sm font-medium rounded-lg transition-colors',
                      activeFilter === filter.value 
                        ? 'bg-[#00A572] text-white' 
                        : 'bg-white text-gray-700 hover:bg-gray-100 border border-gray-200'
                    ]"
                  >
                    {{ filter.label }}
                  </button>
                </div>
                
                <div class="relative w-full sm:w-64">
                  <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <Search class="h-4 w-4 text-gray-400" />
                  </div>
                  <input 
                    type="text"
                    v-model="searchQuery"
                    placeholder="Search notifications..."
                    class="w-full pl-10 pr-4 py-2 text-sm bg-white border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A572]/20 focus:border-[#00A572]"
                  />
                </div>
              </div>
            </div>

            <!-- Scrollable Notifications Content -->
            <div class="flex-1 overflow-y-auto px-6 pb-6 notification-scroll">
              <!-- Empty State -->
              <div v-if="filteredNotifications.length === 0" class="py-16 flex flex-col items-center justify-center">
                <div class="bg-gray-100 p-4 rounded-full mb-4">
                  <BellOff class="h-8 w-8 text-gray-400" />
                </div>
                <h3 class="text-lg font-medium text-gray-900 mb-1">No notifications</h3>
                <p class="text-sm text-gray-500">
                  {{ searchQuery ? 'No results found for your search.' : 'You don\'t have any notifications yet.' }}
                </p>
              </div>

              <!-- Notifications -->
              <div v-else>
                <!-- Today's Notifications -->
                <div v-if="todayNotificationsPage.length > 0" class="mb-4">
                  <div class="px-4 py-2 bg-gray-50 rounded-lg mb-2 sticky top-0 z-10 shadow-sm">
                    <span class="text-sm font-medium text-gray-700">Today</span>
                  </div>
                  <div 
                    v-for="notification in todayNotificationsPage" 
                    :key="notification.id"
                    class="mb-3 p-4 rounded-xl border border-gray-100 hover:bg-gray-50 transition-colors"
                    :class="{ 'bg-blue-50/30 border-blue-100': !notification.read }"
                  >
                    <div class="flex items-start gap-4">
                      <div 
                        class="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center"
                        :class="getNotificationTypeClass(notification.type).bgColor"
                      >
                        <component 
                          :is="getNotificationTypeClass(notification.type).icon" 
                          class="h-5 w-5 text-white" 
                        />
                      </div>
                      <div class="flex-1 min-w-0">
                        <div class="flex items-start justify-between">
                          <h3 class="text-base font-medium text-gray-900 mb-1">{{ notification.title }}</h3>
                          <span class="text-xs text-gray-500 whitespace-nowrap ml-4">{{ formatTime(notification.time) }}</span>
                        </div>
                        <p class="text-sm text-gray-600 mb-2">{{ notification.message }}</p>
                        <div class="flex items-center gap-3">
                          <span 
                            class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                            :class="getNotificationTypeClass(notification.type).badgeColor"
                          >
                            {{ notification.type }}
                          </span>
                          <div v-if="!notification.read" class="flex items-center text-blue-600 text-xs font-medium">
                            <div class="h-1.5 w-1.5 rounded-full bg-blue-500 mr-1.5"></div>
                            Unread
                          </div>
                        </div>
                      </div>
                      <div class="flex items-center gap-2">
                        <button 
                          v-if="!notification.read"
                          @click.stop="markAsRead(notification.id)"
                          class="p-1.5 text-gray-400 hover:text-[#00A572] hover:bg-gray-100 rounded-full transition-colors"
                          title="Mark as read"
                        >
                          <Check class="h-4 w-4" />
                        </button>
                        <button 
                          @click.stop="deleteNotification(notification.id)"
                          class="p-1.5 text-gray-400 hover:text-red-500 hover:bg-gray-100 rounded-full transition-colors"
                          title="Delete"
                        >
                          <Trash2 class="h-4 w-4" />
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Yesterday's Notifications -->
                <div v-if="yesterdayNotificationsPage.length > 0" class="mb-4">
                  <div class="px-4 py-2 bg-gray-50 rounded-lg mb-2 sticky top-0 z-10 shadow-sm">
                    <span class="text-sm font-medium text-gray-700">Yesterday</span>
                  </div>
                  <div 
                    v-for="notification in yesterdayNotificationsPage" 
                    :key="notification.id"
                    class="mb-3 p-4 rounded-xl border border-gray-100 hover:bg-gray-50 transition-colors"
                    :class="{ 'bg-blue-50/30 border-blue-100': !notification.read }"
                  >
                    <div class="flex items-start gap-4">
                      <div 
                        class="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center"
                        :class="getNotificationTypeClass(notification.type).bgColor"
                      >
                        <component 
                          :is="getNotificationTypeClass(notification.type).icon" 
                          class="h-5 w-5 text-white" 
                        />
                      </div>
                      <div class="flex-1 min-w-0">
                        <div class="flex items-start justify-between">
                          <h3 class="text-base font-medium text-gray-900 mb-1">{{ notification.title }}</h3>
                          <span class="text-xs text-gray-500 whitespace-nowrap ml-4">{{ formatTime(notification.time) }}</span>
                        </div>
                        <p class="text-sm text-gray-600 mb-2">{{ notification.message }}</p>
                        <div class="flex items-center gap-3">
                          <span 
                            class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                            :class="getNotificationTypeClass(notification.type).badgeColor"
                          >
                            {{ notification.type }}
                          </span>
                          <div v-if="!notification.read" class="flex items-center text-blue-600 text-xs font-medium">
                            <div class="h-1.5 w-1.5 rounded-full bg-blue-500 mr-1.5"></div>
                            Unread
                          </div>
                        </div>
                      </div>
                      <div class="flex items-center gap-2">
                        <button 
                          v-if="!notification.read"
                          @click.stop="markAsRead(notification.id)"
                          class="p-1.5 text-gray-400 hover:text-[#00A572] hover:bg-gray-100 rounded-full transition-colors"
                          title="Mark as read"
                        >
                          <Check class="h-4 w-4" />
                        </button>
                        <button 
                          @click.stop="deleteNotification(notification.id)"
                          class="p-1.5 text-gray-400 hover:text-red-500 hover:bg-gray-100 rounded-full transition-colors"
                          title="Delete"
                        >
                          <Trash2 class="h-4 w-4" />
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Earlier Notifications -->
                <div v-if="earlierNotificationsPage.length > 0" class="mb-4">
                  <div class="px-4 py-2 bg-gray-50 rounded-lg mb-2 sticky top-0 z-10 shadow-sm">
                    <span class="text-sm font-medium text-gray-700">Earlier</span>
                  </div>
                  <div 
                    v-for="notification in earlierNotificationsPage" 
                    :key="notification.id"
                    class="mb-3 p-4 rounded-xl border border-gray-100 hover:bg-gray-50 transition-colors"
                    :class="{ 'bg-blue-50/30 border-blue-100': !notification.read }"
                  >
                    <div class="flex items-start gap-4">
                      <div 
                        class="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center"
                        :class="getNotificationTypeClass(notification.type).bgColor"
                      >
                        <component 
                          :is="getNotificationTypeClass(notification.type).icon" 
                          class="h-5 w-5 text-white" 
                        />
                      </div>
                      <div class="flex-1 min-w-0">
                        <div class="flex items-start justify-between">
                          <h3 class="text-base font-medium text-gray-900 mb-1">{{ notification.title }}</h3>
                          <span class="text-xs text-gray-500 whitespace-nowrap ml-4">{{ formatTime(notification.time) }}</span>
                        </div>
                        <p class="text-sm text-gray-600 mb-2">{{ notification.message }}</p>
                        <div class="flex items-center gap-3">
                          <span 
                            class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                            :class="getNotificationTypeClass(notification.type).badgeColor"
                          >
                            {{ notification.type }}
                          </span>
                          <div v-if="!notification.read" class="flex items-center text-blue-600 text-xs font-medium">
                            <div class="h-1.5 w-1.5 rounded-full bg-blue-500 mr-1.5"></div>
                            Unread
                          </div>
                        </div>
                      </div>
                      <div class="flex items-center gap-2">
                        <button 
                          v-if="!notification.read"
                          @click.stop="markAsRead(notification.id)"
                          class="p-1.5 text-gray-400 hover:text-[#00A572] hover:bg-gray-100 rounded-full transition-colors"
                          title="Mark as read"
                        >
                          <Check class="h-4 w-4" />
                        </button>
                        <button 
                          @click.stop="deleteNotification(notification.id)"
                          class="p-1.5 text-gray-400 hover:text-red-500 hover:bg-gray-100 rounded-full transition-colors"
                          title="Delete"
                        >
                          <Trash2 class="h-4 w-4" />
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Fixed Pagination Footer -->
            <div class="px-6 py-4 border-t border-gray-100 bg-white">
              <div class="flex items-center justify-between">
                <div class="text-sm text-gray-600">
                  Showing <span class="font-medium">{{ paginatedNotifications.length }}</span> of <span class="font-medium">{{ filteredNotifications.length }}</span> notifications
                </div>
                
                <div class="flex items-center gap-2">
                  <button 
                    class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed"
                    :disabled="currentPage === 1"
                    @click="currentPage--"
                  >
                    <ChevronLeft class="h-4 w-4" />
                  </button>
                  
                  <div class="flex items-center gap-1">
                    <button 
                      v-for="page in totalPages"
                      :key="page"
                      :class="[
                        'px-3 py-1 text-sm font-medium rounded-lg',
                        currentPage === page
                          ? 'bg-[#00A572] text-white'
                          : 'text-gray-500 hover:bg-gray-100'
                      ]"
                      @click="currentPage = page"
                    >
                      {{ page }}
                    </button>
                  </div>
                  
                  <button 
                    class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed"
                    :disabled="currentPage === totalPages || totalPages === 0"
                    @click="currentPage++"
                  >
                    <ChevronRight class="h-4 w-4" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { 
  Bell, 
  BellOff, 
  Check, 
  ArrowLeft, 
  Search, 
  ChevronLeft, 
  ChevronRight,
  AlertTriangle,
  Info,
  AlertCircle,
  Droplet,
  Leaf,
  BarChart,
  Cog,
  Trash2
} from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'

// Filters
const filters = [
  { label: 'All', value: 'all' },
  { label: 'Unread', value: 'unread' },
  { label: 'System', value: 'system' },
  { label: 'Alerts', value: 'alert' },
  { label: 'Data', value: 'data' }
]

const activeFilter = ref('all')
const searchQuery = ref('')
const currentPage = ref(1)
const itemsPerPage = ref(4) // Show 4 items per page

// Sample notifications data - in a real app, this would come from an API
const notifications = ref([
  {
    id: 1,
    title: 'System Update',
    message: 'The system has been updated to version 2.0.1. Please refresh your browser.',
    type: 'system',
    time: new Date(Date.now() - 1000 * 60 * 30), // 30 minutes ago
    read: false
  },
  {
    id: 2,
    title: 'Soil Moisture Alert',
    message: 'Soil moisture levels in Greenhouse 2 have dropped below 30%. Consider irrigation.',
    type: 'alert',
    time: new Date(Date.now() - 1000 * 60 * 60 * 2), // 2 hours ago
    read: false
  },
  {
    id: 3,
    title: 'Temperature Threshold Exceeded',
    message: 'Temperature in Greenhouse 1 has exceeded 32°C. Ventilation system activated.',
    type: 'warning',
    time: new Date(Date.now() - 1000 * 60 * 60 * 5), // 5 hours ago
    read: true
  },
  {
    id: 4,
    title: 'Crop Prediction Complete',
    message: 'Crop prediction analysis for your recent soil sample is now complete.',
    type: 'info',
    time: new Date(Date.now() - 1000 * 60 * 60 * 24), // 1 day ago
    read: false
  },
  {
    id: 5,
    title: 'Water Level Low',
    message: 'Water reservoir level is at 15%. Please refill soon to maintain irrigation.',
    type: 'water',
    time: new Date(Date.now() - 1000 * 60 * 60 * 24), // 1 day ago
    read: true
  },
  {
    id: 6,
    title: 'Weekly Report Generated',
    message: 'Your weekly crop performance report is now available for download.',
    type: 'data',
    time: new Date(Date.now() - 1000 * 60 * 60 * 24 * 2), // 2 days ago
    read: true
  },
  {
    id: 7,
    title: 'Maintenance Scheduled',
    message: 'System maintenance is scheduled for tomorrow at 2:00 AM. Expect brief downtime.',
    type: 'system',
    time: new Date(Date.now() - 1000 * 60 * 60 * 24 * 3), // 3 days ago
    read: true
  },
  {
    id: 8,
    title: 'Humidity Levels Optimal',
    message: 'Humidity levels have stabilized in all greenhouses. No action required.',
    type: 'success',
    time: new Date(Date.now() - 1000 * 60 * 60 * 24 * 4), // 4 days ago
    read: true
  }
])

// Filter notifications based on active filter and search query
const filteredNotifications = computed(() => {
  let result = [...notifications.value]
  
  // Apply filter
  if (activeFilter.value === 'unread') {
    result = result.filter(n => !n.read)
  } else if (activeFilter.value !== 'all') {
    result = result.filter(n => n.type === activeFilter.value)
  }
  
  // Apply search
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(n => 
      n.title.toLowerCase().includes(query) || 
      n.message.toLowerCase().includes(query)
    )
  }
  
  return result
})

// Reset to first page when filter or search changes
watch([activeFilter, searchQuery], () => {
  currentPage.value = 1
})

// Paginated notifications
const paginatedNotifications = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage.value
  return filteredNotifications.value.slice(startIndex, startIndex + itemsPerPage.value)
})

// Group all notifications by date
const todayNotifications = computed(() => {
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  
  return filteredNotifications.value.filter(notification => {
    const notificationDate = new Date(notification.time)
    return notificationDate >= today
  })
})

const yesterdayNotifications = computed(() => {
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  
  const yesterday = new Date(today)
  yesterday.setDate(yesterday.getDate() - 1)
  
  return filteredNotifications.value.filter(notification => {
    const notificationDate = new Date(notification.time)
    return notificationDate >= yesterday && notificationDate < today
  })
})

const earlierNotifications = computed(() => {
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  
  const yesterday = new Date(today)
  yesterday.setDate(yesterday.getDate() - 1)
  
  return filteredNotifications.value.filter(notification => {
    const notificationDate = new Date(notification.time)
    return notificationDate < yesterday
  })
})

// Get notifications for current page by category
const todayNotificationsPage = computed(() => {
  return paginatedNotifications.value.filter(notification => {
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    const notificationDate = new Date(notification.time)
    return notificationDate >= today
  })
})

const yesterdayNotificationsPage = computed(() => {
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  
  const yesterday = new Date(today)
  yesterday.setDate(yesterday.getDate() - 1)
  
  return paginatedNotifications.value.filter(notification => {
    const notificationDate = new Date(notification.time)
    return notificationDate >= yesterday && notificationDate < today
  })
})

const earlierNotificationsPage = computed(() => {
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  
  const yesterday = new Date(today)
  yesterday.setDate(yesterday.getDate() - 1)
  
  return paginatedNotifications.value.filter(notification => {
    const notificationDate = new Date(notification.time)
    return notificationDate < yesterday
  })
})

// Pagination
const totalPages = computed(() => {
  return Math.ceil(filteredNotifications.value.length / itemsPerPage.value) || 1
})

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

// Delete notification
const deleteNotification = (id) => {
  const index = notifications.value.findIndex(n => n.id === id)
  if (index !== -1) {
    notifications.value.splice(index, 1)
  }
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
    return notificationTime.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    })
  }
}

// Get notification type styling
const getNotificationTypeClass = (type) => {
  switch (type) {
    case 'alert':
      return { 
        bgColor: 'bg-red-500',
        badgeColor: 'bg-red-100 text-red-800',
        icon: AlertCircle
      }
    case 'warning':
      return { 
        bgColor: 'bg-orange-500',
        badgeColor: 'bg-orange-100 text-orange-800',
        icon: AlertTriangle
      }
    case 'info':
      return { 
        bgColor: 'bg-blue-500',
        badgeColor: 'bg-blue-100 text-blue-800',
        icon: Info
      }
    case 'success':
      return { 
        bgColor: 'bg-green-500',
        badgeColor: 'bg-green-100 text-green-800',
        icon: Check
      }
    case 'water':
      return { 
        bgColor: 'bg-cyan-500',
        badgeColor: 'bg-cyan-100 text-cyan-800',
        icon: Droplet
      }
    case 'system':
      return { 
        bgColor: 'bg-purple-500',
        badgeColor: 'bg-purple-100 text-purple-800',
        icon: Cog
      }
    case 'data':
      return { 
        bgColor: 'bg-indigo-500',
        badgeColor: 'bg-indigo-100 text-indigo-800',
        icon: BarChart
      }
    default:
      return { 
        bgColor: 'bg-gray-500',
        badgeColor: 'bg-gray-100 text-gray-800',
        icon: Bell
      }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Enhanced scrollbar styling */
.notification-scroll::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

.notification-scroll::-webkit-scrollbar-track {
  background: rgba(20, 83, 45, 0.05);
  border-radius: 4px;
}

.notification-scroll::-webkit-scrollbar-thumb {
  background: rgba(20, 83, 45, 0.3);
  border-radius: 4px;
  transition: background-color 200ms;
}

.notification-scroll::-webkit-scrollbar-thumb:hover {
  background: rgba(20, 83, 45, 0.5);
}

/* Firefox scrollbar styling */
.notification-scroll {
  scrollbar-width: thin;
  scrollbar-color: rgba(20, 83, 45, 0.3) rgba(20, 83, 45, 0.05);
}

/* Ensure proper layout on different browsers */
@supports (-webkit-touch-callout: none) {
  .h-screen {
    height: -webkit-fill-available;
  }
}

/* Focus styles for better keyboard navigation */
:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

/* Print styles for better readability when printed */
@media print {
  body {
    font-size: 12pt;
  }

  .no-print {
    display: none;
  }
}
</style>
