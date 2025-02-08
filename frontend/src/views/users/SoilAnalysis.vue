<template>
  <div class="flex h-screen bg-gray-50">
    <Sidebar />
    
    <!-- Main Content -->
    <div class="flex-1 overflow-auto bg-gradient-to-br from-green-50 to-emerald-50 p-8">
      <!-- Search Filter Bar -->
      <div class="mb-6">
        <SearchFilterBar />
      </div>

      <!-- Header Section -->
      <div class="mb-6">
        <h1 class="text-2xl font-bold text-gray-900 mb-2">Soil Analysis Measurements</h1>
        <div class="flex items-center text-sm text-gray-500">
          <span class="text-green-600">Soil Analysis</span>
          <ChevronRight class="h-4 w-4 mx-1" />
          <span>Data Table</span>
        </div>
      </div>

      <!-- Table Container -->
      <div class="bg-white rounded-xl shadow-lg overflow-hidden border border-gray-200">
        <div class="overflow-x-auto">
          <table class="w-full border-collapse">
            <thead>
              <tr>
                <th 
                  v-for="header in headers" 
                  :key="header.key"
                  class="px-6 py-3 text-left text-xs text-gray-500 uppercase tracking-wider border-b border-r border-gray-200 bg-gray-50 hover:bg-gray-100 transition-colors duration-150 cursor-pointer"
                  @click="toggleSort(header.key)"
                >
                  <div class="flex items-center justify-between">
                    <div>
                      <span :class="header.color">{{ header.label }}</span>
                      <span v-if="header.unit" class="text-gray-500 ml-1">({{ header.unit }})</span>
                    </div>
                    <div class="flex flex-col ml-2">
                      <ChevronUp 
                        class="h-4 w-4 -mb-1" 
                        :class="[
                          sortKey === header.key && sortDirection === 'asc' 
                            ? header.color 
                            : 'text-gray-400'
                        ]"
                      />
                      <ChevronDown 
                        class="h-4 w-4" 
                        :class="[
                          sortKey === header.key && sortDirection === 'desc' 
                            ? header.color 
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
                :key="index"
                class="hover:bg-gray-50 transition-colors duration-150"
              >
                <td class="px-6 py-3 text-sm text-gray-500 border-r border-gray-200">
                  {{ row.date }}
                </td>
                <td class="px-6 py-3 text-sm text-green-600 border-r border-gray-200">
                  {{ row.nitrogen.toFixed(2) }}
                </td>
                <td class="px-6 py-3 text-sm text-blue-600 border-r border-gray-200">
                  {{ row.phosphorus.toFixed(2) }}
                </td>
                <td class="px-6 py-3 text-sm text-purple-600 border-r border-gray-200">
                  {{ row.potassium.toFixed(2) }}
                </td>
                <td class="px-6 py-3 text-sm text-orange-600 border-r border-gray-200">
                  {{ row.ph.toFixed(2) }}
                </td>
                <td class="px-6 py-3 text-sm text-red-600 border-r border-gray-200">
                  {{ row.temperature.toFixed(2) }}
                </td>
                <td class="px-6 py-3 text-sm text-gray-900 border-r border-gray-200">
                  {{ row.humidity.toFixed(2) }}
                </td>
                <td class="px-6 py-3 text-sm text-gray-900 border-r border-gray-200">
                  {{ row.predictedCrop }}
                  <span v-if="row.successRate" class="text-gray-500 text-xs ml-1">({{ row.successRate }})</span>
                </td>
                <td class="px-6 py-3 text-sm text-gray-500 border-r border-gray-200">
                  {{ row.datePredicted || '-' }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Pagination -->
        <div class="mb-6">
          <Pagination />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ChevronRight, ChevronUp, ChevronDown } from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'
import SearchFilterBar from './SearchFilterBar.vue'
import Pagination from '../layout/Pagination.vue'

const headers = [
  { key: 'date', label: 'Date', color: 'text-gray-500' },
  { key: 'nitrogen', label: 'Nitrogen', unit: 'MG/KG', color: 'text-green-600' },
  { key: 'phosphorus', label: 'Phosphorus', unit: 'MG/KG', color: 'text-blue-600' },
  { key: 'potassium', label: 'Potassium', unit: 'MG/KG', color: 'text-purple-600' },
  { key: 'ph', label: 'pH', unit: 'LEVEL', color: 'text-orange-600' },
  { key: 'temperature', label: 'Temperature', unit: '°C', color: 'text-red-600' },
  { key: 'humidity', label: 'Humidity', unit: '%', color: 'text-gray-900' },
  { key: 'predictedCrop', label: 'Predicted Crop', color: 'text-gray-900' },
  { key: 'datePredicted', label: 'Date Predicted', color: 'text-gray-500' }
]

const data = ref([
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
  }
])

const sortKey = ref('date')
const sortDirection = ref('asc')

const toggleSort = (key) => {
  if (sortKey.value === key) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortDirection.value = 'asc'
  }
}

const sortedData = computed(() => {
  let result = [...data.value]

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
  
  return result
})
</script>

<style>
.overflow-x-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(156, 163, 175, 0.5) transparent;
}

.overflow-x-auto::-webkit-scrollbar {
  height: 6px;
}

.overflow-x-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-x-auto::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.5);
  border-radius: 3px;
}
</style>