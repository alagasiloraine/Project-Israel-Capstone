<template>
    <div class="flex h-screen bg-gray-50">
      <Sidebar />
      
      <!-- Main Content -->
      <div class="flex-1 p-6 overflow-auto">
        <!-- Header Section -->
        <div class="mb-6">
          <h1 class="text-2xl font-bold text-gray-900 mb-2">Humidity Data Table</h1>
          <div class="flex items-center text-sm text-gray-500">
            <span class="text-purple-600">Humidity</span>
            <ChevronRight class="h-4 w-4 mx-1" />
            <span>Data Table</span>
          </div>
        </div>
  
        <!-- Search and Actions Bar -->
        <div class="flex justify-between items-center mb-6">
          <div class="relative w-80">
            <input
              type="text"
              placeholder="Search Data..."
              class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              v-model="searchQuery"
            />
            <Search class="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
          </div>
          <button class="p-2 rounded-lg hover:bg-gray-200 transition-colors">
            <Download class="h-5 w-5 text-purple-600" />
          </button>
        </div>
  
        <!-- Data Table -->
        <div class="bg-white rounded-lg shadow overflow-hidden">
          <table class="min-w-full">
            <thead>
              <tr class="bg-gray-200">
                <th 
                  v-for="header in headers" 
                  :key="header.key"
                  class="px-6 py-3 text-left text-sm font-medium text-gray-700 uppercase tracking-wider"
                  :class="{ 'cursor-pointer hover:bg-gray-300': header.key === 'humidity' }"
                  @click="header.key === 'humidity' ? sortByHumidity() : null"
                >
                  <div class="flex items-center space-x-1">
                    <span>{{ header.label }}</span>
                    <ArrowUp v-if="header.key === 'humidity'" class="h-4 w-4" />
                  </div>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr 
                v-for="(row, index) in sortedData" 
                :key="row.id"
                :class="index % 2 === 0 ? 'bg-white' : 'bg-gray-50'"
              >
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ index + 1 }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ row.humidity }}%
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ row.date }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {{ row.time }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { Search, Download, ChevronRight, ArrowUp } from 'lucide-vue-next'
  import Sidebar from './Sidebar.vue'
  
  const headers = [
    { key: 'id', label: 'Id' },
    { key: 'humidity', label: 'Humidity' },
    { key: 'date', label: 'Date' },
    { key: 'time', label: 'Time' }
  ]
  
  const data = ref([
    { id: 1, humidity: 65, date: '2024-05-17', time: '18:58:33' },
    { id: 2, humidity: 68, date: '2024-05-17', time: '18:58:48' },
    { id: 3, humidity: 70, date: '2024-05-17', time: '18:59:24' },
    { id: 4, humidity: 67, date: '2024-05-17', time: '19:00:25' },
  ])
  
  const searchQuery = ref('')
  const isHumiditySorted = ref(false)
  
  const sortByHumidity = () => {
    isHumiditySorted.value = true
  }
  
  const sortedData = computed(() => {
    let filteredData = data.value.filter(item => {
      return Object.values(item).some(value => 
        value.toString().toLowerCase().includes(searchQuery.value.toLowerCase())
      )
    })
  
    if (isHumiditySorted.value) {
      filteredData.sort((a, b) => a.humidity - b.humidity)
    }
  
    return filteredData
  })
  </script>