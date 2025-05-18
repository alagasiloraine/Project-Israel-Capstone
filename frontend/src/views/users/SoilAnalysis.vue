<template>
  <div class="h-screen flex bg-white font-poppins overflow-hidden">
    <Sidebar />
    <main class="flex-1 flex flex-col h-screen pt-32">
      <div class="flex-1 w-full px-4 sm:px-6 md:px:8 lg:px-10 overflow-hidden">
        <!-- Enhanced main container with more appealing design -->
        <div class="bg-white rounded-lg shadow-lg border border-gray-100 h-[calc(100vh-140px)] flex flex-col overflow-hidden">
          <!-- Gradient header for visual appeal -->
          <div class="bg-gradient-to-r from-emerald-50 to-white p-6 border-b border-gray-100 rounded-t-lg">
            <!-- Header with controls aligned side by side -->
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <!-- Title and breadcrumb with enhanced styling -->
              <div>
                <h1 class="text-xl font-semibold text-gray-800 mb-1">Soil Analysis Measurements</h1>
                <div class="flex items-center text-sm text-gray-500">
                  <span class="text-emerald-600 font-medium">Soil Analysis</span>
                  <ChevronRight class="h-3.5 w-3.5 mx-1 text-gray-400" />
                  <span class="text-gray-600">Data Table</span>
                </div>
              </div>
              
              <!-- Controls aligned horizontally with improved styling -->
              <div class="flex items-center gap-2 flex-wrap md:flex-nowrap">
                <!-- Wider search bar -->
                <div class="relative w-72">
                  <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                  <input
                    type="text"
                    placeholder="Search measurements..."
                    class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-gray-200 focus:outline-none focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500 text-sm text-gray-700 placeholder-gray-400 shadow-sm"
                    v-model="searchQuery"
                    @input="performSearch"
                  />
                </div>
  
                <!-- Filter Button with enhanced styling -->
                <div class="relative">
                  <button 
                    @click.stop="toggleDropdown('filter')"
                    class="flex items-center gap-2 px-4 py-2.5 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:text-emerald-600 transition-colors shadow-sm"
                  >
                    <Filter class="h-4 w-4 text-gray-500" />
                    Filter
                    <ChevronDown class="h-4 w-4 text-gray-400" :class="{ 'transform rotate-180': activeDropdown === 'filter' }" />
                  </button>
                  
                  <div 
                    v-show="activeDropdown === 'filter'"
                    class="absolute right-0 mt-2 w-80 bg-white rounded-lg shadow-lg border border-gray-200 z-50 overflow-hidden"
                    @click.stop
                  >
                    <div class="p-4 space-y-4 max-h-[400px] overflow-y-auto">
                      <div v-for="field in filterFields" :key="field.key" class="space-y-2">
                        <label class="block text-sm font-medium text-gray-700">{{ field.label }}</label>
                        <div class="flex items-center gap-2">
                          <input
                            v-model="filters[field.key].min"
                            type="number"
                            placeholder="Min"
                            class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded-md focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500"
                          />
                          <span class="text-gray-400">-</span>
                          <input
                            v-model="filters[field.key].max"
                            type="number"
                            placeholder="Max"
                            class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded-md focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500"
                          />
                        </div>
                      </div>
                      <button 
                        @click="applyFilters"
                        class="w-full px-4 py-2 bg-emerald-500 text-white rounded-lg text-sm font-medium hover:bg-emerald-600 transition-colors"
                      >
                        Apply Filters
                      </button>
                    </div>
                  </div>
                </div>
  
                <!-- Sort Button with enhanced styling -->
                <div class="relative">
                  <button 
                    @click.stop="toggleDropdown('sort')"
                    class="flex items-center gap-2 px-4 py-2.5 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:text-emerald-600 transition-colors shadow-sm"
                  >
                    <ArrowUpDown class="h-4 w-4 text-gray-500" />
                    Sort
                    <ChevronDown class="h-4 w-4 text-gray-400" :class="{ 'transform rotate-180': activeDropdown === 'sort' }" />
                  </button>
                  
                  <div 
                    v-show="activeDropdown === 'sort'"
                    class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 z-50 overflow-hidden"
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
                        <ArrowUpDown v-if="sortKey === header.key" class="h-3 w-3 text-emerald-500" />
                      </button>
                    </div>
                  </div>
                </div>
  
                <!-- Export Button with enhanced styling -->
                <div class="relative">
                  <button 
                    @click.stop="toggleDropdown('export')"
                    class="flex items-center gap-2 px-4 py-2.5 rounded-lg bg-emerald-500 text-white text-sm font-medium hover:bg-emerald-600 transition-colors shadow-sm"
                  >
                    <Download class="h-4 w-4" />
                    Export
                    <ChevronDown class="h-4 w-4" :class="{ 'transform rotate-180': activeDropdown === 'export' }" />
                  </button>
                  
                  <div 
                    v-show="activeDropdown === 'export'"
                    class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 z-50 overflow-hidden"
                    @click.stop
                  >
                    <div class="py-1">
                      <button
                        v-for="format in exportFormats"
                        :key="format"
                        @click="exportData(format)"
                        class="w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-50 flex items-center"
                      >
                        <span v-if="format === 'csv'" class="mr-2 text-emerald-500"><FileText class="h-4 w-4" /></span>
                        <span v-else-if="format === 'pdf'" class="mr-2 text-red-500"><FileText class="h-4 w-4" /></span>
                        <span v-else class="mr-2 text-blue-500"><FileText class="h-4 w-4" /></span>
                        Export as {{ format.toUpperCase() }}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Table Section with Fixed Header - Enhanced styling -->
          <div class="flex-1 overflow-hidden">
            <!-- Table container with fixed header -->
            <div class="w-full h-full flex flex-col">
              <!-- Fixed Header with enhanced styling -->
              <div class="w-full border-b border-gray-200 sticky top-0 z-10 bg-gray-50">
                <table class="min-w-full">
                  <thead>
                    <tr>
                      <th class="w-[14%] py-3.5 px-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b">
                        Reading Date
                      </th>
                      <th class="w-[8%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-green-600">Nitrogen</div>
                        <div class="text-gray-400 text-[10px]">(MG/KG)</div>
                      </th>
                      <th class="w-[8%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-blue-600">Phosphorus</div>
                        <div class="text-gray-400 text-[10px]">(MG/KG)</div>
                      </th>
                      <th class="w-[8%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-purple-600">Potassium</div>
                        <div class="text-gray-400 text-[10px]">(MG/KG)</div>
                      </th>
                      <th class="w-[6%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-orange-600">pH</div>
                        <div class="text-gray-400 text-[10px]">(LEVEL)</div>
                      </th>
                      <th class="w-[8%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-red-600">Temperature</div>
                        <div class="text-gray-400 text-[10px]">(°C)</div>
                      </th>
                      <th class="w-[8%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-gray-600">Humidity</div>
                        <div class="text-gray-400 text-[10px]">(%)</div>
                      </th>
                      <th class="w-[8%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-cyan-600">Moisture</div>
                        <div class="text-gray-400 text-[10px]">(%)</div>
                      </th>
                      <th class="w-[16%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-emerald-600">Predicted Crop</div>
                        <div class="text-gray-400 text-[10px]">RECOMMENDATION</div>
                      </th>
                      <th class="w-[14%] py-3.5 px-4 text-left text-xs font-medium uppercase tracking-wider border-b">
                        <div class="text-gray-600">Prediction Time</div>
                        <div class="text-gray-400 text-[10px]">DATE & TIME</div>
                      </th>
                    </tr>
                  </thead>
                </table>
              </div>
              
              <!-- Scrollable Body with enhanced styling -->
              <div class="flex-1 overflow-y-auto">
                <table class="min-w-full">
                  <tbody>
                    <tr>
                      <div v-if="isLoading" class="py-8 flex flex-col items-center justify-center">
                        <div class="w-8 h-8 border-2 border-green-500 border-t-transparent rounded-full animate-spin mb-2"></div>
                        <p class="text-sm text-gray-500">Loading soil analysis data...</p>
                      </div>
                    </tr>

                    <tr 
                      v-for="(row, index) in paginatedData" 
                      :key="index"
                      class="border-b border-gray-50 last:border-0"
                    >
                      <td class="w-[14%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-gray-700">{{ row.date }}</div>
                      </td>
                      <td class="w-[8%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-green-600">
                          {{ row.nitrogen }}
                        </div>
                      </td>
                      <td class="w-[8%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-blue-600">
                          {{ row.phosphorus }}
                        </div>
                      </td>
                      <td class="w-[8%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-purple-600">
                          {{ row.potassium }}
                        </div>
                      </td>
                      <td class="w-[6%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-orange-600">
                          {{ row.ph }}
                        </div>
                      </td>
                      <td class="w-[8%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-red-600">
                          {{ row.temperature }}
                        </div>
                      </td>
                      <td class="w-[8%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-gray-600">
                          {{ row.humidity }}
                        </div>
                      </td>
                      <td class="w-[8%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium text-cyan-600">
                          {{ row.soilMoisture }}
                        </div>
                      </td>
                      <td class="w-[16%] px-4 py-3.5 whitespace-nowrap">
                        <div class="flex items-center">
                          <div v-if="row.predictedCrop !== '--'" class="text-sm font-medium text-emerald-600">
                            {{ row.predictedCrop.split('(')[0].trim() }}
                            <span class="ml-1 text-xs text-emerald-500">
                              {{ row.predictedCrop.match(/$$(.*?)$$/)?.[0] || '' }}
                            </span>
                          </div>
                          <div v-else class="text-sm font-medium text-gray-400">
                            --
                          </div>
                        </div>
                      </td>
                      <td class="w-[14%] px-4 py-3.5 whitespace-nowrap">
                        <div class="text-sm font-medium" :class="row.datePredicted !== '--' ? 'text-gray-700' : 'text-gray-400'">
                          {{ row.datePredicted }}
                        </div>
                      </td>
                    </tr>
                    <!-- Empty state when no data - Enhanced styling -->
                    <tr v-if="paginatedData.length === 0 && !isLoading">
                      <td colspan="10" class="px-6 py-16 text-center">
                        <div class="flex flex-col items-center justify-center">
                          <FileSearch class="h-16 w-16 text-gray-300 mb-4" />
                          <p class="text-gray-500 text-lg font-medium">No soil analysis data found</p>
                          <p class="text-gray-400 text-sm mt-1">Try adjusting your search or filters</p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
  
          <!-- Fixed Pagination Section with enhanced styling -->
          <div class="border-t border-gray-100 py-4 px-6 bg-gradient-to-r from-white to-emerald-50 rounded-b-lg">
            <!-- Enhanced Pagination -->
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
              <div class="text-sm text-gray-600 flex items-center gap-2">
                <span class="hidden sm:inline">Showing</span>
                <select 
                  v-model="itemsPerPage" 
                  class="bg-white border border-gray-200 rounded-lg px-2 py-1.5 text-sm font-medium text-gray-700 focus:outline-none focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500 shadow-sm"
                  @change="updatePagination"
                >
                  <option value="20">20</option>
                  <option value="25">25</option>
                  <option value="30">30</option>
                  <option value="50">50</option>
                </select>
                <span class="hidden sm:inline">entries per page</span>
                <span class="text-gray-400 mx-2 hidden sm:inline">|</span>
                <span>
                  {{ (currentPage - 1) * itemsPerPage + 1 }} - {{ Math.min(currentPage * itemsPerPage, sortedData.length) }}
                  <span class="text-gray-400">of</span>
                  {{ sortedData.length }}
                </span>
              </div>
  
              <div class="flex items-center gap-1">
                <button 
                  @click="prevPage"
                  :disabled="currentPage === 1"
                  class="inline-flex items-center justify-center px-3 py-1.5 text-sm font-medium transition-colors rounded-md
                    disabled:opacity-50 disabled:cursor-not-allowed disabled:text-gray-400
                    enabled:text-gray-700 enabled:hover:text-emerald-600 enabled:hover:bg-emerald-50"
                >
                  <ChevronLeft class="w-4 h-4 mr-1" />
                  Prev
                </button>
  
                <div class="flex items-center">
                  <button
                    v-for="page in displayedPages"
                    :key="page"
                    @click="goToPage(page)"
                    :class="[
                      'relative inline-flex items-center justify-center w-8 h-8 text-sm transition-colors mx-0.5 rounded-md',
                      page === currentPage
                        ? 'text-white bg-emerald-500 font-semibold'
                        : page === '...'
                          ? 'cursor-default text-gray-400'
                          : 'text-gray-700 hover:text-emerald-600 hover:bg-emerald-50'
                    ]"
                  >
                    {{ page }}
                  </button>
                </div>
  
                <button 
                  @click="nextPage"
                  :disabled="currentPage >= totalPages"
                  class="inline-flex items-center justify-center px-3 py-1.5 text-sm font-medium transition-colors rounded-md
                    disabled:opacity-50 disabled:cursor-not-allowed disabled:text-gray-400
                    enabled:text-gray-700 enabled:hover:text-emerald-600 enabled:hover:bg-emerald-50"
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

    <!-- Loading Page Component -->
    <!-- <LoadingPage 
      :isVisible="isLoading" 
      title="Loading Soil Analysis Data" 
      message="Please wait while we fetch the latest soil measurements"
    /> -->
  </div>
</template>
  
<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { Search, Filter, Download, ChevronDown, ChevronRight, ChevronLeft, ArrowUpDown, FileText, FileSearch } from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'
import LoadingPage from '../layout/LoadingPage.vue'
import {
  getFirestore,
  collection,
  query,
  orderBy,
  getDocs,
  where
} from 'firebase/firestore'

const db = getFirestore()
const soilData = ref([])
const isLoading = ref(true)

// Fetch both soil data and crop recommendations
const fetchSoilDataWithRecommendations = async () => {
  try {
    isLoading.value = true
    
    // First, get all soil readings
    const soilQuery = query(
      collection(db, "sensor_readings"),
      orderBy("timestamp", "desc")  // Latest first
    )
    const soilSnapshot = await getDocs(soilQuery)
    
    // Get all crop recommendations
    const cropQuery = query(
      collection(db, "crop_recommendations"),
      orderBy("timestamp", "desc")
    )
    const cropSnapshot = await getDocs(cropQuery)
    
    // Create a map of recommendations by soil reading ID
    const cropRecommendationsMap = new Map()
    cropSnapshot.docs.forEach(doc => {
      const data = doc.data()
      if (data.soilReadingId) {
        // If we already have a recommendation for this soil reading, only keep the one with higher success rate
        if (!cropRecommendationsMap.has(data.soilReadingId) || 
            cropRecommendationsMap.get(data.soilReadingId).successRate < data.successRate) {
          cropRecommendationsMap.set(data.soilReadingId, {
            crop: data.recommendedCrop,
            timestamp: data.timestamp,
            successRate: data.successRate
          })
        }
      }
    })

    // Process soil readings and match with recommendations
    const processedData = soilSnapshot.docs.map(doc => {
      const data = doc.data()
      
      // Handle soil reading timestamp
      let formattedDate = '--'
      let timestampSeconds = 0
      try {
        const timestamp = data.timestamp?.toDate?.() || 
                         (data.timestamp?.seconds ? new Date(data.timestamp.seconds * 1000) : new Date())
        // Replace date-fns format with native Date formatting
        formattedDate = formatDate(timestamp)
        timestampSeconds = data.timestamp?.seconds || Date.now() / 1000
      } catch (e) {
        console.error("Error formatting date:", e)
      }

      // Get matching recommendation
      const recommendation = cropRecommendationsMap.get(doc.id)
      let formattedRecDate = '--'
      
      if (recommendation?.timestamp) {
        try {
          // Handle string timestamp format: "2025-05-09T12:45:36.686088"
          const recTimestamp = recommendation.timestamp.includes('T') 
            ? new Date(recommendation.timestamp)
            : recommendation.timestamp?.toDate?.() || 
              (recommendation.timestamp?.seconds ? new Date(recommendation.timestamp.seconds * 1000) : null)

          if (recTimestamp) {
            // Replace date-fns format with native Date formatting
            formattedRecDate = formatDate(recTimestamp)
          }
        } catch (e) {
          console.error("Error formatting recommendation date:", e)
        }
      }

      // Format the predicted crop with success rate
      const predictedCropDisplay = recommendation?.crop && recommendation?.successRate
        ? `${recommendation.crop} (${Number(recommendation.successRate).toFixed(2)}%)`
        : '--'

      // Return processed data with soil moisture included
      return {
        date: formattedDate,
        timestamp: timestampSeconds,
        nitrogen: data.nitrogen !== undefined && data.nitrogen !== null ? Number(data.nitrogen).toFixed(2) : '--',
        phosphorus: data.phosphorus !== undefined && data.phosphorus !== null ? Number(data.phosphorus).toFixed(2) : '--',
        potassium: data.potassium !== undefined && data.potassium !== null ? Number(data.potassium).toFixed(2) : '--',
        ph: data.soilPh !== undefined && data.soilPh !== null ? Number(data.soilPh).toFixed(2) : '--',
        temperature: data.temperature !== undefined && data.temperature !== null ? Number(data.temperature).toFixed(2) : '--',
        humidity: data.humidity !== undefined && data.humidity !== null ? Number(data.humidity).toFixed(2) : '--',
        soilMoisture: data.soilMoisture !== undefined && data.soilMoisture !== null ? Number(data.soilMoisture).toFixed(2) : '--',
        predictedCrop: predictedCropDisplay,
        datePredicted: formattedRecDate
      }
    })

    // Sort by timestamp ascending
    processedData.sort((a, b) => a.timestamp - b.timestamp)
    
    // Simulate a minimum loading time for better UX (remove in production if not needed)
    setTimeout(() => {
      soilData.value = processedData
      isLoading.value = false
    }, 1500)
  } catch (error) {
    console.error("❌ Error fetching data:", error)
    isLoading.value = false
  }
}

// Add a custom date formatting function to replace date-fns
const formatDate = (date) => {
  if (!date) return '--'

  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  const day = date.getDate().toString().padStart(2, '0')
  const month = months[date.getMonth()]
  const year = date.getFullYear()
  const hours = date.getHours().toString().padStart(2, '0')
  const minutes = date.getMinutes().toString().padStart(2, '0')

  return `${month} ${day}, ${year} ${hours}:${minutes}`
}

// Initialize filters object
const filters = ref({
  nitrogen: { min: '', max: '' },
  phosphorus: { min: '', max: '' },
  potassium: { min: '', max: '' },
  ph: { min: '', max: '' },
  temperature: { min: '', max: '' },
  humidity: { min: '', max: '' },
  soilMoisture: { min: '', max: '' } // Added soil moisture filter
})

// Reactive state
const searchQuery = ref('')
const itemsPerPage = ref(20)
const currentPage = ref(1)
const activeDropdown = ref(null)
const sortKey = ref('date')
const sortDirection = ref('asc')
const activeFilters = ref({})

const filterFields = [
  { key: 'nitrogen', label: 'Nitrogen' },
  { key: 'phosphorus', label: 'Phosphorus' },
  { key: 'potassium', label: 'Potassium' },
  { key: 'ph', label: 'pH' },
  { key: 'temperature', label: 'Temperature' },
  { key: 'humidity', label: 'Humidity' },
  { key: 'soilMoisture', label: 'Soil Moisture' } // Added soil moisture filter field
]

const headers = [
  { key: 'date', label: 'Date' },
  { key: 'nitrogen', label: 'Nitrogen' },
  { key: 'phosphorus', label: 'Phosphorus' },
  { key: 'potassium', label: 'Potassium' },
  { key: 'ph', label: 'pH' },
  { key: 'temperature', label: 'Temperature' },
  { key: 'humidity', label: 'Humidity' },
  { key: 'soilMoisture', label: 'Soil Moisture' }, // Added soil moisture header
  { key: 'predictedCrop', label: 'Predicted Crop' },
  { key: 'datePredicted', label: 'Date Predicted' }
]

const exportFormats = ['csv', 'pdf', 'docs']

// Computed properties
const filteredData = computed(() => {
  let result = [...soilData.value]

  // Apply search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(row => {
      return Object.values(row).some(value => 
        String(value).toLowerCase().includes(query)
      )
    })
  }

  // Apply range filters
  Object.keys(activeFilters.value).forEach(key => {
    const { min, max } = activeFilters.value[key]
    if (min !== '' && max !== '') {
      result = result.filter(row => row[key] >= min && row[key] <= max)
    } else if (min !== '') {
      result = result.filter(row => row[key] >= min)
    } else if (max !== '') {
      result = result.filter(row => row[key] <= max)
    }
  })

  return result
})

const sortedData = computed(() => {
  if (!sortKey.value) return filteredData.value

  return [...filteredData.value].sort((a, b) => {
    let aValue = a[sortKey.value]
    let bValue = b[sortKey.value]
    
    // Handle empty values
    if (aValue === '' || aValue === undefined) aValue = sortDirection.value === 'asc' ? -Infinity : Infinity
    if (bValue === '' || bValue === undefined) bValue = sortDirection.value === 'asc' ? -Infinity : Infinity
    
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

const paginatedData = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage.value
  const endIndex = startIndex + itemsPerPage.value
  return sortedData.value.slice(startIndex, endIndex)
})

const totalPages = computed(() => {
  return Math.ceil(sortedData.value.length / itemsPerPage.value)
})

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

// Methods
const toggleDropdown = (dropdownName) => {
  if (activeDropdown.value === dropdownName) {
    activeDropdown.value = null
  } else {
    activeDropdown.value = dropdownName
  }
}

const handleClickOutside = (event) => {
  if (!event.target.closest('.relative')) {
    activeDropdown.value = null
  }
}

const performSearch = () => {
  currentPage.value = 1 // Reset to first page when searching
}

const applyFilters = () => {
  // Create a new object with only the filters that have values
  const newFilters = {}

  Object.keys(filters.value).forEach(key => {
    const min = parseFloat(filters.value[key].min)
    const max = parseFloat(filters.value[key].max)
    
    if (!isNaN(min) || !isNaN(max)) {
      newFilters[key] = {
        min: isNaN(min) ? '' : min,
        max: isNaN(max) ? '' : max
      }
    }
  })

  activeFilters.value = newFilters
  currentPage.value = 1 // Reset to first page when filtering
  activeDropdown.value = null // Close dropdown after applying
}

const setSortKey = (key) => {
  if (sortKey.value === key) {
    // Toggle direction if clicking the same column
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortDirection.value = 'asc' // Default to ascending for new column
  }
  activeDropdown.value = null // Close dropdown after sorting
}

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
  currentPage.value = 1 // Reset to first page when changing items per page
}

const goToPage = (page) => {
  if (typeof page === 'number') {
    currentPage.value = page
  }
}

const exportData = (format) => {
  // Get the data to export (all filtered and sorted data, not just current page)
  const dataToExport = sortedData.value

  if (format === 'csv') {
    exportAsCSV(dataToExport)
  } else if (format === 'pdf') {
    exportAsPDF(dataToExport)
  } else if (format === 'docs') {
    exportAsDocs(dataToExport)
  }

  activeDropdown.value = null // Close dropdown after exporting
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
  link.setAttribute('download', 'soil_analysis_data.csv')
  link.style.visibility = 'hidden'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

const exportAsPDF = (data) => {
  // In a real application, you would use a library like jsPDF
  alert('PDF export would be implemented with a library like jsPDF')
  console.log('Data to export as PDF:', data)
}

const exportAsDocs = (data) => {
  // In a real application, you would use a library to generate DOCS
  alert('DOCS export would be implemented with a library for document generation')
  console.log('Data to export as DOCS:', data)
}

// Watch for changes that should reset pagination
watch([searchQuery, activeFilters, itemsPerPage], () => {
  currentPage.value = 1
})

// Lifecycle hooks
onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  fetchSoilDataWithRecommendations()
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>
  
<style>
/* Core styles */
.relative {
  position: relative;
}

[v-show] {
  transition: opacity 0.2s;
}

.relative:hover {
  z-index: 50;
}

/* Remove all hover animations from the main container */
.main-container {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.bg-white {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.rounded-lg {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.shadow-lg {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.border {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.border-gray-100 {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.h-\[calc100vh-140px\] {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.flex {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.flex-col {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.bg-gradient-to-r {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.from-emerald-50 {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.to-white {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.from-white {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

.to-emerald-50 {
  transition: none !important;
  animation: none !important;
  transform: none !important;
}

/* Text styling for better readability */
* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Button styling - transition only colors not position */
button {
  transition: color 0.2s ease, background-color 0.2s ease, border-color 0.2s ease;
  transform: none !important;
}

/* Table styling */
table {
  table-layout: fixed;
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}

/* Fix table header and body alignment */
thead th, tbody td {
  box-sizing: border-box;
}

/* Responsive styles */
@media (max-width: 1200px) {
  th, td {
    padding-left: 0.75rem !important;
    padding-right: 0.75rem !important;
  }
}

@media (max-width: 992px) {
  th, td {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }
}

@media (max-width: 768px) {
  .overflow-x-auto {
    -webkit-overflow-scrolling: touch;
  }

  th, td {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
    font-size: 0.875rem;
  }

  th div, td div {
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}

@media (max-width: 640px) {
  .flex-col {
    row-gap: 0.5rem;
  }

  th, td {
    padding-left: 0.25rem !important;
    padding-right: 0.25rem !important;
    font-size: 0.75rem;
  }
}

@media (max-width: 480px) {
  table {
    font-size: 0.75rem;
  }

  th, td {
    padding-left: 0.25rem !important;
    padding-right: 0.25rem !important;
  }
}
</style>