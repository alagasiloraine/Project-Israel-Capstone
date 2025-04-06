<template>
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <main class="flex-1 flex flex-col h-screen pt-32">
      <div class="flex-1 w-full px-4 sm:px-6 md:px:8 lg:px-10 overflow-hidden">
        <!-- Main container with curved edges on all corners -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] flex flex-col transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Fixed Header Section -->
          <div class="p-6 border-b border-gray-100">
            <!-- Header -->
            <div class="mb-6">
              <h1 class="text-2xl font-bold text-gray-900 mb-2">Soil Analysis Measurements</h1>
              <div class="flex items-center text-sm text-gray-500">
                <span class="text-green-600">Soil Analysis</span>
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

              <!-- Filter Button -->
              <div class="relative">
                <button 
                  @click.stop="toggleDropdown('filter')"
                  class="flex items-center gap-2 px-4 py-2 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50"
                >
                  <Filter class="h-4 w-4" />
                  Filter by Range
                  <ChevronDown class="h-4 w-4" :class="{ 'transform rotate-180': activeDropdown === 'filter' }" />
                </button>
                
                <div 
                  v-show="activeDropdown === 'filter'"
                  class="absolute right-0 mt-2 w-80 bg-white rounded-lg shadow-lg border border-gray-200 z-50"
                  @click.stop
                >
                  <div class="p-4 space-y-4">
                    <div v-for="field in filterFields" :key="field.key" class="space-y-2">
                      <label class="block text-sm font-medium text-gray-700">{{ field.label }}</label>
                      <div class="flex items-center gap-2">
                        <input
                          v-model="filters[field.key].min"
                          type="number"
                          placeholder="Min"
                          class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded-md focus:ring-2 focus:ring-green-500/20"
                        />
                        <span class="text-gray-400">-</span>
                        <input
                          v-model="filters[field.key].max"
                          type="number"
                          placeholder="Max"
                          class="w-full px-3 py-1.5 text-sm border border-gray-200 rounded-md focus:ring-2 focus:ring-green-500/20"
                        />
                      </div>
                    </div>
                    <button 
                      @click="applyFilters"
                      class="w-full px-4 py-2 bg-green-500 text-white rounded-lg text-sm font-medium hover:bg-green-600"
                    >
                      Apply Filters
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
                  Sort by {{ sortKey ? headers.find(h => h.key === sortKey)?.label : '' }}
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

          <!-- Table Section - No Scrolling -->
          <div class="flex-1 p-4 overflow-auto">
            <!-- Table container without scrolling -->
            <div class="w-full bg-white rounded-xl shadow-sm">
              <table class="min-w-full table-fixed">
                <thead>
                  <tr class="bg-gray-50 border-b border-gray-200">
                    <th class="w-[15%] px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Date
                    </th>
                    <th class="w-[10%] px-6 py-4 text-left text-xs font-medium uppercase tracking-wider">
                      <div class="text-green-600">Nitrogen</div>
                      <div class="text-gray-400 text-[10px]">(MG/KG)</div>
                    </th>
                    <th class="w-[10%] px-6 py-4 text-left text-xs font-medium uppercase tracking-wider">
                      <div class="text-blue-600">Phosphorus</div>
                      <div class="text-gray-400 text-[10px]">(MG/KG)</div>
                    </th>
                    <th class="w-[10%] px-6 py-4 text-left text-xs font-medium uppercase tracking-wider">
                      <div class="text-purple-600">Potassium</div>
                      <div class="text-gray-400 text-[10px]">(MG/KG)</div>
                    </th>
                    <th class="w-[8%] px-6 py-4 text-left text-xs font-medium uppercase tracking-wider">
                      <div class="text-orange-600">pH</div>
                      <div class="text-gray-400 text-[10px]">(LEVEL)</div>
                    </th>
                    <th class="w-[10%] px-6 py-4 text-left text-xs font-medium uppercase tracking-wider">
                      <div class="text-red-600">Temperature</div>
                      <div class="text-gray-400 text-[10px]">(°C)</div>
                    </th>
                    <th class="w-[8%] px-6 py-4 text-left text-xs font-medium uppercase tracking-wider">
                      <div class="text-gray-600">Humidity</div>
                      <div class="text-gray-400 text-[10px]">(%)</div>
                    </th>
                    <th class="w-[15%] px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Predicted Crop
                    </th>
                    <th class="w-[14%] px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Date Predicted
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                  <tr 
                    v-for="(row, index) in filteredAndSortedData" 
                    :key="index"
                    class="group transition-colors duration-150 hover:bg-gray-50"
                  >
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-600">{{ row.date }}</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-medium text-green-600 bg-green-50/30 px-2 py-1 rounded-md inline-block text-center w-[80px]">
                        {{ row.nitrogen }}
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-medium text-blue-600 bg-blue-50/30 px-2 py-1 rounded-md inline-block text-center w-[80px]">
                        {{ row.phosphorus }}
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-medium text-purple-600 bg-purple-50/30 px-2 py-1 rounded-md inline-block text-center w-[80px]">
                        {{ row.potassium }}
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-medium text-orange-600 bg-orange-50/30 px-2 py-1 rounded-md inline-block text-center w-[60px]">
                        {{ row.ph }}
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-medium text-red-600 bg-red-50/30 px-2 py-1 rounded-md inline-block text-center w-[80px]">
                        {{ row.temperature }}
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-medium text-gray-600 bg-gray-50 px-2 py-1 rounded-md inline-block text-center w-[60px]">
                        {{ row.humidity }}
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div v-if="row.predictedCrop" class="flex items-center">
                        <span class="text-sm text-gray-800 bg-emerald-50 px-3 py-1 rounded-full">
                          {{ row.predictedCrop }}
                          <span v-if="row.successRate" class="text-gray-500 text-xs ml-1">({{ row.successRate }})</span>
                        </span>
                      </div>
                      <div v-else class="text-sm text-gray-400">-</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                      {{ row.datePredicted || '-' }}
                    </td>
                  </tr>
                  <tr v-if="filteredAndSortedData.length === 0">
                    <td colspan="9" class="px-6 py-4 text-center text-sm text-gray-500">
                      No data found matching your criteria
                    </td>
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
                  <option value="5">5</option>
                  <option value="10">10</option>
                  <option value="20">20</option>
                  <option value="50">50</option>
                </select>
                <span class="hidden sm:inline">entries per page</span>
                <span class="text-gray-400 mx-2">|</span>
                <span>
                  {{ (currentPage - 1) * itemsPerPage + 1 }} - {{ Math.min(currentPage * itemsPerPage, sortedData.length) }}
                  <span class="text-gray-400">of</span>
                  {{ sortedData.length }}
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
import { Search, Filter, Download, ChevronDown, ChevronRight, ChevronLeft, ArrowUpDown } from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'

// Original data
const originalData = ref([
  {
    date: 'Nov 28, 2024 14:34:00',
    nitrogen: 78.29,
    phosphorus: 34.57,
    potassium: 72.47,
    ph: 5.50,
    temperature: 20.32,
    humidity: 46.70,
    predictedCrop: '',
    successRate: '',
    datePredicted: ''
  },
  {
    date: 'Nov 28, 2024 14:34:11',
    nitrogen: 127.97,
    phosphorus: 8.83,
    potassium: 105.09,
    ph: 5.90,
    temperature: 21.34,
    humidity: 49.64,
    predictedCrop: '',
    successRate: '',
    datePredicted: ''
  },
  {
    date: 'Nov 28, 2024 14:34:21',
    nitrogen: 74.64,
    phosphorus: 18.55,
    potassium: 145.24,
    ph: 7.18,
    temperature: 30.67,
    humidity: 72.06,
    predictedCrop: '',
    successRate: '',
    datePredicted: ''
  },
  {
    date: 'Nov 28, 2024 14:34:31',
    nitrogen: 96.01,
    phosphorus: 22.85,
    potassium: 87.04,
    ph: 7.22,
    temperature: 32.52,
    humidity: 76.68,
    predictedCrop: 'chickpea',
    successRate: '99.68%',
    datePredicted: 'Dec 09, 2024 06:23'
  }
])

// Add more sample data to demonstrate pagination
const generateMoreData = () => {
  const additionalData = []
  for (let i = 0; i < 20; i++) {
    const baseData = originalData.value[i % 4]
    additionalData.push({
      ...baseData,
      date: `Nov ${28 + Math.floor(i/4)}, 2024 ${14 + Math.floor(i/8)}:${34 + i}:${Math.floor(Math.random() * 60)}`,
      nitrogen: +(baseData.nitrogen * (0.9 + Math.random() * 0.2)).toFixed(2),
      phosphorus: +(baseData.phosphorus * (0.9 + Math.random() * 0.2)).toFixed(2),
      potassium: +(baseData.potassium * (0.9 + Math.random() * 0.2)).toFixed(2),
      ph: +(baseData.ph * (0.95 + Math.random() * 0.1)).toFixed(2),
      temperature: +(baseData.temperature * (0.95 + Math.random() * 0.1)).toFixed(2),
      humidity: +(baseData.humidity * (0.95 + Math.random() * 0.1)).toFixed(2),
    })
  }
  return [...originalData.value, ...additionalData]
}

// Working data copy with more entries to demonstrate pagination
const data = ref(generateMoreData())

// Initialize filters object
const filters = ref({
  nitrogen: { min: '', max: '' },
  phosphorus: { min: '', max: '' },
  potassium: { min: '', max: '' },
  ph: { min: '', max: '' },
  temperature: { min: '', max: '' },
  humidity: { min: '', max: '' }
})

// Reactive state
const searchQuery = ref('')
const itemsPerPage = ref(5) // Changed default from 6 to 5
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
  { key: 'humidity', label: 'Humidity' }
]

const headers = [
  { key: 'date', label: 'Date' },
  { key: 'nitrogen', label: 'Nitrogen' },
  { key: 'phosphorus', label: 'Phosphorus' },
  { key: 'potassium', label: 'Potassium' },
  { key: 'ph', label: 'pH' },
  { key: 'temperature', label: 'Temperature' },
  { key: 'humidity', label: 'Humidity' },
  { key: 'predictedCrop', label: 'Predicted Crop' },
  { key: 'datePredicted', label: 'Date Predicted' }
]

// Changed from 'excel' to 'docs'
const exportFormats = ['csv', 'pdf', 'docs']

// Computed properties
const filteredData = computed(() => {
  let result = [...data.value]
  
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

const filteredAndSortedData = computed(() => {
  return paginatedData.value
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
  } else if (format === 'docs') { // Changed from 'excel' to 'docs'
    exportAsDocs(dataToExport) // Changed function name
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
  // For this example, we'll just show an alert
  alert('PDF export would be implemented with a library like jsPDF')
  console.log('Data to export as PDF:', data)
}

// Changed from exportAsExcel to exportAsDocs
const exportAsDocs = (data) => {
  // In a real application, you would use a library to generate DOCS
  // For this example, we'll just show an alert
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
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style>
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