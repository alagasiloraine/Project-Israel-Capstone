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
            <!-- Top Metrics Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6 mb-10">
              <!-- Nitrogen Level -->
              <div class="group bg-white rounded-2xl p-5 border-2 border-green-100 shadow-lg transition-all duration-300 hover:border-green-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-3">
                  <Leaf class="h-6 w-6 text-green-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-green-600 bg-green-100 px-2 py-1 rounded-full">N</span>
                </div>
                <div class="text-2xl font-bold text-green-700">{{ nitrogen }}</div>
                <div class="text-xs text-green-600">Nitrogen (mg/kg)</div>  
              </div>

              <!-- Phosphorus Level -->
              <div class="group bg-white rounded-2xl p-5 border-2 border-blue-100 shadow-lg transition-all duration-300 hover:border-blue-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-3">
                  <TestTube class="h-6 w-6 text-blue-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-blue-600 bg-blue-100 px-2 py-1 rounded-full">P</span>
                </div>
                <div class="text-2xl font-bold text-blue-700">{{ phosphorus }}</div>
                <div class="text-xs text-blue-600">Phosphorus (mg/kg)</div>
              </div>

              <!-- Potassium Level -->
              <div class="group bg-white rounded-2xl p-5 border-2 border-purple-100 shadow-lg transition-all duration-300 hover:border-purple-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-3">
                  <TestTubes class="h-6 w-6 text-purple-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-purple-600 bg-purple-100 px-2 py-1 rounded-full">K</span>
                </div>
                <div class="text-2xl font-bold text-purple-700">{{ potassium }}</div>
                <div class="text-xs text-purple-600">Potassium (mg/kg)</div>
              </div>

              <!-- Soil pH Level -->
              <div class="group bg-white rounded-2xl p-5 border-2 border-orange-100 shadow-lg transition-all duration-300 hover:border-orange-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-3">
                  <Beaker class="h-6 w-6 text-orange-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-orange-600 bg-orange-100 px-2 py-1 rounded-full">pH</span>
                </div>
                <div class="text-2xl font-bold text-orange-700">{{ soilpH }}</div>
                <div class="text-xs text-orange-600">Soil pH Level</div>
              </div>

              <!-- Temperature -->
              <div class="group bg-white rounded-2xl p-5 border-2 border-red-100 shadow-lg transition-all duration-300 hover:border-red-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-3">
                  <Thermometer class="h-6 w-6 text-red-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-red-600 bg-red-100 px-2 py-1 rounded-full">Temp</span>
                </div>
                <div class="text-2xl font-bold text-red-700">{{ temperature }}</div>
                <div class="text-xs text-red-600">Temperature (°C)</div>
              </div>

              <!-- Humidity -->
              <div class="group bg-white rounded-2xl p-5 border-2 border-sky-100 shadow-lg transition-all duration-300 hover:border-sky-400 hover:shadow-xl hover:-translate-y-1">
                <div class="flex items-center justify-between mb-3">
                  <Droplets class="h-6 w-6 text-sky-500 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-semibold text-sky-600 bg-sky-100 px-2 py-1 rounded-full">RH</span>
                </div>
                <div class="text-2xl font-bold text-sky-700">{{ humidity }}</div>
                <div class="text-xs text-sky-600">Humidity (%)</div>
              </div>
            </div>

            <!-- Charts Section -->
            <div class="grid grid-cols-1 gap-8">
              <!-- First Row - Water Level, Motor Status, and Weather -->
              <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Enhanced Water Level Card -->
                <div class="bg-white rounded-2xl p-6 shadow-lg border border-blue-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
                  <!-- Header section with adjusted text sizes and spacing -->
                  <div class="flex flex-col items-start space-y-2 mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-blue-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <Waves class="w-4 h-4 text-blue-500" />
                        <h3 class="text-sm font-semibold text-blue-700 tracking-wide">Water Level</h3>
                      </div>
                      <div class="bg-blue-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                        LIVE
                      </div>
                    </div>
                    <div class="w-full">
                      <p class="text-xs text-blue-600 font-medium bg-blue-100 px-3 py-1 rounded-full shadow-sm inline-block">
                        Current Status
                      </p>
                    </div>
                  </div>
                  
                  <!-- Enhanced 3D Water Tank Visualization with adjusted positioning -->
                  <div class="relative w-52 h-52 mx-auto transform-gpu water-tank-container mt-16">
                    <!-- Main Tank Container with enhanced 3D effect -->
                    <div class="absolute inset-0 transform-gpu water-tank">
                      <!-- Back panel shadow for depth -->
                      <div class="absolute inset-0 bg-blue-50/50 rounded-lg transform translate-x-6 translate-y-2 blur-md"></div>
                      
                      <!-- Front face with enhanced glass effect -->
                      <div class="absolute inset-0 bg-gradient-to-br from-blue-50/90 to-white/80 border-2 border-blue-200 rounded-lg shadow-lg backdrop-blur-sm overflow-hidden">
                        <!-- Water fill with enhanced gradients -->
                        <div 
                          class="absolute bottom-0 left-0 right-0 transition-all duration-300"
                          :style="{ 
                            height: `${waterLevel}%`,
                            background: `linear-gradient(180deg, 
                              rgba(96, 165, 250, 0.2) 0%,
                              rgba(96, 165, 250, 0.4) 50%,
                              rgba(37, 99, 235, 0.5) 100%
                            )`
                          }"
                        >
                          <!-- Enhanced glass reflection effect -->
                          <div class="absolute inset-0 bg-gradient-to-tr from-transparent via-white/10 to-white/30"></div>
                        </div>
                        
                        <!-- Multiple glass reflection layers -->
                        <div class="absolute inset-0">
                          <div class="absolute inset-0 bg-gradient-to-br from-white/50 via-transparent to-transparent"></div>
                          <div class="absolute inset-0 bg-gradient-to-tl from-white/30 via-transparent to-transparent"></div>
                        </div>
                      </div>

                      <!-- Enhanced right side face -->
                      <div class="absolute top-0 bottom-0 right-0 w-8 bg-gradient-to-r from-blue-100/90 to-blue-50/80 transform origin-left skew-y-[45deg] translate-x-8 -translate-y-4 border-r-2 border-t-2 border-blue-200/80 backdrop-blur-sm"></div>

                      <!-- Enhanced top face -->
                      <div class="absolute top-0 left-0 right-8 h-8 bg-gradient-to-b from-blue-50/90 to-white/80 transform origin-bottom skew-x-[45deg] -translate-y-8 border-t-2 border-l-2 border-blue-200/80 backdrop-blur-sm"></div>

                      <!-- Enhanced level markers with better visibility -->
                      <div class="absolute top-2 bottom-2 right-[-32px] w-8 flex flex-col justify-between">
                        <div v-for="n in 5" :key="n" class="flex items-center gap-2">
                          <div class="h-[2px] w-3 bg-blue-400 shadow-sm"></div>
                          <span class="text-xs font-medium text-blue-600 bg-white/80 px-1 rounded">
                            {{ 100 - (n - 1) * 25 }}%
                          </span>
                        </div>
                      </div>

                      <!-- Enhanced percentage display -->
                      <div class="absolute inset-0 flex items-center justify-center">
                        <div class="bg-white/90 backdrop-blur px-4 py-2 rounded-xl shadow-lg border border-blue-100 transform hover:scale-105 transition-transform duration-300">
                          <span class="text-3xl font-bold text-blue-600 drop-shadow-sm">{{ waterLevel }}%</span>
                        </div>
                      </div>

                      <!-- Additional 3D effects -->
                      <div class="absolute inset-0 rounded-lg shadow-[inset_0_2px_15px_rgba(148,163,184,0.1)] pointer-events-none"></div>
                      <div class="absolute inset-0 rounded-lg ring-1 ring-blue-200/50 ring-inset pointer-events-none"></div>
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

                  <!-- <div class="flex justify-between items-start mb-4">
                    <div class="flex items-center justify-between w-full">
                      <div class="bg-sky-50 rounded-full px-2.5 py-1 flex items-center space-x-1.5 shadow-inner">
                        <CloudSun class="w-4 h-4 text-sky-500" />
                        <h3 class="text-sm font-semibold text-sky-700 tracking-wide">Weather Forecast</h3>
                      </div>
                      <div class="bg-sky-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                        LIVE
                      </div>
                    </div>
                  </div>

                  <div class="flex items-center justify-between mb-4">
                    <div>
                      <div class="flex items-end space-x-1">
                        <p class="text-4xl font-bold text-gray-900">{{ weatherData[6].temp }}</p>
                        <p class="text-xl font-semibold text-gray-600 mb-1">°C</p>
                      </div>
                      <p class="text-base mt-1 text-gray-600">{{ getWeatherDescription(weatherData[6].weather) }}</p>
                    </div>
                    <div class="weather-icon-wrapper">
                      <component 
                        :is="getWeatherIcon(weatherData[6].weather)"
                        :class="['h-14 w-14 transform transition-transform hover:scale-110', getWeatherIconColor(weatherData[6].weather)]"
                      />
                    </div>
                  </div>

                  <div class="grid grid-cols-2 gap-3 mb-4">
                    <div v-for="(detail, index) in weatherDetails" :key="index" 
                         class="bg-gray-50 rounded-lg p-2 transition-all duration-300 hover:bg-gray-100">
                      <div class="flex items-center space-x-2">
                        <component :is="detail.icon" :class="['h-4 w-4', getDetailIconColor(detail.label)]" />
                        <div>
                          <p class="text-xs text-gray-500">{{ detail.label }}</p>
                          <p class="text-sm font-semibold text-gray-900">{{ detail.value }}</p>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div>
                    <h4 class="text-xs font-semibold mb-2 text-gray-900">7-Day Forecast</h4>
                    <div class="grid grid-cols-7 gap-1">
                      <div v-for="(day, index) in weatherData" 
                           :key="index" 
                           class="flex flex-col items-center p-1 rounded-lg transition-all duration-300 hover:bg-gray-50"
                      >
                        <span class="text-[10px] mb-1 text-gray-600">{{ day.date.slice(0, 3) }}</span>
                        <component 
                          :is="getWeatherIcon(day.weather)"
                          :class="['h-6 w-6 mb-1', getWeatherIconColor(day.weather)]"
                        />
                        <span class="text-xs font-bold text-gray-900">{{ day.temp }}°</span>
                      </div>
                    </div>
                  </div> -->
                
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
                        <p class="text-4xl font-bold text-gray-900">{{ weather?.temperature_f }}</p>
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
                      <div v-for="(day, index) in weatherData" :key="index" class="flex flex-col items-center p-1 rounded-lg transition-all duration-300 hover:bg-gray-50">
                        <span class="text-[10px] mb-1 text-gray-600">{{ day.date.slice(0, 3) }}</span>
                        <component 
                          :is="getWeatherIcon(day.weather)"
                          :class="['h-6 w-6 mb-1', getWeatherIconColor(day.weather)]"
                        />
                        <span class="text-xs font-bold text-gray-900">{{ day.temp }}°</span>
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
                        <span class="text-3xl font-bold text-emerald-600">45%</span>
                        <span class="ml-2 text-sm text-emerald-500">Optimal Range</span>
                      </div>
                      <div class="flex items-center mt-1">
                        <ArrowUp class="w-4 h-4 text-emerald-500 mr-1" />
                        <span class="text-xs font-medium text-emerald-600">2.5% increase from yesterday</span>
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
                        <span class="text-3xl font-bold text-sky-600">76.68%</span>
                        <span class="ml-2 text-sm text-sky-500">High Humidity</span>
                      </div>
                      <div class="flex items-center mt-1">
                        <ArrowDown class="w-4 h-4 text-sky-500 mr-1" />
                        <span class="text-xs font-medium text-sky-600">1.2% decrease from yesterday</span>
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
                        <span class="text-3xl font-bold text-red-600">28°C</span>
                        <span class="ml-2 text-sm text-red-500">Normal Range</span>
                      </div>
                      <div class="flex items-center mt-1">
                        <ArrowUp class="w-4 h-4 text-red-500 mr-1" />
                        <span class="text-xs font-medium text-red-600">1.8°C increase from yesterday</span>
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
                        <span class="text-3xl font-bold text-orange-600">7.22</span>
                        <span class="ml-2 text-sm text-orange-500">Neutral pH</span>
                      </div>
                      <div class="flex items-center mt-1">
                        <ArrowUp class="w-4 h-4 text-orange-500 mr-1" />
                        <span class="text-xs font-medium text-orange-600">0.05 increase from yesterday</span>
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
                  <div v-for="(npk, index) in npkLevels" :key="index" 
                      :class="`p-4 rounded-xl border border-${npk.color}-100 bg-${npk.color}-50/30 backdrop-blur-sm transition-all duration-300 hover:shadow-lg hover:scale-105`">
                    <div class="text-center">
                      <div class="relative inline-flex items-center justify-center">
                        <svg class="w-32 h-32 transform -rotate-90">
                          <!-- Background circle with enhanced styling -->
                          <circle
                            :class="`text-${npk.color}-100`"
                            stroke-width="12"
                            :stroke="npk.title === 'Nitrogen' ? '#4ADE80' : npk.title === 'Phosphorus' ? '#60A5FA' : '#A78BFA'"
                            fill="transparent"
                            r="56"
                            cx="64"
                            cy="64"
                            opacity="0.2"
                          />
                          <!-- Progress circle with enhanced styling -->
                          <circle
                            :class="`text-${npk.color}-500`"
                            stroke-width="12"
                            :stroke-dasharray="circumference"
                            :stroke-dashoffset="getDashOffset(npk.value)"
                            stroke-linecap="round"
                            stroke="currentColor"
                            fill="transparent"
                            r="56"
                            cx="64"
                            cy="64"
                          >
                            <!-- Add subtle animation -->
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
                        <!-- Enhanced value display -->
                        <div class="absolute inset-0 flex flex-col items-center justify-center">
                          <span :class="`text-3xl font-bold text-${npk.color}-700`">{{ npk.value }}%</span>
                          <span :class="`text-sm font-medium text-${npk.color}-600 mt-1`">{{ npk.title }}</span>
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

Chart.register(...registerables);

const lineChartRefs = ref([]);
const performanceChartRef = ref(null);
const waterLevel = ref(75);

const soilMoistureChartRef = ref(null);
const humidityChartRef = ref(null);
const temperatureChartRef = ref(null);
const soilPhChartRef = ref(null);

// Update the motorStatus and motorStatusPercentage variables
const motorStatus = ref(false);
const motorOnPercentage = ref(65.7); // Example: motor was on 65.7% of the week

const circumference = 2 * Math.PI * 48;
const dashOffset = computed(() => circumference * (1 - motorOnPercentage.value / 100));


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

const npkLevels = [
  { title: 'Nitrogen', value: 96, color: 'green' },
  { title: 'Phosphorus', value: 23, color: 'blue' },
  { title: 'Potassium', value: 87, color: 'purple' },
];

const getDashOffset = (value) => {
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

// // Weather Data
// const weatherData = ref([
//   { 
//     date: 'Monday', 
//     temp: 22, 
//     weather: 'partly-cloudy',
//     humidity: 65,
//     windSpeed: 12,
//     precipitation: 0
//   },
//   { 
//     date: 'Tuesday', 
//     temp: 24, 
//     weather: 'sunny',
//     humidity: 55,
//     windSpeed: 8,
//     precipitation: 0
//   },
//   { 
//     date: 'Wednesday', 
//     temp: 20, 
//     weather: 'rainy',
//     humidity: 85,
//     windSpeed: 15,
//     precipitation: 25
//   },
//   { 
//     date: 'Thursday', 
//     temp: 23, 
//     weather: 'cloudy',
//     humidity: 70,
//     windSpeed: 10,
//     precipitation: 0
//   },
//   { 
//     date: 'Friday', 
//     temp: 26, 
//     weather: 'sunny',
//     humidity: 50,
//     windSpeed: 5,
//     precipitation: 0
//   },
//   { 
//     date: 'Saturday', 
//     temp: 25, 
//     weather: 'partly-cloudy',
//     humidity: 60,
//     windSpeed: 7,
//     precipitation: 0
//   },
//   { 
//     date: 'Today', 
//     temp: 21, 
//     weather: 'rainy',
//     humidity: 80,
//     windSpeed: 18,
//     precipitation: 15
//   },
// ]);

// // Weather details data
// const weatherDetails = computed(() => [
//   {
//     label: 'Humidity',
//     value: `${weatherData.value[6].humidity}%`,
//     icon: Droplets
//   },
//   {
//     label: 'Wind Speed',
//     value: `${weatherData.value[6].windSpeed} km/h`,
//     icon: Wind
//   },
//   {
//     label: 'Precipitation',
//     value: `${weatherData.value[6].precipitation}%`,
//     icon: CloudRain
//   },
//   {
//     label: 'UV Index',
//     value: 'Low',
//     icon: Sun
//   }
// ]);

const weatherData = ref({})
const npkData = ref({})
const weather = ref(null)
let socket

const nitrogen = ref(null)
const phosphorus = ref(null)
const potassium = ref(null)
const soilpH = ref(null)
const temperature = ref(null)
const humidity = ref(null)
  

onMounted(() => {
    const protocol = location.protocol === 'https:' ? 'wss' : 'ws'
    const host = 'localhost:8000'
    socket = new WebSocket(`${protocol}://${host}/api/weather/ws/weather`)
  
    socket.onopen = () => {
      console.log('[Weather WS] Connected')
    }
  
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data)
      console.log('[Weather WS] Data received:', data)
      weather.value = data
    }
  
    socket.onerror = (err) => {
      console.error('[Weather WS] Error:', err)
    }
  
    socket.onclose = () => {
      console.warn('[Weather WS] Disconnected')
    }

    const eventSource = new EventSource('http://localhost:8000/stream')
      eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data)
        nitrogen.value = data.nitrogen
        phosphorus.value = data.phosphorus
        potassium.value = data.potassium
        soilpH.value = data.soilpH
        temperature.value = data.temperature
        humidity.value = data.humidity
      }


})

onBeforeUnmount(() => {
    if (socket) socket.close()
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


// const getWeatherDescription = (weather) => {
//   switch (weather) {
//     case 'sunny': return 'Clear skies'
//     case 'partly-cloudy': return 'Partly cloudy'
//     case 'cloudy': return 'Overcast'
//     case 'rainy': return 'Rainy'
//     case 'stormy': return 'Thunderstorms'
//     case 'drizzle': return 'Light rain'
//     default: return 'Mixed conditions'
//   }
// }

// const getWeatherIcon = (weather) => {
//   switch (weather) {
//     case 'sunny': return 'SunIcon'
//     case 'partly-cloudy': return 'CloudSunIcon'
//     case 'cloudy': return 'CloudIcon'
//     case 'rainy': return 'CloudRainIcon'
//     case 'stormy': return 'CloudLightningIcon'
//     case 'drizzle': return 'CloudDrizzleIcon'
//     default: return 'CloudIcon'
//   }
// }

// const getWeatherIconColor = (weather) => {
//   switch (weather) {
//     case 'sunny': return 'text-amber-400'
//     case 'partly-cloudy': return 'text-blue-400'
//     case 'cloudy': return 'text-gray-400'
//     case 'rainy': return 'text-blue-500'
//     case 'stormy': return 'text-indigo-600'
//     case 'drizzle': return 'text-blue-400'
//     default: return 'text-blue-500'
//   }
// }

// const getDetailIconColor = (label) => {
//   switch (label) {
//     case 'Humidity': return 'text-blue-500'
//     case 'Wind': return 'text-teal-500'
//     case 'Precipitation': return 'text-indigo-500'
//     case 'UV Index': return 'text-amber-500'
//     default: return 'text-gray-500'
//   }
// }


// Helper Functions

const getWeatherIcon = (weather) => {
  switch (weather) {
    case 'sunny':
      return Sun;
    case 'partly-cloudy':
      return CloudSun;
    case 'cloudy':
      return Cloud;
    case 'rainy':
      return CloudRain;
    case 'stormy':
      return CloudLightning;
    case 'drizzle':
      return CloudDrizzle;
    default:
      return CloudSun;
  }
};

const getWeatherDescription = (weather) => {
  switch (weather) {
    case 'sunny':
      return 'Clear skies';
    case 'partly-cloudy':
      return 'Partly cloudy';
    case 'cloudy':
      return 'Overcast';
    case 'rainy':
      return 'Rainy';
    case 'stormy':
      return 'Thunderstorms';
    case 'drizzle':
      return 'Light rain';
    default:
      return 'Mixed conditions';
  }
};

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

onMounted(() => {
  // Initialize all line charts
  metrics.forEach((metric, index) => {
    if (metric.type === 'line' && lineChartRefs.value[index]) {
      new Chart(lineChartRefs.value[index].getContext('2d'), {
        type: 'line',
        data: metric.chartData,
        options: lineChartOptions
      });
    }
  });

  // Initialize performance chart for NPK Sensor
  if (performanceChartRef.value) {
    new Chart(performanceChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['19 July', '20 July', '21 July', '22 July', '23 July', '24 July', '25 July', '26 July'],
        datasets: [
          {
            label: 'Nitrogen',
            data: [45, 42, 40, 38, 32, 35, 38, 40],
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
            data: [35, 38, 32, 28, 25, 30, 35, 38],
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
            data: [50, 48, 52, 55, 49, 47, 51, 53],
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
            grid: {
              display: false
            },
            ticks: {
              color: '#6B7280'
            }
          },
          y: {
            beginAtZero: true,
            max: 100,
            ticks: {
              stepSize: 20,
              color: '#6B7280'
            },
            grid: {
              color: '#E5E7EB'
            }
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });
  }

  // Initialize new charts
  if (soilMoistureChartRef.value) {
    new Chart(soilMoistureChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
        datasets: [{
          label: 'Soil Moisture',
          data: [40, 42, 45, 47, 45, 43],
          borderColor: '#10b981',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          fill: true,
          tension: 0.4,
          borderWidth: 2,
          pointRadius: 0,
          pointHoverRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(255, 255, 255, 0.9)',
            titleColor: '#10b981',
            bodyColor: '#065f46',
            borderColor: '#10b981',
            borderWidth: 1,
            padding: 10,
            displayColors: false,
            callbacks: {
              label: function(context) {
                return `Moisture: ${context.parsed.y}%`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { 
              color: '#065f46',
              font: {
                size: 10
              }
            }
          },
          y: {
            beginAtZero: true,
            max: 100,
            ticks: { 
              stepSize: 20,
              color: '#065f46',
              font: {
                size: 10
              }
            },
            grid: { 
              color: 'rgba(16, 185, 129, 0.1)',
              drawBorder: false
            }
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });
  }

  if (humidityChartRef.value) {
    new Chart(humidityChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
        datasets: [{
          label: 'Humidity',
          data: [70, 72, 76, 78, 77, 75],
          borderColor: '#0ea5e9',
          backgroundColor: 'rgba(14, 165, 233, 0.1)',
          fill: true,
          tension: 0.4,
          borderWidth: 2,
          pointRadius: 0,
          pointHoverRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(255, 255, 255, 0.9)',
            titleColor: '#0ea5e9',
            bodyColor: '#0369a1',
            borderColor: '#0ea5e9',
            borderWidth: 1,
            padding: 10,
            displayColors: false,
            callbacks: {
              label: function(context) {
                return `Humidity: ${context.parsed.y}%`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { 
              color: '#0369a1',
              font: {
                size: 10
              }
            }
          },
          y: {
            beginAtZero: true,
            max: 100,
            ticks: { 
              stepSize: 20,
              color: '#0369a1',
              font: {
                size: 10
              }
            },
            grid: { 
              color: 'rgba(14, 165, 233, 0.1)',
              drawBorder: false
            }
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });
  }

  // Update Temperature Chart
  if (temperatureChartRef.value) {
    new Chart(temperatureChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
        datasets: [{
          label: 'Temperature',
          data: [25, 26, 28, 30, 29, 27],
          borderColor: '#ef4444',
          backgroundColor: 'rgba(239, 68, 68, 0.1)',
          fill: true,
          tension: 0.4,
          borderWidth: 2,
          pointRadius: 0,
          pointHoverRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(255, 255, 255, 0.9)',
            titleColor: '#ef4444',
            bodyColor: '#b91c1c',
            borderColor: '#ef4444',
            borderWidth: 1,
            padding: 10,
            displayColors: false,
            callbacks: {
              label: function(context) {
                return `Temperature: ${context.parsed.y}°C`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { 
              color: '#b91c1c',
              font: {
                size: 10
              }
            }
          },
          y: {
            beginAtZero: true,
            max: 40,
            ticks: { 
              stepSize: 10,
              color: '#b91c1c',
              font: {
                size: 10
              }
            },
            grid: { 
              color: 'rgba(239, 68, 68, 0.1)',
              drawBorder: false
            }
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });
  }

  // Update Soil pH Chart
  if (soilPhChartRef.value) {
    new Chart(soilPhChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
        datasets: [{
          label: 'Soil pH',
          data: [7.1, 7.15, 7.22, 7.2, 7.25, 7.22],
          borderColor: '#f97316',
          backgroundColor: 'rgba(249, 115, 22, 0.1)',
          fill: true,
          tension: 0.4,
          borderWidth: 2,
          pointRadius: 0,
          pointHoverRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'rgba(255, 255, 255, 0.9)',
            titleColor: '#f97316',
            bodyColor: '#c2410c',
            borderColor: '#f97316',
            borderWidth: 1,
            padding: 10,
            displayColors: false,
            callbacks: {
              label: function(context) {
                return `Soil pH: ${context.parsed.y}`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { 
              color: '#c2410c',
              font: {
                size: 10
              }
            }
          },
          y: {
            beginAtZero: false,
            min: 6.5,
            max: 7.5,
            ticks: { 
              stepSize: 0.2,
              color: '#c2410c',
              font: {
                size: 10
              }
            },
            grid: { 
              color: 'rgba(249, 115, 22, 0.1)',
              drawBorder: false
            }
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });
  }
});
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
</style>

