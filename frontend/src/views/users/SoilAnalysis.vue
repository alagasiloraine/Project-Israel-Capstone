<template>
    <div class="flex h-screen bg-gray-50">
      <Sidebar />
      
      <!-- Main Content -->
      <div class="flex-1 p-6 overflow-auto">
        <!-- Header Section -->
        <div class="mb-6">
          <h1 class="text-2xl font-bold text-gray-900 mb-2">Soil Analysis Measurements</h1>
        </div>
  
        <!-- Search and Actions Bar -->
        <!-- Removed Search and Actions Bar -->
  
        <!-- Data Table -->
        <div class="bg-white rounded-lg shadow overflow-hidden">
          <div class="overflow-x-auto">
            <table class="min-w-full">
              <thead>
                <tr class="bg-gray-50 border-b border-gray-200">
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Date
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium tracking-wider">
                    <span class="text-green-500">NITROGEN</span>
                    <span class="text-gray-500">(MG/KG)</span>
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium tracking-wider">
                    <span class="text-blue-500">PHOSPHORUS</span>
                    <span class="text-gray-500">(MG/KG)</span>
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium tracking-wider">
                    <span class="text-purple-500">POTASSIUM</span>
                    <span class="text-gray-500">(MG/KG)</span>
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium tracking-wider">
                    <span class="text-orange-500">PH</span>
                    <span class="text-gray-500">LEVEL</span>
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium tracking-wider">
                    <span class="text-red-500">TEMPERATURE</span>
                    <span class="text-gray-500">(°C)</span>
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium tracking-wider">
                    <span class="text-gray-900">HUMIDITY</span>
                    <span class="text-gray-500">(%)</span>
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Predicted Crop<br/>(Highest Success Rate)
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Date Predicted
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr 
                  v-for="(row, index) in data" 
                  :key="index"
                  :class="index % 2 === 0 ? 'bg-white' : 'bg-gray-50'"
                >
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ row.date }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-medium">
                    {{ row.nitrogen.toFixed(2) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-blue-600 font-medium">
                    {{ row.phosphorus.toFixed(2) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-purple-600 font-medium">
                    {{ row.potassium.toFixed(2) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-orange-500 font-medium">
                    {{ row.ph.toFixed(2) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-red-500 font-medium">
                    {{ row.temperature.toFixed(2) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-medium">
                    {{ row.humidity.toFixed(2) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                    {{ row.predictedCrop }}
                    <span class="text-gray-500">({{ row.successRate }})</span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ row.datePredicted }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import Sidebar from './Sidebar.vue'
  
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
  </script>
  
  <style>
  /* Add custom scrollbar styling */
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