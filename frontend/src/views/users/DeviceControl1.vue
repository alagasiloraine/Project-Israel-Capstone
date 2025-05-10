<template>
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen pt-32">
      <!-- Container Wrapper with proper spacing -->
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Main Container with adjusted width -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Title Section with breadcrumb navigation -->
          <div class="p-6 pb-0">
            <h1 class="text-2xl font-bold text-gray-800 mb-2">Device Control</h1>
            <div class="flex items-center text-sm text-gray-500">
              <span class="text-green-600">Device Setup</span>
              <ChevronRight class="h-4 w-4 mx-1" />
              <span>Overview</span>
            </div>
          </div>
          
          <!-- Content Wrapper -->
          <div class="p-6 md:p-8">
            
            <!-- Environmental Controls Section -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
              <!-- Temperature Control Card -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex items-center justify-between mb-5">
                  <div class="flex items-center gap-2">
                    <div class="text-red-500">
                      <Thermometer class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Temperature</h2>
                  </div>
                  <div class="text-xs text-gray-500">
                    Ideal: 10-40°C
                  </div>
                </div>
                
                <!-- Temperature Value Display -->
                <div class="flex items-center justify-center mb-6">
                  <div class="relative w-32 h-32">
                    <svg class="w-full h-full -rotate-90" viewBox="0 0 100 100">
                      <circle cx="50" cy="50" r="45" fill="none" stroke="#f1f5f9" stroke-width="10" />
                      <circle 
                        cx="50" 
                        cy="50" 
                        r="45" 
                        fill="none" 
                        :stroke="getTemperatureColor" 
                        stroke-width="10" 
                        stroke-linecap="round"
                        :stroke-dasharray="circumference"
                        :stroke-dashoffset="getTemperatureRangeDashOffset"
                      />
                    </svg>
                    <div class="absolute inset-0 flex flex-col items-center justify-center">
                      <span class="text-3xl font-bold" :class="getTemperatureTextColor">{{ temperatureRange }}°</span>
                      <span class="text-xs text-gray-500">Celsius</span>
                    </div>
                  </div>
                </div>
                
                <!-- Temperature Slider - Disabled for manual adjustment -->
                <div class="mb-6">
                  <div class="flex justify-between mb-1">
                    <span class="text-sm font-medium text-gray-500">10°</span>
                    <span class="text-sm font-medium text-gray-500">50°</span>
                  </div>
                  <div class="relative h-4 flex items-center">
                    <div class="absolute inset-x-0 h-2 top-1/2 -translate-y-1/2 rounded-full bg-gradient-to-r from-blue-500 via-green-500 to-red-500"></div>
                    <!-- Slider visualization - not interactive -->
                    <div 
                      class="absolute h-4 top-0 left-0 pointer-events-none"
                      :style="{ width: `${((minTemperature - 10) / 40) * 100}%` }"
                    ></div>
                    <div 
                      class="absolute h-4 top-0 right-0 pointer-events-none"
                      :style="{ width: `${((50 - maxTemperature) / 40) * 100}%` }"
                    ></div>
                    <!-- Slider thumb visualization -->
                    <div 
                      class="absolute w-5 h-5 bg-white rounded-full border-2 border-green-500 shadow-md top-1/2 -translate-y-1/2 -translate-x-1/2 pointer-events-none"
                      :style="{ left: `${((minTemperature - 10) / 40) * 100}%` }"
                    ></div>
                    <div 
                      class="absolute w-5 h-5 bg-white rounded-full border-2 border-green-500 shadow-md top-1/2 -translate-y-1/2 -translate-x-1/2 pointer-events-none"
                      :style="{ left: `${((maxTemperature - 10) / 40) * 100}%` }"
                    ></div>
                  </div>
                </div>
                
                <!-- Temperature Range Controls -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center bg-gray-50 rounded-lg overflow-hidden shadow-sm">
                      <button 
                        @click="decrementMinTemperature" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="minTemperature <= 10"
                        :class="{ 'opacity-50 cursor-not-allowed': minTemperature <= 10 }"
                      >
                        <Minus class="w-3.5 h-3.5" />
                      </button>
                      <div class="relative w-16 h-8">
                        <input 
                          type="number" 
                          v-model.number="minTemperature" 
                          min="10"
                          max="49"
                          class="w-full h-full text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0 pr-6"
                          @change="validateMinTemperature"
                          :style="{ color: getTemperatureInputColor(minTemperature) }"
                        />
                        <span class="absolute right-2 top-1/2 transform -translate-y-1/2 text-xs text-gray-400">°C</span>
                      </div>
                      <button 
                        @click="incrementMinTemperature" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="minTemperature >= maxTemperature - 1"
                        :class="{ 'opacity-50 cursor-not-allowed': minTemperature >= maxTemperature - 1 }"
                      >
                        <Plus class="w-3.5 h-3.5" />
                      </button>
                    </div>
                    
                    <span class="text-gray-400 text-xs">to</span>
                    
                    <div class="flex items-center bg-gray-50 rounded-lg overflow-hidden shadow-sm">
                      <button 
                        @click="decrementMaxTemperature" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="maxTemperature <= minTemperature + 1"
                        :class="{ 'opacity-50 cursor-not-allowed': maxTemperature <= minTemperature + 1 }"
                      >
                        <Minus class="w-3.5 h-3.5" />
                      </button>
                      <div class="relative w-16 h-8">
                        <input 
                          type="number" 
                          v-model.number="maxTemperature" 
                          min="11"
                          max="50"
                          class="w-full h-full text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0 pr-6"
                          @change="validateMaxTemperature"
                          :style="{ color: getTemperatureInputColor(maxTemperature) }"
                        />
                        <span class="absolute right-2 top-1/2 transform -translate-y-1/2 text-xs text-gray-400">°C</span>
                      </div>
                      <button 
                        @click="incrementMaxTemperature" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="maxTemperature >= 50"
                        :class="{ 'opacity-50 cursor-not-allowed': maxTemperature >= 50 }"
                      >
                        <Plus class="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </div>
                  <div class="text-xs px-3 py-1 rounded-full shadow-sm" :class="getTemperatureStatusClass">
                    {{ getTemperatureStatus }}
                  </div>
                </div>
              </div>
              
              <!-- Humidity Control Card -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex items-center justify-between mb-5">
                  <div class="flex items-center gap-2">
                    <div class="text-blue-500">
                      <Droplets class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Humidity</h2>
                  </div>
                  <div class="text-xs text-gray-500">
                    Ideal: 40-80%
                  </div>
                </div>
                
                <!-- Humidity Value Display -->
                <div class="flex items-center justify-center mb-6">
                  <div class="relative w-32 h-32">
                    <svg class="w-full h-full -rotate-90" viewBox="0 0 100 100">
                      <circle cx="50" cy="50" r="45" fill="none" stroke="#f1f5f9" stroke-width="10" />
                      <circle 
                        cx="50" 
                        cy="50" 
                        r="45" 
                        fill="none" 
                        :stroke="getHumidityColor" 
                        stroke-width="10" 
                        stroke-linecap="round"
                        :stroke-dasharray="circumference"
                        :stroke-dashoffset="getHumidityRangeDashOffset"
                      />
                    </svg>
                    <div class="absolute inset-0 flex flex-col items-center justify-center">
                      <span class="text-3xl font-bold" :class="getHumidityTextColor">{{ humidityRange }}%</span>
                      <span class="text-xs text-gray-500">Relative</span>
                    </div>
                  </div>
                </div>
                
                <!-- Humidity Slider - Disabled for manual adjustment -->
                <div class="mb-6">
                  <div class="flex justify-between mb-1">
                    <span class="text-sm font-medium text-gray-500">1%</span>
                    <span class="text-sm font-medium text-gray-500">100%</span>
                  </div>
                  <div class="relative h-4 flex items-center">
                    <div class="absolute inset-x-0 h-2 top-1/2 -translate-y-1/2 rounded-full bg-gradient-to-r from-amber-500 via-green-500 to-blue-500"></div>
                    <!-- Slider visualization - not interactive -->
                    <div 
                      class="absolute h-4 top-0 left-0 pointer-events-none"
                      :style="{ width: `${((minHumidity - 1) / 99) * 100}%` }"
                    ></div>
                    <div 
                      class="absolute h-4 top-0 right-0 pointer-events-none"
                      :style="{ width: `${((100 - maxHumidity) / 99) * 100}%` }"
                    ></div>
                    <!-- Slider thumb visualization -->
                    <div 
                      class="absolute w-5 h-5 bg-white rounded-full border-2 border-green-500 shadow-md top-1/2 -translate-y-1/2 -translate-x-1/2 pointer-events-none"
                      :style="{ left: `${((minHumidity - 1) / 99) * 100}%` }"
                    ></div>
                    <div 
                      class="absolute w-5 h-5 bg-white rounded-full border-2 border-green-500 shadow-md top-1/2 -translate-y-1/2 -translate-x-1/2 pointer-events-none"
                      :style="{ left: `${((maxHumidity - 1) / 99) * 100}%` }"
                    ></div>
                  </div>
                </div>
                
                <!-- Humidity Range Controls -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center bg-gray-50 rounded-lg overflow-hidden shadow-sm">
                      <button 
                        @click="decrementMinHumidity" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="minHumidity <= 1"
                        :class="{ 'opacity-50 cursor-not-allowed': minHumidity <= 1 }"
                      >
                        <Minus class="w-3.5 h-3.5" />
                      </button>
                      <div class="relative w-16 h-8">
                        <input 
                          type="number" 
                          v-model.number="minHumidity" 
                          min="1"
                          max="99"
                          class="w-full h-full text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0 pr-6"
                          @change="validateMinHumidity"
                          :style="{ color: getHumidityInputColor(minHumidity) }"
                        />
                        <span class="absolute right-2 top-1/2 transform -translate-y-1/2 text-xs text-gray-400">%</span>
                      </div>
                      <button 
                        @click="incrementMinHumidity" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="minHumidity >= maxHumidity - 1"
                        :class="{ 'opacity-50 cursor-not-allowed': minHumidity >= maxHumidity - 1 }"
                      >
                        <Plus class="w-3.5 h-3.5" />
                      </button>
                    </div>
                    
                    <span class="text-gray-400 text-xs">to</span>
                    
                    <div class="flex items-center bg-gray-50 rounded-lg overflow-hidden shadow-sm">
                      <button 
                        @click="decrementMaxHumidity" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="maxHumidity <= minHumidity + 1"
                        :class="{ 'opacity-50 cursor-not-allowed': maxHumidity <= minHumidity + 1 }"
                      >
                        <Minus class="w-3.5 h-3.5" />
                      </button>
                      <div class="relative w-16 h-8">
                        <input 
                          type="number" 
                          v-model.number="maxHumidity" 
                          min="2"
                          max="100"
                          class="w-full h-full text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0 pr-6"
                          @change="validateMaxHumidity"
                          :style="{ color: getHumidityInputColor(maxHumidity) }"
                        />
                        <span class="absolute right-2 top-1/2 transform -translate-y-1/2 text-xs text-gray-400">%</span>
                      </div>
                      <button 
                        @click="incrementMaxHumidity" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="maxHumidity >= 100"
                        :class="{ 'opacity-50 cursor-not-allowed': maxHumidity >= 100 }"
                      >
                        <Plus class="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </div>
                  <div class="text-xs px-3 py-1 rounded-full shadow-sm" :class="getHumidityStatusClass">
                    {{ getHumidityStatus }}
                  </div>
                </div>
              </div>
              
              <!-- Soil Moisture Control Card -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex items-center justify-between mb-5">
                  <div class="flex items-center gap-2">
                    <div class="text-emerald-500">
                      <Waves class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Soil Moisture</h2>
                  </div>
                  <div class="text-xs text-gray-500">
                    Ideal: 30-70%
                  </div>
                </div>
                
                <!-- Soil Moisture Value Display -->
                <div class="flex items-center justify-center mb-6">
                  <div class="relative w-32 h-32">
                    <svg class="w-full h-full -rotate-90" viewBox="0 0 100 100">
                      <circle cx="50" cy="50" r="45" fill="none" stroke="#f1f5f9" stroke-width="10" />
                      <circle 
                        cx="50" 
                        cy="50" 
                        r="45" 
                        fill="none" 
                        :stroke="getSoilMoistureColor" 
                        stroke-width="10" 
                        stroke-linecap="round"
                        :stroke-dasharray="circumference"
                        :stroke-dashoffset="getSoilMoistureRangeDashOffset"
                      />
                    </svg>
                    <div class="absolute inset-0 flex flex-col items-center justify-center">
                      <span class="text-3xl font-bold" :class="getSoilMoistureTextColor">{{ soilMoistureRange }}%</span>
                      <span class="text-xs text-gray-500">Moisture</span>
                    </div>
                  </div>
                </div>
                
                <!-- Soil Moisture Slider - Disabled for manual adjustment -->
                <div class="mb-6">
                  <div class="flex justify-between mb-1">
                    <span class="text-sm font-medium text-gray-500">1%</span>
                    <span class="text-sm font-medium text-gray-500">100%</span>
                  </div>
                  <div class="relative h-4 flex items-center">
                    <div class="absolute inset-x-0 h-2 top-1/2 -translate-y-1/2 rounded-full bg-gradient-to-r from-amber-500 via-green-500 to-blue-500"></div>
                    <!-- Slider visualization - not interactive -->
                    <div 
                      class="absolute h-4 top-0 left-0 pointer-events-none"
                      :style="{ width: `${((minSoilMoisture - 1) / 99) * 100}%` }"
                    ></div>
                    <div 
                      class="absolute h-4 top-0 right-0 pointer-events-none"
                      :style="{ width: `${((100 - maxSoilMoisture) / 99) * 100}%` }"
                    ></div>
                    <!-- Slider thumb visualization -->
                    <div 
                      class="absolute w-5 h-5 bg-white rounded-full border-2 border-green-500 shadow-md top-1/2 -translate-y-1/2 -translate-x-1/2 pointer-events-none"
                      :style="{ left: `${((minSoilMoisture - 1) / 99) * 100}%` }"
                    ></div>
                    <div 
                      class="absolute w-5 h-5 bg-white rounded-full border-2 border-green-500 shadow-md top-1/2 -translate-y-1/2 -translate-x-1/2 pointer-events-none"
                      :style="{ left: `${((maxSoilMoisture - 1) / 99) * 100}%` }"
                    ></div>
                  </div>
                </div>
                
                <!-- Soil Moisture Range Controls -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center bg-gray-50 rounded-lg overflow-hidden shadow-sm">
                      <button 
                        @click="decrementMinSoilMoisture" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="minSoilMoisture <= 1"
                        :class="{ 'opacity-50 cursor-not-allowed': minSoilMoisture <= 1 }"
                      >
                        <Minus class="w-3.5 h-3.5" />
                      </button>
                      <div class="relative w-16 h-8">
                        <input 
                          type="number" 
                          v-model.number="minSoilMoisture" 
                          min="1"
                          max="99"
                          class="w-full h-full text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0 pr-6"
                          @change="validateMinSoilMoisture"
                          :style="{ color: getSoilMoistureInputColor(minSoilMoisture) }"
                        />
                        <span class="absolute right-2 top-1/2 transform -translate-y-1/2 text-xs text-gray-400">%</span>
                      </div>
                      <button 
                        @click="incrementMinSoilMoisture" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="minSoilMoisture >= maxSoilMoisture - 1"
                        :class="{ 'opacity-50 cursor-not-allowed': minSoilMoisture >= maxSoilMoisture - 1 }"
                      >
                        <Plus class="w-3.5 h-3.5" />
                      </button>
                    </div>
                    
                    <span class="text-gray-400 text-xs">to</span>
                    
                    <div class="flex items-center bg-gray-50 rounded-lg overflow-hidden shadow-sm">
                      <button 
                        @click="decrementMaxSoilMoisture" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="maxSoilMoisture <= minSoilMoisture + 1"
                        :class="{ 'opacity-50 cursor-not-allowed': maxSoilMoisture <= minSoilMoisture + 1 }"
                      >
                        <Minus class="w-3.5 h-3.5" />
                      </button>
                      <div class="relative w-16 h-8">
                        <input 
                          type="number" 
                          v-model.number="maxSoilMoisture" 
                          min="2"
                          max="100"
                          class="w-full h-full text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0 pr-6"
                          @change="validateMaxSoilMoisture"
                          :style="{ color: getSoilMoistureInputColor(maxSoilMoisture) }"
                        />
                        <span class="absolute right-2 top-1/2 transform -translate-y-1/2 text-xs text-gray-400">%</span>
                      </div>
                      <button 
                        @click="incrementMaxSoilMoisture" 
                        class="w-8 h-8 flex items-center justify-center text-gray-500 hover:bg-gray-100 transition-colors"
                        :disabled="maxSoilMoisture >= 100"
                        :class="{ 'opacity-50 cursor-not-allowed': maxSoilMoisture >= 100 }"
                      >
                        <Plus class="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </div>
                  <div class="text-xs px-3 py-1 rounded-full shadow-sm" :class="getSoilMoistureStatusClass">
                    {{ getSoilMoistureStatus }}
                  </div>
                </div>
              </div>
            </div>
            
            <!-- System Controls Section -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <!-- Motor Control Card - Left Position -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex items-center justify-between mb-6">
                  <div class="flex items-center gap-2">
                    <div class="text-purple-500">
                      <Droplet class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Motor Control</h2>
                  </div>
                </div>
                
                <!-- Motor Status and Toggle - Redesigned to be more minimalist -->
                <div class="mt-6">
                  <div class="flex items-center justify-between mb-4">
                    <span class="text-sm font-medium text-gray-700">Motor Status</span>
                    <div class="flex items-center gap-2">
                      <div class="w-2.5 h-2.5 rounded-full" :class="waterPumpActive ? 'bg-green-500' : 'bg-gray-300'"></div>
                      <span class="text-xs font-medium tracking-wider" :class="waterPumpActive ? 'text-green-500' : 'text-gray-400'">
                        {{ waterPumpActive ? 'ACTIVE' : 'INACTIVE' }}
                      </span>
                    </div>
                  </div>
                  
                  <!-- Modern Minimalist Toggle Switch - Fixed to work properly -->
                  <div class="relative h-12 mb-6 overflow-hidden rounded-full">
                    <!-- Full toggle container -->
                    <div class="flex w-full h-full">
                      <!-- OFF side - Make it clickable -->
                      <button 
                        @click="setWaterPumpActive(false)" 
                        class="flex items-center justify-center w-1/2 transition-colors duration-300 ease-in-out focus:outline-none"
                        :class="!waterPumpActive ? 'bg-gray-200' : 'bg-gray-200 opacity-70'"
                      >
                        <span class="text-sm font-medium text-gray-700">OFF</span>
                      </button>
                      
                      <!-- ON side - Make it clickable -->
                      <button 
                        @click="setWaterPumpActive(true)" 
                        class="flex items-center justify-center w-1/2 transition-colors duration-300 ease-in-out focus:outline-none"
                        :class="waterPumpActive ? 'bg-green-500 text-white' : 'bg-gray-200 opacity-70'"
                      >
                        <span class="text-sm font-medium" :class="waterPumpActive ? 'text-white' : 'text-gray-700'">ON</span>
                      </button>
                    </div>
                  </div>
                  
                  <!-- Motor Activity History - New section -->
                  <div class="mt-6 space-y-3">
                    <h3 class="text-sm font-medium text-gray-700">Recent Activity</h3>
                    <div class="space-y-2">
                      <div class="flex items-center justify-between bg-gray-50 rounded-lg p-3">
                        <div class="flex items-center gap-2">
                          <div class="w-2 h-2 rounded-full bg-green-500"></div>
                          <span class="text-xs text-gray-600">Today, 09:15 AM</span>
                        </div>
                        <span class="text-xs font-medium text-green-600">Turned ON</span>
                      </div>
                      <div class="flex items-center justify-between bg-gray-50 rounded-lg p-3">
                        <div class="flex items-center gap-2">
                          <div class="w-2 h-2 rounded-full bg-gray-400"></div>
                          <span class="text-xs text-gray-600">Today, 07:30 AM</span>
                        </div>
                        <span class="text-xs font-medium text-gray-600">Turned OFF</span>
                      </div>
                      <div class="flex items-center justify-between bg-gray-50 rounded-lg p-3">
                        <div class="flex items-center gap-2">
                          <div class="w-2 h-2 rounded-full bg-green-500"></div>
                          <span class="text-xs text-gray-600">Yesterday, 06:30 PM</span>
                        </div>
                        <span class="text-xs font-medium text-green-600">Turned ON</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Watering Schedule Card - Now in the Middle Position -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex items-center justify-between mb-5">
                  <div class="flex items-center gap-2">
                    <div class="text-green-500">
                      <Clock class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Watering Schedule</h2>
                  </div>
                  <div class="flex items-center">
                    <span class="text-xs text-gray-500 mr-2">Mode:</span>
                    <select 
                      v-model="wateringMode" 
                      class="text-xs bg-gray-50 border border-gray-200 rounded-md px-3 py-1 focus:outline-none focus:ring-1 focus:ring-green-500"
                      :disabled="!isEditingSchedule"
                    >
                      <option value="weekly">Weekly</option>
                      <option value="daily">Daily</option>
                      <option value="custom">Custom</option>
                    </select>
                  </div>
                </div>
                
                <!-- Next Scheduled Watering - Moved from Motor Control -->
                <div class="mb-5 bg-green-50 rounded-lg p-3 flex items-center justify-between">
                  <div class="flex items-center gap-2">
                    <CalendarClock class="w-4 h-4 text-green-600" />
                    <span class="text-xs text-gray-600">Next scheduled watering</span>
                  </div>
                  <span class="text-sm font-medium text-green-700">{{ nextWateringTime }}</span>
                </div>
                
                <!-- Weekly Schedule - Updated with 3-letter day names -->
                <div v-if="wateringMode === 'weekly'" class="mb-4">
                  <div class="grid grid-cols-7 gap-1.5">
                    <button 
                      v-for="(day, index) in weekDays" 
                      :key="day"
                      @click="toggleWateringDay(index)"
                      :disabled="!isEditingSchedule"
                      :class="[
                        'py-1.5 rounded-md transition-colors text-xs font-medium',
                        wateringDays[index] ? 'bg-green-500 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200',
                        !isEditingSchedule ? 'opacity-60 cursor-not-allowed' : ''
                      ]"
                    >
                      {{ day.substring(0, 3) }}
                    </button>
                  </div>
                </div>
                
                <!-- Daily Schedule -->
                <div v-if="wateringMode === 'daily' || wateringMode === 'weekly'" class="space-y-4 mb-4">
                  <div class="flex items-center justify-between">
                    <span class="text-sm text-gray-600">Time of day</span>
                    <div class="flex items-center">
                      <div class="bg-gray-50 rounded-lg px-3 py-1.5">
                        <input 
                          type="text" 
                          v-model="formattedHour" 
                          class="w-8 text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0"
                          @blur="validateHour"
                          :disabled="!isEditingSchedule"
                          :class="!isEditingSchedule ? 'opacity-60 cursor-not-allowed' : ''"
                        />
                        <span class="text-gray-400 mx-1">:</span>
                        <input 
                          type="text" 
                          v-model="formattedMinute" 
                          class="w-8 text-center bg-transparent border-0 text-sm focus:outline-none focus:ring-0"
                          @blur="validateMinute"
                          :disabled="!isEditingSchedule"
                          :class="!isEditingSchedule ? 'opacity-60 cursor-not-allowed' : ''"
                        />
                      </div>
                    </div>
                  </div>
                  
                  <div class="flex items-center justify-between">
                    <span class="text-sm text-gray-600">Duration</span>
                    <div class="flex items-center gap-2">
                      <input 
                        type="number" 
                        v-model.number="wateringDuration"
                        min="1"
                        max="120"
                        class="w-16 bg-gray-50 rounded-lg px-3 py-1.5 text-center border-0 text-sm focus:outline-none focus:ring-0"
                        :disabled="!isEditingSchedule"
                        :class="!isEditingSchedule ? 'opacity-60 cursor-not-allowed' : ''"
                      />
                      <span class="text-sm text-gray-500">min</span>
                    </div>
                  </div>
                </div>
                
                <!-- Custom Schedule -->
                <div v-if="wateringMode === 'custom'" class="space-y-4 mb-4">
                  <div class="flex items-center justify-between">
                    <span class="text-sm text-gray-600">Interval</span>
                    <div class="flex items-center gap-2">
                      <input 
                        type="number" 
                        v-model.number="wateringInterval"
                        min="1"
                        max="30"
                        class="w-16 bg-gray-50 rounded-lg px-3 py-1.5 text-center border-0 text-sm focus:outline-none focus:ring-0"
                        :disabled="!isEditingSchedule"
                        :class="!isEditingSchedule ? 'opacity-60 cursor-not-allowed' : ''"
                      />
                      <select 
                        v-model="wateringIntervalUnit" 
                        class="bg-gray-50 rounded-lg border-0 text-sm text-gray-500 focus:outline-none focus:ring-0 px-2 py-1.5"
                        :disabled="!isEditingSchedule"
                        :class="!isEditingSchedule ? 'opacity-60 cursor-not-allowed' : ''"
                      >
                        <option value="hours">hours</option>
                        <option value="days">days</option>
                      </select>
                    </div>
                  </div>
                  
                  <div class="flex items-center justify-between">
                    <span class="text-sm text-gray-600">Duration</span>
                    <div class="flex items-center gap-2">
                      <input 
                        type="number" 
                        v-model.number="wateringDuration"
                        min="1"
                        max="120"
                        class="w-16 bg-gray-50 rounded-lg px-3 py-1.5 text-center border-0 text-sm focus:outline-none focus:ring-0"
                        :disabled="!isEditingSchedule"
                        :class="!isEditingSchedule ? 'opacity-60 cursor-not-allowed' : ''"
                      />
                      <span class="text-sm text-gray-500">min</span>
                    </div>
                  </div>
                </div>
                
                <div class="flex justify-center gap-3 mt-4">
                  <button 
                    @click="handleAddSchedule" 
                    class="bg-white border border-green-500 text-green-600 hover:bg-green-50 text-sm font-medium rounded-lg px-4 py-2 transition-colors shadow-sm"
                    :disabled="isEditingSchedule"
                    :class="isEditingSchedule ? 'opacity-50 cursor-not-allowed' : ''"
                  >
                    Add Schedule
                  </button>
                  <button 
                    @click="saveWateringSchedule" 
                    :disabled="!isEditingSchedule"
                    class="bg-green-500 hover:bg-green-600 text-white text-sm font-medium rounded-lg px-4 py-2 transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    Save Schedule
                  </button>
                </div>
              </div>

              <!-- Saved Schedules Card (formerly Water Level) - Right Position -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex items-center justify-between mb-5">
                  <div class="flex items-center gap-2">
                    <div class="text-blue-500">
                      <CalendarClock class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Saved Schedules</h2>
                  </div>
                  <div class="text-xs text-gray-500">
                    Upcoming Waterings
                  </div>
                </div>
                
                <div class="text-sm text-gray-500 mb-4">All scheduled waterings:</div>
                
                <!-- Saved Schedules List -->
                <div class="space-y-3 max-h-[300px] overflow-y-auto pr-1">
                  <div v-if="savedSchedules.length === 0" class="flex flex-col items-center justify-center py-8 text-center">
                    <CalendarClock class="w-12 h-12 text-gray-300 mb-3" />
                    <p class="text-gray-400">No schedules saved yet</p>
                    <p class="text-xs text-gray-400 mt-1">Add a schedule to see it here</p>
                  </div>
                  
                  <div 
                    v-for="(schedule, index) in savedSchedules" 
                    :key="index"
                    class="bg-gray-50 rounded-lg p-4 border border-gray-100 hover:border-green-200 transition-colors"
                  >
                    <div class="flex items-center justify-between mb-2">
                      <div class="flex items-center gap-2">
                        <div class="w-2 h-2 rounded-full bg-green-500"></div>
                        <span class="text-sm font-medium text-gray-700">{{ schedule.dateTime }}</span>
                      </div>
                      <button 
                        @click="removeSchedule(index)" 
                        class="text-gray-400 hover:text-red-500 transition-colors"
                      >
                        <X class="w-4 h-4" />
                      </button>
                    </div>
                    
                    <div class="flex items-center gap-4 text-xs text-gray-500 mt-2">
                      <div class="flex items-center gap-1">
                        <Clock class="w-3.5 h-3.5" />
                        <span>{{ schedule.duration }} min</span>
                      </div>
                      
                      <div class="flex items-center gap-1">
                        <Calendar class="w-3.5 h-3.5" />
                        <span>{{ schedule.mode }}</span>
                      </div>
                    </div>
                    
                    <div v-if="schedule.mode === 'weekly'" class="flex flex-wrap gap-1 mt-3">
                      <span 
                        v-for="(day, dayIndex) in weekDays" 
                        :key="dayIndex"
                        :class="[
                          'text-xs px-2 py-0.5 rounded-full',
                          schedule.days[dayIndex] ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-400'
                        ]"
                      >
                        {{ day.substring(0, 3) }}
                      </span>
                    </div>
                  </div>
                </div>
                
                <!-- Add New Schedule Button -->
                <div class="mt-4 text-center">
                  <button 
                    @click="handleAddSchedule" 
                    class="inline-flex items-center gap-1 text-sm text-green-600 hover:text-green-700 transition-colors"
                    :disabled="isEditingSchedule"
                  >
                    <Plus class="w-4 h-4" />
                    <span>Add New Schedule</span>
                  </button>
                </div>
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
  Thermometer, 
  Droplets, 
  Waves, 
  Droplet, 
  Clock,
  CalendarClock,
  Plus,
  Minus,
  Play,
  Pause,
  RefreshCw,
  X,
  Calendar,
  ChevronRight
} from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'

// Environmental control values
const temperature = ref(25)
const humidity = ref(50)
const soilMoisture = ref(50)

// Range control values
const minTemperature = ref(20)
const maxTemperature = ref(30)
const minHumidity = ref(40)
const maxHumidity = ref(80)
const minSoilMoisture = ref(30)
const maxSoilMoisture = ref(70)

// System control values
const waterPumpActive = ref(false)
const waterLevel = ref(55.68)

// Motor control values
const wateringMode = ref('weekly')
const wateringDays = ref([true, false, true, false, true, false, false]) // Mon, Wed, Fri
const weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
const wateringHour = ref(6) // 6 AM
const wateringMinute = ref(30) // 30 minutes
const wateringDuration = ref(20)
const wateringDurationUnit = ref('minutes')
const wateringInterval = ref(2)
const wateringIntervalUnit = ref('days')
const wateringTime = ref('11h')

// State to track if we're in schedule editing mode
const isEditingSchedule = ref(false)

// Saved schedules array
const savedSchedules = ref([
  {
    dateTime: 'Mon, Mar 31, 06:30 AM',
    duration: 20,
    mode: 'weekly',
    days: [true, false, true, false, true, false, false]
  },
  {
    dateTime: 'Wed, Apr 2, 08:00 AM',
    duration: 15,
    mode: 'weekly',
    days: [false, false, true, false, false, false, false]
  },
  {
    dateTime: 'Fri, Apr 4, 07:15 AM',
    duration: 25,
    mode: 'weekly',
    days: [false, false, false, false, true, false, false]
  }
])

// Formatted time inputs
const formattedHour = computed({
  get: () => wateringHour.value.toString().padStart(2, '0'),
  set: (value) => {
    const hour = parseInt(value)
    if (!isNaN(hour) && hour >= 0 && hour <= 23) {
      wateringHour.value = hour
    }
  }
})

const formattedMinute = computed({
  get: () => wateringMinute.value.toString().padStart(2, '0'),
  set: (value) => {
    const minute = parseInt(value)
    if (!isNaN(minute) && minute >= 0 && minute <= 59) {
      wateringMinute.value = minute
    }
  }
})

// Validation functions
const validateHour = () => {
  let hour = parseInt(formattedHour.value)
  if (isNaN(hour) || hour < 0) hour = 0
  if (hour > 23) hour = 23
  wateringHour.value = hour
}

const validateMinute = () => {
  let minute = parseInt(formattedMinute.value)
  if (isNaN(minute) || minute < 0) minute = 0
  if (minute > 59) minute = 59
  wateringMinute.value = minute
}

// Circle calculations
const circumference = 2 * Math.PI * 45

// Timer Logic
const timer = ref({
  hours: 8,
  minutes: 3,
  seconds: 40
})

let timerInterval

const formatTime = (value) => {
  return value.toString().padStart(2, '0')
}

const updateTimer = () => {
  if (timer.value.seconds > 0) {
    timer.value.seconds--
  } else {
    if (timer.value.minutes > 0) {
      timer.value.minutes--
      timer.value.seconds = 59
    } else {
      if (timer.value.hours > 0) {
        timer.value.hours--
        timer.value.minutes = 59
        timer.value.seconds = 59
      }
    }
  }
}

// Computed properties for ranges
const temperatureRange = computed(() => {
  return maxTemperature.value - minTemperature.value
})

const humidityRange = computed(() => {
  return maxHumidity.value - minHumidity.value
})

const soilMoistureRange = computed(() => {
  return maxSoilMoisture.value - minSoilMoisture.value
})

// Validation functions for input fields
const validateMinTemperature = () => {
  // Ensure minTemperature is within bounds
  if (minTemperature.value < 10) minTemperature.value = 10
  if (minTemperature.value >= maxTemperature.value) minTemperature.value = maxTemperature.value - 1
}

const validateMaxTemperature = () => {
  // Ensure maxTemperature is within bounds
  if (maxTemperature.value > 50) maxTemperature.value = 50
  if (maxTemperature.value <= minTemperature.value) maxTemperature.value = minTemperature.value + 1
}

const validateMinHumidity = () => {
  // Ensure minHumidity is within bounds
  if (minHumidity.value < 1) minHumidity.value = 1
  if (minHumidity.value >= maxHumidity.value) minHumidity.value = maxHumidity.value - 1
}

const validateMaxHumidity = () => {
  // Ensure maxHumidity is within bounds
  if (maxHumidity.value > 100) maxHumidity.value = 100
  if (maxHumidity.value <= minHumidity.value) maxHumidity.value = minHumidity.value + 1
}

const validateMinSoilMoisture = () => {
  // Ensure minSoilMoisture is within bounds
  if (minSoilMoisture.value < 1) minSoilMoisture.value = 1
  if (minSoilMoisture.value >= maxSoilMoisture.value) minSoilMoisture.value = maxSoilMoisture.value - 1
}

const validateMaxSoilMoisture = () => {
  // Ensure maxSoilMoisture is within bounds
  if (maxSoilMoisture.value > 100) maxSoilMoisture.value = 100
  if (maxSoilMoisture.value <= minSoilMoisture.value) maxSoilMoisture.value = minSoilMoisture.value + 1
}

// Increment/decrement functions for temperature
const incrementMinTemperature = () => {
  if (minTemperature.value < maxTemperature.value - 1) {
    minTemperature.value++
  }
}

const decrementMinTemperature = () => {
  if (minTemperature.value > 10) {
    minTemperature.value--
  }
}

const incrementMaxTemperature = () => {
  if (maxTemperature.value < 50) {
    maxTemperature.value++
  }
}

const decrementMaxTemperature = () => {
  if (maxTemperature.value > minTemperature.value + 1) {
    maxTemperature.value--
  }
}

// Increment/decrement functions for humidity
const incrementMinHumidity = () => {
  if (minHumidity.value < maxHumidity.value - 1) {
    minHumidity.value++
  }
}

const decrementMinHumidity = () => {
  if (minHumidity.value > 1) {
    minHumidity.value--
  }
}

const incrementMaxHumidity = () => {
  if (maxHumidity.value < 100) {
    maxHumidity.value++
  }
}

const decrementMaxHumidity = () => {
  if (maxHumidity.value > minHumidity.value + 1) {
    maxHumidity.value--
  }
}

// Increment/decrement functions for soil moisture
const incrementMinSoilMoisture = () => {
  if (minSoilMoisture.value < maxSoilMoisture.value - 1) {
    minSoilMoisture.value++
  }
}

const decrementMinSoilMoisture = () => {
  if (minSoilMoisture.value > 1) {
    minSoilMoisture.value--
  }
}

const incrementMaxSoilMoisture = () => {
  if (maxSoilMoisture.value < 100) {
    maxSoilMoisture.value++
  }
}

const decrementMaxSoilMoisture = () => {
  if (maxSoilMoisture.value > minSoilMoisture.value + 1) {
    maxSoilMoisture.value--
  }
}

// Color functions for input fields based on agricultural standards
const getTemperatureInputColor = (value) => {
  if (value < 10) return '#3b82f6' // blue-600
  if (value > 40) return '#ef4444' // red-600
  return '#1f2937' // gray-800
}

const getHumidityInputColor = (value) => {
  if (value < 40) return '#f59e0b' // amber-600
  if (value > 80) return '#3b82f6' // blue-600
  return '#1f2937' // gray-800
}

const getSoilMoistureInputColor = (value) => {
  if (value < 30) return '#f59e0b' // amber-600
  if (value > 70) return '#3b82f6' // blue-600
  return '#1f2937' // gray-800
}

// Temperature status and colors based on agricultural standards
const getTemperatureStatus = computed(() => {
  // Check if the range crosses into stress zones
  if (minTemperature.value < 10 && maxTemperature.value < 10) return 'Cold Stress'
  if (minTemperature.value > 40 && maxTemperature.value > 40) return 'Heat Stress'
  if (minTemperature.value < 10 || maxTemperature.value > 40) return 'Partial Stress'
  return 'Optimal'
})

const getTemperatureStatusClass = computed(() => {
  if (minTemperature.value < 10 && maxTemperature.value < 10) return 'bg-blue-100 text-blue-800'
  if (minTemperature.value > 40 && maxTemperature.value > 40) return 'bg-red-100 text-red-800'
  if (minTemperature.value < 10 || maxTemperature.value > 40) return 'bg-amber-100 text-amber-800'
  return 'bg-green-100 text-green-800'
})

const getTemperatureColor = computed(() => {
  if (minTemperature.value < 10 && maxTemperature.value < 10) return '#3b82f6' // blue-500
  if (minTemperature.value > 40 && maxTemperature.value > 40) return '#ef4444' // red-500
  if (minTemperature.value < 10 || maxTemperature.value > 40) return '#f59e0b' // amber-500
  return '#10b981' // green-500
})

const getTemperatureTextColor = computed(() => {
  if (minTemperature.value < 10 && maxTemperature.value < 10) return 'text-blue-600'
  if (minTemperature.value > 40 && maxTemperature.value > 40) return 'text-red-600'
  if (minTemperature.value < 10 || maxTemperature.value > 40) return 'text-amber-600'
  return 'text-gray-800'
})

// Humidity status and colors based on agricultural standards
const getHumidityStatus = computed(() => {
  if (minHumidity.value < 40 && maxHumidity.value < 40) return 'Drought Risk'
  if (minHumidity.value > 80 && maxHumidity.value > 80) return 'Mold Risk'
  if (minHumidity.value < 40 || maxHumidity.value > 80) return 'Partial Risk'
  return 'Optimal'
})

const getHumidityStatusClass = computed(() => {
  if (minHumidity.value < 40 && maxHumidity.value < 40) return 'bg-amber-100 text-amber-800'
  if (minHumidity.value > 80 && maxHumidity.value > 80) return 'bg-blue-100 text-blue-800'
  if (minHumidity.value < 40 || maxHumidity.value > 80) return 'bg-amber-100 text-amber-800'
  return 'bg-green-100 text-green-800'
})

const getHumidityColor = computed(() => {
  if (minHumidity.value < 40 && maxHumidity.value < 40) return '#f59e0b' // amber-500
  if (minHumidity.value > 80 && maxHumidity.value > 80) return '#3b82f6' // blue-500
  if (minHumidity.value < 40 || maxHumidity.value > 80) return '#f59e0b' // amber-500
  return '#10b981' // green-500
})

const getHumidityTextColor = computed(() => {
  if (minHumidity.value < 40 && maxHumidity.value < 40) return 'text-amber-600'
  if (minHumidity.value > 80 && maxHumidity.value > 80) return 'text-blue-600'
  if (minHumidity.value < 40 || maxHumidity.value > 80) return 'text-amber-600'
  return 'text-gray-800'
})

// Soil Moisture status and colors based on agricultural standards
const getSoilMoistureStatus = computed(() => {
  if (minSoilMoisture.value < 30 && maxSoilMoisture.value < 30) return 'Dry Soil'
  if (minSoilMoisture.value > 70 && maxSoilMoisture.value > 70) return 'Overwatering'
  if (minSoilMoisture.value < 30 || maxSoilMoisture.value > 70) return 'Partial Risk'
  return 'Optimal'
})

const getSoilMoistureStatusClass = computed(() => {
  if (minSoilMoisture.value < 30 && maxSoilMoisture.value < 30) return 'bg-amber-100 text-amber-800'
  if (minSoilMoisture.value > 70 && maxSoilMoisture.value > 70) return 'bg-blue-100 text-blue-800'
  if (minSoilMoisture.value < 30 || maxSoilMoisture.value > 70) return 'bg-amber-100 text-amber-800'
  return 'bg-green-100 text-green-800'
})

const getSoilMoistureColor = computed(() => {
  if (minSoilMoisture.value < 30 && maxSoilMoisture.value < 30) return '#f59e0b' // amber-500
  if (minSoilMoisture.value > 70 && maxSoilMoisture.value > 70) return '#3b82f6' // blue-500
  if (minSoilMoisture.value < 30 || maxSoilMoisture.value > 70) return '#f59e0b' // amber-500
  return '#10b981' // green-500
})

const getSoilMoistureTextColor = computed(() => {
  if (minSoilMoisture.value < 30 && maxSoilMoisture.value < 30) return 'text-amber-600'
  if (minSoilMoisture.value > 70 && maxSoilMoisture.value > 70) return 'text-blue-600'
  if (minSoilMoisture.value < 30 || maxSoilMoisture.value > 70) return 'text-amber-600'
  return 'text-gray-800'
})

// Circle visualization for ranges
const getTemperatureRangeDashOffset = computed(() => {
  // Map temperature range to 0-100%
  const maxPossibleRange = 40 // 50 - 10
  const percentage = (temperatureRange.value / maxPossibleRange) * 100
  return circumference - (percentage / 100) * circumference
})

const getHumidityRangeDashOffset = computed(() => {
  // Map humidity range to 0-100%
  const maxPossibleRange = 99 // 100 - 1
  const percentage = (humidityRange.value / maxPossibleRange) * 100
  return circumference - (percentage / 100) * circumference
})

const getSoilMoistureRangeDashOffset = computed(() => {
  // Map soil moisture range to 0-100%
  const maxPossibleRange = 99 // 100 - 1
  const percentage = (soilMoistureRange.value / maxPossibleRange) * 100
  return circumference - (percentage / 100) * circumference
})

// Water Level computed properties
const getWaterLevelDashOffset = computed(() => {
  return circumference - (waterLevel.value / 100) * circumference
})

const getWaterLevelStatus = computed(() => {
  if (waterLevel.value <= 30) return 'Low Level'
  if (waterLevel.value >= 80) return 'High Level'
  return 'Optimal Level'
})

const getWaterLevelStatusClass = computed(() => {
  if (waterLevel.value <= 30) return 'bg-amber-100 text-amber-800'
  if (waterLevel.value >= 80) return 'bg-blue-100 text-blue-800'
  return 'bg-green-100 text-green-800'
})

// Toggle watering day
const toggleWateringDay = (index) => {
  wateringDays.value[index] = !wateringDays.value[index]
}

// Function to handle adding a schedule
const handleAddSchedule = () => {
  isEditingSchedule.value = true
  console.log('Now editing schedule, inputs enabled')
}

// Function to set water pump active state directly
const setWaterPumpActive = (state) => {
  waterPumpActive.value = state
  
  // Add to activity log when toggled
  if (state) {
    // Add "Turned ON" activity
    const now = new Date()
    console.log(`Water pump turned ON at ${now.toLocaleTimeString()}`)
  } else {
    // Add "Turned OFF" activity
    const now = new Date()
    console.log(`Water pump turned OFF at ${now.toLocaleTimeString()}`)
  }
}

// Save watering schedule - updated to add to savedSchedules
const saveWateringSchedule = () => {
  // Create a new schedule object
  const newSchedule = {
    dateTime: nextWateringTime.value,
    duration: wateringDuration.value,
    mode: wateringMode.value,
    days: [...wateringDays.value] // Create a copy of the array
  }
  
  // Add to saved schedules
  savedSchedules.value.push(newSchedule)
  
  // Reset the editing state after saving
  isEditingSchedule.value = false
  
  // Show a success message or notification
  alert('Watering schedule saved successfully!')
}

// Function to remove a schedule
const removeSchedule = (index) => {
  if (confirm('Are you sure you want to remove this schedule?')) {
    savedSchedules.value.splice(index, 1)
  }
}

// Format the next watering time based on the schedule
const nextWateringTime = computed(() => {
  const now = new Date()
  let nextDate = new Date()

  if (wateringMode.value === 'weekly') {
    // Find the next day that has watering enabled
    const currentDay = now.getDay() // 0 = Sunday, 1 = Monday, etc.
    const adjustedCurrentDay = currentDay === 0 ? 6 : currentDay - 1 // Convert to 0 = Monday, 6 = Sunday
    
    // Check if there's a watering day enabled
    if (!wateringDays.value.some(day => day)) {
      return 'No schedule set'
    }
    
    // Find the next watering day
    let daysToAdd = 0
    for (let i = 1; i <= 7; i++) {
      const checkDay = (adjustedCurrentDay + i) % 7
      if (wateringDays.value[checkDay]) {
        daysToAdd = i
        break
      }
    }
    
    nextDate.setDate(now.getDate() + daysToAdd)
  } else if (wateringMode.value === 'daily') {
    // If it's already past the watering time for today, schedule for tomorrow
    if (now.getHours() > wateringHour.value || 
        (now.getHours() === wateringHour.value && now.getMinutes() >= wateringMinute.value)) {
      nextDate.setDate(now.getDate() + 1)
    }
  } else if (wateringMode.value === 'custom') {
    // Add the interval to the current date
    if (wateringIntervalUnit.value === 'hours') {
      nextDate.setHours(now.getHours() + wateringInterval.value)
    } else {
      nextDate.setDate(now.getDate() + wateringInterval.value)
    }
  }

  // Set the time
  nextDate.setHours(wateringHour.value)
  nextDate.setMinutes(wateringMinute.value)
  nextDate.setSeconds(0)

  // Format the date
  return nextDate.toLocaleString('en-US', { 
    weekday: 'short',
    month: 'short', 
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  })
})

onMounted(() => {
  timerInterval = setInterval(updateTimer, 1000)
})

onUnmounted(() => {
  if (timerInterval) clearInterval(timerInterval)
})
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Custom slider styling - Updated for better centering */
input[type=range] {
-webkit-appearance: none;
appearance: none; /* Added standard property */
background: transparent;
}

input[type=range]:focus {
outline: none;
}

input[type=range]::-webkit-slider-thumb {
-webkit-appearance: none;
appearance: none; /* Added standard property */
width: 18px;
height: 18px;
background: white;
border-radius: 50%;
cursor: pointer;
border: 2px solid #10b981;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
margin-top: -8px; /* This centers the thumb on the track */
}

input[type=range]::-moz-range-thumb {
width: 18px;
height: 18px;
background: white;
border-radius: 50%;
cursor: pointer;
border: 2px solid #10b981;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

input[type=range]::-webkit-slider-runnable-track {
width: 100%;
height: 2px;
cursor: pointer;
background: transparent;
border-radius: 999px;
}

input[type=range]::-moz-range-track {
width: 100%;
height: 2px;
cursor: pointer;
background: transparent;
border-radius: 999px;
}

/* Remove number input arrows */
input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { 
-webkit-appearance: none; 
appearance: none; /* Added standard property */
margin: 0; 
}

input[type=number] {
-moz-appearance: textfield;
appearance: textfield; /* Added standard property */
}

/* Custom scrollbar styling */
::-webkit-scrollbar {
width: 6px;
height: 6px;
}

::-webkit-scrollbar-track {
background: rgba(20, 83, 45, 0.05);
border-radius: 4px;
}

::-webkit-scrollbar-thumb {
background: rgba(20, 83, 45, 0.3);
border-radius: 4px;
transition: background-color 200ms;
}

::-webkit-scrollbar-thumb:hover {
background: rgba(20, 83, 45, 0.5);
}

/* Smooth transitions */
* {
transition: all 200ms ease-in-out;
}

/* Firefox scrollbar styling */
* {
scrollbar-width: thin;
scrollbar-color: rgba(20, 83, 45, 0.3) rgba(20, 83, 45, 0.05);
}

/* Custom toggle styling */
.toggle-track {
transition: background-color 0.3s ease;
}

.toggle-thumb {
transition: transform 0.3s ease, background-color 0.3s ease;
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
</style>