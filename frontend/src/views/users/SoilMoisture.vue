<template>
  <div class="min-h-screen bg-green-100 font-poppins">
    <Sidebar />
    <!-- Main Content -->
    <main class="min-h-screen bg-green-100">
      <!-- Fixed Navbar Space - matches navbar height -->
      <div class="h-[100px]"></div>
      
      <!-- Container Wrapper with increased spacing and animations -->
      <div class="w-full px-6 pt-14">
        <!-- Main Container with enhanced styling -->
        <div class="bg-white rounded-[12px] shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-200 h-[calc(100vh-180px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_8px_40px_rgb(0,0,0,0.06)]">
          <!-- Content Wrapper with improved padding -->
          <div class="p-8">
            <!-- Header Section -->
            <div class="mb-6">
              <h1 class="text-2xl font-bold text-gray-900 mb-2">Soil Moisture Data Table</h1>
              <div class="flex items-center text-sm text-gray-500">
                <span class="text-green-600">Soil Moisture</span>
                <ChevronRight class="h-4 w-4 mx-1" />
                <span>Data Table</span>
              </div>
            </div>

            <!-- Search Filter Bar -->
            <div class="mb-6">
              <SearchFilterBar />
            </div>

            <!-- Table Container with floating effect -->
            <div class="bg-white rounded-xl shadow-[0_4px_12px_rgba(0,0,0,0.1)] overflow-hidden border border-gray-200">
              <table class="w-full border-collapse">
                <thead>
                  <tr class="bg-gray-300 border-b border-gray-200">
                    <th 
                      v-for="header in headers" 
                      :key="header.key"
                      class="px-6 py-3 text-left text-sm font-medium text-gray-800 border-b border-r border-gray-300 bg-gray-100 hover:bg-gray-200/90 transition-colors duration-150 cursor-pointer relative"
                      @click="toggleSort(header.key)"
                    >
                      <div class="flex items-center justify-between">
                        <span class="uppercase text-gray-800">{{ header.label }}</span>
                        <div class="flex flex-col ml-2">
                          <ChevronUp 
                            class="h-4 w-4 -mb-1" 
                            :class="[
                              sortKey === header.key && sortDirection === 'asc' 
                                ? 'text-green-600' 
                                : 'text-gray-400'
                            ]"
                          />
                          <ChevronDown 
                            class="h-4 w-4" 
                            :class="[
                              sortKey === header.key && sortDirection === 'desc' 
                                ? 'text-green-600' 
                                : 'text-gray-400'
                            ]"
                          />
                        </div>
                      </div>
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                  <tr 
                    v-for="(row, index) in sortedData" 
                    :key="row.id"
                    class="hover:bg-gray-50 transition-colors duration-150"
                  >
                    <td class="px-6 py-3 text-sm font-medium text-gray-900 border-r border-gray-200">
                      {{ (currentPage - 1) * itemsPerPage + index + 1 }}
                    </td>
                    <td class="px-6 py-3 text-sm font-medium border-r border-gray-200">
                      <span 
                        :class="[
                          'px-2 py-1 rounded-full text-sm font-medium',
                          row.soilStatus === 'WET' ? 'bg-green-100 text-green-800' :
                          row.soilStatus === 'MEDIUM' ? 'bg-yellow-100 text-yellow-800' :
                          'bg-red-100 text-red-800'
                        ]"
                      >
                        {{ row.soilStatus }}
                      </span>
                    </td>
                    <td class="px-6 py-3 text-sm font-medium text-gray-900 border-r border-gray-200">
                      {{ row.soilMoisture }}
                    </td>
                    <td class="px-6 py-3 text-sm font-medium border-r border-gray-200">
                      <span 
                        :class="[
                          'px-2 py-1 rounded-full text-sm font-medium',
                          row.motorStatus === 'ON' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                        ]"
                      >
                        {{ row.motorStatus }}
                      </span>
                    </td>
                    <td class="px-6 py-3 text-sm font-medium text-gray-900 border-r border-gray-200">
                      {{ row.date }}
                    </td>
                    <td class="px-6 py-3 text-sm font-medium text-gray-900 border-r border-gray-200">
                      {{ row.time }}
                    </td>
                  </tr>
                </tbody>
              </table>

              <div class="p-4 border-t border-gray-200">
                <Pagination />
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
// Keep the existing script setup code unchanged
import { ref, computed } from 'vue'
import { Search, Download, ChevronRight, ChevronUp, ChevronDown } from 'lucide-vue-next'
import Pagination from '../layout/Pagination.vue'
import SearchFilterBar from './SearchFilterBar.vue'
import Sidebar from '../layout/Sidebar.vue'

const headers = [
  { key: 'id', label: 'Id' },
  { key: 'soilStatus', label: 'Soil Status' },
  { key: 'soilMoisture', label: 'Soil Moisture' },
  { key: 'motorStatus', label: 'Motor Status' },
  { key: 'date', label: 'Date' },
  { key: 'time', label: 'Time' }
]

const data = ref([
  { id: 1, soilStatus: 'WET', soilMoisture: 100, motorStatus: 'OFF', date: '2024-05-17', time: '18:58:33' },
  { id: 2, soilStatus: 'MEDIUM', soilMoisture: 33, motorStatus: 'OFF', date: '2024-05-17', time: '18:58:48' },
  { id: 3, soilStatus: 'MEDIUM', soilMoisture: 32, motorStatus: 'OFF', date: '2024-05-17', time: '18:59:24' },
  { id: 4, soilStatus: 'DRY', soilMoisture: 30, motorStatus: 'ON', date: '2024-05-17', time: '19:00:25' },
  { id: 5, soilStatus: 'WET', soilMoisture: 89, motorStatus: 'OFF', date: '2024-05-17', time: '19:01:10' },
  { id: 6, soilStatus: 'WET', soilMoisture: 95, motorStatus: 'OFF', date: '2024-05-17', time: '19:01:26' },
  { id: 7, soilStatus: 'WET', soilMoisture: 94, motorStatus: 'OFF', date: '2024-05-17', time: '19:01:57' },
  { id: 8, soilStatus: 'WET', soilMoisture: 94, motorStatus: 'OFF', date: '2024-05-17', time: '19:02:28' },
])

const currentPage = ref(1)
const itemsPerPage = ref(10)
const searchQuery = ref('')
const sortKey = ref('id')
const sortDirection = ref('asc')

const toggleSort = (key) => {
  if (sortKey.value === key) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortDirection.value = 'asc'
  }
}

const filteredData = computed(() => {
  return data.value.filter(item => {
    return Object.values(item).some(value => 
      value.toString().toLowerCase().includes(searchQuery.value.toLowerCase())
    )
  })
})

const sortedData = computed(() => {
  let result = [...filteredData.value]

  if (sortDirection.value && sortKey.value) {
    result.sort((a, b) => {
      const aVal = a[sortKey.value]
      const bVal = b[sortKey.value]
      
      if (sortDirection.value === 'asc') {
        return aVal > bVal ? 1 : -1
      } else {
        return aVal < bVal ? 1 : -1
      }
    })
  }

  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  
  return result.slice(start, end)
})

const totalPages = computed(() => 
  Math.ceil(filteredData.value.length / itemsPerPage.value)
)
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
