<template>

  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen pt-32">
      <!-- Container Wrapper -->
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Main Container -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Title Section - Styled like Soil Analysis Measurements with breadcrumb -->
          <div class="p-6 pb-0">
            <h1 class="text-2xl font-bold text-gray-800 mb-2">Weather Forecasting</h1>
            <div class="flex items-center text-sm text-gray-500">
              <span class="text-green-600">Weather Forecast</span>
              <ChevronRight class="h-4 w-4 mx-1" />
              <span>Overview</span>
            </div>
          </div>
          
          <!-- Content Wrapper -->
          <div class="p-6 md:p-8">
            <!-- Top Section: Current Weather & Map -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
              <!-- Current Weather Card - Redesigned with minimalist style -->
              <div class="bg-white rounded-2xl p-6 shadow-lg border border-emerald-100 transition-all duration-300 hover:shadow-xl hover:-translate-y-1 overflow-hidden flex flex-col">
                <!-- Weather Card Header -->
                <div class="flex justify-between items-start mb-5">
                  <div class="flex items-center justify-between w-full">
                    <div class="bg-emerald-50 rounded-full px-3 py-1.5 flex items-center space-x-2 shadow-inner">
                      <CloudSun class="w-5 h-5 text-emerald-500" />
                      <h3 class="text-sm font-semibold text-emerald-700 tracking-wide">Current Weather Today</h3>
                    </div>
                    <div class="bg-emerald-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md">
                      LIVE
                    </div>
                  </div>
                </div>

                <!-- Current Weather -->
                <div class="flex items-center justify-between mb-6">
                  <div>
                    <div class="flex items-end space-x-1">
                      <p class="text-5xl font-bold text-emerald-900">24</p>
                      <p class="text-2xl font-semibold text-emerald-700 mb-1">°C</p>
                    </div>
                    <p class="text-base mt-1 text-emerald-600">Heavy Rain</p>
                  </div>
                  <div class="weather-icon-wrapper">
                    <CloudRain class="h-16 w-16 transform transition-transform hover:scale-110 text-emerald-500" />
                  </div>
                </div>

                <!-- Weather Details - Modified with different colors for each metric -->
                <div class="mt-auto grid grid-cols-2 gap-4 flex-grow">
                  <!-- Pressure - Teal color scheme -->
                  <div class="bg-teal-50 rounded-xl p-4 flex items-center justify-between h-full shadow-sm hover:shadow transition-all duration-300">
                    <div class="flex items-center">
                      <Waves class="h-6 w-6 text-teal-500 mr-3" />
                      <span class="text-sm font-medium text-teal-700">Pressure</span>
                    </div>
                    <span class="text-lg font-semibold text-teal-800">173</span>
                  </div>
                  
                  <!-- Humidity - Cyan/blue color scheme -->
                  <div class="bg-cyan-50 rounded-xl p-4 flex items-center justify-between h-full shadow-sm hover:shadow transition-all duration-300">
                    <div class="flex items-center">
                      <Droplet class="h-6 w-6 text-cyan-500 mr-3" />
                      <span class="text-sm font-medium text-cyan-700">Humidity</span>
                    </div>
                    <span class="text-lg font-semibold text-cyan-800">92%</span>
                  </div>
                  
                  <!-- Wind Speed - Green color scheme -->
                  <div class="bg-green-50 rounded-xl p-4 flex items-center justify-between h-full shadow-sm hover:shadow transition-all duration-300">
                    <div class="flex items-center">
                      <Wind class="h-6 w-6 text-green-500 mr-3" />
                      <span class="text-sm font-medium text-green-700">Wind Speed</span>
                    </div>
                    <span class="text-lg font-semibold text-green-800">6 km/h</span>
                  </div>
                  
                  <!-- UV Index - Amber/yellow color scheme -->
                  <div class="bg-amber-50 rounded-xl p-4 flex items-center justify-between h-full shadow-sm hover:shadow transition-all duration-300">
                    <div class="flex items-center">
                      <Sun class="h-6 w-6 text-amber-500 mr-3" />
                      <span class="text-sm font-medium text-amber-700">UV Index</span>
                    </div>
                    <span class="text-lg font-semibold text-amber-800">3</span>
                  </div>
                </div>
              </div>
              
              <!-- Interactive Map Card - Enhanced with 3D effect -->
              <div class="bg-gradient-to-br from-emerald-50 to-emerald-100 rounded-2xl overflow-hidden shadow-sm relative group hover:shadow-md transition-all duration-300 transform hover:-translate-y-1">
                <div class="absolute inset-0 bg-grid-emerald-500/5"></div>
                <div class="relative h-full p-6">
                  <div class="flex justify-between items-start mb-4">
                    <div class="bg-white px-3 py-1 rounded-full shadow-sm flex items-center">
                      <Map class="w-3.5 h-3.5 text-emerald-600 mr-1" />
                      <h2 class="text-sm font-bold text-emerald-700">Weather Map</h2>
                    </div>
                    <div class="flex space-x-2">
                      <button class="bg-white p-1.5 rounded-full shadow-sm hover:bg-emerald-50 transition-colors">
                        <RefreshCw class="h-3.5 w-3.5 text-emerald-600" />
                      </button>
                      <button class="bg-white p-1.5 rounded-full shadow-sm hover:bg-emerald-50 transition-colors">
                        <MoreVertical class="h-3.5 w-3.5 text-emerald-600" />
                      </button>
                    </div>
                  </div>
                  
                  <!-- Map placeholder with enhanced styling -->
                  <div class="mt-4 h-[calc(100%-3rem)] rounded-xl bg-white/40 backdrop-blur-sm border border-white/60 shadow-inner flex items-center justify-center overflow-hidden relative">
                    <!-- Map grid lines -->
                    <div class="absolute inset-0 bg-grid-emerald-500/10"></div>
                    
                    <!-- Map content -->
                    <div class="text-center z-10">
                      <div class="relative">
                        <Map class="h-16 w-16 mx-auto mb-2 text-emerald-400" />
                        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-4 h-4 bg-emerald-500 rounded-full animate-ping opacity-75"></div>
                      </div>
                      <p class="text-sm text-emerald-700 font-medium">Interactive Weather Map</p>
                      <p class="text-xs text-emerald-600 mt-1">Click to explore weather patterns</p>
                    </div>
                    
                    <!-- Map controls -->
                    <div class="absolute bottom-3 right-3 flex space-x-2">
                      <button class="bg-white p-1.5 rounded-full shadow-sm hover:bg-emerald-50 transition-colors">
                        <Plus class="h-3.5 w-3.5 text-emerald-600" />
                      </button>
                      <button class="bg-white p-1.5 rounded-full shadow-sm hover:bg-emerald-50 transition-colors">
                        <Minus class="h-3.5 w-3.5 text-emerald-600" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Popular Cities Card - Enhanced with hover effects -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex justify-between items-center mb-4">
                  <h2 class="text-lg font-bold text-gray-800 flex items-center">
                    <Globe class="w-5 h-5 mr-2 text-emerald-500" />
                    Popular Cities
                  </h2>
                  <button class="text-xs font-medium text-emerald-600 hover:text-emerald-700 transition-colors flex items-center">
                    View more
                    <ChevronRight class="w-3.5 h-3.5 ml-0.5" />
                  </button>
                </div>
                
                <div class="space-y-1">
                  <div v-for="(city, index) in popularCities" :key="city.name" 
                       class="flex items-center justify-between p-2.5 rounded-xl hover:bg-emerald-50 transition-all duration-200 cursor-pointer group"
                       :class="{'bg-emerald-50/50': index === 0}">
                    <div class="flex items-center">
                      <div class="bg-white rounded-full p-2 shadow-sm mr-3 group-hover:bg-emerald-100 transition-colors">
                        <component :is="getWeatherIcon(city.condition)" class="h-4 w-4 text-emerald-600" />
                      </div>
                      <div>
                        <div class="text-sm font-medium text-gray-800">{{ city.name }}</div>
                        <div class="text-xs text-gray-500">{{ city.temperature }}°C</div>
                      </div>
                    </div>
                    <div class="text-right">
                      <div class="text-xs font-medium" :class="getConditionColor(city.condition)">
                        {{ city.condition }}
                      </div>
                      <div class="text-[10px] text-gray-500">{{ city.time }}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Bottom Section: Forecast & Chart -->
            <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
              <!-- 7-Day Forecast Card - Enhanced with better spacing -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex justify-between items-center mb-4">
                  <h2 class="text-lg font-bold text-gray-800 flex items-center">
                    <CalendarDays class="w-5 h-5 mr-2 text-emerald-500" />
                    Forecast
                  </h2>
                  <div class="flex rounded-full bg-gray-100 p-0.5">
                    <button class="px-3 py-1 rounded-full text-xs font-medium bg-emerald-500 text-white shadow-sm">7 Days</button>
                    <button class="px-3 py-1 rounded-full text-xs font-medium text-gray-600 hover:bg-gray-200 transition-colors">10 Days</button>
                  </div>
                </div>
                
                <div class="space-y-3 mt-4">
                  <div v-for="day in forecast" :key="day.date" 
                       class="flex items-center justify-between p-3 rounded-xl hover:bg-emerald-50 transition-all duration-200 cursor-pointer border border-transparent hover:border-emerald-100">
                    <div class="flex items-center">
                      <div class="bg-white rounded-full p-2 shadow-sm mr-3">
                        <component :is="getWeatherIcon(day.condition)" class="h-5 w-5 text-emerald-600" />
                      </div>
                      <div class="text-sm font-medium text-gray-800">{{ day.highTemp }}° / {{ day.lowTemp }}°</div>
                    </div>
                    <div class="text-xs text-gray-600">{{ day.date }}</div>
                  </div>
                </div>
              </div>
              
              <!-- Today's Forecast Card with Tab Functionality -->
              <div class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 lg:col-span-3">
                <!-- Header with tabs -->
                <div class="flex justify-between items-center mb-3">
                  <div class="flex items-center">
                    <h2 class="text-lg font-bold text-gray-800">Today's Forecast</h2>
                    <span class="ml-2 text-xs text-gray-500 bg-gray-100 px-2 py-0.5 rounded-full">Sat 29</span>
                  </div>
                  <div class="flex rounded-full bg-gray-100 p-0.5">
                    <button 
                      @click="setActiveTab('summary')" 
                      class="px-3 py-1 rounded-full text-xs font-medium transition-all duration-200"
                      :class="activeTab === 'summary' ? 'bg-emerald-500 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-200'"
                    >
                      Summary
                    </button>
                    <button 
                      @click="setActiveTab('hourly')" 
                      class="px-3 py-1 rounded-full text-xs font-medium transition-all duration-200"
                      :class="activeTab === 'hourly' ? 'bg-emerald-500 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-200'"
                    >
                      Hourly
                    </button>
                    <button 
                      @click="setActiveTab('details')" 
                      class="px-3 py-1 rounded-full text-xs font-medium transition-all duration-200"
                      :class="activeTab === 'details' ? 'bg-emerald-500 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-200'"
                    >
                      Details
                    </button>
                  </div>
                </div>
                
                <!-- Summary View -->
                <div v-if="activeTab === 'summary'" class="h-full">
                  <!-- Temperature display at top -->
                  <div class="flex justify-between mb-1 px-1">
                    <div v-for="temp in hourlyTemps" :key="temp" class="text-xs font-medium text-emerald-700">
                      {{ temp }}
                    </div>
                  </div>
                  
                  <!-- Temperature Chart -->
                  <div class="relative h-[38%] bg-gradient-to-b from-emerald-50/50 to-white rounded-xl overflow-hidden border border-emerald-100 mb-4">
                    <svg class="w-full h-full" viewBox="0 0 1000 200" preserveAspectRatio="none">
                      <!-- Grid lines -->
                      <line x1="0" y1="50" x2="1000" y2="50" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="5,5" />
                      <line x1="0" y1="100" x2="1000" y2="100" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="5,5" />
                      <line x1="0" y1="150" x2="1000" y2="150" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="5,5" />
                      
                      <!-- Temperature path with animation -->
                      <path 
                        d="M0,100 C50,80 100,60 150,70 C200,80 250,90 300,100 C350,110 400,120 450,110 C500,100 550,90 600,80 C650,70 700,60 750,70 C800,80 850,90 900,80 C950,70 1000,60 1000,60" 
                        fill="none" 
                        stroke="url(#lineGradient)" 
                        stroke-width="3"
                        stroke-linecap="round"
                        class="temperature-path"
                      />
                      
                      <!-- Area fill under the curve -->
                      <path 
                        d="M0,100 C50,80 100,60 150,70 C200,80 250,90 300,100 C350,110 400,120 450,110 C500,100 550,90 600,80 C650,70 700,60 750,70 C800,80 850,90 900,80 C950,70 1000,60 1000,60 L1000,200 L0,200 Z" 
                        fill="url(#areaGradient)" 
                        class="temperature-area"
                      />
                      
                      <!-- Gradient definitions -->
                      <defs>
                        <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                          <stop offset="0%" stop-color="#10b981" />
                          <stop offset="50%" stop-color="#059669" />
                          <stop offset="100%" stop-color="#10b981" />
                        </linearGradient>
                        
                        <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                          <stop offset="0%" stop-color="rgba(16, 185, 129, 0.3)" />
                          <stop offset="100%" stop-color="rgba(16, 185, 129, 0.05)" />
                        </linearGradient>
                      </defs>
                    </svg>
                    
                    <!-- Temperature points with tooltips -->
                    <div class="absolute top-0 left-0 w-full h-full flex justify-between px-4 items-center pointer-events-none">
                      <div v-for="(hour, index) in hourlyForecast.slice(0, 10)" :key="`point-${index}`" 
                           class="relative flex flex-col items-center">
                        <div class="w-2.5 h-2.5 rounded-full bg-white border-2 border-emerald-500 shadow-md"></div>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Precipitation Chance label with better spacing -->
                  <div class="flex items-center mb-3 mt-2 px-1 bg-emerald-50/30 py-2 rounded-lg">
                    <Droplet class="h-4 w-4 text-emerald-600 mr-2.5" />
                    <h3 class="text-sm font-medium text-emerald-700">Precipitation Chance</h3>
                  </div>
                  
                  <!-- Precipitation bars -->
                  <div class="grid grid-cols-10 gap-1 h-[48%]">
                    <div v-for="(hour, index) in hourlyForecast.slice(0, 10)" :key="`forecast-${index}`" 
                         class="flex flex-col h-full">
                      <!-- Weather icon -->
                      <div class="bg-emerald-50 p-1.5 rounded-full mb-1 mx-auto">
                        <component :is="getWeatherIcon(hour.condition)" class="h-3.5 w-3.5 text-emerald-600" />
                      </div>
                      
                      <!-- Precipitation bar -->
                      <div class="flex-grow w-full px-0.5 flex flex-col">
                        <div class="flex-grow bg-emerald-50 rounded-md relative overflow-hidden">
                          <div 
                            class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-emerald-500 to-emerald-300 transition-all duration-500"
                            :style="{ height: `${hour.rainChance}%` }"
                          ></div>
                        </div>
                        <div class="text-[10px] font-medium text-emerald-600 text-center mt-0.5">{{ hour.rainChance }}%</div>
                        <div class="text-[10px] text-gray-500 text-center mt-0.5">{{ hour.time }}</div>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Hourly View -->
                <div v-else-if="activeTab === 'hourly'" class="h-full overflow-auto">
                  <div class="space-y-3">
                    <div v-for="(hour, index) in hourlyForecast" :key="`hourly-${index}`" 
                         class="flex items-center justify-between p-3 rounded-xl hover:bg-emerald-50 transition-all duration-200 border border-transparent hover:border-emerald-100">
                      <div class="flex items-center space-x-4">
                        <div class="w-16 text-sm font-medium text-gray-700">{{ hour.time }}</div>
                        <div class="bg-white rounded-full p-2 shadow-sm">
                          <component :is="getWeatherIcon(hour.condition)" class="h-6 w-6" :class="getWeatherIconColor(hour.condition)" />
                        </div>
                        <div class="text-sm font-medium text-gray-800">{{ hour.temperature }}°C</div>
                      </div>
                      <div class="flex items-center space-x-6">
                        <div class="flex items-center">
                          <Droplet class="h-4 w-4 text-emerald-500 mr-1.5" />
                          <span class="text-sm text-gray-700">{{ hour.rainChance }}%</span>
                        </div>
                        <div class="flex items-center">
                          <Wind class="h-4 w-4 text-teal-500 mr-1.5" />
                          <span class="text-sm text-gray-700">{{ getRandomWindSpeed() }} km/h</span>
                        </div>
                        <div class="w-20 text-sm font-medium" :class="getConditionColor(hour.condition)">
                          {{ hour.condition }}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Details View -->
                <div v-else-if="activeTab === 'details'" class="h-full">
                  <div class="grid grid-cols-2 gap-4">
                    <!-- Left column - Weather details -->
                    <div class="space-y-4">
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <CloudRain class="h-4 w-4 mr-2 text-emerald-600" />
                          Precipitation
                        </h3>
                        <div class="space-y-2">
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Total Today</span>
                            <span class="text-sm font-medium text-gray-800">12.4 mm</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Chance of Rain</span>
                            <span class="text-sm font-medium text-gray-800">76%</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Humidity</span>
                            <span class="text-sm font-medium text-gray-800">92%</span>
                          </div>
                        </div>
                      </div>
                      
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <Wind class="h-4 w-4 mr-2 text-emerald-600" />
                          Wind
                        </h3>
                        <div class="space-y-2">
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Speed</span>
                            <span class="text-sm font-medium text-gray-800">6 km/h</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Direction</span>
                            <span class="text-sm font-medium text-gray-800">NE</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Gusts</span>
                            <span class="text-sm font-medium text-gray-800">12 km/h</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    <!-- Right column - More weather details -->
                    <div class="space-y-4">
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <Sun class="h-4 w-4 mr-2 text-emerald-600" />
                          Sun & Moon
                        </h3>
                        <div class="space-y-2">
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Sunrise</span>
                            <span class="text-sm font-medium text-gray-800">6:12 AM</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Sunset</span>
                            <span class="text-sm font-medium text-gray-800">7:48 PM</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">UV Index</span>
                            <span class="text-sm font-medium text-gray-800">3 (Moderate)</span>
                          </div>
                        </div>
                      </div>
                      
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <Thermometer class="h-4 w-4 mr-2 text-emerald-600" />
                          Temperature
                        </h3>
                        <div class="space-y-2">
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Feels Like</span>
                            <span class="text-sm font-medium text-gray-800">22°C</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">High / Low</span>
                            <span class="text-sm font-medium text-gray-800">25° / 19°</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Pressure</span>
                            <span class="text-sm font-medium text-gray-800">1013 hPa</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    <!-- Full width - Air Quality -->
                    <div class="col-span-2 bg-emerald-50/50 rounded-xl p-4">
                      <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                        <Wind class="h-4 w-4 mr-2 text-emerald-600" />
                        Air Quality
                      </h3>
                      <div class="flex items-center justify-between">
                        <div>
                          <div class="text-2xl font-bold text-emerald-700">42</div>
                          <div class="text-xs text-emerald-600">Good</div>
                        </div>
                        
                        <!-- Air Quality Bar -->
                        <div class="w-3/4 h-3 bg-gray-200 rounded-full overflow-hidden">
                          <div class="h-full bg-gradient-to-r from-emerald-500 to-emerald-300 w-[42%]"></div>
                        </div>
                      </div>
                      <div class="mt-2 text-xs text-gray-600">
                        Air quality is considered satisfactory, and air pollution poses little or no risk.
                      </div>
                    </div>
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
import { ref, onMounted } from 'vue'
import { 
  Calendar as CalendarIcon,
  CalendarDays,
  ChevronRight,
  Cloud,
  CloudDrizzle,
  CloudLightning,
  CloudRain,
  CloudSun,
  Droplet,
  Globe,
  Map,
  Minus,
  MoreVertical,
  Plus,
  RefreshCw,
  Sun,
  Thermometer,
  Waves,
  Wind
} from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'

// Active tab state
const activeTab = ref('summary')

// Popular cities data with added temperature and time
const popularCities = ref([
  { name: 'Delhi', condition: 'Partly Cloudy', temperature: 32, time: '6:30 PM' },
  { name: 'Mumbai', condition: 'Drizzle Rain', temperature: 28, time: '6:25 PM' },
  { name: 'Hyderabad', condition: 'Heavy Rain', temperature: 24, time: '6:25 PM' },
  { name: 'Bangalore', condition: 'Light Thunders', temperature: 26, time: '6:25 PM' },
  { name: 'Kolkata', condition: 'Mostly Sunny', temperature: 33, time: '6:55 PM' }
])

// 7-day forecast data
const forecast = ref([
  { date: '25 Jul, Thu', highTemp: 24, lowTemp: 22, condition: 'Heavy Rain' },
  { date: '26 Jul, Fri', highTemp: 24, lowTemp: 22, condition: 'Partly Cloudy' },
  { date: '27 Jul, Sat', highTemp: 24, lowTemp: 22, condition: 'Heavy Rain' },
  { date: '28 Jul, Sun', highTemp: 24, lowTemp: 22, condition: 'Heavy Rain' },
  { date: '29 Jul, Mon', highTemp: 25, lowTemp: 23, condition: 'Light Rain' },
  { date: '30 Jul, Tue', highTemp: 26, lowTemp: 22, condition: 'Partly Cloudy' },
  { date: '31 Jul, Wed', highTemp: 27, lowTemp: 23, condition: 'Mostly Sunny' }
])

// Hourly forecast data
const hourlyForecast = ref([
  { time: 'Now', temperature: 22, condition: 'Heavy Rain', rainChance: 70 },
  { time: '7 PM', temperature: 20, condition: 'Heavy Rain', rainChance: 79 },
  { time: '9 PM', temperature: 22, condition: 'Heavy Rain', rainChance: 76 },
  { time: '11 PM', temperature: 19, condition: 'Heavy Rain', rainChance: 81 },
  { time: '1 AM', temperature: 21, condition: 'Heavy Rain', rainChance: 76 },
  { time: '3 AM', temperature: 22, condition: 'Heavy Rain', rainChance: 78 },
  { time: '5 AM', temperature: 23, condition: 'Light Rain', rainChance: 68 },
  { time: '7 AM', temperature: 24, condition: 'Light Rain', rainChance: 61 },
  { time: '9 AM', temperature: 25, condition: 'Light Rain', rainChance: 69 },
  { time: '11 AM', temperature: 23, condition: 'Partly Cloudy', rainChance: 70 }
])

// Temperature values for the chart
const hourlyTemps = ref(['22°', '20°', '22°', '19°', '21°', '22°', '23°', '24°', '25°', '23°'])

// Function to set the active tab
const setActiveTab = (tab) => {
  activeTab.value = tab
}

// Function to return the appropriate weather icon based on condition
const getWeatherIcon = (condition) => {
  const conditionLower = condition.toLowerCase()
  
  if (conditionLower.includes('heavy rain')) {
    return CloudRain
  } else if (conditionLower.includes('light rain') || conditionLower.includes('drizzle')) {
    return CloudDrizzle
  } else if (conditionLower.includes('thunder')) {
    return CloudLightning
  } else if (conditionLower.includes('partly cloudy')) {
    return CloudSun
  } else if (conditionLower.includes('sunny') || conditionLower.includes('clear')) {
    return Sun
  } else {
    return Cloud
  }
}

// Function to get text color based on weather condition
const getConditionColor = (condition) => {
  const conditionLower = condition.toLowerCase()
  
  if (conditionLower.includes('rain') || conditionLower.includes('drizzle')) {
    return 'text-emerald-600' // Updated to emerald for consistency
  } else if (conditionLower.includes('thunder')) {
    return 'text-purple-600'
  } else if (conditionLower.includes('sunny') || conditionLower.includes('clear')) {
    return 'text-amber-600'
  } else if (conditionLower.includes('cloudy')) {
    return 'text-gray-600'
  } else {
    return 'text-emerald-600'
  }
}

// Function to get weather icon colors
const getWeatherIconColor = (condition) => {
  const conditionLower = condition.toLowerCase()
  
  if (conditionLower.includes('rain') || conditionLower.includes('drizzle')) {
    return 'text-emerald-500' // Updated to emerald for consistency
  } else if (conditionLower.includes('thunder')) {
    return 'text-purple-600'
  } else if (conditionLower.includes('sunny') || conditionLower.includes('clear')) {
    return 'text-amber-400'
  } else if (conditionLower.includes('cloudy')) {
    return 'text-gray-400'
  } else {
    return 'text-emerald-500'
  }
}

// Helper function to generate random wind speed for hourly view
const getRandomWindSpeed = () => {
  return Math.floor(Math.random() * 8) + 4
}

onMounted(() => {
  // Animation for temperature path could be initialized here if needed
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Grid background pattern */
.bg-grid-emerald-500\/5 {
  background-image: linear-gradient(to right, rgba(16, 185, 129, 0.05) 1px, transparent 1px),
                    linear-gradient(to bottom, rgba(16, 185, 129, 0.05) 1px, transparent 1px);
  background-size: 20px 20px;
}

.bg-grid-emerald-500\/10 {
  background-image: linear-gradient(to right, rgba(16, 185, 129, 0.1) 1px, transparent 1px),
                    linear-gradient(to bottom, rgba(16, 185, 129, 0.1) 1px, transparent 1px);
  background-size: 20px 20px;
}

/* Animations */
@keyframes pulse {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 0.4; }
}

.animate-pulse {
  animation: pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}

.animate-ping {
  animation: ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
}

/* Temperature chart animations */
.temperature-path {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  animation: dash 2s ease-in-out forwards;
}

.temperature-area {
  opacity: 0;
  animation: fadeIn 2s ease-in-out forwards;
  animation-delay: 0.5s;
}

@keyframes dash {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
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
  transition: all 0.3s ease;
}

.weather-icon-wrapper svg {
  animation: float 3s ease-in-out infinite;
}

/* Custom scrollbar styling */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgba(16, 185, 129, 0.05);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: rgba(16, 185, 129, 0.3);
  border-radius: 4px;
  transition: background-color 200ms;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(16, 185, 129, 0.5);
}

/* Smooth transitions */
* {
  transition: all 200ms ease-in-out;
}

/* Firefox scrollbar styling */
* {
  scrollbar-width: thin;
  scrollbar-color: rgba(16, 185, 129, 0.3) rgba(16, 185, 129, 0.05);
}

/* Media queries for better responsiveness */
@media (max-width: 1280px) {
  .grid-cols-10 {
    grid-template-columns: repeat(5, minmax(0, 1fr));
  }
  
  .h-\[38\%\] {
    height: 33%;
  }
  
  .h-\[48\%\] {
    height: 58%;
  }
}

@media (max-width: 768px) {
  .grid-cols-10 {
    grid-template-columns: repeat(5, minmax(0, 1fr));
  }
  
  .text-\[10px\] {
    font-size: 0.65rem;
  }
}

@media (max-width: 640px) {
  .p-5 {
    padding: 0.75rem;
  }
  
  .h-\[38\%\] {
    height: 30%;
  }
  
  .h-\[48\%\] {
    height: 63%;
  }
  
  .grid-cols-10 {
    grid-template-columns: repeat(5, minmax(0, 1fr));
    grid-template-rows: repeat(2, minmax(0, 1fr));
    gap: 0.5rem;
  }
}

/* Ensure the forecast card fills available space */
.lg\:col-span-3 {
  height: 100%;
  display: flex;
  flex-direction: column;
}

/* Make sure precipitation bars are responsive */
@supports (height: 100%) {
  .flex-grow {
    min-height: 0;
  }
}
</style>
    <div>
      <h2>30-Day Weather Forecast</h2>
      <table v-if="forecast.length">
        <thead>
          <tr>
            <th v-for="(value, key) in forecast[0]" :key="key">{{ key }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in forecast" :key="index">
            <td v-for="(value, key) in row" :key="key">{{ value }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>Loading forecast data...</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import api from '../../api/index.js'
  
  const forecast = ref([])
  
  onMounted(async () => {
    try {
      const res = await api.get('/weather/forecast')
      forecast.value = res.data.forecast
    } catch (err) {
      console.error('Error fetching forecast:', err)
    }
  })
  </script>
