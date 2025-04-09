<template>
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen pt-32">
      <!-- Container Wrapper with proper spacing -->
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Main Container with adjusted width -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Content Wrapper -->
          <div class="p-6">
            <!-- Find the Top Metrics Cards section and replace it with this updated version -->
  
            <!-- Top Metrics Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-7 gap-4 mb-8">
              <!-- Nitrogen Level -->
              <div class="group bg-white rounded-xl p-4 border-2 border-green-100 shadow-lg transition-all duration-300 hover:border-green-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-2">
                  <Leaf class="h-5 w-5 text-green-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-green-600 bg-green-100 px-2 py-0.5 rounded-full">N</span>
                </div>
                <div class="text-xl font-bold text-green-700">{{ nitrogen }}</div>
                <div class="text-xs text-green-600">Nitrogen (mg/kg)</div>  
              </div>

              <!-- Phosphorus Level -->
              <div class="group bg-white rounded-xl p-4 border-2 border-blue-100 shadow-lg transition-all duration-300 hover:border-blue-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-2">
                  <TestTube class="h-5 w-5 text-blue-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-blue-600 bg-blue-100 px-2 py-0.5 rounded-full">P</span>
                </div>
                <div class="text-xl font-bold text-blue-700">{{ phosphorus }}</div>
                <div class="text-xs text-blue-600">Phosphorus (mg/kg)</div>
              </div>

              <!-- Potassium Level -->
              <div class="group bg-white rounded-xl p-4 border-2 border-purple-100 shadow-lg transition-all duration-300 hover:border-purple-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-2">
                  <TestTubes class="h-5 w-5 text-purple-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-purple-600 bg-purple-100 px-2 py-0.5 rounded-full">K</span>
                </div>
                <div class="text-xl font-bold text-purple-700">{{ potassium }}</div>
                <div class="text-xs text-purple-600">Potassium (mg/kg)</div>
              </div>

              <!-- Soil pH Level -->
              <div class="group bg-white rounded-xl p-4 border-2 border-orange-100 shadow-lg transition-all duration-300 hover:border-orange-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-2">
                  <Beaker class="h-5 w-5 text-orange-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-orange-600 bg-orange-100 px-2 py-0.5 rounded-full">pH</span>
                </div>
                <div class="text-xl font-bold text-orange-700">{{ soilpH }}</div>
                <div class="text-xs text-orange-600">Soil pH Level</div>
              </div>

              <!-- Soil Moisture -->
              <div class="group bg-white rounded-xl p-4 border-2 border-emerald-100 shadow-lg transition-all duration-300 hover:border-emerald-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-2">
                  <Sprout class="h-5 w-5 text-emerald-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-emerald-600 bg-emerald-100 px-2 py-0.5 rounded-full">SM</span>
                </div>
                <div class="text-xl font-bold text-emerald-700">{{ soilMoisture }}</div>
                <div class="text-xs text-emerald-600">Soil Moisture</div>
              </div>

              <!-- Temperature -->
              <div class="group bg-white rounded-xl p-4 border-2 border-red-100 shadow-lg transition-all duration-300 hover:border-red-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-2">
                  <Thermometer class="h-5 w-5 text-red-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-red-600 bg-red-100 px-2 py-0.5 rounded-full">Temp</span>
                </div>
                <div class="text-xl font-bold text-red-700">{{ temperature }}</div>
                <div class="text-xs text-red-600">Temperature (°C)</div>
              </div>

              <!-- Humidity -->
              <div class="group bg-white rounded-xl p-4 border-2 border-sky-100 shadow-lg transition-all duration-300 hover:border-sky-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-2">
                  <Droplets class="h-5 w-5 text-sky-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-sky-600 bg-sky-100 px-2 py-0.5 rounded-full">RH</span>
                </div>
                <div class="text-xl font-bold text-sky-700">{{ humidity }}</div>
                <div class="text-xs text-sky-600">Humidity (%)</div>
              </div>
            </div>

            <!-- Charts Section -->
            <div class="grid grid-cols-1 gap-8">
              <!-- First Row - Water Level, Motor Status, and Weather -->
              <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Enhanced Water Level Card -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-blue-100 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                  <!-- Header -->
                  <div class="flex justify-between items-center mb-4">
                    <div class="flex items-center bg-blue-50 rounded-full px-2.5 py-1 shadow-inner space-x-1.5">
                      <Waves class="w-4 h-4 text-blue-500" />
                      <h3 class="text-sm font-semibold text-blue-700 tracking-wide">Water Level</h3>
                    </div>
                    <div class="bg-blue-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">LIVE</div>
                  </div>

                  <!-- Water Tank -->
                  <div class="relative w-64 h-80 mx-auto mt-4">
                    <div class="relative w-full h-full rounded-[2rem] border-[6px] border-blue-300 bg-white shadow-2xl overflow-hidden tank-style">

                      <!-- Water Fill Area (shifted vertically by percentage) -->
                      <!-- Water Fill Area -->
                      <div class="absolute bottom-0 left-0 w-full h-full z-10 overflow-hidden">
                        <div
                          class="absolute top-0 left-0 w-full h-full transition-transform duration-700 ease-in-out"
                          :style="{ transform: `translateY(${100 - waterLevel}%)` }"
                        >
                          <div class="relative w-[900%] h-full">
                            <!-- Wave 1 -->
                            <div class="absolute w-full h-full left-0 top-0 animate-long-wave-1">
                              <svg viewBox="0 0 1200 300" preserveAspectRatio="none" class="w-full h-full">
                                <path
                                  d="M0,0 C200,60 400,-60 600,0 C800,60 1000,-60 1200,0 L1200,300 L0,300 Z"
                                  fill="#3B82F6" fill-opacity="0.6"
                                />
                              </svg>
                            </div>
                            <!-- Wave 2 -->
                            <div class="absolute w-full h-full left-0 top-0 animate-long-wave-2">
                              <svg viewBox="0 0 1200 300" preserveAspectRatio="none" class="w-full h-full">
                                <path
                                  d="M0,0 C200,50 400,-50 600,0 C800,50 1000,-50 1200,0 L1200,300 L0,300 Z"
                                  fill="#60A5FA" fill-opacity="0.4"
                                />
                              </svg>
                            </div>
                            <!-- Wave 3 -->
                            <div class="absolute w-full h-full left-0 top-0 animate-long-wave-3">
                              <svg viewBox="0 0 1200 300" preserveAspectRatio="none" class="w-full h-full">
                                <path
                                  d="M0,0 C200,40 400,-40 600,0 C800,40 1000,-40 1200,0 L1200,300 L0,300 Z"
                                  fill="#3B82F6" fill-opacity="0.2"
                                />
                              </svg>
                            </div>
                          </div>
                        </div>
                      </div>


                      <!-- Water Percentage -->
                      <div class="absolute inset-0 flex items-center justify-center z-20">
                        <div class="bg-white/80 backdrop-blur px-4 py-2 rounded-xl shadow-lg border border-blue-100">
                          <span class="text-4xl font-bold text-blue-600">{{ waterLevel }}%</span>
                        </div>
                      </div>
                    </div>

                    <!-- Level Markers -->
                    <div class="absolute top-2 bottom-2 -right-14 w-10 flex flex-col justify-between z-30">
                      <div v-for="n in 5" :key="n" class="flex items-center gap-2">
                        <div class="h-[2px] w-4 bg-blue-400 shadow-sm"></div>
                        <span class="text-sm font-medium text-blue-600 bg-white/90 px-1 rounded">
                          {{ 100 - (n - 1) * 25 }}%
                        </span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Updated Motor Status Card with Smaller Purple 3D Button -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-purple-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
                  <!-- Header section -->
                  <div class="flex flex-col items-start space-y-2 mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-purple-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <Power class="w-4 h-4 text-purple-500" />
                        <h3 class="text-sm font-semibold text-purple-700 tracking-wide">Motor Status</h3>
                      </div>
                      <div class="bg-purple-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                        WEEKLY
                      </div>
                    </div>
                    <div class="w-full">
                      <p class="text-xs text-purple-600 font-medium bg-purple-100 px-3 py-1 rounded-full shadow-sm inline-block">
                        Last 7 Days Overview
                      </p>
                    </div>
                  </div>
                  
                  <!-- Smaller Enhanced 3D Power Button with Circular Progress -->
                  <div class="relative w-40 h-40 mx-auto transform-gpu power-button-container mt-4">
                    <svg class="w-full h-full" viewBox="0 0 100 100">
                      <!-- Background circle -->
                      <circle cx="50" cy="50" r="48" fill="none" stroke="#E9D5FF" stroke-width="4" />
                      <!-- Progress circle -->
                      <circle 
                        cx="50" 
                        cy="50" 
                        r="48" 
                        fill="none" 
                        stroke="#A855F7" 
                        stroke-width="4" 
                        stroke-linecap="round"
                        :stroke-dasharray="circumference"
                        :stroke-dashoffset="dashOffset"
                        transform="rotate(-90 50 50)"
                      />
                    </svg>
                    <div 
                      class="absolute inset-2 rounded-full shadow-lg overflow-hidden cursor-pointer transition-all duration-300 hover:shadow-xl power-button"
                      :class="motorStatus ? 'power-on' : 'power-off'"
                      @click="toggleMotorStatus"
                    >
                      <div class="absolute inset-0 bg-gradient-to-br from-purple-400 to-purple-600"></div>
                      <div class="absolute inset-0 bg-black opacity-20"></div>
                      <div class="absolute inset-0 flex items-center justify-center">
                        <div class="text-center">
                          <Power :class="['w-10 h-10 transition-all duration-300', motorStatus ? 'text-white' : 'text-purple-200']" />
                          <span class="block mt-1 text-xl font-bold text-white">{{ motorStatus ? 'ON' : 'OFF' }}</span>
                          <span class="block text-sm font-medium text-purple-100">{{ motorOnPercentage.toFixed(1) }}%</span>
                        </div>
                      </div>
                      <div class="absolute inset-0 bg-gradient-to-t from-black to-transparent opacity-20"></div>
                      <div class="absolute inset-0 rounded-full border-4 border-purple-300 opacity-20"></div>
                      <div v-if="motorStatus" class="absolute inset-0 bg-purple-500 animate-pulse opacity-30"></div>
                    </div>
                  </div>

                  <!-- Status Information -->
                  <div class="mt-6 text-center">
                    <p class="text-base font-semibold text-purple-700">
                      Motor was <span class="text-purple-500">ON</span> for <span class="text-purple-500">{{ motorOnPercentage.toFixed(1) }}%</span> of the week
                    </p>
                    <p class="text-sm text-purple-600 mt-1">
                      Total runtime: {{ (motorOnPercentage * 1.68).toFixed(1) }} hours
                    </p>
                  </div>

                  <!-- Weekly Breakdown -->
                  <div class="mt-4">
                    <h4 class="text-xs font-semibold text-purple-700 mb-2">Weekly Breakdown</h4>
                    <div class="grid grid-cols-7 gap-1">
                      <div v-for="(day, index) in weeklyData" :key="index" class="flex flex-col items-center">
                        <div class="w-full bg-purple-100 rounded-full overflow-hidden">
                          <div 
                            class="bg-purple-500 h-1" 
                            :style="{ width: `${day.percentage}%` }"
                          ></div>
                        </div>
                        <span class="text-[10px] text-purple-600 mt-1">{{ day.label }}</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Enhanced Weather Card with Colored Icons -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-blue-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1 overflow-hidden">
                  <div class="flex justify-between items-start mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-sky-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <CloudSun class="w-4 h-4 text-sky-500" />
                        <h3 class="text-sm font-semibold text-sky-700 tracking-wide">Weather Forecast</h3>
                      </div>
                      <div class="bg-sky-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">LIVE</div>
                    </div>
                  </div>

                  <!-- Current Weather -->
                  <div class="flex items-center justify-between mb-4">
                    <div>
                      <div class="flex items-end space-x-1">
                        <p class="text-4xl font-bold text-gray-900">{{ weather?.temperature_c }}</p>
                        <p class="text-xl font-semibold text-gray-600 mb-1">°C</p>
                      </div>
                      <p class="text-base mt-1 text-gray-600">{{ weather?.weather_condition }}</p>
                    </div>
                    <div class="weather-icon-wrapper">
                      <component 
                        :is="getWeatherIcon(weather?.weather_condition)"
                        :class="['h-14 w-14 transform transition-transform hover:scale-110', getWeatherIconColor(weatherData[0]?.weather)]"
                      />
                    </div>
                  </div>

                  <!-- Weather Details -->
                  <div class="grid grid-cols-2 gap-3 mb-4">
                    <div v-for="(detail, index) in weatherDetails" :key="index" class="bg-gray-50 rounded-lg p-2 transition-all duration-300 hover:bg-gray-100">
                      <div class="flex items-center space-x-2">
                        <component :is="detail.icon" :class="['h-4 w-4', getDetailIconColor(detail.label)]" />
                        <div>
                          <p class="text-xs text-gray-500">{{ detail.label }}</p>
                          <p class="text-sm font-semibold text-gray-900">{{ detail.value }}</p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- 7-Day Forecast -->
                  <div>
                    <h4 class="text-xs font-semibold mb-2 text-gray-900">7-Day Forecast</h4>
                    <div class="grid grid-cols-7 gap-1">
                      <div 
                        v-for="(day, index) in forecast" 
                        :key="index" 
                        class="flex flex-col items-center p-1 rounded-lg transition-all duration-300 hover:bg-gray-50"
                      >
                        <span class="text-[10px] mb-1 text-gray-600">
                          {{ new Date(day.date).toLocaleDateString('en-US', { weekday: 'short' }) }}
                        </span>

                        <!-- Use actual condition if available -->
                        <component 
                          :is="getWeatherIcon(day.temp || 'Clear')" 
                          class="h-6 w-6 mb-1 text-yellow-500"
                        />

                        <span class="text-xs font-bold text-gray-900">
                          {{ typeof day.temp === 'number' ? `${day.temp.toFixed(1)}°` : 'N/A' }}
                        </span>
                      </div>
                    </div>
                  </div>

                </div>
              </div>

              <!-- Second Row - Soil Moisture and Humidity -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Enhanced Soil Moisture Card -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-emerald-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
                  <!-- Header section with adjusted text sizes and spacing -->
                  <div class="flex flex-col items-start space-y-2 mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-emerald-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <Sprout class="w-4 h-4 text-emerald-500" />
                        <h3 class="text-sm font-semibold text-emerald-700 tracking-wide">Soil Moisture</h3>
                      </div>
                      <div class="bg-emerald-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                        LIVE
                      </div>
                    </div>
                    <div class="w-full">
                      <p class="text-xs text-emerald-600 font-medium bg-emerald-100 px-3 py-1 rounded-full shadow-sm inline-block">
                        Last 24 Hours
                      </p>
                    </div>
                  </div>

                  <!-- Current Value with Enhanced Styling -->
                  <div class="flex items-center space-x-3 mb-6">
                    <div class="flex-1">
                      <div class="flex items-baseline">
                        <span class="text-3xl font-bold text-emerald-600">{{ soilMoisture ?? '0.0' }}%</span>
                        <span
                          class="ml-2 text-sm font-medium"
                          :class="getSoilMoistureStatus(todayReading?.soilMoisture).color"
                        >
                          {{ getSoilMoistureStatus(todayReading?.soilMoisture).label }}
                        </span>
                      </div>
                      <div class="flex items-center mt-1" v-if="soilMoistureChange">
                        <component
                          :is="soilMoistureChange.direction === 'up' ? ArrowUp : ArrowDown"
                          class="w-4 h-4 mr-1"
                          :class="soilMoistureChange.direction === 'up' ? 'text-emerald-500' : 'text-red-500'"
                        />
                        <span
                          class="text-xs font-medium"
                          :class="soilMoistureChange.direction === 'up' ? 'text-emerald-600' : 'text-red-600'"
                        >
                          {{ soilMoistureChange.percent }}% {{ soilMoistureChange.direction === 'up' ? 'increase' : 'decrease' }} from yesterday
                        </span>
                      </div>

                    </div>
                    <div class="bg-emerald-50 p-3 rounded-2xl">
                      <Droplets class="w-8 h-8 text-emerald-500" />
                    </div>
                  </div>

                  <!-- Enhanced Chart Container -->
                  <div class="bg-white rounded-xl p-4 border border-emerald-100">
                    <div class="h-[180px]">
                      <canvas ref="soilMoistureChartRef"></canvas>
                    </div>
                  </div>
                </div>

                <!-- Enhanced Humidity Card -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-sky-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
                  <!-- Header section with adjusted text sizes and spacing -->
                  <div class="flex flex-col items-start space-y-2 mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-sky-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <Droplets class="w-4 h-4 text-sky-500" />
                        <h3 class="text-sm font-semibold text-sky-700 tracking-wide">Humidity</h3>
                      </div>
                      <div class="bg-sky-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                        LIVE
                      </div>
                    </div>
                    <div class="w-full">
                      <p class="text-xs text-sky-600 font-medium bg-sky-100 px-3 py-1 rounded-full shadow-sm inline-block">
                        Last 24 Hours
                      </p>
                    </div>
                  </div>

                  <!-- Current Value with Enhanced Styling -->
                  <div class="flex items-center space-x-3 mb-6">
                    <div class="flex-1">
                      <div class="flex items-baseline">
                        <span class="text-3xl font-bold text-sky-600">{{ humidity % 100 ?? '0.0'}}</span>
                        <span
                          class="ml-2 text-sm font-medium"
                          :class="getHumidityStatus(todayReading?.humidity).color"
                        >
                          {{ getHumidityStatus(todayReading?.humidity).label }}
                        </span>


                      </div>
                      <div class="flex items-center mt-1" v-if="humidityChange">
                        <component
                          :is="humidityChange.direction === 'up' ? ArrowUp : ArrowDown"
                          class="w-4 h-4 mr-1"
                          :class="humidityChange.direction === 'up' ? 'text-emerald-500' : 'text-red-500'"
                        />
                        <span
                          class="text-xs font-medium"
                          :class="humidityChange.direction === 'up' ? 'text-emerald-600' : 'text-red-600'"
                        >
                          {{ humidityChange.percent }}% {{ humidityChange.direction === 'up' ? 'increase' : 'decrease' }} from yesterday
                        </span>
                      </div>

                    </div>
                    <div class="bg-sky-50 p-3 rounded-2xl">
                      <Cloud class="w-8 h-8 text-sky-500" />
                    </div>
                  </div>

                  <!-- Enhanced Chart Container -->
                  <div class="bg-white rounded-xl p-4 border border-sky-100">
                    <div class="h-[180px]">
                      <canvas ref="humidityChartRef"></canvas>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Third Row - Temperature and Soil pH -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Enhanced Temperature Card -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-red-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
                  <!-- Header section with adjusted text sizes and spacing -->
                  <div class="flex flex-col items-start space-y-2 mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-red-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <Thermometer class="w-4 h-4 text-red-500" />
                        <h3 class="text-sm font-semibold text-red-700 tracking-wide">Temperature</h3>
                      </div>
                      <div class="bg-red-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                        LIVE
                      </div>
                    </div>
                    <div class="w-full">
                      <p class="text-xs text-red-600 font-medium bg-red-100 px-3 py-1 rounded-full shadow-sm inline-block">
                        Last 24 Hours
                      </p>
                    </div>
                  </div>

                  <!-- Current Value with Enhanced Styling -->
                  <div class="flex items-center space-x-3 mb-6">
                    <div class="flex-1">
                      <div class="flex items-baseline">
                        <span class="text-3xl font-bold text-red-600">{{ temperature ?? '0.0' }}°C</span>
                        <span
                          class="ml-2 text-sm font-medium"
                          :class="getTemperatureStatus(todayReading?.temperature).color"
                        >
                          {{ getTemperatureStatus(todayReading?.temperature).label }}
                        </span>
                      </div>
                      <div class="flex items-center mt-1" v-if="temperatureChange">
                        <component
                          :is="temperatureChange.direction === 'up' ? ArrowUp : ArrowDown"
                          class="w-4 h-4 mr-1"
                          :class="temperatureChange.direction === 'up' ? 'text-emerald-500' : 'text-red-500'"
                        />
                        <span
                          class="text-xs font-medium"
                          :class="temperatureChange.direction === 'up' ? 'text-emerald-600' : 'text-red-600'"
                        >
                          {{ temperatureChange.percent }}°C {{ temperatureChange.direction === 'up' ? 'increase' : 'decrease' }} from yesterday
                        </span>
                      </div>
                    </div>
                    <div class="bg-red-50 p-3 rounded-2xl">
                      <Sun class="w-8 h-8 text-red-500" />
                    </div>
                  </div>

                  <!-- Enhanced Chart Container -->
                  <div class="bg-white rounded-xl p-4 border border-red-100">
                    <div class="h-[180px]">
                      <canvas ref="temperatureChartRef"></canvas>
                    </div>
                  </div>
                </div>

                <!-- Enhanced Soil pH Card -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-orange-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
                  <!-- Header section with adjusted text sizes and spacing -->
                  <div class="flex flex-col items-start space-y-2 mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-orange-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <Beaker class="w-4 h-4 text-orange-500" />
                        <h3 class="text-sm font-semibold text-orange-700 tracking-wide">Soil pH</h3>
                      </div>
                      <div class="bg-orange-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                        LIVE
                      </div>
                    </div>
                    <div class="w-full">
                      <p class="text-xs text-orange-600 font-medium bg-orange-100 px-3 py-1 rounded-full shadow-sm inline-block">
                        Last 24 Hours
                      </p>
                    </div>
                  </div>

                  <!-- Current Value with Enhanced Styling -->
                  <div class="flex items-center space-x-3 mb-6">
                    <div class="flex-1">
                      <div class="flex items-baseline">
                        <span class="text-3xl font-bold text-orange-600">{{ soilpH ?? '0.0' }}</span>
                        <span
                          class="ml-2 text-sm font-medium"
                          :class="getPhStatus(todayReading?.soilPh).color"
                        >
                          {{ getPhStatus(todayReading?.soilPh).label }}
                        </span>
                      </div>
                      <div class="flex items-center mt-1" v-if="soilPhChange">
                        <component
                          :is="soilPhChange.direction === 'up' ? ArrowUp : ArrowDown"
                          class="w-4 h-4 mr-1"
                          :class="soilPhChange.direction === 'up' ? 'text-emerald-500' : 'text-red-500'"
                        />
                        <span
                          class="text-xs font-medium"
                          :class="soilPhChange.direction === 'up' ? 'text-emerald-600' : 'text-red-600'"
                        >
                          {{ soilPhChange.percent }}% {{ soilPhChange.direction === 'up' ? 'increase' : 'decrease' }} from yesterday
                        </span>
                      </div>
                    </div>
                    <div class="bg-orange-50 p-3 rounded-2xl">
                      <FlaskConical class="w-8 h-8 text-orange-500" />
                    </div>
                  </div>

                  <!-- Enhanced Chart Container -->
                  <div class="bg-white rounded-xl p-4 border border-orange-100">
                    <div class="h-[180px]">
                      <canvas ref="soilPhChartRef"></canvas>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Fourth Row - Overall Performance -->
              <div class="bg-white rounded-2xl p-6 shadow-lg border border-green-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
                <!-- Enhanced Header section with adjusted text sizes and spacing -->
                <div class="flex flex-col items-start space-y-2 mb-6">
                  <div class="flex items-center justify-between w-full">
                    <div class="bg-green-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                      <FlaskConical class="w-4 h-4 text-green-500" />
                      <h3 class="text-sm font-semibold text-green-700 tracking-wide">NPK Levels</h3>
                    </div>
                    <div class="bg-green-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                      WEEKLY
                    </div>
                  </div>
                  <div class="w-full">
                    <p class="text-xs text-green-600 font-medium bg-green-100 px-3 py-1 rounded-full shadow-sm inline-block">
                      Weekly Performance Overview
                    </p>
                  </div>
                </div>

                <!-- Enhanced Legend Section -->
                <div class="flex flex-wrap gap-3 mb-6">
                  <div v-for="(npk, index) in npkLevels" :key="index" 
                      class="flex items-center px-3 py-1.5 rounded-lg transition-all duration-300"
                      :class="`bg-${npk.color}-50 hover:bg-${npk.color}-100`">
                    <div :class="`w-2.5 h-2.5 rounded-full bg-${npk.color}-400 mr-2 ring-2 ring-${npk.color}-400/30`"></div>
                    <span :class="`text-sm font-medium text-${npk.color}-700`">{{ npk.title }}</span>
                  </div>
                </div>

                <!-- Enhanced Circular Progress Section -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                  <div
                    v-for="(npk, index) in npkLevels"
                    :key="index"
                    :class="`p-4 rounded-xl border border-${npk.color}-100 bg-${npk.color}-50/30 backdrop-blur-sm transition-all duration-300 hover:shadow-lg hover:scale-105`"
                  >
                    <div class="text-center">
                      <div class="relative inline-flex items-center justify-center">
                        <svg class="w-32 h-32 transform -rotate-90">
                          <!-- Background circle -->
                          <circle
                            stroke-width="12"
                            :stroke="npk.title === 'Nitrogen' ? '#4ADE80' : npk.title === 'Phosphorus' ? '#60A5FA' : '#A78BFA'"
                            fill="transparent"
                            r="56"
                            cx="64"
                            cy="64"
                            opacity="0.2"
                          />

                          <!-- Foreground animated circle -->
                          <circle
                            stroke-width="12"
                            :stroke="npk.title === 'Nitrogen' ? '#4ADE80' : npk.title === 'Phosphorus' ? '#60A5FA' : '#A78BFA'"
                            :stroke-dasharray="circumference"
                            :stroke-dashoffset="getDashOffset(npk.value)"
                            stroke-linecap="round"
                            fill="transparent"
                            r="56"
                            cx="64"
                            cy="64"
                          >
                            <animate
                              attributeName="stroke-dashoffset"
                              :from="circumference"
                              :to="getDashOffset(npk.value)"
                              dur="1.5s"
                              fill="freeze"
                              calcMode="spline"
                              keySplines="0.4 0 0.2 1"
                            />
                          </circle>
                        </svg>

                        <!-- Text inside circle -->
                        <div class="absolute inset-0 flex flex-col items-center justify-center">
                          <span :class="`text-3xl font-bold text-${npk.color}-700`">
                            {{ Number(npk.value?.value || 0).toFixed(1) }}%
                          </span>
                          <span :class="`text-sm font-medium text-${npk.color}-600 mt-1`">
                            {{ npk.title }}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>


                <!-- Enhanced Chart Container -->
                <div class="bg-white rounded-xl p-4 border border-green-100 transition-all duration-300 hover:shadow-md">
                  <div class="h-[300px]">
                    <canvas ref="performanceChartRef"></canvas>
                  </div>
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
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { Chart, registerables } from 'chart.js';
import { 
  Sprout,
  Thermometer, 
  Droplets,
  Waves, 
  Power,
  Leaf,
  TestTube,
  TestTubes,
  Beaker,
  CloudSun,
  Cloud, 
  CloudRain, 
  Sun, 
  CloudLightning,
  CloudDrizzle,
  Wind,
  ArrowUp,
  ArrowDown,
  FlaskConical
} from 'lucide-vue-next';
import Sidebar from '../layout/Sidebar.vue'
import api from '../../api/index'

Chart.register(...registerables);

const lineChartRefs = ref([]);
const waterLevel = ref(0);

// Refs for chart instances
const soilMoistureChartInstance = ref(null);
const humidityChartInstance = ref(null);
const temperatureChartInstance = ref(null);
const soilPhChartInstance = ref(null);
const performanceChartInstance = ref(null);

// Refs for chart DOM elements
const performanceChartRef = ref(null);
const soilMoistureChartRef = ref(null);
const humidityChartRef = ref(null);
const temperatureChartRef = ref(null);
const soilPhChartRef = ref(null);

// Update the motorStatus and motorStatusPercentage variables
const motorStatus = ref(false);
const motorOnPercentage = ref(65.7); 

// const circumference = 2 * Math.PI * 48;
const dashOffset = computed(() => circumference * (1 - motorOnPercentage.value / 100));


const weatherData = ref({})
const npkData = ref({})
const weather = ref(null)
const forecast = ref([])
let socket

const nitrogen = ref(null)
const phosphorus = ref(null)
const potassium = ref(null)
const soilpH = ref(null)
const temperature = ref(null)
const humidity = ref(null)
const soilMoisture = ref(null)
const sensorReadings = ref([]);


const weeklyData = [
  { label: 'M', percentage: 70 },
  { label: 'T', percentage: 65 },
  { label: 'W', percentage: 80 },
  { label: 'T', percentage: 55 },
  { label: 'F', percentage: 75 },
  { label: 'S', percentage: 50 },
  { label: 'S', percentage: 65 },
];

const metrics = [
  {
    title: 'Soil Moisture',
    value: '45%',
    icon: Sprout,
    iconColor: 'text-emerald-500',
    type: 'line',
    chartData: {
      labels: ['0', '10', '20', '30', '40', '50'],
      datasets: [{
        data: [30, 40, 45, 50, 45, 45],
        borderColor: '#10b981',
        backgroundColor: 'rgba(16, 185, 129, 0.1)',
        fill: true
      }]
    }
  },
  {
    title: 'Temperature',
    value: '28°C',
    icon: Thermometer,
    iconColor: 'text-red-500',
    type: 'line',
    chartData: {
      labels: ['0', '10', '20', '30', '40', '50'],
      datasets: [{
        data: [25, 27, 28, 28, 29, 28],
        borderColor: '#ef4444',
        backgroundColor: 'rgba(239, 68, 68, 0.1)',
        fill: true
      }]
    }
  },
  {
    title: 'Soil pH',
    value: '7.22',
    icon: Beaker,
    iconColor: 'text-orange-600',
    type: 'line',
    chartData: {
      labels: ['0', '10', '20', '30', '40', '50'],
      datasets: [{
        data: [7.1, 7.15, 7.22, 7.2, 7.25, 7.22],
        borderColor: '#f97316',
        backgroundColor: 'rgba(249, 115, 22, 0.1)',
        fill: true,
        tension: 0.4
      }]
    }
  }
];

// const latestNpk = computed(() => sensorReadings.value.length > 0 ? sensorReadings.value[0] : {});

// const totalNpk = computed(() => {
//   const { nitrogen = 0, phosphorus = 0, potassium = 0 } = latestNpk.value;
//   return nitrogen + phosphorus + potassium;
// });

// const npkLevels = [
//   {
//     title: 'Nitrogen',
//     value: computed(() => {
//       const { nitrogen = 0 } = latestNpk.value;
//       return totalNpk.value > 0 ? (nitrogen / totalNpk.value) * 100 : 0;
//     }),
//     color: 'green'
//   },
//   {
//     title: 'Phosphorus',
//     value: computed(() => {
//       const { phosphorus = 0 } = latestNpk.value;
//       return totalNpk.value > 0 ? (phosphorus / totalNpk.value) * 100 : 0;
//     }),
//     color: 'blue'
//   },
//   {
//     title: 'Potassium',
//     value: computed(() => {
//       const { potassium = 0 } = latestNpk.value;
//       return totalNpk.value > 0 ? (potassium / totalNpk.value) * 100 : 0;
//     }),
//     color: 'purple'
//   }
// ];

// const circumference = 2 * Math.PI * 56;

// const getDashOffset = (val) => {
//   const value = typeof val === 'object' && 'value' in val ? val.value : val;
//   return circumference - (value / 100) * circumference;
// };


// Step 1: Calculate average values
const avgNitrogen = computed(() => {
  const total = sensorReadings.value.reduce((sum, r) => sum + (r.nitrogen || 0), 0);
  return sensorReadings.value.length ? total / sensorReadings.value.length : 0;
});

const avgPhosphorus = computed(() => {
  const total = sensorReadings.value.reduce((sum, r) => sum + (r.phosphorus || 0), 0);
  return sensorReadings.value.length ? total / sensorReadings.value.length : 0;
});

const avgPotassium = computed(() => {
  const total = sensorReadings.value.reduce((sum, r) => sum + (r.potassium || 0), 0);
  return sensorReadings.value.length ? total / sensorReadings.value.length : 0;
});

// Step 2: Normalize so total = 100%
const totalNpk = computed(() => avgNitrogen.value + avgPhosphorus.value + avgPotassium.value);

const npkLevels = [
  {
    title: 'Nitrogen',
    value: computed(() =>
      totalNpk.value > 0 ? (avgNitrogen.value / totalNpk.value) * 100 : 0
    ),
    color: 'green',
  },
  {
    title: 'Phosphorus',
    value: computed(() =>
      totalNpk.value > 0 ? (avgPhosphorus.value / totalNpk.value) * 100 : 0
    ),
    color: 'blue',
  },
  {
    title: 'Potassium',
    value: computed(() =>
      totalNpk.value > 0 ? (avgPotassium.value / totalNpk.value) * 100 : 0
    ),
    color: 'purple',
  },
];

const circumference = 2 * Math.PI * 56;
const getDashOffset = (val) => {
  const value = typeof val === 'object' && 'value' in val ? val.value : val;
  return circumference - (value / 100) * circumference;
};


const lineChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    }
  },
  scales: {
    x: {
      display: true,
      grid: {
        display: false
      }
    },
    y: {
      display: true,
      beginAtZero: true,
      max: 100,
      ticks: {
        stepSize: 10
      }
    }
  },
  elements: {
    line: {
      tension: 0.4
    },
    point: {
      radius: 4
    }
  }
};

// Function to toggle motor status
const toggleMotorStatus = () => {
  motorStatus.value = !motorStatus.value;
};


onMounted(() => {
  const protocol = location.protocol === 'https:' ? 'wss' : 'ws'
  const host = 'localhost:8000'
  const socket = new WebSocket(`${protocol}://${host}/api/weather/ws/weather`)

  socket.onopen = () => {
    console.log('[Weather WS] Connected')
  }

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data)
    console.log('[Weather WS] Data received:', data)

    weather.value = data.current_weather
    forecast.value = data.forecast_7_days.map(day => ({
      ...day,
      temp: parseFloat(day.temperature_max),
      condition: day.condition || 'Clear'  // optional: adjust if CSV has this
    }))
  }

  socket.onerror = (err) => {
    console.error('[Weather WS] Error:', err)
  }

  socket.onclose = () => {
    console.warn('[Weather WS] Disconnected')
  }

  const eventSource = new EventSource('http://localhost:8000/api/stream')
    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data)
      nitrogen.value = data.nitrogen
      phosphorus.value = data.phosphorus
      potassium.value = data.potassium
      soilpH.value = data.soilPh
      temperature.value = data.temperature
      humidity.value = data.humidity
      soilMoisture.value = data.soilMoisture
    }

  const eventWaterSource = new EventSource('http://localhost:8000/api/water-stream')

  eventWaterSource.onmessage = (event) => {
    const data = JSON.parse(event.data)

    if (data.type === 'water') {
      waterLevel.value = data.data.waterLevel
      console.log("💧 Updated Water Level:", waterLevel.value + "%")
    }
  }

eventSource.onerror = (e) => {
  console.error("❌ SSE Error:", e)
}
  
  fetchSensorData();
})

const fetchSensorData = async () => {
  try {
    const res = await api.get('/sensor/readings')
    sensorReadings.value = res.data
    console.log(sensorReadings)
    initAllCharts()
  } catch (err) {
    console.error("Error fetching sensor data:", err)
  }
}


const initAllCharts = () => {
  if (!sensorReadings.value.length) return;

  const readings = sensorReadings.value.slice(0, 6).reverse(); // get recent 6 data points
  const labels = readings.map(r => new Date(r.timestamp).toLocaleTimeString());

  const extract = (key) => readings.map(r => r[key]);

  if (soilMoistureChartRef.value) {
    const data = extract('soilMoisture');
    const maxY = getMaxY(data);

    soilMoistureChartInstance.value = new Chart(soilMoistureChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels,
        datasets: [{
          label: 'Soil Moisture',
          data,
          borderColor: '#10b981',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          fill: true,
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: maxY,
            ticks: { stepSize: maxY / 5 }
          }
        }
      }
    });
  }


  if (humidityChartRef.value) {
    const data = extract('humidity');
    const maxY = getMaxY(data);

    humidityChartInstance.value = new Chart(humidityChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels,
        datasets: [{
          label: 'Humidity',
          data,
          borderColor: '#0ea5e9',
          backgroundColor: 'rgba(14, 165, 233, 0.1)',
          fill: true,
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: maxY,
            ticks: { stepSize: maxY / 5 }
          }
        }
      }
    });
  }


  if (temperatureChartRef.value) {
    const data = extract('temperature');
    const maxY = getMaxY(data);

    temperatureChartInstance.value = new Chart(temperatureChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels,
        datasets: [{
          label: 'Temperature',
          data,
          borderColor: '#ef4444',
          backgroundColor: 'rgba(239, 68, 68, 0.1)',
          fill: true,
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: maxY,
            ticks: { stepSize: maxY / 5 }
          }
        }
      }
    });
  }


  if (soilPhChartRef.value) {
    const data = extract('soilPh');
    const maxY = Math.ceil(Math.max(...data) * 10) / 10;
    const minY = Math.floor(Math.min(...data) * 10) / 10;

    soilPhChartInstance.value = new Chart(soilPhChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels,
        datasets: [{
          label: 'Soil pH',
          data,
          borderColor: '#f97316',
          backgroundColor: 'rgba(249, 115, 22, 0.1)',
          fill: true,
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: false,
            min: minY,
            max: maxY,
            ticks: {
              stepSize: 0.2
            }
          }
        }
      }
    });
  }


  if (performanceChartRef.value) {
    const readings = sensorReadings.value.slice(0, 8).reverse();
    const labels = readings.map(r => new Date(r.timestamp).toLocaleDateString());

    const nitrogenData = readings.map(r => r.nitrogen || 0);
    const phosphorusData = readings.map(r => r.phosphorus || 0);
    const potassiumData = readings.map(r => r.potassium || 0);

    const maxNpk = Math.max(...nitrogenData, ...phosphorusData, ...potassiumData);
    const maxY = Math.ceil(maxNpk / 10) * 10;

    performanceChartInstance.value = new Chart(performanceChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels,
        datasets: [
          {
            label: 'Nitrogen',
            data: nitrogenData,
            borderColor: '#4ADE80',
            backgroundColor: 'rgba(74, 222, 128, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#4ADE80'
          },
          {
            label: 'Phosphorus',
            data: phosphorusData,
            borderColor: '#60A5FA',
            backgroundColor: 'rgba(96, 165, 250, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#60A5FA'
          },
          {
            label: 'Potassium',
            data: potassiumData,
            borderColor: '#A78BFA',
            backgroundColor: 'rgba(167, 139, 250, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#A78BFA'
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
            position: 'top'
          },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'white',
            titleColor: '#374151',
            bodyColor: '#374151',
            borderColor: '#E5E7EB',
            borderWidth: 1,
            padding: 12,
            displayColors: true
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { color: '#6B7280' }
          },
          y: {
            beginAtZero: true,
            max: maxY,
            ticks: {
              stepSize: maxY / 5,
              color: '#6B7280'
            },
            grid: { color: '#E5E7EB' }
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });
  }


};

const todayReading = computed(() => {
  return sensorReadings.value.length > 0 ? sensorReadings.value[0] : null;
});

const yesterdayReading = computed(() => {
  const now = new Date();
  const oneDayAgo = new Date(now.getTime() - 24 * 60 * 60 * 1000);

  return sensorReadings.value.find(r => {
    const ts = new Date(r.timestamp);
    return ts < oneDayAgo; // First reading older than 24h
  });
});

function getChange(current, previous) {
  if (current === null || previous === null || previous === 0) return null;
  const diff = current - previous;
  const percent = (diff / previous) * 100;
  return {
    direction: diff >= 0 ? 'up' : 'down',
    percent: Math.abs(percent).toFixed(1)
  };
}

const soilMoistureChange = computed(() => {
  return getChange(todayReading.value?.soilMoisture, yesterdayReading.value?.soilMoisture);
});

const humidityChange = computed(() => {
  return getChange(todayReading.value?.humidity, yesterdayReading.value?.humidity);
});

const temperatureChange = computed(() => {
  return getChange(todayReading.value?.temperature, yesterdayReading.value?.temperature);
});

const soilPhChange = computed(() => {
  return getChange(todayReading.value?.soilPh, yesterdayReading.value?.soilPh);
});


const readings = sensorReadings.value.slice(0, 8).reverse();

const nitrogenData = readings.map(r => r.nitrogen || 0);
const phosphorusData = readings.map(r => r.phosphorus || 0);
const potassiumData = readings.map(r => r.potassium || 0);

function getSoilMoistureStatus(value) {
  if (value <= 30) return { label: 'Too Dry', color: 'text-red-500' };
  if (value <= 55) return { label: 'Moist (Optimal)', color: 'text-emerald-500' };
  if (value <= 75) return { label: 'Wet', color: 'text-yellow-500' };
  return { label: 'Too Wet', color: 'text-blue-500' };
}

function getHumidityStatus(value) {
  if (value <= 30) return { label: 'Very Dry', color: 'text-red-500' };
  if (value <= 50) return { label: 'Comfortable', color: 'text-emerald-500' };
  if (value <= 70) return { label: 'Humid', color: 'text-yellow-500' };
  return { label: 'Very Humid', color: 'text-blue-500' };
}

function getTemperatureStatus(value) {
  if (value < 20) return { label: 'Too Cold', color: 'text-blue-500' };
  if (value <= 25) return { label: 'Cool', color: 'text-yellow-500' };
  if (value <= 32) return { label: 'Optimal', color: 'text-emerald-500' };
  return { label: 'Too Hot', color: 'text-red-500' };
}

function getPhStatus(value) {
  if (value < 5.5) return { label: 'Too Acidic', color: 'text-red-500' };
  if (value < 6.5) return { label: 'Slightly Acidic', color: 'text-yellow-500' };
  if (value <= 7.5) return { label: 'Neutral (Optimal)', color: 'text-emerald-500' };
  return { label: 'Alkaline', color: 'text-blue-500' };
}

// Get highest value among all NPK
const maxNpk = Math.max(
  ...nitrogenData,
  ...phosphorusData,
  ...potassiumData
);

// Round up to nearest multiple of 10 (for clean y-axis)
const maxY = Math.ceil(maxNpk / 10) * 10;

const getMaxY = (data, step = 10) => {
  const max = Math.max(...data);
  return Math.ceil(max / step) * step;
};

onBeforeUnmount(() => {
    if (socket) socket.close()
    try {
      performanceChartInstance.value?.destroy()
      soilMoistureChartInstance.value?.destroy()
      humidityChartInstance.value?.destroy()
      temperatureChartInstance.value?.destroy()
      soilPhChartInstance.value?.destroy()
    } catch (e) {
      console.warn('Error while destroying chart:', e)
    }
})

const weatherDetails = computed(() => {
  if (!weather.value) return []
  return [
    { label: 'Humidity', value: weather.value.humidity + '%', icon: Droplets },
    { label: 'Wind', value: weather.value.wind_speed_ms + ' m/s', icon: Wind },
    { label: 'Precipitation', value: weather.value.rain_mm + ' mm', icon: CloudRain },
    { label: 'UV Index', value: weather.value.uv, icon: Sun },
  ]
})

// Add new helper function for weather icon colors
const getWeatherIconColor = (weather) => {
  switch (weather) {
    case 'sunny':
      return 'text-amber-400';
    case 'partly-cloudy':
      return 'text-blue-400';
    case 'cloudy':
      return 'text-gray-400';
    case 'rainy':
      return 'text-blue-500';
    case 'stormy':
      return 'text-indigo-600';
    case 'drizzle':
      return 'text-blue-400';
    default:
      return 'text-blue-500';
  }
};

const getWeatherIcon = (temperature) => {
  const temp = typeof temperature === 'number' ? temperature : parseFloat(temperature);

  if (isNaN(temp)) return Cloud; // fallback if invalid

  if (temp >= 32) {
    return Sun; // very hot
  } else if (temp >= 26 && temp < 32) {
    return CloudSun; // warm and partly cloudy
  } else if (temp >= 20 && temp < 26) {
    return Cloud; // moderate
  } else if (temp >= 15 && temp < 20) {
    return CloudDrizzle; // cool and damp
  } else if (temp >= 5 && temp < 15) {
    return CloudRain; // cold rain
  } else if (temp >= -5 && temp < 5) {
    return Snowflake; // cold
  } else {
    return CloudLightning; // extreme cold/storm
  }
};

// Add new helper function for detail icon colors
const getDetailIconColor = (label) => {
  switch (label) {
    case 'Humidity':
      return 'text-blue-500';
    case 'Wind Speed':
      return 'text-teal-500';
    case 'Precipitation':
      return 'text-indigo-500';
    case 'UV Index':
      return 'text-amber-500';
    default:
      return 'text-gray-500';
  }
};

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Enhanced scrollbar styling */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(20, 83, 45, 0.1);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: rgba(20, 83, 45, 0.5);
  border-radius: 4px;
  transition: background-color 200ms;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(20, 83, 45, 0.7);
}

/* Smooth transitions */
* {
  transition: all 200ms ease-in-out;
}

/* Ensure proper layout on different browsers */
@supports (-webkit-touch-callout: none) {
  .h-screen {
    height: -webkit-fill-available;
  }
}

/* Firefox scrollbar styling */
* {
  scrollbar-width: thin;
  scrollbar-color: rgba(20, 83, 45, 0.5) rgba(20, 83, 45, 0.1);
}

/* Weather card styles */
.weather-card-gradient {
  background: linear-gradient(
    135deg,
    rgba(186, 230, 253, 0.2) 0%,
    rgba(147, 197, 253, 0.3) 100%
  );
}

/* Glassmorphism effects */
.glass-effect {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Weather icon animations */
@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0);
  }
  50% {
    transform: translateY(-6px) rotate(2deg);
  }
}

.weather-icon-wrapper {
  position: relative;
  padding: 1rem;
  border-radius: 50%;
  background: rgba(243, 244, 246, 0.5);
  transition: all 0.3s ease;
}

.weather-icon-wrapper:hover {
  background: rgba(243, 244, 246, 0.8);
  transform: translateY(-2px);
}

.weather-icon-wrapper svg {
  animation: float 3s ease-in-out infinite;
}

/* Temperature gradient text */
.temperature-text {
  background: linear-gradient(135deg, #f97316, #ef4444);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Water tank styles */
.water-tank-container {
  perspective: 1200px;
}

.water-tank {
  transform: rotateX(12deg) rotateY(-22deg);
  transform-style: preserve-3d;
  transition: all 0.4s ease;
}

.water-tank:hover {
  transform: rotateX(15deg) rotateY(-28deg) scale(1.05);
  filter: drop-shadow(0 20px 30px rgba(59, 130, 246, 0.1));
}

/* Power button styles */
.power-button-container {
  perspective: 1000px;
}

.power-button {
  transform: translateZ(0) rotateX(10deg);
  transform-style: preserve-3d;
  transition: all 0.4s ease;
}

.power-button:hover {
  transform: translateZ(10px) rotateX(15deg) scale(1.05);
}

.power-button:active {
  transform: translateZ(0) rotateX(10deg) scale(0.95);
}

.power-on {
  box-shadow: 
    0 0 0 2px rgba(168, 85, 247, 0.5),
    0 0 20px 5px rgba(168, 85, 247, 0.5),
    0 0 0 4px rgba(168, 85, 247, 0.3);
}

.power-off {
  box-shadow: 
    0 0 0 2px rgba(168, 85, 247, 0.3),
    0 0 15px 2px rgba(168, 85, 247, 0.2),
    0 0 0 4px rgba(168, 85, 247, 0.1);
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.3;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* Chart container styles */
.chart-container {
  position: relative;
  transition: all 0.3s ease;
}

.chart-container:hover {
  transform: scale(1.02);
}

/* Enhanced tooltip styling */
.chartjs-tooltip {
  background-color: rgba(255, 255, 255, 0.95) !important;
  backdrop-filter: blur(8px);
  border-radius: 8px !important;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
}

/* NPK Levels card styles */
.npk-card {
  transition: all 0.3s ease;
}

.npk-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

/* Responsive design adjustments */
@media (max-width: 640px) {
  .grid {
    grid-template-columns: 1fr;
  }
  
  .chart-container {
    height: 250px;
  }
}

@media (min-width: 641px) and (max-width: 1024px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Accessibility improvements */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* Focus styles for better keyboard navigation */
:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

/* Print styles for better readability when printed */
@media print {
  body {
    font-size: 12pt;
  }

  .chart-container {
    break-inside: avoid;
  }

  .no-print {
    display: none;
  }
}

@keyframes longWave1 {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
@keyframes longWave2 {
  0% { transform: translateX(0); }
  100% { transform: translateX(-60%); }
}
@keyframes longWave3 {
  0% { transform: translateX(0); }
  100% { transform: translateX(-70%); }
}

.animate-long-wave-1 {
  animation: longWave1 4s linear infinite;
}
.animate-long-wave-2 {
  animation: longWave2 7s linear infinite;
}
.animate-long-wave-3 {
  animation: longWave3 10s linear infinite;
}

.tank-style {
  background: linear-gradient(to top, #e0f2fe, #f8fafc);
  box-shadow:
    inset 0 0 15px rgba(59, 130, 246, 0.2),
    0 10px 20px rgba(0, 0, 0, 0.05);
  border-radius: 2rem;
}
</style>

