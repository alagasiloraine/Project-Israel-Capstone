<template>
    <div class="flex h-screen bg-gray-50">
      <Sidebar />
      
      <!-- Main Content -->
      <div class="flex-1 p-6 overflow-auto">
        <!-- Header Section -->
        <div class="mb-6">
          <h1 class="text-2xl font-bold text-gray-900 mb-2">Motor Control Data Table</h1>
          <div class="flex items-center text-sm text-gray-500">
            <span class="text-orange-600">Motor Control</span>
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
              class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
              v-model="searchQuery"
            />
            <Search class="h-5 w-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
          </div>
          <button class="p-2 rounded-lg hover:bg-gray-200 transition-colors">
            <Download class="h-5 w-5 text-orange-600" />
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
                >
                  <div class="flex items-center space-x-1">
                    <span>{{ header.label }}</span>
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
                <td class="px-6 py-4 whitespace-nowrap text-sm">
                  <span 
                    :class="[
                      'px-3 py-1 rounded-full text-sm font-medium',
                      row.motorControl === 'ON' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                    ]"
                  >
                    {{ row.motorControl }}
                  </span>
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
  import { Search, Download, ChevronRight } from 'lucide-vue-next'
  import Sidebar from './Sidebar.vue'
  
  const headers = [
    { key: 'id', label: 'Id' },
    { key: 'motorControl', label: 'Motor Control' },
    { key: 'date', label: 'Date' },
    { key: 'time', label: 'Time' }
  ]
  
  const data = ref([
    { id: 1, motorControl: 'ON', date: '2024-05-17', time: '18:58:33' },
    { id: 2, motorControl: 'OFF', date: '2024-05-17', time: '18:58:48' },
    { id: 3, motorControl: 'ON', date: '2024-05-17', time: '18:59:24' },
    { id: 4, motorControl: 'OFF', date: '2024-05-17', time: '19:00:25' },
  ])
  
  const searchQuery = ref('')
  
  const sortedData = computed(() => {
    return data.value.filter(item => {
      return Object.values(item).some(value => 
        value.toString().toLowerCase().includes(searchQuery.value.toLowerCase())
      )
    })
  })
  </script>