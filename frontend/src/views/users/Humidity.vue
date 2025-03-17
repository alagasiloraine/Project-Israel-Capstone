<template>
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <main class="flex-1 flex flex-col h-screen pt-32">
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <div class="p-6">
            <!-- Header -->
            <div class="mb-6">
              <h1 class="text-2xl font-bold text-gray-900 mb-2">Humidity Data Table</h1>
              <div class="flex items-center text-sm text-gray-500">
                <span class="text-sky-600">Humidity</span>
                <ChevronRight class="h-4 w-4 mx-1" />
                <span>Data Table</span>
              </div>
            </div>

            <!-- Controls -->
            <div class="flex items-center gap-4 mb-6">
              <div class="relative flex-1">
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
                  Sort by {{ sortKey ? headers.find(h => h.key === sortKey)?.label : 'ID' }}
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

            <!-- Table -->
            <div class="overflow-x-auto">
              <table class="min-w-full divide-y divide-gray-200">
                <thead>
                  <tr>
                    <th v-for="header in headers" :key="header.key" class="px-6 py-3 text-left text-xs font-medium tracking-wider">
                      <div class="flex items-center justify-between cursor-pointer" @click="setSortKey(header.key)">
                        <span>{{ header.label }}</span>
                        <ArrowUpDown class="h-4 w-4 ml-1" :class="sortKey === header.key ? 'text-sky-600' : 'text-gray-400'" />
                      </div>
                    </th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="(row, index) in paginatedData" :key="index">
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.id }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm">
                      <span 
                        :class="[
                          'px-2 py-1 rounded-full text-sm font-medium',
                          row.humidity >= 70 ? 'bg-blue-100 text-blue-800' :
                          row.humidity >= 40 ? 'bg-yellow-100 text-yellow-800' :
                          'bg-red-100 text-red-800'
                        ]"
                      >
                        {{ row.humidity }}%
                      </span>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.date }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ row.time }}</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Enhanced Pagination -->
            <div class="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4 px-2">
              <div class="text-sm text-gray-600 flex items-center gap-2">
                <span class="hidden sm:inline">Showing</span>
                <select 
                  v-model="itemsPerPage" 
                  class="bg-white border border-gray-200 rounded-lg px-3 py-1.5 text-sm font-medium text-gray-700 hover:border-gray-300 focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-colors"
                  @change="updatePagination"
                >
                  <option value="10">10</option>
                  <option value="20">20</option>
                  <option value="50">50</option>
                </select>
                <span class="hidden sm:inline">entries per page</span>
                <span class="text-gray-400 mx-2">|</span>
                <span>
                  {{ (currentPage - 1) * itemsPerPage + 1 }} - {{ Math.min(currentPage * itemsPerPage, filteredData.length) }}
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
import { Search, Filter, Download, ChevronDown, ChevronRight, ChevronLeft, ArrowUpDown } from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'

// Headers definition
const headers = [
  { key: 'id', label: 'ID' },
  { key: 'humidity', label: 'HUMIDITY' },
  { key: 'date', label: 'DATE' },
  { key: 'time', label: 'TIME' }
]

// Data
const data = ref([
  { id: 1, humidity: 85, date: '2024-05-17', time: '18:58:33' },
  { id: 2, humidity: 45, date: '2024-05-17', time: '18:58:48' },
  { id: 3, humidity: 30, date: '2024-05-17', time: '18:59:24' },
  { id: 4, humidity: 75, date: '2024-05-17', time: '19:00:25' },
  { id: 5, humidity: 25, date: '2024-05-17', time: '19:01:25' },
  { id: 6, humidity: 90, date: '2024-05-17', time: '19:02:25' },
  { id: 7, humidity: 92, date: '2024-05-17', time: '19:03:25' },
  { id: 8, humidity: 88, date: '2024-05-17', time: '19:04:25' },
])

// Reactive state
const searchQuery = ref('')
const itemsPerPage = ref(10)
const currentPage = ref(1)
const activeDropdown = ref(null)
const sortKey = ref('id')
const sortDirection = ref('asc')
const activeFilters = ref({})

const filterFields = [
  { key: 'humidity', label: 'Humidity' }
]

const filters = ref({
  humidity: { min: '', max: '' }
})

const exportFormats = ['csv', 'pdf', 'excel']

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
  } else if (format === 'excel') {
    exportAsExcel(dataToExport)
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
  link.setAttribute('download', 'humidity_data.csv')
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
  // In a real application, you would use a library like SheetJS
  // For this example, we'll just show an alert
  alert('Excel export would be implemented with a library like SheetJS')
  console.log('Data to export as Excel:', data)
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
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Enhanced scrollbar styling with dark green color */
.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(20, 83, 45, 0.5) transparent;
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgba(20, 83, 45, 0.5);
  border-radius: 9999px;
  transition: background-color 200ms;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
  background-color: rgba(20, 83, 45, 0.7);
}

/* Add smooth transitions for all elements */
* {
  transition: color 200ms, background-color 200ms;
}
</style>