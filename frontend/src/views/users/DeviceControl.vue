<template>
    <div class="flex h-screen bg-[#f8f9fa] font-poppins">
      <!-- Sidebar -->
      <Sidebar />
  
      <!-- Main Content -->
      <div class="flex-1 flex flex-col overflow-hidden">
        <div class="flex-1 overflow-auto bg-gradient-to-br from-green-50 to-emerald-50 p-6 relative">
          <!-- Background Pattern -->
          <!-- <div class="absolute inset-0 pattern-dots pattern-green-500 pattern-bg-white pattern-size-2 pattern-opacity-5"></div> -->
  
          <!-- Main Content -->
          <div class="flex gap-8 max-w-[1600px] mx-auto relative z-10 mt-[110px]">
            <!-- Left Section -->
            <div class="flex-1 flex flex-col gap-16">
              <!-- Top Controls Grid -->
              <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Temperature Control -->
                <div class="bg-white rounded-3xl p-8 shadow-xl">
                  <div class="flex items-center justify-between mb-6">
                    <div class="flex items-center gap-2">
                      <Thermometer class="w-6 h-6" :class="temperatureColor" />
                      <h2 class="text-xl font-semibold text-gray-800">Temperature</h2>
                    </div>
                    <span class="text-sm text-gray-500">Range: 10-50°C</span>
                  </div>
  
                  <!-- Circular Control -->
                  <div class="relative w-48 h-48 mx-auto mb-6">
                    <div class="absolute inset-0 rounded-full bg-gradient-to-r from-[#4ade80] to-[#fb923c] opacity-70"></div>
                    <div class="absolute inset-2 rounded-full bg-white"></div>
                    <div class="absolute inset-0 flex items-center justify-center">
                      <span class="text-4xl font-bold" :class="temperatureTextColor">{{ temperature }}°</span>
                    </div>
                    <div 
                      class="absolute inset-0 rounded-full opacity-80"
                      :style="{
                        background: temperatureIndicatorColor
                      }"
                    ></div>
                  </div>
  
                  <!-- Slider Control -->
                  <div class="relative">
                    <input 
                      type="range" 
                      v-model="temperature" 
                      min="10" 
                      max="50"
                      class="w-full h-2 rounded-lg appearance-none cursor-pointer range-slider"
                    />
                    <div class="flex justify-between mt-2 text-sm text-gray-600">
                      <span>10°C</span>
                      <span>50°C</span>
                    </div>
                  </div>
                </div>
  
                <!-- Humidity Control -->
                <div class="bg-white rounded-3xl p-8 shadow-xl">
                  <div class="flex items-center justify-between mb-6">
                    <div class="flex items-center gap-2">
                      <Droplets class="w-6 h-6" :class="humidityColor" />
                      <h2 class="text-xl font-semibold text-gray-800">Humidity</h2>
                    </div>
                    <span class="text-sm text-gray-500">Range: 1-100%</span>
                  </div>
  
                  <!-- Circular Control -->
                  <div class="relative w-48 h-48 mx-auto mb-6">
                    <div class="absolute inset-0 rounded-full bg-gradient-to-r from-[#4ade80] to-[#fb923c] opacity-70"></div>
                    <div class="absolute inset-2 rounded-full bg-white"></div>
                    <div class="absolute inset-0 flex items-center justify-center">
                      <span class="text-4xl font-bold" :class="humidityTextColor">{{ humidity }}%</span>
                    </div>
                    <div 
                      class="absolute inset-0 rounded-full opacity-80"
                      :style="{
                        background: humidityIndicatorColor
                      }"
                    ></div>
                  </div>
  
                  <!-- Slider Control -->
                  <div class="relative">
                    <input 
                      type="range" 
                      v-model="humidity" 
                      min="1" 
                      max="100"
                      class="w-full h-2 rounded-lg appearance-none cursor-pointer range-slider"
                    />
                    <div class="flex justify-between mt-2 text-sm text-gray-600">
                      <span>1%</span>
                      <span>100%</span>
                    </div>
                  </div>
                </div>
  
                <!-- Soil Moisture Control -->
                <div class="bg-white rounded-3xl p-8 shadow-xl">
                  <div class="flex items-center justify-between mb-6">
                    <div class="flex items-center gap-2">
                      <Waves class="w-6 h-6" :class="soilMoistureColor" />
                      <h2 class="text-xl font-semibold text-gray-800">Soil Moisture</h2>
                    </div>
                    <span class="text-sm text-gray-500">Range: 1-100%</span>
                  </div>
  
                  <!-- Circular Control -->
                  <div class="relative w-48 h-48 mx-auto mb-6">
                    <div class="absolute inset-0 rounded-full bg-gradient-to-r from-[#4ade80] to-[#fb923c] opacity-70"></div>
                    <div class="absolute inset-2 rounded-full bg-white"></div>
                    <div class="absolute inset-0 flex items-center justify-center">
                      <span class="text-4xl font-bold" :class="soilMoistureTextColor">{{ soilMoisture }}%</span>
                    </div>
                    <div 
                      class="absolute inset-0 rounded-full opacity-80"
                      :style="{
                        background: soilMoistureIndicatorColor
                      }"
                    ></div>
                  </div>
  
                  <!-- Slider Control -->
                  <div class="relative">
                    <input 
                      type="range" 
                      v-model="soilMoisture" 
                      min="1" 
                      max="100"
                      class="w-full h-2 rounded-lg appearance-none cursor-pointer range-slider"
                    />
                    <div class="flex justify-between mt-2 text-sm text-gray-600">
                      <span>1%</span>
                      <span>100%</span>
                    </div>
                  </div>
                </div>
              </div>
  
              <!-- Water Level Control -->
              <div class="bg-white rounded-3xl shadow-xl w-full max-w-xl mx-auto">
                <div class="p-8">
                  <div class="flex items-center justify-between mb-8">
                    <div class="flex items-center gap-3">
                      <Droplet class="w-8 h-8 text-[#4ade80]" />
                      <h2 class="text-2xl font-semibold text-gray-800">Motor Control</h2>
                    </div>
                  </div>
  
                  <!-- Toggle Switch -->
                  <div class="flex items-center justify-center bg-gray-50 p-6 rounded-2xl gap-8">
                    <span class="text-xl font-medium text-gray-700 w-24 text-right mr-16">Status:</span>
                    <label class="relative inline-flex items-center cursor-pointer">
                      <input 
                        type="checkbox"
                        v-model="waterPumpActive"
                        class="sr-only peer"
                      />
                      <div class="w-48 h-16 bg-gray-200 rounded-full peer 
                                peer-checked:after:translate-x-32
                                after:content-[''] 
                                after:absolute 
                                after:top-1 
                                after:left-1 
                                after:bg-white 
                                after:rounded-full 
                                after:h-14 
                                after:w-14 
                                after:transition-all 
                                after:duration-300
                                after:shadow-lg
                                peer-checked:bg-[#4ade80]
                                transition-colors
                                duration-300">
                      </div>
                    </label>
                    <span class="text-2xl font-semibold w-24 ml-16" 
                          :class="waterPumpActive ? 'text-[#4ade80]' : 'text-gray-400'">
                      {{ waterPumpActive ? 'ON' : 'OFF' }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
  
            <!-- Right Section -->
            <div class="w-80 space-y-6">
              <!-- Timer Card -->
              <div class="bg-white rounded-3xl p-6 shadow-xl">
                <div class="grid grid-cols-3 gap-4 text-center">
                  <div>
                    <div class="text-4xl font-bold text-[#4ade80]">{{ formatTime(timer.hours) }}</div>
                    <div class="text-sm text-gray-500 mt-1">Hours</div>
                  </div>
                  <div>
                    <div class="text-4xl font-bold text-[#4ade80]">{{ formatTime(timer.minutes) }}</div>
                    <div class="text-sm text-gray-500 mt-1">Minutes</div>
                  </div>
                  <div>
                    <div class="text-4xl font-bold text-[#4ade80]">{{ formatTime(timer.seconds) }}</div>
                    <div class="text-sm text-gray-500 mt-1">Seconds</div>
                  </div>
                </div>
              </div>
  
              <!-- Water Level Card -->
              <div class="bg-white rounded-3xl p-8 shadow-xl">
                <div class="flex items-center justify-between mb-4">
                  <div class="text-xl font-bold mb-14">Water Level</div>
                  <Waves class="w-6 h-6 text-[#4ade80]" />
                </div>
                <div class="text-sm text-gray-500 mb-6">As of now:</div>
                
                <!-- Water Level Pie Chart -->
                <div class="relative w-48 h-48 mx-auto">
                  <div class="absolute inset-0 rounded-full bg-gray-100"></div>
                  <div 
                    class="absolute inset-0 rounded-full transition-all duration-1000"
                    :style="{
                      background: `conic-gradient(#3b82f6 ${waterLevel * 3.6}deg, #f3f4f6 ${waterLevel * 3.6}deg)`
                    }"
                  ></div>
                  <div class="absolute inset-4 rounded-full bg-white flex items-center justify-center">
                    <span class="text-3xl font-bold text-gray-800">{{ waterLevel }}%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, onUnmounted } from 'vue'
  import { Thermometer, Droplets, Waves, Droplet } from 'lucide-vue-next'
  import Sidebar from './Sidebar.vue'
  
  const temperature = ref(25)
  const humidity = ref(50)
  const soilMoisture = ref(50)
  const waterPumpActive = ref(false)
  const waterLevel = ref(73.68)
  
  // Timer Logic
  const timer = ref({
    hours: 8,
    minutes: 4,
    seconds: 41
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
  
  onMounted(() => {
    timerInterval = setInterval(updateTimer, 1000)
  })
  
  onUnmounted(() => {
    if (timerInterval) clearInterval(timerInterval)
  })
  
  // Temperature colors
  const temperatureIndicatorColor = computed(() => {
    const percentage = ((temperature.value - 10) / 40) * 100
    if (percentage >= 80) {
      return `conic-gradient(from 180deg, #4ade80 0%, #fbbf24 40%, #fb923c 60%, #ef4444 ${(temperature.value - 10) * 9}deg, transparent ${(temperature.value - 10) * 9}deg)`
    } else if (percentage >= 50) {
      return `conic-gradient(from 180deg, #4ade80 0%, #fbbf24 50%, #fb923c ${(temperature.value - 10) * 9}deg, transparent ${(temperature.value - 10) * 9}deg)`
    }
    return `conic-gradient(from 180deg, #4ade80 ${(temperature.value - 10) * 9}deg, transparent ${(temperature.value - 10) * 9}deg)`
  })
  
  const temperatureColor = computed(() => {
    if (temperature.value >= 40) return 'text-orange-400'
    if (temperature.value >= 30) return 'text-amber-400'
    return 'text-green-500'
  })
  
  const temperatureTextColor = computed(() => {
    if (temperature.value >= 40) return 'text-orange-500'
    if (temperature.value >= 30) return 'text-amber-500'
    return 'text-gray-800'
  })
  
  // Humidity colors
  const humidityIndicatorColor = computed(() => {
    if (humidity.value >= 80) {
      return `conic-gradient(from 180deg, #4ade80 0%, #fbbf24 40%, #fb923c 60%, #ef4444 ${humidity.value * 3.6}deg, transparent ${humidity.value * 3.6}deg)`
    } else if (humidity.value >= 50) {
      return `conic-gradient(from 180deg, #4ade80 0%, #fbbf24 50%, #fb923c ${humidity.value * 3.6}deg, transparent ${humidity.value * 3.6}deg)`
    }
    return `conic-gradient(from 180deg, #4ade80 ${humidity.value * 3.6}deg, transparent ${humidity.value * 3.6}deg)`
  })
  
  const humidityColor = computed(() => {
    if (humidity.value >= 80) return 'text-orange-400'
    if (humidity.value >= 60) return 'text-amber-400'
    return 'text-green-500'
  })
  
  const humidityTextColor = computed(() => {
    if (humidity.value >= 80) return 'text-orange-500'
    if (humidity.value >= 60) return 'text-amber-500'
    return 'text-gray-800'
  })
  
  // Soil Moisture colors
  const soilMoistureIndicatorColor = computed(() => {
    if (soilMoisture.value >= 80) {
      return `conic-gradient(from 180deg, #4ade80 0%, #fbbf24 40%, #fb923c 60%, #ef4444 ${soilMoisture.value * 3.6}deg, transparent ${soilMoisture.value * 3.6}deg)`
    } else if (soilMoisture.value >= 50) {
      return `conic-gradient(from 180deg, #4ade80 0%, #fbbf24 50%, #fb923c ${soilMoisture.value * 3.6}deg, transparent ${soilMoisture.value * 3.6}deg)`
    }
    return `conic-gradient(from 180deg, #4ade80 ${soilMoisture.value * 3.6}deg, transparent ${soilMoisture.value * 3.6}deg)`
  })
  
  const soilMoistureColor = computed(() => {
    if (soilMoisture.value >= 80) return 'text-orange-400'
    if (soilMoisture.value >= 60) return 'text-amber-400'
    return 'text-green-500'
  })
  
  const soilMoistureTextColor = computed(() => {
    if (soilMoisture.value >= 80) return 'text-orange-500'
    if (soilMoisture.value >= 60) return 'text-amber-500'
    return 'text-gray-800'
  })
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  
  .pattern-dots {
    background-image: radial-gradient(currentColor 1px, transparent 1px);
    background-size: calc(10 * 1px) calc(10 * 1px);
  }
  
  /* Custom slider styling */
  .range-slider {
    background: linear-gradient(to right, #4ade80, #fb923c);
    height: 4px;
    border-radius: 2px;
  }
  
  .range-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #4ade80;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .range-slider::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #4ade80;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  </style>