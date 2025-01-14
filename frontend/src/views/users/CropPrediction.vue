<template>
    <div class="p-6 bg-white rounded-lg shadow-md">
      <h2 class="text-2xl font-bold mb-4">Soil Analysis</h2>
      <div class="space-y-4">
        <!-- Nitrogen -->
        <div class="space-y-2">
          <label class="flex items-center text-gray-700 font-medium">
            <Nitrogen class="w-5 h-5 text-blue-500 mr-2" />
            Nitrogen
          </label>
          <input
            v-model="formData.nitrogen"
            type="text"
            class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all"
            placeholder="10.00"
          />
        </div>
  
        <!-- Phosphorus -->
        <div class="space-y-2">
          <label class="flex items-center text-gray-700 font-medium">
            <Phosphorus class="w-5 h-5 text-yellow-500 mr-2" />
            Phosphorus
          </label>
          <input
            v-model="formData.phosphorus"
            type="text"
            class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-yellow-500 focus:ring-2 focus:ring-yellow-200 transition-all"
            placeholder="5.00"
          />
        </div>
  
        <!-- Potassium -->
        <div class="space-y-2">
          <label class="flex items-center text-gray-700 font-medium">
            <Potassium class="w-5 h-5 text-purple-500 mr-2" />
            Potassium
          </label>
          <input
            v-model="formData.potassium"
            type="text"
            class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-purple-500 focus:ring-2 focus:ring-purple-200 transition-all"
            placeholder="15.00"
          />
        </div>
  
        <!-- Soil pH Level -->
        <div class="space-y-2">
          <label class="flex items-center text-gray-700 font-medium">
            <Ph class="w-5 h-5 text-red-500 mr-2" />
            Soil pH Level
          </label>
          <input
            v-model="formData.ph"
            type="text"
            class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-red-500 focus:ring-2 focus:ring-red-200 transition-all"
            placeholder="6.5"
          />
        </div>
  
        <!-- Soil Moisture -->
        <div class="space-y-2">
          <label class="flex items-center text-gray-700 font-medium">
            <Droplets class="w-5 h-5 text-green-500 mr-2" />
            Soil Moisture
          </label>
          <input 
            v-model="formData.moisture"
            type="text"
            readonly
            class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
            placeholder="45.00"
          />
        </div>
  
        <!-- Temperature -->
        <div class="space-y-2">
          <label class="flex items-center text-gray-700 font-medium">
            <Temperature class="w-5 h-5 text-orange-500 mr-2" />
            Temperature
          </label>
          <input
            v-model="formData.temperature"
            type="text"
            class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-200 transition-all"
            placeholder="25.00"
          />
        </div>
  
        <!-- Humidity -->
        <div class="space-y-2">
          <label class="flex items-center text-gray-700 font-medium">
            <Humidity class="w-5 h-5 text-indigo-500 mr-2" />
            Humidity
          </label>
          <input
            v-model="formData.humidity"
            type="text"
            class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 transition-all"
            placeholder="75.00"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { Nitrogen, Phosphorus, Potassium, Ph, Temperature, Humidity, Droplets } from 'lucide-vue-next';
  
  const formData = ref({
    nitrogen: '',
    phosphorus: '',
    potassium: '',
    ph: '',
    moisture: '',
    temperature: '',
    humidity: ''
  })
  </script>
  
  