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
                      <p class="text-5xl font-bold text-emerald-900">{{ weather?.temperature_c }}</p>
                      <p class="text-2xl font-semibold text-emerald-700 mb-1">°C</p>
                    </div>
                    <p class="text-base mt-1 text-emerald-600">{{weather?.weather_condition}}</p>
                  </div>
                  <div class="weather-icon-wrapper">
                    <component 
                        :is="getWeatherIcon(weather?.weather_condition)"
                        :class="['h-14 w-14 transform transition-transform hover:scale-110', getWeatherIconColor(weather?.weather_condition)]"
                      />
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
<<<<<<< HEAD
                    <span class="text-lg font-semibold text-teal-800">{{ weather?.pressure_hpa }}</span>
=======
                    <span class="text-lg font-semibold text-teal-800">{{ weather?.pressure }}</span>
>>>>>>> cy
                  </div>
                  
                  <!-- Humidity - Cyan/blue color scheme -->
                  <div class="bg-cyan-50 rounded-xl p-4 flex items-center justify-between h-full shadow-sm hover:shadow transition-all duration-300">
                    <div class="flex items-center">
                      <Droplet class="h-6 w-6 text-cyan-500 mr-3" />
                      <span class="text-sm font-medium text-cyan-700">Humidity</span>
                    </div>
                    <span class="text-lg font-semibold text-cyan-800">{{ weather?.humidity }}%</span>
                  </div>
                  
                  <!-- Wind Speed - Green color scheme -->
                  <div class="bg-green-50 rounded-xl p-4 flex items-center justify-between h-full shadow-sm hover:shadow transition-all duration-300">
                    <div class="flex items-center">
                      <Wind class="h-6 w-6 text-green-500 mr-3" />
                      <span class="text-sm font-medium text-green-700">Wind Speed</span>
                    </div>
<<<<<<< HEAD
                    <span class="text-lg font-semibold text-green-800">{{ weather?.wind_speed_kph }} km/h</span>
=======
                    <span class="text-lg font-semibold text-green-800">{{ weather?.wind_speed }} km/h</span>
>>>>>>> cy
                  </div>
                  
                  <!-- UV Index - Amber/yellow color scheme -->
                  <div class="bg-amber-50 rounded-xl p-4 flex items-center justify-between h-full shadow-sm hover:shadow transition-all duration-300">
                    <div class="flex items-center">
                      <Sun class="h-6 w-6 text-amber-500 mr-3" />
                      <span class="text-sm font-medium text-amber-700">UV Index</span>
                    </div>
<<<<<<< HEAD
                    <span class="text-lg font-semibold text-amber-800">{{ weather?.uv }}</span>
=======
                    <span class="text-lg font-semibold text-amber-800">{{ weather?.uv_index }}</span>
>>>>>>> cy
                  </div>
                </div>
              </div>
              
<<<<<<< HEAD
              <!-- Interactive Map Card - Enhanced with 3D effect -->
              <!-- <div class="bg-gradient-to-br from-emerald-50 to-emerald-100 rounded-2xl overflow-hidden shadow-sm relative group hover:shadow-md transition-all duration-300 transform hover:-translate-y-1">
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
                  
                  <!-- Map placeholder with enhanced styling --
                  <div class="mt-4 h-[calc(100%-3rem)] rounded-xl bg-white/40 backdrop-blur-sm border border-white/60 shadow-inner flex items-center justify-center overflow-hidden relative">
                    <!-- Map grid lines ->
                    <div class="absolute inset-0 bg-grid-emerald-500/10"></div>
                    
                    <!-- Map content --
                    <div class="text-center z-10">
                      <div class="relative">
                        <Map class="h-16 w-16 mx-auto mb-2 text-emerald-400" />
                        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-4 h-4 bg-emerald-500 rounded-full animate-ping opacity-75"></div>
                      </div>
                      <p class="text-sm text-emerald-700 font-medium">Interactive Weather Map</p>
                      <p class="text-xs text-emerald-600 mt-1">Click to explore weather patterns</p>
                    </div>
                    
                    <!-- Map controls --
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
              </div> -->
              
=======
>>>>>>> cy
              <div class="bg-gradient-to-br from-emerald-50 to-emerald-100 rounded-2xl overflow-hidden shadow-sm relative group hover:shadow-md transition-all duration-300 transform hover:-translate-y-1">
                <div class="absolute inset-0 bg-grid-emerald-500/5"></div>
                <div class="relative h-full p-6">
                  <div class="flex justify-between items-start mb-4">
                    <div class="bg-white px-3 py-1 rounded-full shadow-sm flex items-center">
                      <Map class="w-3.5 h-3.5 text-emerald-600 mr-1" />
                      <h2 class="text-sm font-bold text-emerald-700">Map</h2>
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

                  <!-- Actual Interactive Map -->
                  <div class="mt-4 h-[calc(100%-3rem)] rounded-xl overflow-hidden relative border border-white/60 shadow-inner">
                    <div id="weather-map" class="w-full h-full rounded-xl z-10"></div>
                  </div>
                </div>
              </div>

<<<<<<< HEAD

=======
>>>>>>> cy
              <!-- Popular Cities Card - Enhanced with hover effects -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex justify-between items-center mb-4">
                  <h2 class="text-lg font-bold text-gray-800 flex items-center">
                    <Globe class="w-5 h-5 mr-2 text-emerald-500" />
                    Popular Cities
                  </h2>
<<<<<<< HEAD
                  <button class="text-xs font-medium text-emerald-600 hover:text-emerald-700 transition-colors flex items-center">
                    View more
                    <ChevronRight class="w-3.5 h-3.5 ml-0.5" />
                  </button>
=======
                  <!-- <button class="text-xs font-medium text-emerald-600 hover:text-emerald-700 transition-colors flex items-center">
                    View more
                    <ChevronRight class="w-3.5 h-3.5 ml-0.5" />
                  </button> -->
>>>>>>> cy
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
<<<<<<< HEAD
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
=======
                    <button
                      class="px-3 py-1 rounded-full text-xs font-medium"
                      :class="selectedDays === 7 ? 'bg-emerald-500 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-200'"
                      @click="selectedDays = 7"
                    >
                      7 Days
                    </button>
                    <button
                      class="px-3 py-1 rounded-full text-xs font-medium"
                      :class="selectedDays === 10 ? 'bg-emerald-500 text-white shadow-sm' : 'text-gray-600 hover:bg-gray-200'"
                      @click="selectedDays = 10"
                    >
                      10 Days
                    </button>
                  </div>
                </div>

                <div class="space-y-3 mt-4">
                  <div
                    v-for="day in forecast.slice(0, selectedDays)"
                    :key="day.date"
                    class="flex items-center justify-between p-3 rounded-xl hover:bg-emerald-50 transition-all duration-200 cursor-pointer border border-transparent hover:border-emerald-100"
                  >
                    <div class="flex items-center">
                      <div class="bg-white rounded-full p-2 shadow-sm mr-3">
                        <component :is="getWeatherIcon(day.condition_code)" class="h-5 w-5 text-emerald-600" />
>>>>>>> cy
                      </div>
                      <div class="text-sm font-medium text-gray-800">
                        {{ Number(day.temperature_max).toFixed(1) }}° / {{ Number(day.temperature_min).toFixed(1) }}°
                      </div>
<<<<<<< HEAD

=======
>>>>>>> cy
                    </div>
                    <div class="text-xs text-gray-600">
                      {{ new Date(day.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) }}
                    </div>
<<<<<<< HEAD

                  </div>
                </div>
              </div>
=======
                  </div>
                </div>
              </div>

>>>>>>> cy
              
              <!-- Today's Forecast Card with Tab Functionality -->
              <div class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 lg:col-span-3">
                <!-- Header with tabs -->
                <div class="flex justify-between items-center mb-3">
                  <div class="flex items-center">
                    <h2 class="text-lg font-bold text-gray-800">Today's Forecast</h2>
<<<<<<< HEAD
                    <span class="ml-2 text-xs text-gray-500 bg-gray-100 px-2 py-0.5 rounded-full">Sat 29</span>
=======
                    <span class="ml-2 text-xs text-gray-500 bg-gray-100 px-2 py-0.5 rounded-full">{{ currentDate }}</span>
>>>>>>> cy
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
<<<<<<< HEAD
                  <!-- Temperature display at top -->
                  <div class="flex justify-between mb-1 px-1">
                    <div v-for="temp in hourlyTemps" :key="temp" class="text-xs font-medium text-emerald-700">
                      {{ temp }}
                    </div>
                  </div>
                  
                  <!-- Temperature Chart -->
                  <div class="relative h-[38%] bg-gradient-to-b from-emerald-50/50 to-white rounded-xl overflow-hidden border border-emerald-100 mb-4">
=======
                  
                  <!-- Temperature Chart -->
                  <div class="relative w-full h-52">
>>>>>>> cy
                    <svg class="w-full h-full" viewBox="0 0 1000 200" preserveAspectRatio="none">
                      <!-- Grid lines -->
                      <line x1="0" y1="50" x2="1000" y2="50" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="5,5" />
                      <line x1="0" y1="100" x2="1000" y2="100" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="5,5" />
                      <line x1="0" y1="150" x2="1000" y2="150" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="5,5" />
<<<<<<< HEAD
                      
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
=======

                      <!-- Temperature line path -->
                      <path
                        :d="temperaturePath"
                        fill="none"
                        stroke="url(#lineGradient)"
                        stroke-width="3"
                        stroke-linecap="round"
                        ref="pathRef"
                      />

                      <!-- Area under curve -->
                      <path
                        :d="areaPath"
                        fill="url(#areaGradient)"
                      />

                      <!-- Gradient defs -->
>>>>>>> cy
                      <defs>
                        <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                          <stop offset="0%" stop-color="#10b981" />
                          <stop offset="50%" stop-color="#059669" />
                          <stop offset="100%" stop-color="#10b981" />
                        </linearGradient>
<<<<<<< HEAD
                        
=======
>>>>>>> cy
                        <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                          <stop offset="0%" stop-color="rgba(16, 185, 129, 0.3)" />
                          <stop offset="100%" stop-color="rgba(16, 185, 129, 0.05)" />
                        </linearGradient>
                      </defs>
                    </svg>
<<<<<<< HEAD
                    
                    <!-- Temperature points with tooltips -->
                    <div class="absolute top-0 left-0 w-full h-full flex justify-between px-4 items-center pointer-events-none">
                      <div v-for="(hour, index) in hourlyForecast.slice(0, 10)" :key="`point-${index}`" 
                           class="relative flex flex-col items-center">
=======

                    <!-- Tooltips and points -->
                    <div class="absolute top-0 left-0 w-full h-full pointer-events-none">
                      <div
                        v-for="(temp, index) in hourlyTemps"
                        :key="index"
                        class="absolute flex flex-col items-center"
                        :style="{
                          left: `calc(${(index / (hourlyTemps.length - 1)) * 100}% - 6px)`,
                          bottom: `${((temp - minTemp) / (maxTemp - minTemp)) * 80 + 10}%`
                        }"
                      >
                        <div class="text-[10px] mb-1 text-emerald-600 font-semibold">{{ temp }}°C</div>
>>>>>>> cy
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
<<<<<<< HEAD
                        <div class="text-sm font-medium text-gray-800">{{ hour.temperature }}°C</div>
=======
                        <div class="text-sm font-medium text-gray-800">{{ hour.temp }}°C</div>
>>>>>>> cy
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
<<<<<<< HEAD
                    <!-- Left column - Weather details -->
                    <div class="space-y-4">
=======
                    <!-- Left column -->
                    <div class="space-y-4">
                      <!-- Precipitation -->
>>>>>>> cy
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <CloudRain class="h-4 w-4 mr-2 text-emerald-600" />
                          Precipitation
                        </h3>
                        <div class="space-y-2">
                          <div class="flex justify-between items-center">
<<<<<<< HEAD
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
                      
=======
                            <span class="text-xs text-gray-600">Hourly Value</span>
                            <span class="text-sm font-medium text-gray-800">
                              {{ weather.precipitation?.toFixed(1) ?? '--' }} mm
                            </span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Chance of Rain</span>
                            <span class="text-sm font-medium text-gray-800">{{ hourlyForecast[0].rainChance }}%</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Humidity</span>
                            <span class="text-sm font-medium text-gray-800">{{ weather.humidity ?? '--' }}%</span>
                          </div>
                        </div>
                      </div>

                      <!-- Wind -->
>>>>>>> cy
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <Wind class="h-4 w-4 mr-2 text-emerald-600" />
                          Wind
                        </h3>
                        <div class="space-y-2">
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Speed</span>
<<<<<<< HEAD
                            <span class="text-sm font-medium text-gray-800">6 km/h</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Direction</span>
                            <span class="text-sm font-medium text-gray-800">NE</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Gusts</span>
                            <span class="text-sm font-medium text-gray-800">12 km/h</span>
=======
                            <span class="text-sm font-medium text-gray-800">{{ weather.wind_speed ?? '--' }} km/h</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Direction</span>
                            <span class="text-sm font-medium text-gray-800">{{ getCompassDirection(weather.wind_direction ?? '--') }}</span>
>>>>>>> cy
                          </div>
                        </div>
                      </div>
                    </div>
<<<<<<< HEAD
                    
                    <!-- Right column - More weather details -->
                    <div class="space-y-4">
=======

                    <!-- Right column -->
                    <div class="space-y-4">
                      <!-- Sun & Moon (placeholder values since not provided by Open-Meteo) -->
>>>>>>> cy
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <Sun class="h-4 w-4 mr-2 text-emerald-600" />
                          Sun & Moon
                        </h3>
                        <div class="space-y-2">
<<<<<<< HEAD
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
                      
=======
                          
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Sunrise</span>
                            <span class="text-sm font-medium text-gray-800">
                              {{ sunriseDisplay }}
                            </span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Sunset</span>
                            <span class="text-sm font-medium text-gray-800">
                              {{ sunsetDisplay }}
                            </span>
                          </div>

                        </div>
                      </div>

                      <!-- Temperature -->
>>>>>>> cy
                      <div class="bg-emerald-50/50 rounded-xl p-4">
                        <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                          <Thermometer class="h-4 w-4 mr-2 text-emerald-600" />
                          Temperature
                        </h3>
                        <div class="space-y-2">
                          <div class="flex justify-between items-center">
<<<<<<< HEAD
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
=======
                            <span class="text-xs text-gray-600">Current</span>
                            <span class="text-sm font-medium text-gray-800">{{ weather.temperature_c ?? '--' }}°C</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">High / Low</span>
                            <span class="text-sm font-medium text-gray-800">{{ forecast[0].temperature_max }}° / {{ forecast[0].temperature_min }}°</span>
                          </div>
                          <div class="flex justify-between items-center">
                            <span class="text-xs text-gray-600">Pressure</span>
                            <span class="text-sm font-medium text-gray-800">{{ weather.pressure ?? '--' }} hPa</span>
>>>>>>> cy
                          </div>
                        </div>
                      </div>
                    </div>
<<<<<<< HEAD
                    
                    <!-- Full width - Air Quality -->
=======

                    <!-- Air Quality Card -->
>>>>>>> cy
                    <div class="col-span-2 bg-emerald-50/50 rounded-xl p-4">
                      <h3 class="text-sm font-semibold text-emerald-800 mb-3 flex items-center">
                        <Wind class="h-4 w-4 mr-2 text-emerald-600" />
                        Air Quality
                      </h3>
                      <div class="flex items-center justify-between">
                        <div>
<<<<<<< HEAD
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
=======
                          <!-- Display PM2.5 concentration -->
                          <div class="text-2xl font-bold text-emerald-700">
                            {{ airQual?.pm2_5.toFixed(1) }} µg/m³
                          </div>
                          <div class="text-xs text-emerald-600">
                            PM₂.₅ Concentration
                          </div>
                        </div>

                        <!-- Progress bar: assuming 0–50µg/m³ is "good" -->
                        <div class="w-3/4 h-3 bg-gray-200 rounded-full overflow-hidden">
                          <div
                            class="h-full bg-gradient-to-r from-emerald-500 to-emerald-300"
                            :style="{ width: `${Math.min((airQual?.pm2_5 / 50) * 100, 100)}%` }"
                          ></div>
                        </div>
                      </div>
                      <div class="mt-2 text-xs text-gray-600">
                        Air quality index based on PM₂.₅ levels.
>>>>>>> cy
                      </div>
                    </div>
                  </div>
                </div>
<<<<<<< HEAD
=======

                
>>>>>>> cy
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
<<<<<<< HEAD
import { ref, onMounted } from 'vue'
=======
import { ref, onMounted, computed } from 'vue'
>>>>>>> cy
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
  Snowflake,   // ✅ Add this for cold weather
  Sun,
  Thermometer,
  Waves,
<<<<<<< HEAD
  Wind
} from 'lucide-vue-next'

=======
  Wind,
  CloudSnow,     // for snow (71, 73, 75)
} from 'lucide-vue-next'
import { getWeatherData, getWeatherDataForPopularCities, mapWeatherCode  } from '../../utils/weather';
>>>>>>> cy
import Sidebar from '../layout/Sidebar.vue'
import api from '../../api/index.js'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'

<<<<<<< HEAD
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
//const forecast = ref([
//  { date: '25 Jul, Thu', highTemp: 24, lowTemp: 22, condition: 'Heavy Rain' },
//  { date: '26 Jul, Fri', highTemp: 24, lowTemp: 22, condition: 'Partly Cloudy' },
//  { date: '27 Jul, Sat', highTemp: 24, lowTemp: 22, condition: 'Heavy Rain' },
//  { date: '28 Jul, Sun', highTemp: 24, lowTemp: 22, condition: 'Heavy Rain' },
//  { date: '29 Jul, Mon', highTemp: 25, lowTemp: 23, condition: 'Light Rain' },
//  { date: '30 Jul, Tue', highTemp: 26, lowTemp: 22, condition: 'Partly Cloudy' },
//  { date: '31 Jul, Wed', highTemp: 27, lowTemp: 23, condition: 'Mostly Sunny' }
//])

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
=======
const activeTab = ref('summary')
const popularCities = ref([]);
const hourlyForecast = ref([])
const weather = ref(null)
const forecast = ref([])
const selectedDays = ref(7);
const sunData = ref([])
const airQual = ref([])
const hourlyTemps = computed(() => hourlyForecast.value.map(h => h.temp))
const sunriseDisplay = computed(() => formatTimeHM(sunData.value?.sunrise))
const sunsetDisplay  = computed(() => formatTimeHM(sunData.value?.sunset))
let intervalId = null;

const svgWidth = 1000
const svgHeight = 200
const paddingTop = 10
const paddingBottom = 10

// Calculate min and max temperatures
const minTemp = computed(() =>
  hourlyTemps.value.length ? Math.min(...hourlyTemps.value) : 0
)
const maxTemp = computed(() =>
  hourlyTemps.value.length ? Math.max(...hourlyTemps.value) : 1
)

// Map temperature to Y coordinate
const temperatureToYpx = (temp) => {
  if (maxTemp.value === minTemp.value) return svgHeight / 2
  return (
    svgHeight - paddingBottom -
    ((temp - minTemp.value) / (maxTemp.value - minTemp.value)) *
    (svgHeight - paddingTop - paddingBottom)
  )
}

// Create SVG path for line
const temperaturePath = computed(() => {
  const points = hourlyTemps.value.map((t, i) => {
    const x = (i / (hourlyTemps.value.length - 1)) * svgWidth
    const y = temperatureToYpx(t)
    return [x, y]
  })

  if (points.length < 2) return ''

  let path = `M${points[0][0]},${points[0][1]}`
  for (let i = 1; i < points.length; i++) {
    const [x1, y1] = points[i - 1]
    const [x2, y2] = points[i]
    const cx = (x1 + x2) / 2
    path += ` Q${x1},${y1} ${cx},${(y1 + y2) / 2}`
  }
  const [lastX, lastY] = points[points.length - 1]
  path += ` T${lastX},${lastY}`
  return path
})

// Create path for area under the curve
const areaPath = computed(() => {
  const points = hourlyTemps.value.map((t, i) => {
    const x = (i / (hourlyTemps.value.length - 1)) * svgWidth
    const y = temperatureToYpx(t)
    return [x, y]
  })
  if (points.length < 2) return ''

  let path = `M${points[0][0]},${svgHeight} L${points[0][0]},${points[0][1]}`
  for (let i = 1; i < points.length; i++) {
    const [x1, y1] = points[i - 1]
    const [x2, y2] = points[i]
    const cx = (x1 + x2) / 2
    path += ` Q${x1},${y1} ${cx},${(y1 + y2) / 2}`
  }
  const [lastX, lastY] = points[points.length - 1]
  path += ` T${lastX},${lastY}`
  path += ` L${lastX},${svgHeight} Z`
  return path
})

function getCompassDirection(degree) {
  const directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'];
  const index = Math.round(degree / 45) % 8;
  return directions[index];
}

// Animate path
const pathRef = ref(null)
onMounted(() => {
  if (pathRef.value) {
    const length = pathRef.value.getTotalLength()
    pathRef.value.style.strokeDasharray = length
    pathRef.value.style.strokeDashoffset = length
    pathRef.value.getBoundingClientRect() // force reflow
    pathRef.value.style.transition = 'stroke-dashoffset 1s ease-in-out'
    pathRef.value.style.strokeDashoffset = '0'
  }
})

const currentDate = computed(() => {
  const today = new Date()
  const weekday = today.toLocaleDateString('en-US', { weekday: 'short' })  // "Sat"
  const day = today.getDate()                                              // 3
  return `${weekday} ${day}`
})
>>>>>>> cy

// Function to set the active tab
const setActiveTab = (tab) => {
  activeTab.value = tab
}

// Function to return the appropriate weather icon based on condition
<<<<<<< HEAD
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
=======
const getWeatherIcon = (condition) => {
  switch (condition) {
    case 'Clear':
    case 'Mainly Clear':
      return Sun
    case 'Partly Cloudy':
      return CloudSun
    case 'Overcast':
      return Cloud
    case 'Fog':
    case 'Depositing Rime Fog':
      return Fog
    case 'Light Drizzle':
    case 'Moderate Drizzle':
    case 'Dense Drizzle':
      return CloudDrizzle
    case 'Light Rain':
    case 'Moderate Rain':
    case 'Heavy Rain':
    case 'Rain Showers':
    case 'Heavy Rain Showers':
    case 'Violent Rain Showers':
      return CloudRain
    case 'Light Snowfall':
    case 'Moderate Snowfall':
    case 'Heavy Snowfall':
      return CloudSnow
    case 'Thunderstorm':
    case 'Thunderstorm with Hail':
    case 'Severe Thunderstorm':
      return CloudLightning
    default:
      return Cloud  // fallback
  }
}
>>>>>>> cy

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
  if (!condition) return 'text-gray-300'
  const conditionLower = condition.toLowerCase()

  if (conditionLower.includes('rain') || conditionLower.includes('drizzle')) {
    return 'text-emerald-500'
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

<<<<<<< HEAD

=======
>>>>>>> cy
// Helper function to generate random wind speed for hourly view
const getRandomWindSpeed = () => {
  return Math.floor(Math.random() * 8) + 4
}

<<<<<<< HEAD
const weather = ref(null)
const forecast = ref([])

const MAPTILER_KEY = import.meta.env.VITE_MAPTILER_API 

onMounted(async () => {
  // Animation for temperature path could be initialized here if needed
  // try {
  //   const res = await api.get('/weather/forecast')
  //   forecast.value = res.data.forecast
  // } catch (err) {
  //   console.error('Error fetching forecast:', err)
  // }

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
=======
function formatTimeHM(iso) {
  if (!iso) return '--:--'
  const parts = iso.split('T')
  if (parts.length !== 2) return '--:--'
  const [hour, minute] = parts[1].split(':')
  let hours = parseInt(hour)
  const isAM = hours < 12
  hours = hours % 12 || 12 // Convert 0-23 to 1-12 format
  const ampm = isAM ? 'AM' : 'PM'
  return `${hours}:${minute.padStart(2, '0')} ${ampm}`
}

const MAPTILER_KEY = import.meta.env.VITE_MAPTILER_API 

const loadWeather = async () => {
  try {
    const data = await getWeatherData();
    console.log("Weather Data:", data)
    weather.value = data.current;
    forecast.value = data.forecast;
    sunData.value = data.sunData;
    airQual.value = data.airQuality;
    hourlyForecast.value = data.hourlyForecast.slice(0, 10)

    
    if (data && data.hourlyForecast && Array.isArray(data.hourlyForecast)) {
      hourlyForecast.value = data.hourlyForecast.slice(0, 10)
    } else {
      console.error("hourlyForecast is missing or not an array", data)
    }
    popularCities.value = await getWeatherDataForPopularCities();
  } catch (error) {
    console.error('Failed to load weather:', error);
  }
};

onMounted(async () => {
  await loadWeather(); 
  intervalId = setInterval(loadWeather, 600000);
>>>>>>> cy

  const map = new maplibregl.Map({
    container: 'weather-map',
    style: `https://api.maptiler.com/maps/hybrid/style.json?key=${MAPTILER_KEY}`, // 🛰️ Satellite + Labels
    center: [121.2151274080352, 13.405165290699628],
    zoom: 14
  })

  map.addControl(new maplibregl.NavigationControl())

  new maplibregl.Marker({ color: '#059669' })
    .setLngLat([121.2151274080352, 13.405165290699628])
    .setPopup(new maplibregl.Popup().setText('📍 Your Location'))
    .addTo(map)
})

<<<<<<< HEAD

=======
>>>>>>> cy
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
<<<<<<< HEAD
=======
  stroke-linecap: round;
>>>>>>> cy
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
