<template>
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <main class="flex-1 flex flex-col h-screen pt-32">
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Main container with curved edges on all corners -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] flex flex-col transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Fixed Header Section -->
          <div class="p-6 border-b border-gray-100">
            <!-- Header -->
            <div class="mb-6">
              <h1 class="text-2xl font-bold text-gray-900 mb-2">Motor Control Data Table</h1>
              <div class="flex items-center text-sm text-gray-500">
                <span class="text-green-600">Motor Control</span>
                <ChevronRight class="h-4 w-4 mx-1" />
                <span>Data Table</span>
              </div>
            </div>

            <!-- Controls - Fixed -->
            <div class="flex flex-wrap items-center gap-4 mb-2">
              <div class="relative flex-1 min-w-[200px]">
                <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                <input
                  type="text"
                  placeholder="Search anything here..."
                  class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 text-sm text-gray-800 placeholder-gray-400"
                  v-model="searchQuery"
                  @input="performSearch"
                />
              </div>

              <!-- Date Range Filter -->
              <div class="relative">
                <button 
                  @click.stop="toggleDropdown('dateFilter')"
                  class="flex items-center gap-2 px-4 py-2 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50"
                >
                  <Calendar class="h-4 w-4" />
                  Date Range
                  <ChevronDown class="h-4 w-4" :class="{ 'transform rotate-180': activeDropdown === 'dateFilter' }" />
                </button>
                
                <div 
                  v-show="activeDropdown === 'dateFilter'"
                  class="absolute right-0 mt-2 w-80 bg-white rounded-lg shadow-lg border border-gray-200 z-50"
                  @click.stop
                >
                  <div class="p-4 space-y-4">
                    <div class="space-y-2">
                      <label class="block text-sm font-medium text-gray-700">Start Date</label>
                      <input
                        v-model="dateFilter.startDate"
                        type="date"
                        class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded-md focus:ring-2 focus:ring-green-500/20"
                      />
                    </div>
                    <div class="space-y-2">
                      <label class="block text-sm font-medium text-gray-700">End Date</label>
                      <input
                        v-model="dateFilter.endDate"
                        type="date"
                        class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded-md focus:ring-2 focus:ring-green-500/20"
                      />
                    </div>
                    <div class="flex gap-2">
                      <button 
                        @click="applyDateFilter"
                        class="flex-1 px-4 py-2 bg-green-500 text-white rounded-lg text-sm font-medium hover:bg-green-600"
                      >
                        Apply
                      </button>
                      <button 
                        @click="clearDateFilter"
                        class="px-4 py-2 border border-gray-200 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-50"
                      >
                        Clear
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Status Filter -->
              <div class="relative">
                <button 
                  @click.stop="toggleDropdown('statusFilter')"
                  class="flex items-center gap-2 px-4 py-2 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50"
                >
                  <Filter class="h-4 w-4" />
                  Status
                  <ChevronDown class="h-4 w-4" :class="{ 'transform rotate-180': activeDropdown === 'statusFilter' }" />
                </button>
                
                <div 
                  v-show="activeDropdown === 'statusFilter'"
                  class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 z-50"
                  @click.stop
                >
                  <div class="p-3 space-y-2">
                    <div class="flex items-center">
                      <input 
                        id="filter-all" 
                        type="radio" 
                        v-model="statusFilter" 
                        value="all"
                        class="h-4 w-4 text-green-600 focus:ring-green-500"
                      />
                      <label for="filter-all" class="ml-2 text-sm text-gray-700">All</label>
                    </div>
                    <div class="flex items-center">
                      <input 
                        id="filter-on" 
                        type="radio" 
                        v-model="statusFilter" 
                        value="on"
                        class="h-4 w-4 text-green-600 focus:ring-green-500"
                      />
                      <label for="filter-on" class="ml-2 text-sm text-gray-700">ON</label>
                    </div>
                    <div class="flex items-center">
                      <input 
                        id="filter-off" 
                        type="radio" 
                        v-model="statusFilter" 
                        value="off"
                        class="h-4 w-4 text-green-600 focus:ring-green-500"
                      />
                      <label for="filter-off" class="ml-2 text-sm text-gray-700">OFF</label>
                    </div>
                    <button 
                      @click="applyStatusFilter"
                      class="w-full mt-2 px-4 py-2 bg-green-500 text-white rounded-lg text-sm font-medium hover:bg-green-600"
                    >
                      Apply
                    </button>
                  </div>
                </div>
              </div>

              <!-- Sort Button -->
              <div class="relative">
                <button 
                  @click.stop="toggleDropdown('sort')"
                  class="flex items-center gap-2 px-4 py-2 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50"
                >
                  Sort by {{ sortKey ? headers.find(h => h.key === sortKey)?.label : 'Time' }}
                  <ChevronDown class="h-4 w-4" :class="{ 'transform rotate-180': activeDropdown === 'sort' }" />
                </button>
                
                <div 
                  v-show="activeDropdown === 'sort'"
                  class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 z-50"
                  @click.stop
                >
                  <div class="py-1">
                    <button
                      v-for="header in headers"
                      :key="header.key"
                      @click="setSortKey(header.key)"
                      class="w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-50 flex items-center justify-between"
                    >
                      {{ header.label }}
                      <ArrowUpDown v-if="sortKey === header.key" class="h-3 w-3" />
                    </button>
                  </div>
                </div>
              </div>

              <!-- Export Button -->
              <div class="relative">
                <button 
                  @click.stop="toggleDropdown('export')"
                  class="flex items-center gap-2 px-4 py-2 rounded-lg bg-emerald-500 text-white text-sm font-medium hover:bg-emerald-600"
                >
                  <Download class="h-4 w-4" />
                  Export
                  <ChevronDown class="h-4 w-4" :class="{ 'transform rotate-180': activeDropdown === 'export' }" />
                </button>
                
                <div 
                  v-show="activeDropdown === 'export'"
                  class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 z-50"
                  @click.stop
                >
                  <div class="py-1">
                    <button
                      v-for="format in exportFormats"
                      :key="format"
                      @click="exportData(format)"
                      class="w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-50"
                    >
                      Export as {{ format.toUpperCase() }}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Loading State -->
          <div v-if="isLoading" class="flex-1 flex items-center justify-center">
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 border-4 border-green-500 border-t-transparent rounded-full animate-spin mb-4"></div>
              <p class="text-gray-600">Loading motor status data...</p>
            </div>
          </div>

          <!-- Error State -->
          <div v-else-if="error" class="flex-1 flex items-center justify-center">
            <div class="text-center p-6 max-w-md">
              <div class="bg-red-100 p-3 rounded-full inline-flex mb-4">
                <AlertTriangle class="h-8 w-8 text-red-600" />
              </div>
              <h3 class="text-lg font-medium text-gray-900 mb-2">Error Loading Data</h3>
              <p class="text-gray-600 mb-4">{{ error }}</p>
              <button 
                @click="fetchMotorStatusData" 
                class="px-4 py-2 bg-green-500 text-white rounded-lg text-sm font-medium hover:bg-green-600"
              >
                Try Again
              </button>
            </div>
          </div>

          <!-- Empty State -->
          <div v-else-if="filteredData.length === 0" class="flex-1 flex items-center justify-center">
            <div class="text-center p-6 max-w-md">
              <div class="bg-gray-100 p-3 rounded-full inline-flex mb-4">
                <Database class="h-8 w-8 text-gray-400" />
              </div>
              <h3 class="text-lg font-medium text-gray-900 mb-2">No Data Found</h3>
              <p class="text-gray-600">
                {{ searchQuery || dateFilter.applied || statusFilter !== 'all' 
                  ? 'No records match your search criteria. Try adjusting your filters.' 
                  : 'There are no motor status records in the database yet.' }}
              </p>
            </div>
          </div>

          <!-- Table Section - Scrollable -->
          <div v-else class="flex-1 p-4 overflow-auto">
            <!-- Table container -->
            <div class="w-full bg-white rounded-xl shadow-sm">
              <table class="min-w-full table-fixed">
                <thead>
                  <tr class="bg-gray-50 border-b border-gray-200">
                    <th v-for="header in headers" :key="header.key" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      <div class="text-gray-900">{{ header.label }}</div>
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                  <tr 
                    v-for="(row, index) in paginatedData" 
                    :key="index"
                    class="group transition-colors duration-150 hover:bg-gray-50"
                  >
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.id }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm">
                      <span 
                        :class="[
                          'px-2 py-1 rounded-full text-sm font-medium',
                          row.status ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                        ]"
                      >
                        {{ row.status ? 'ON' : 'OFF' }}
                      </span>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.date }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.time }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.user }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.device_id }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Fixed Pagination Section -->
          <div class="border-t border-gray-100 p-4 bg-white rounded-b-[20px]">
            <!-- Enhanced Pagination -->
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4 px-2">
              <div class="text-sm text-gray-600 flex items-center gap-2">
                <span class="hidden sm:inline">Showing</span>
                <select 
                  v-model="itemsPerPage" 
                  class="bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm font-medium text-gray-700 hover:border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-colors"
                  @change="updatePagination"
                >
                  <option value="6">6</option>
                  <option value="10">10</option>
                  <option value="20">20</option>
                  <option value="50">50</option>
                </select>
                <span class="hidden sm:inline">entries per page</span>
                <span class="text-gray-400 mx-2">|</span>
                <span>
                  {{ filteredData.length > 0 ? (currentPage - 1) * itemsPerPage + 1 : 0 }} - {{ Math.min(currentPage * itemsPerPage, filteredData.length) }}
                  <span class="text-gray-400">of</span>
                  {{ filteredData.length }}
                </span>
              </div>

              <div class="flex items-center gap-2">
                <button 
                  @click="prevPage"
                  :disabled="currentPage === 1"
                  class="inline-flex items-center justify-center px-3 py-1.5 text-sm font-medium rounded-lg transition-colors
                    disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-400
                    enabled:hover:bg-gray-100 enabled:text-gray-700 enabled:hover:text-gray-900"
                >
                  <ChevronLeft class="w-4 h-4 mr-1" />
                  Previous
                </button>

                <div class="flex items-center">
                  <button
                    v-for="page in displayedPages"
                    :key="page"
                    @click="goToPage(page)"
                    :class="[
                      'relative inline-flex items-center justify-center w-9 h-9 text-sm font-medium rounded-lg transition-colors',
                      page === currentPage
                        ? 'bg-green-500 text-white shadow-sm hover:bg-green-600'
                        : page === '...'
                          ? 'cursor-default text-gray-400'
                          : 'text-gray-700 hover:bg-gray-100 hover:text-gray-900'
                    ]"
                  >
                    {{ page }}
                  </button>
                </div>

                <button 
                  @click="nextPage"
                  :disabled="currentPage >= totalPages"
                  class="inline-flex items-center justify-center px-3 py-1.5 text-sm font-medium rounded-lg transition-colors
                    disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-400
                    enabled:hover:bg-gray-100 enabled:text-gray-700 enabled:hover:text-gray-900"
                >
                  Next
                  <ChevronRight class="w-4 h-4 ml-1" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { 
  Search, 
  Filter, 
  Download, 
  ChevronDown, 
  ChevronRight, 
  ChevronLeft, 
  ArrowUpDown, 
  Calendar,
  AlertTriangle,
  Database
} from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'
import {
  getFirestore,
  collection,
  getDocs,
  query,
  orderBy,
  doc,
  getDoc,
  where,
  Timestamp
} from 'firebase/firestore'

// Get Firestore instance
const db = getFirestore()

// Headers definition
const headers = [
  { key: 'id', label: 'ID' },
  { key: 'status', label: 'MOTOR CONTROL' },
  { key: 'date', label: 'DATE' },
  { key: 'time', label: 'TIME' },
  { key: 'user', label: 'USER' },
  { key: 'device_id', label: 'DEVICE ID' }
]

// Reactive state
const motorStatusData = ref([])
const isLoading = ref(true)
const error = ref(null)
const searchQuery = ref('')
const itemsPerPage = ref(6)
const currentPage = ref(1)
const activeDropdown = ref(null)
const sortKey = ref('timestamp')
const sortDirection = ref('desc')
const dateFilter = ref({
  startDate: '',
  endDate: '',
  applied: false
})
const statusFilter = ref('all')
const appliedStatusFilter = ref('all')

const exportFormats = ['csv', 'pdf', 'excel']

// Fetch motor status data from Firestore
const fetchMotorStatusData = async () => {
  try {
    isLoading.value = true
    error.value = null
    motorStatusData.value = []
    
    // Get all history logs - ONLY fetch from history/logs, not the current document
    const historyRef = collection(db, 'motor_status', 'history', 'logs')
    const historyQuery = query(historyRef, orderBy('timestamp', 'desc'))
    const historySnapshot = await getDocs(historyQuery)
    
    let counter = 1
    historySnapshot.forEach(doc => {
      const data = doc.data()
      
      // Format the data for display
      motorStatusData.value.push({
        id: counter++,
        status: data.status,
        date: formatDate(data.timestamp?.toDate() || new Date()),
        time: formatTime(data.timestamp?.toDate() || new Date()),
        timestamp: data.timestamp?.toDate() || new Date(),
        user: data.user || 'system',
        device_id: data.device_id || 'main_motor',
        raw: data
      })
    })
    
    console.log(`Fetched ${motorStatusData.value.length} motor status records`)
    
  } catch (err) {
    console.error('Error fetching motor status data:', err)
    error.value = 'Failed to load motor status data. Please try again.'
  } finally {
    isLoading.value = false
  }
}

// Format date for display
const formatDate = (date) => {
  if (!date) return 'N/A'
  return date.toISOString().split('T')[0]
}

// Format time for display
const formatTime = (date) => {
  if (!date) return 'N/A'
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })
}

// Toggle dropdown
const toggleDropdown = (dropdownName) => {
  if (activeDropdown.value === dropdownName) {
    activeDropdown.value = null
  } else {
    activeDropdown.value = dropdownName
  }
}

// Handle click outside to close dropdowns
const handleClickOutside = (event) => {
  if (!event.target.closest('.relative')) {
    activeDropdown.value = null
  }
}

// Apply date filter
const applyDateFilter = () => {
  if (dateFilter.value.startDate || dateFilter.value.endDate) {
    dateFilter.value.applied = true
  }
  activeDropdown.value = null
  currentPage.value = 1
}

// Clear date filter
const clearDateFilter = () => {
  dateFilter.value.startDate = ''
  dateFilter.value.endDate = ''
  dateFilter.value.applied = false
  activeDropdown.value = null
  currentPage.value = 1
}

// Apply status filter
const applyStatusFilter = () => {
  appliedStatusFilter.value = statusFilter.value
  activeDropdown.value = null
  currentPage.value = 1
}

// Set sort key
const setSortKey = (key) => {
  if (sortKey.value === key) {
    // Toggle direction if clicking the same column
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortDirection.value = 'desc' // Default to descending for new column
  }
  activeDropdown.value = null
}

// Perform search
const performSearch = () => {
  currentPage.value = 1
}

// Filtered data based on search, date filter, and status filter
const filteredData = computed(() => {
  let result = [...motorStatusData.value]
  
  // Apply search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(row => {
      return Object.values(row).some(value => {
        if (value === null || value === undefined) return false
        if (value instanceof Date) return false
        if (typeof value === 'object') return false
        return String(value).toLowerCase().includes(query)
      })
    })
  }
  
  // Apply date filter
  if (dateFilter.value.applied) {
    if (dateFilter.value.startDate) {
      const startDate = new Date(dateFilter.value.startDate)
      startDate.setHours(0, 0, 0, 0)
      result = result.filter(row => row.timestamp >= startDate)
    }
    
    if (dateFilter.value.endDate) {
      const endDate = new Date(dateFilter.value.endDate)
      endDate.setHours(23, 59, 59, 999)
      result = result.filter(row => row.timestamp <= endDate)
    }
  }
  
  // Apply status filter
  if (appliedStatusFilter.value !== 'all') {
    const statusValue = appliedStatusFilter.value === 'on'
    result = result.filter(row => row.status === statusValue)
  }
  
  return result
})

// Sorted data
const sortedData = computed(() => {
  if (!sortKey.value) return filteredData.value
  
  return [...filteredData.value].sort((a, b) => {
    let aValue = a[sortKey.value]
    let bValue = b[sortKey.value]
    
    // Special handling for timestamp
    if (sortKey.value === 'timestamp') {
      aValue = a.timestamp?.getTime() || 0
      bValue = b.timestamp?.getTime() || 0
    }
    
    // Handle empty values
    if (aValue === '' || aValue === undefined || aValue === null) {
      aValue = sortDirection.value === 'asc' ? -Infinity : Infinity
    }
    if (bValue === '' || bValue === undefined || bValue === null) {
      bValue = sortDirection.value === 'asc' ? -Infinity : Infinity
    }
    
    // Handle string comparison
    if (typeof aValue === 'string' && typeof bValue === 'string') {
      return sortDirection.value === 'asc' 
        ? aValue.localeCompare(bValue)
        : bValue.localeCompare(aValue)
    }
    
    // Handle numeric comparison
    return sortDirection.value === 'asc' ? aValue - bValue : bValue - aValue
  })
})

// Paginated data
const paginatedData = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage.value
  const endIndex = startIndex + itemsPerPage.value
  return sortedData.value.slice(startIndex, endIndex)
})

// Total pages
const totalPages = computed(() => {
  return Math.max(1, Math.ceil(sortedData.value.length / itemsPerPage.value))
})

// Displayed pages for pagination
const displayedPages = computed(() => {
  const total = totalPages.value
  const current = currentPage.value
  const pages = []

  if (total <= 7) {
    // If 7 or fewer pages, show all
    for (let i = 1; i <= total; i++) {
      pages.push(i)
    }
  } else {
    // Always show first page
    pages.push(1)

    if (current <= 3) {
      // If near start, show 2-5 then ellipsis
      pages.push(2, 3, 4, 5, '...', total)
    } else if (current >= total - 2) {
      // If near end, show ellipsis then last 4
      pages.push('...', total - 4, total - 3, total - 2, total - 1, total)
    } else {
      // Otherwise show ellipsis, current -1, current, current + 1, ellipsis
      pages.push('...', current - 1, current, current + 1, '...', total)
    }
  }

  return pages
})

// Pagination methods
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const updatePagination = () => {
  currentPage.value = 1
}

const goToPage = (page) => {
  if (typeof page === 'number') {
    currentPage.value = page
  }
}

// Export data methods
const exportData = (format) => {
  const dataToExport = sortedData.value
  
  if (format === 'csv') {
    exportAsCSV(dataToExport)
  } else if (format === 'pdf') {
    exportAsPDF(dataToExport)
  } else if (format === 'excel') {
    exportAsExcel(dataToExport)
  }
  
  activeDropdown.value = null
}

const exportAsCSV = (data) => {
  // Get headers
  const headerRow = headers.map(h => h.label).join(',')
  
  // Convert data to CSV rows
  const rows = data.map(row => {
    return headers.map(header => {
      // Handle special cases like objects or arrays
      const value = row[header.key]
      if (typeof value === 'string' && value.includes(',')) {
        return `"${value}"`
      }
      return value
    }).join(',')
  })
  
  // Combine headers and rows
  const csvContent = [headerRow, ...rows].join('\n')
  
  // Create a blob and download
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.setAttribute('href', url)
  link.setAttribute('download', 'motor_status_data.csv')
  link.style.visibility = 'hidden'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

const exportAsPDF = (data) => {
  // In a real application, you would use a library like jsPDF
  // For this example, we'll just show an alert
  alert('PDF export would be implemented with a library like jsPDF')
  console.log('Data to export as PDF:', data)
}

const exportAsExcel = (data) => {
  // In a real application, you would use a library like xlsx
  // For this example, we'll just show an alert
  alert('Excel export would be implemented with a library like xlsx')
  console.log('Data to export as Excel:', data)
}

// Watch for changes that should reset pagination
watch([searchQuery, dateFilter, appliedStatusFilter, itemsPerPage], () => {
  currentPage.value = 1
})

// Lifecycle hooks
onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  fetchMotorStatusData()
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Enhanced scrollbar styling with dark green color */
.overflow-y-auto, .overflow-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(20, 83, 45, 0.5) transparent;
}

.overflow-y-auto::-webkit-scrollbar, .overflow-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track, .overflow-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb, .overflow-auto::-webkit-scrollbar-thumb {
  background-color: rgba(20, 83, 45, 0.5);
  border-radius: 9999px;
  transition: background-color 200ms;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover, .overflow-auto::-webkit-scrollbar-thumb:hover {
  background-color: rgba(20, 83, 45, 0.7);
}

/* Add smooth transitions for all elements */
* {
  transition: color 200ms, background-color 200ms;
}

.relative {
  position: relative;
}

[v-show] {
  transition: opacity 0.2s, transform 0.2s;
}

.relative:hover {
  z-index: 50;
}

/* Add smooth transitions for pagination buttons */
button {
  transition: all 0.2s ease-in-out;
}

.pagination-enter-active,
.pagination-leave-active {
  transition: opacity 0.2s ease-in-out;
}

.pagination-enter-from,
.pagination-leave-to {
  opacity: 0;
}

/* Add responsive styles for table */
@media (max-width: 768px) {
  .overflow-x-auto {
    -webkit-overflow-scrolling: touch;
  }
  
  th, td {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }
}

/* Ensure responsive layout on smaller screens */
@media (max-width: 640px) {
  .flex-col {
    row-gap: 0.5rem;
  }
  
  .pagination-container {
    justify-content: center;
  }
}

/* Improve table responsiveness */
@media (max-width: 480px) {
  table {
    font-size: 0.75rem;
  }
  
  th, td {
    padding-left: 0.25rem !important;
    padding-right: 0.25rem !important;
  }
}

/* Add subtle hover effect to table rows */
tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.02) !important;
  transition: background-color 0.2s ease;
}
</style>