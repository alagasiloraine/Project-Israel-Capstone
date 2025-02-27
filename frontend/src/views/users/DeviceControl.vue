<template>
  <div class="flex h-screen bg-[#f8f9fa] font-poppins">
    <!-- Sidebar -->
    <Sidebar />
  
    <!-- Main Content -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <div class="flex-1 overflow-auto bg-gradient-to-br from-green-50 to-emerald-50 p-6 relative">
        <!-- Main Content -->
        <div class="flex gap-8 max-w-[1600px] mx-auto relative z-10 mt-[55px]">
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
  
            <!-- Bottom Controls Section -->
            <div class="flex gap-4">
              <!-- Motor Control -->
              <div class="bg-white rounded-3xl shadow-xl w-[500px] mx-auto mr-[20px] mb-8">
                <div class="p-8">
                  <div class="flex items-center justify-between mb-16">
                    <div class="flex items-center gap-2">
                      <Droplet class="w-8 h-8 text-[#4ade80]" />
                      <h2 class="text-xl font-semibold text-gray-800">Motor Control</h2>
                         <!-- Add Watering Time Input -->
                         <div class="flex items-center bg-blue-500 rounded-full ml-4 px-3 py-1.5">
                        <span class="text-white text-sm mr-2">Watering time (weekly)</span>
                        <input 
                          type="text" 
                          v-model="wateringTime"
                          class="w-12 bg-transparent text-white text-center border-b border-white/30 focus:outline-none focus:border-white"
                          placeholder="11h"
                        />
                        <Droplet class="w-4 h-4 text-white ml-1 opacity-70" />
                      </div>
                    </div>
                  </div>
  
                  <!-- Toggle Switch -->
                  <div class="flex items-center justify-center bg-gray-50 p-6 rounded-2xl gap-8">
                    <span class="text-xl font-medium text-gray-700 w-24 text-right ml-12">Status:</span>
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
                    <span class="text-2xl font-semibold w-24 mr-16" 
                          :class="waterPumpActive ? 'text-[#4ade80]' : 'text-gray-400'">
                      {{ waterPumpActive ? 'ON' : 'OFF' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Hourly Forecast -->
              <div class="bg-white rounded-2xl p-4 mb-6">
                <div class="overflow-x-auto">
                  <div class="flex gap-6 min-w-max">
                    <div v-for="hour in hourlyForecast" :key="hour.time" 
                         class="flex flex-col items-center">
                      <span class="text-xs text-gray-500 mb-2">{{ hour.time }}</span>
                      <Cloud class="w-5 h-5 text-gray-600 mb-2" />
                      <span class="text-sm font-medium text-gray-800">{{ hour.temp }}°C</span>
                    </div>
                  </div>
                </div>

                <!-- Daily Forecast -->
                <div class="flex gap-2 p-4">
                  <div v-for="day in forecast" :key="day.day" 
                      class="bg-gray-100 rounded-xl p-3 flex flex-col items-center min-w-[72px]">
                    <span class="text-sm font-medium mb-2">{{ day.day }}</span>
                    <component 
                      :is="day.icon" 
                      class="w-6 h-6 mb-2"
                      :class="day.iconColor"
                    />
                    <span class="text-sm font-medium">{{ day.temp }}°C</span>
                  </div>
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
<div class="bg-white rounded-3xl p-6 shadow-xl">
  <div class="flex items-center justify-between mb-4">
    <div class="text-xl font-bold mb-4">Water Level</div>
    <Waves class="w-6 h-6" :style="{ color: waterLevelColor }" />
  </div>
  <div class="text-sm text-gray-500 mb-6">As of now:</div>
  
  <!-- Water Level Pie Chart -->
  <div class="relative w-48 h-48 mx-auto">
    <div class="absolute inset-0 rounded-full bg-gray-100"></div>
    <div 
      class="absolute inset-0 rounded-full transition-all duration-1000"
      :style="{
        background: `conic-gradient(${waterLevelColor} ${waterLevel * 3.6}deg, #f3f4f6 ${waterLevel * 3.6}deg)`
      }"
    ></div>
    <div class="absolute inset-4 rounded-full bg-white flex items-center justify-center">
      <span class="text-3xl font-bold text-gray-800">{{ waterLevel }}%</span>
    </div>
  </div>
</div>

            <!-- Weather Forecast -->
            <div class="bg-white rounded-3xl shadow-xl w-[330px]">
              <div class="p-6">
                <!-- Location and Date Container -->
                <div class="flex items-center justify-between mb-3 h-14">
                  <div class="flex items-center gap-2">
                    <MapPin class="w-6 h-6 text-[#4ade80]" />
                    <h2 class="text-lg font-semibold text-gray-800">Calapan, PH</h2>
                  </div>
                  <div class="text-sm text-gray-600">Thursday, Jan 23</div>
                </div>

                <!-- Current Weather -->
                <div class="flex items-center justify-center bg-gray-50 p-4 rounded-xl mb-4">
                  <div class="text-center">
                    <Cloud class="w-12 h-12 mx-auto mb-1 text-gray-600" />
                    <div class="text-3xl font-bold text-gray-800">25°C</div>
                    <div class="text-sm text-gray-600">Overcast clouds</div>
                  </div>
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
import { Thermometer, Droplets, Waves, Droplet, Cloud, MapPin, Sun, Moon } from 'lucide-vue-next'
<<<<<<< HEAD
import Sidebar from './Sidebar.vue'
=======
import Sidebar from '../layout/Sidebar.vue'
>>>>>>> origin/loreng

const temperature = ref(25)
const humidity = ref(50)
const soilMoisture = ref(50)
const waterPumpActive = ref(false)
const waterLevel = ref(55.68)
const wateringTime = ref('11h')

const waterLevelColor = computed(() => {
  if (waterLevel.value <= 30) return '#4ade80' // green
  if (waterLevel.value <= 65) return '#fb923c' // orange
  return '#3b82f6' // blue
})

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

// Weather data
const hourlyForecast = ref([
  { time: '12:00 AM', temp: 25 },
  { time: '3:00 AM', temp: 26 },
  { time: '6:00 AM', temp: 27 },
  { time: '9:00 AM', temp: 26 },
  { time: '12:00 PM', temp: 26 },
  { time: '3:00 PM', temp: 26 },
  { time: '6:00 PM', temp: 25 },
  { time: '9:00 PM', temp: 25 }
])

const forecast = [
  {
    day: 'Mon',
    icon: Cloud,
    iconColor: 'text-amber-400',
    temp: 23
  },
  {
    day: 'Tue',
    icon: Sun,
    iconColor: 'text-amber-400',
    temp: 23
  },
  {
    day: 'Wed',
    icon: Moon,
    iconColor: 'text-amber-400',
    temp: 21
  },
  {
    day: 'Thu',
    icon: Cloud,
    iconColor: 'text-gray-400',
    temp: 19
  },
  {
    day: 'Fri',
    icon: Cloud,
    iconColor: 'text-gray-400',
    temp: 18
  },
  {
    day: 'Sat',
    icon: Sun,
    iconColor: 'text-amber-400',
    temp: 21
  },
  {
    day: 'Sun',
    icon: Moon,
    iconColor: 'text-amber-400',
    temp: 23
  },
]
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

/* Custom scrollbar for hourly forecast */
.overflow-x-auto {
  scrollbar-width: thin;
  scrollbar-color: rgb(34 197 94) transparent;
}

.overflow-x-auto::-webkit-scrollbar {
  height: 4px;
}

.overflow-x-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-x-auto::-webkit-scrollbar-thumb {
  background-color: rgb(34 197 94);
  border-radius: 2px;
}
</style>