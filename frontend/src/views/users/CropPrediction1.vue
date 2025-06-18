<template>
  <div class="min-h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen pt-24 sm:pt-24 md:pt-32">
      <!-- Container Wrapper with proper spacing -->
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Main Container with adjusted width -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-115px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Content Wrapper -->
          <div class="p-4 sm:p-6">
            <!-- Clean Minimalist Metrics Section -->
            <div class="grid grid-cols-4 gap-4 mb-6">
              <!-- Total Predictions -->
              <div class="bg-white rounded-xl p-5 border border-gray-100 shadow-sm">
                <div class="flex items-center justify-between mb-2">
                  <div class="flex items-center gap-2">
                    <ChartBarIcon class="h-5 w-5 text-purple-500" />
                    <span class="text-sm font-medium text-gray-700">Total</span>
                  </div>
                </div>
                <div class="flex flex-col">
                  <div class="text-2xl font-bold text-gray-900 mb-2">{{ totalRecommendations }}</div>
                  <div 
                    :class="[
                      'text-xs font-medium',
                      isIncrease ? 'text-green-600' : 'text-red-600'
                    ]"
                  >
                    <span class="flex items-center">
                      <component
                        :is="isIncrease ? ArrowUpIcon : ArrowDownIcon"
                        class="w-3 h-3 mr-1"
                      />
                      {{ isIncrease ? '+' : '-' }}{{ percentageChange }}% {{ isIncrease ? 'increase' : 'decrease' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Planted -->
              <div class="bg-white rounded-xl p-5 border border-gray-100 shadow-sm">
                <div class="flex items-center justify-between mb-2">
                  <div class="flex items-center gap-2">
                    <SproutIcon class="h-5 w-5 text-green-500" />
                    <span class="text-sm font-medium text-gray-700">Planted</span>
                  </div>
                </div>
                <div class="flex flex-col">
                  <div class="text-2xl font-bold text-gray-900 mb-2">{{ plantedCount }}</div>
                  <div 
                    :class="[
                      'text-xs font-medium',
                      plantedIsIncrease ? 'text-green-600' : 'text-red-600'
                    ]"
                  >
                    <span class="flex items-center">
                      <component
                        :is="plantedIsIncrease ? ArrowUpIcon : ArrowDownIcon"
                        class="w-3 h-3 mr-1"
                      />
                      {{ plantedIsIncrease ? '+' : '-' }}{{ plantedPercentageChange }}% {{ plantedIsIncrease ? 'increase' : 'decrease' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Success Rate -->
              <div class="bg-white rounded-xl p-5 border border-gray-100 shadow-sm">
                <div class="flex items-center justify-between mb-2">
                  <div class="flex items-center gap-2">
                    <ActivityIcon class="h-5 w-5 text-blue-500" />
                    <span class="text-sm font-medium text-gray-700">Rate</span>
                  </div>
                </div>
                <div class="flex flex-col">
                  <div class="text-2xl font-bold text-gray-900 mb-2">{{ successRate }}%</div>
                  <div 
                    :class="[
                      'text-xs font-medium',
                      isIncrease ? 'text-green-600' : 'text-red-600'
                    ]"
                  >
                    <span class="flex items-center">
                      <component
                        :is="isIncrease ? ArrowUpIcon : ArrowDownIcon"
                        class="w-3 h-3 mr-1"
                      />
                      {{ isIncrease ? '+' : '-' }}{{ percentageChange }}% {{ isIncrease ? 'increase' : 'decrease' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Ongoing -->
              <div class="bg-white rounded-xl p-5 border border-gray-100 shadow-sm">
                <div class="flex items-center justify-between mb-2">
                  <div class="flex items-center gap-2">
                    <ClipboardListIcon class="h-5 w-5 text-red-500" />
                    <span class="text-sm font-medium text-gray-700">Active</span>
                  </div>
                </div>
                <div class="flex flex-col">
                  <div class="text-2xl font-bold text-gray-900 mb-2">{{ ongoingCount }}</div>
                  <div 
                    :class="[
                      'text-xs font-medium',
                      ongoingIsIncrease ? 'text-green-600' : 'text-red-600'
                    ]"
                  >
                    <span class="flex items-center">
                      <component
                        :is="ongoingIsIncrease ? ArrowUpIcon : ArrowDownIcon"
                        class="w-3 h-3 mr-1"
                      />
                      {{ ongoingIsIncrease ? '+' : '-' }}{{ ongoingPercentageChange }}% {{ ongoingIsIncrease ? 'increase' : 'decrease' }}
                    </span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Rest of the content remains the same -->
            <!-- Main Content Area -->
            <div class="space-y-6">
              <!-- Modified Prediction Form - Enhanced UI -->
              <div class="bg-white rounded-xl shadow-md p-5 sm:p-6 border border-gray-100 relative overflow-hidden">
                <!-- Background Pattern -->
                <div class="absolute top-0 right-0 w-64 h-64 bg-gradient-to-bl from-green-50 to-transparent opacity-50 -z-10"></div>
                
                <!-- Enhanced Header -->
                <div class="mb-6">
                  <h2 class="text-xl font-semibold text-gray-800 flex items-center gap-2">
                    <ActivitySquareIcon class="w-5 h-5 text-green-500" />
                    Crop Recommendations
                  </h2>
                  <p class="text-sm text-gray-500 mt-1">
                    Real-time soil analysis and environmental parameters
                  </p>
                </div>

                <!-- Form Fields Container -->
                <div class="space-y-6">
                  <!-- Primary Measurements Section -->
                  <div>
                    <h3 class="text-sm font-medium text-gray-700 mb-4 flex items-center">
                      <span class="inline-block w-1.5 h-1.5 bg-green-500 rounded-full mr-2"></span>
                      Soil Composition Analysis
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                      <!-- Nitrogen Level -->
                      <div class="relative group">
                        <div class="absolute inset-0 bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl transition-opacity opacity-0 group-hover:opacity-100"></div>
                        <div class="relative bg-white rounded-lg p-4 border border-gray-100 transition-all duration-300 hover:border-green-300 hover:shadow-md">
                          <div class="flex items-center gap-3 mb-3">
                            <div class="p-2 bg-green-50 rounded-lg">
                              <BeakerIcon class="w-4 h-4 text-green-600" />
                            </div>
                            <div>
                              <label class="block text-sm font-medium text-gray-500">Nitrogen (N)</label>
                              <div class="flex items-baseline gap-1 mt-0.5">
                                <input 
                                  type="number"
                                  v-model="nitrogen"
                                  class="text-xl font-bold text-gray-900 bg-transparent w-20 focus:outline-none"
                                />
                                <span class="text-xs text-gray-500">mg/kg</span>
                              </div>
                            </div>
                          </div>
                          <div class="h-1.5 w-full bg-gray-100 rounded-full">
                            <div 
                              class="h-1.5 bg-green-500 rounded-full transition-all duration-500"
                              :style="{ width: `${(parseFloat(nitrogen) / 150) * 100}%` }"
                            ></div>
                          </div>
                        </div>
                      </div>

                      <!-- Phosphorus Level -->
                      <div class="relative group">
                        <div class="absolute inset-0 bg-gradient-to-r from-blue-50 to-sky-50 rounded-xl transition-opacity opacity-0 group-hover:opacity-100"></div>
                        <div class="relative bg-white rounded-lg p-4 border border-gray-100 transition-all duration-300 hover:border-blue-300 hover:shadow-md">
                          <div class="flex items-center gap-3 mb-3">
                            <div class="p-2 bg-blue-50 rounded-lg">
                              <TestTubesIcon class="w-4 h-4 text-blue-600" />
                            </div>
                            <div>
                              <label class="block text-sm font-medium text-gray-500">Phosphorus (P)</label>
                              <div class="flex items-baseline gap-1 mt-0.5">
                                <input 
                                  type="number"
                                  v-model="phosphorus"
                                  class="text-xl font-bold text-gray-900 bg-transparent w-20 focus:outline-none"
                                />
                                <span class="text-xs text-gray-500">mg/kg</span>
                              </div>
                            </div>
                          </div>
                          <div class="h-1.5 w-full bg-gray-100 rounded-full">
                            <div 
                              class="h-1.5 bg-blue-500 rounded-full transition-all duration-500"
                              :style="{ width: `${(parseFloat(phosphorus) / 150) * 100}%` }"
                            ></div>
                          </div>
                        </div>
                      </div>

                      <!-- Potassium Level -->
                      <div class="relative group">
                        <div class="absolute inset-0 bg-gradient-to-r from-purple-50 to-violet-50 rounded-xl transition-opacity opacity-0 group-hover:opacity-100"></div>
                        <div class="relative bg-white rounded-lg p-4 border border-gray-100 transition-all duration-300 hover:border-purple-300 hover:shadow-md">
                          <div class="flex items-center gap-3 mb-3">
                            <div class="p-2 bg-purple-50 rounded-lg">
                              <BeakerIcon class="w-4 h-4 text-purple-600" />
                            </div>
                            <div>
                              <label class="block text-sm font-medium text-gray-500">Potassium (K)</label>
                              <div class="flex items-baseline gap-1 mt-0.5">
                                <input 
                                  type="number"
                                  v-model="potassium"
                                  class="text-xl font-bold text-gray-900 bg-transparent w-20 focus:outline-none"
                                />
                                <span class="text-xs text-gray-500">mg/kg</span>
                              </div>
                            </div>
                          </div>
                          <div class="h-1.5 w-full bg-gray-100 rounded-full">
                            <div 
                              class="h-1.5 bg-purple-500 rounded-full transition-all duration-500"
                              :style="{ width: `${(parseFloat(potassium) / 150) * 100}%` }"
                            ></div>
                          </div>
                        </div>
                      </div>

                      <!-- pH Level -->
                      <div class="relative group">
                        <div class="absolute inset-0 bg-gradient-to-r from-amber-50 to-yellow-50 rounded-xl transition-opacity opacity-0 group-hover:opacity-100"></div>
                        <div class="relative bg-white rounded-lg p-4 border border-gray-100 transition-all duration-300 hover:border-amber-300 hover:shadow-md">
                          <div class="flex items-center gap-3 mb-3">
                            <div class="p-2 bg-amber-50 rounded-lg">
                              <DropletIcon class="w-4 h-4 text-amber-600" />
                            </div>
                            <div>
                              <label class="block text-sm font-medium text-gray-500">Soil pH</label>
                              <div class="flex items-baseline gap-1 mt-0.5">
                                <input 
                                  type="number"
                                  v-model="soilpH"
                                  class="text-xl font-bold text-gray-900 bg-transparent w-20 focus:outline-none"
                                />
                                <span class="text-xs text-gray-500">pH</span>
                              </div>
                            </div>
                          </div>
                          <div class="h-1.5 w-full bg-gray-100 rounded-full">
                            <div 
                              class="h-1.5 bg-amber-500 rounded-full transition-all duration-500"
                              :style="{ width: `${(parseFloat(soilpH) / 14) * 100}%` }"
                            ></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Environmental Parameters Section -->
                  <div>
                    <h3 class="text-sm font-medium text-gray-700 mb-4 flex items-center">
                      <span class="inline-block w-1.5 h-1.5 bg-blue-500 rounded-full mr-2"></span>
                      Environmental Parameters
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                      <!-- Soil Moisture -->
                      <div class="relative group">
                        <div class="absolute inset-0 bg-gradient-to-r from-cyan-50 to-sky-50 rounded-xl transition-opacity opacity-0 group-hover:opacity-100"></div>
                        <div class="relative bg-white rounded-lg p-4 border border-gray-100 transition-all duration-300 hover:border-cyan-300 hover:shadow-md">
                          <div class="flex items-center gap-3 mb-3">
                            <div class="p-2 bg-cyan-50 rounded-lg">
                              <WavesIcon class="w-4 h-4 text-cyan-600" />
                            </div>
                            <div>
                              <label class="block text-sm font-medium text-gray-500">Soil Moisture</label>
                              <div class="flex items-baseline gap-1 mt-0.5">
                                <input 
                                  type="number"
                                  v-model="soilMoisture"
                                  class="text-xl font-bold text-gray-900 bg-transparent w-20 focus:outline-none"
                                />
                                <span class="text-xs text-gray-500">%</span>
                              </div>
                            </div>
                          </div>
                          <div class="h-1.5 w-full bg-gray-100 rounded-full">
                            <div 
                              class="h-1.5 bg-cyan-500 rounded-full transition-all duration-500"
                              :style="{ width: `${parseFloat(soilMoisture)}%` }"
                            ></div>
                          </div>
                        </div>
                      </div>

                      <!-- Temperature -->
                      <div class="relative group">
                        <div class="absolute inset-0 bg-gradient-to-r from-orange-50 to-red-50 rounded-xl transition-opacity opacity-0 group-hover:opacity-100"></div>
                        <div class="relative bg-white rounded-lg p-4 border border-gray-100 transition-all duration-300 hover:border-orange-300 hover:shadow-md">
                          <div class="flex items-center gap-3 mb-3">
                            <div class="p-2 bg-orange-50 rounded-lg">
                              <ThermometerIcon class="w-4 h-4 text-orange-600" />
                            </div>
                            <div>
                              <label class="block text-sm font-medium text-gray-500">Temperature</label>
                              <div class="flex items-baseline gap-1 mt-0.5">
                                <input 
                                  type="number"
                                  v-model="temperature"
                                  class="text-xl font-bold text-gray-900 bg-transparent w-20 focus:outline-none"
                                />
                                <span class="text-xs text-gray-500">°C</span>
                              </div>
                            </div>
                          </div>
                          <div class="h-1.5 w-full bg-gray-100 rounded-full">
                            <div 
                              class="h-1.5 bg-orange-500 rounded-full transition-all duration-500"
                              :style="{ width: `${(parseFloat(temperature) / 50) * 100}%` }"
                            ></div>
                          </div>
                        </div>
                      </div>

                      <!-- Humidity -->
                      <div class="relative group">
                        <div class="absolute inset-0 bg-gradient-to-r from-teal-50 to-emerald-50 rounded-xl transition-opacity opacity-0 group-hover:opacity-100"></div>
                        <div class="relative bg-white rounded-lg p-4 border border-gray-100 transition-all duration-300 hover:border-teal-300 hover:shadow-md">
                          <div class="flex items-center gap-3 mb-3">
                            <div class="p-2 bg-teal-50 rounded-lg">
                              <CloudIcon class="w-4 h-4 text-teal-600" />
                            </div>
                            <div>
                              <label class="block text-sm font-medium text-gray-500">Humidity</label>
                              <div class="flex items-baseline gap-1 mt-0.5">
                                <input 
                                  type="number"
                                  v-model="humidity"
                                  class="text-xl font-bold text-gray-900 bg-transparent w-20 focus:outline-none"
                                />
                                <span class="text-xs text-gray-500">%</span>
                              </div>
                            </div>
                          </div>
                          <div class="h-1.5 w-full bg-gray-100 rounded-full">
                            <div 
                              class="h-1.5 bg-teal-500 rounded-full transition-all duration-500"
                              :style="{ width: `${parseFloat(humidity)}%` }"
                            ></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Action Button -->
                  <div class="flex justify-center mt-8">
                    <button 
                      type="submit"
                      @click="submitForm"
                      class="inline-flex items-center justify-center px-6 sm:px-8 py-3 text-base font-medium text-white bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl transition-all duration-300 hover:from-green-600 hover:to-emerald-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 gap-2"
                    >
                      <SproutIcon class="w-5 h-5" />
                      <span>Get Crop Recommendations</span>
                    </button>
                  </div>
                </div>
              </div>

              <!-- Table Section with Enhanced UI and Truly Fixed Height -->
              <div class="bg-white rounded-xl shadow-md p-5 sm:p-6 border border-gray-100 relative overflow-hidden">
                <!-- Background Pattern -->
                <div class="absolute top-0 right-0 w-64 h-64 bg-gradient-to-bl from-blue-50 to-transparent opacity-50 -z-10"></div>
                
                <!-- Enhanced Filter Tabs -->
                <div class="border-b border-gray-100 mb-6">
                  <div class="flex gap-4 overflow-x-auto scrollbar-thin scrollbar-thumb-gray-200 scrollbar-track-transparent pb-2">
                    <button 
                      v-for="filter in filters" 
                      :key="filter.name"
                      :class="[
                        'px-4 py-2.5 text-sm font-medium transition-all duration-200 relative whitespace-nowrap',
                        activeFilter === filter.name 
                          ? 'text-green-600' 
                          : 'text-gray-500 hover:text-gray-700'
                      ]"
                      @click="activeFilter = filter.name"
                    >
                      {{ filter.name }}
                      <div 
                        :class="[
                          'absolute bottom-0 left-0 w-full h-0.5 transition-all duration-200',
                          activeFilter === filter.name 
                            ? 'bg-green-500' 
                            : 'bg-transparent group-hover:bg-gray-100'
                        ]"
                      />
                    </button>
                  </div>
                </div>

                <!-- Enhanced Search and Actions -->
                <div class="flex flex-wrap justify-between items-center mb-6 gap-4">
                  <div class="relative flex-1 max-w-md">
                    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                      <SearchIcon class="h-4 w-4 text-gray-400" />
                    </div>
                    <input 
                      type="text"
                      v-model="searchQuery"
                      placeholder="Search predictions..."
                      class="w-full pl-10 pr-4 py-2 text-sm bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
                    />
                  </div>
                  <div class="flex items-center gap-2">
                    <button 
                      class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-50 rounded-lg transition-colors duration-200"
                      @click="toggleGridView"
                      :class="{'bg-gray-100': isGridView}"
                      aria-label="Toggle grid view"
                    >
                      <LayoutGridIcon class="h-4 w-4" />
                    </button>
                    <button 
                      class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-50 rounded-lg transition-colors duration-200"
                      @click="toggleFilterPanel"
                      :class="{'bg-gray-100': showFilterPanel}"
                      aria-label="Toggle filter panel"
                    >
                      <FilterIcon class="h-4 w-4" />
                    </button>
                  </div>
                </div>

                <!-- Filter Panel -->
                <div 
                  v-if="showFilterPanel" 
                  class="bg-gray-50 rounded-lg p-4 mb-6 transition-all duration-300 ease-in-out"
                >
                  <div class="flex justify-between items-center mb-4">
                    <h3 class="text-sm font-medium text-gray-700">Advanced Filters</h3>
                    <button 
                      @click="toggleFilterPanel"
                      class="text-gray-400 hover:text-gray-600"
                    >
                      <XIcon class="h-4 w-4" />
                    </button>
                  </div>
                  
                  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <!-- Success Rate Range -->
                    <div>
                      <label class="block text-xs font-medium text-gray-600 mb-2">Success Rate</label>
                      <div class="flex items-center gap-2">
                        <input 
                          type="number" 
                          v-model="filterSuccessRateMin" 
                          min="0" 
                          max="100"
                          placeholder="Min" 
                          class="w-full px-3 py-2 text-sm bg-white border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500"
                        />
                        <span class="text-gray-400">-</span>
                        <input 
                          type="number" 
                          v-model="filterSuccessRateMax" 
                          min="0" 
                          max="100"
                          placeholder="Max" 
                          class="w-full px-3 py-2 text-sm bg-white border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500"
                        />
                      </div>
                    </div>
                    
                    <!-- Date Range -->
                    <div>
                      <label class="block text-xs font-medium text-gray-600 mb-2">Date Range</label>
                      <div class="flex items-center gap-2">
                        <input 
                          type="date" 
                          v-model="filterDateStart" 
                          class="w-full px-3 py-2 text-sm bg-white border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500"
                        />
                        <span class="text-gray-400">-</span>
                        <input 
                          type="date" 
                          v-model="filterDateEnd" 
                          class="w-full px-3 py-2 text-sm bg-white border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500"
                        />
                      </div>
                    </div>
                    
                    <!-- Status Filter -->
                    <div>
                      <label class="block text-xs font-medium text-gray-600 mb-2">Status</label>
                      <select 
                        v-model="filterStatus" 
                        class="w-full px-3 py-2 text-sm bg-white border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500"
                      >
                        <option value="">All Statuses</option>
                        <option value="Planted">Planted</option>
                        <option value="Ongoing">Ongoing</option>
                        <option value="Harvested">Harvested</option>
                        <option value="Cancelled">Cancelled</option>
                      </select>
                    </div>
                  </div>
                  
                  <div class="flex justify-end mt-4 gap-2">
                    <button 
                      @click="resetFilters"
                      class="px-4 py-2 text-sm font-medium text-gray-600 bg-white rounded-lg border border-gray-200 hover:bg-gray-50 transition-colors"
                    >
                      Reset
                    </button>
                    <button 
                      @click="applyFilters"
                      class="px-4 py-2 text-sm font-medium text-white bg-gradient-to-r from-green-500 to-emerald-500 rounded-lg hover:from-green-600 hover:to-emerald-600 transition-colors"
                    >
                      Apply Filters
                    </button>
                  </div>
                </div>

                <!-- Grid View -->
                <div 
                  v-if="isGridView" 
                  class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-6 transition-all duration-300 ease-in-out"
                >
                  <div 
                    v-for="prediction in paginatedPredictions" 
                    :key="prediction.id"
                    class="bg-white rounded-lg border border-gray-200 p-4 hover:shadow-md transition-all duration-200 hover:-translate-y-1"
                  >
                    <div class="flex items-center gap-3 mb-3">
                      <div class="flex items-center justify-center w-10 h-10 rounded-lg bg-green-50 text-green-600">
                        <SproutIcon class="h-5 w-5" />
                      </div>
                      <div>
                        <h3 class="text-sm font-medium text-gray-900">{{ prediction.crop }}</h3>
                        <p class="text-xs text-gray-500">{{ prediction.date.split(',')[0] }}</p>
                      </div>
                    </div>
                    
                    <div class="space-y-2 mb-3">
                      <div class="flex justify-between items-center">
                        <span class="text-xs text-gray-600">Success Rate:</span>
                        <span class="text-xs font-medium text-gray-900">{{ prediction.successRate }}%</span>
                      </div>
                      <div class="w-full bg-gray-100 rounded-full h-1.5">
                        <div 
                          class="bg-green-500 h-1.5 rounded-full"
                          :style="{ width: `${prediction.successRate}%` }"
                        />
                      </div>
                    </div>
                    
                    <div class="flex items-center justify-between">
                      <span 
                        :class="[
                          'inline-flex items-center px-2 py-1 rounded-full text-xs font-medium',
                          getStatusClass(prediction.status)
                        ]"
                      >
                        <span 
                          :class="[
                            'w-1.5 h-1.5 rounded-full mr-1.5',
                            {
                              'bg-green-500': prediction.status === 'Planted',
                              'bg-blue-500': prediction.status === 'Ongoing',
                              'bg-red-500': prediction.status === 'Cancelled',
                              'bg-gray-500': prediction.status === 'Harvested'
                            }
                          ]"
                        />
                        {{ prediction.status }}
                      </span>
                      
                      <button 
                        @click="showDetails(prediction)"
                        class="inline-flex items-center justify-center px-3 py-1 text-xs font-medium text-white bg-gradient-to-r from-green-500 to-emerald-500 rounded-lg hover:from-green-600 hover:to-emerald-600 transition-colors duration-200 gap-1"
                      >
                        <EyeIcon class="h-3 w-3" />
                        Details
                      </button>
                    </div>
                  </div>
                </div>

                <!-- Enhanced Table with Truly Fixed Height -->
                <div 
                  v-if="!isGridView"
                  class="overflow-hidden rounded-lg border border-gray-100 transition-all duration-300 ease-in-out"
                >
                  <div class="overflow-x-auto">
                    <div class="overflow-y-auto" style="height: 370px"> <!-- Fixed height container -->
                      <table class="w-full">
                        <thead class="sticky top-0 bg-gray-50/95 backdrop-blur-sm z-10">
                          <tr>
                            <th 
                              v-for="header in tableHeaders" 
                              :key="header.key"
                              class="px-4 py-3.5 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                            >
                              {{ header.label }}
                            </th>
                          </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100">
                          <tr 
                            v-for="prediction in paginatedPredictions" 
                            :key="prediction.id"
                            class="group hover:bg-gray-50/50 transition-colors duration-200"
                          >
                            <td class="px-4 py-3.5 whitespace-nowrap">
                              <div class="flex items-center gap-3">
                                <div class="flex items-center justify-center w-8 h-8 rounded-lg bg-green-50 text-green-600">
                                  <SproutIcon class="h-4 w-4" />
                                </div>
                                <span class="text-sm font-medium text-gray-900">
                                  {{ prediction.crop }}
                                </span>
                              </div>
                            </td>
                            <td class="px-4 py-3.5 whitespace-nowrap">
                              <div class="flex flex-col">
                                <span class="text-sm font-medium text-gray-900">
                                  {{ prediction.date.split(',')[1] }}
                                </span>
                                <span class="text-xs text-gray-500">
                                  {{ prediction.date.split(',')[0] }}
                                </span>
                              </div>
                            </td>
                            <td class="px-4 py-3.5 whitespace-nowrap">
                              <div class="flex items-center gap-2">
                                <div class="w-16 bg-gray-100 rounded-full h-1.5">
                                  <div 
                                    class="bg-green-500 h-1.5 rounded-full"
                                    :style="{ width: `${prediction.successRate}%` }"
                                  />
                                </div>
                                <span class="text-sm font-medium text-gray-900">
                                  {{ prediction.successRate }}%
                                </span>
                              </div>
                            </td>
                            <td class="px-4 py-3.5 whitespace-nowrap">
                              <span 
                                :class="[
                                  'inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium',
                                  getStatusClass(prediction.status)
                                ]"
                              >
                                <span 
                                  :class="[
                                    'w-1.5 h-1.5 rounded-full mr-1.5',
                                    {
                                      'bg-green-500': prediction.status === 'Planted',
                                      'bg-blue-500': prediction.status === 'Ongoing',
                                      'bg-red-500': prediction.status === 'Cancelled',
                                      'bg-gray-500': prediction.status === 'Harvested'
                                    }
                                  ]"
                                />
                                {{ prediction.status }}
                              </span>
                            </td>
                            <td class="px-4 py-3.5 whitespace-nowrap">
                              <button 
                                @click="showDetails(prediction)"
                                class="inline-flex items-center justify-center px-3 py-1.5 text-xs font-medium text-white bg-gradient-to-r from-green-500 to-emerald-500 rounded-lg hover:from-green-600 hover:to-emerald-600 transition-colors duration-200 gap-1.5"
                              >
                                <EyeIcon class="h-3.5 w-3.5" />
                                Show
                              </button>
                            </td>
                          </tr>
                          <!-- Placeholder rows to maintain height -->
                          <tr v-for="n in Math.max(0, itemsPerPage - paginatedPredictions.length)" :key="n">
                            <td colspan="6" class="px-4 py-3.5">&nbsp;</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                <!-- Enhanced Pagination -->
                <div class="mt-6 flex flex-wrap items-center justify-between gap-4">
                  <div class="flex items-center gap-2">
                    <label class="text-sm text-gray-600">Items per page</label>
                    <select 
                      v-model="itemsPerPage"
                      class="text-sm border border-gray-200 rounded-lg px-2 py-1 focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500"
                    >
                      <option value="5">5</option>
                      <option value="10">10</option>
                      <option value="20">20</option>
                    </select>
                  </div>
                  
                  <div class="flex items-center gap-2">
                    <button 
                      class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-50 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200"
                      :disabled="currentPage === 1"
                      @click="currentPage--"
                    >
                      <ChevronLeftIcon class="h-4 w-4" />
                    </button>
                    
                    <div class="flex items-center gap-1">
                      <button 
                        v-for="page in totalPages"
                        :key="page"
                        :class="[
                          'px-3 py-1 text-sm font-medium rounded-lg transition-colors duration-200',
                          currentPage === page
                            ? 'bg-gradient-to-r from-green-500 to-emerald-500 text-white'
                            : 'text-gray-500 hover:bg-gray-50'
                        ]"
                        @click="currentPage = page"
                      >
                        {{ page }}
                      </button>
                    </div>
                    
                    <button 
                      class="p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-50 rounded-lg disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200"
                      :disabled="currentPage === totalPages"
                      @click="currentPage++"
                    >
                      <ChevronRightIcon class="h-4 w-4" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Modal Overlay - Completely separate from the main content -->
    <div v-if="showModal" class="fixed inset-0 z-50 overflow-hidden">
      <!-- Backdrop with blur effect -->
      <div class="absolute inset-0 bg-black/50 backdrop-blur-[2px]" @click="closeModal"></div>
      
      <!-- Modal Content - Centered and above the backdrop -->
      <div class="absolute inset-0 flex items-center justify-center p-4">
        <div class="relative bg-white rounded-2xl shadow-xl max-w-xl w-full mx-auto">
          <!-- Modal Header -->
          <div class="text-center p-6 pb-0">
            <h2 class="text-xl font-semibold text-gray-800">Crop Recommendations</h2>
            <p class="text-xs text-gray-500 mt-0.5">Based on your soil parameters</p>
          </div>

          <!-- Main Content Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5 p-6">
            <!-- Left Column -->
            <div class="space-y-4">
              <!-- Primary Recommendation -->
              <div class="bg-gradient-to-br from-green-50 to-emerald-50/50 rounded-lg p-5">
                <div class="flex items-center gap-2 text-green-600 mb-3">
                  <SproutIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Recommended Crop</span>
                </div>
                <h3 class="text-xl font-bold text-green-700 mb-2">{{ recommendedCrop }}</h3>
                <div class="flex items-baseline gap-1 mb-2">
                  <span class="text-2xl font-bold text-green-600">{{ successRate }}</span>
                  <span class="text-sm font-medium text-green-600">%</span>
                </div>
                <p class="text-xs text-gray-600">
                  This crop has a {{ successRate }}% chance of success based on your soil composition.
                </p>
              </div>

              <!-- Success Metrics -->
              <div class="bg-white rounded-lg p-4 border border-gray-100 shadow-sm">
                <div class="flex items-center gap-2 text-green-600 mb-3">
                  <TrendingUpIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Success Metrics</span>
                </div>
                <div class="space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs text-gray-600">Soil Compatibility</span>
                    <span class="text-xs font-medium text-gray-900">{{ soilCompatibility }}%</span>
                  </div>
                  <div class="w-full bg-gray-100 rounded-full h-1.5 mb-1">
                    <div 
                      class="bg-green-500 h-1.5 rounded-full"
                      :style="{ width: `${soilCompatibility}%` }"
                    />
                  </div>
                  
                  <div class="flex items-center justify-between">
                    <span class="text-xs text-gray-600">Growth Rate</span>
                    <span class="text-xs font-medium text-gray-900">{{ growthRate }}%</span>
                  </div>
                  <div class="w-full bg-gray-100 rounded-full h-1.5 mb-1">
                    <div 
                      class="bg-blue-500 h-1.5 rounded-full"
                      :style="{ width: `${growthRate}%` }"
                    />
                  </div>
                  
                  <div class="flex items-center justify-between">
                    <span class="text-xs text-gray-600">Yield Potential</span>
                    <span class="text-xs font-medium text-gray-900">{{ yieldPotential }}%</span>
                  </div>
                  <div class="w-full bg-gray-100 rounded-full h-1.5 mb-1">
                    <div 
                      class="bg-purple-500 h-1.5 rounded-full"
                      :style="{ width: `${yieldPotential}%` }"
                    />
                  </div>
                </div>
              </div>
            </div>

            <!-- Right Column -->
            <div class="space-y-4">
              <!-- Alternative Options -->
              <div class="bg-white rounded-lg p-4 border border-gray-100 shadow-sm">
                <div class="flex items-center gap-2 text-green-600 mb-3">
                  <ListIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Alternative Options</span>
                </div>
                <div class="space-y-3">
                  <div v-for="option in alternativeOptions" :key="option.crop" 
                       class="group">
                    <div class="flex items-center justify-between mb-1.5">
                      <div>
                        <h4 class="text-sm font-medium text-gray-900">
                          {{ option.crop }}
                        </h4>
                        <p class="text-[10px] text-gray-500">Recommended alternative</p>
                      </div>
                      <div class="text-right">
                        <div class="text-sm font-semibold text-gray-900">
                          {{ option.confidence }}%
                        </div>
                        <div class="text-[10px] text-gray-500">Success rate</div>
                      </div>
                    </div>
                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                      <div 
                        class="h-full bg-gradient-to-r from-green-500 to-emerald-500 rounded-full transition-all" 
                        :style="{ width: `${option.confidence}%` }"
                      ></div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Crop Rotation Tip -->
              <div class="bg-gradient-to-br from-green-50 to-emerald-50/50 rounded-lg p-3">
                <div class="flex items-start gap-2">
                  <div class="mt-0.5">
                    <InfoIcon class="h-3.5 w-3.5 text-green-600" />
                  </div>
                  <div>
                    <h5 class="text-xs font-medium text-green-700 mb-1">Crop Rotation Tip</h5>
                    <p class="text-[11px] leading-relaxed text-green-600">
                      Consider rotating between these crops to maintain soil health and maximize yields over time.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex justify-end gap-2 p-6 pt-0 border-t border-gray-100">
            <button 
              @click="closeModal"
              class="px-4 py-2 text-sm font-medium text-gray-600 rounded-lg hover:bg-gray-100 hover:text-gray-900 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gray-200"
            >
              Close
            </button>
            <button 
              @click="saveRecommendation"
              class="px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-500 text-white text-sm font-medium rounded-lg hover:from-green-600 hover:to-emerald-600 transition-colors flex items-center gap-1.5 shadow-sm"
            >
              <DownloadIcon class="h-3.5 w-3.5" />
              Save Recommendation
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Details Modal - Using the same approach as the recommendation modal -->
    <div v-if="showDetailsModal" class="fixed inset-0 z-50 overflow-hidden">
      <!-- Backdrop with blur effect -->
      <div class="absolute inset-0 bg-black/50 backdrop-blur-[2px]" @click="closeDetailsModal"></div>
    
      <!-- Modal Content - Centered and above the backdrop -->
      <div class="absolute inset-0 flex items-center justify-center p-4">
        <div class="relative bg-white rounded-2xl shadow-xl max-w-xl w-full mx-auto max-h-[90vh] overflow-y-auto">
          <!-- Modal Header -->
          <div class="text-center p-4 pb-0">
            <h2 class="text-lg font-semibold text-gray-800">Crop Details</h2>
            <p class="text-xs text-gray-500 mt-0.5">Detailed information and management</p>
          </div>

          <!-- Main Content Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 p-4">
            <!-- Left Column -->
            <div class="space-y-3">
              <!-- Primary Recommendation -->
              <div class="bg-gradient-to-br from-green-50 to-emerald-50/50 rounded-lg p-4">
                <div class="flex items-center gap-2 text-green-600 mb-2">
                  <SproutIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Recommended Crop</span>
                </div>
                <h3 class="text-lg font-bold text-green-700 mb-1">{{ selectedPrediction?.crop }}</h3>
                <div class="flex items-baseline gap-1 mb-1">
                  <span class="text-xl font-bold text-green-600">{{ selectedPrediction?.successRate }}</span>
                  <span class="text-sm font-medium text-green-600">%</span>
                </div>
                <p class="text-xs text-gray-600">
                  Recommended on {{ new Date(selectedPrediction?.date).toLocaleString() }}
                </p>
              </div>

              <!-- Recommended Fertilizer -->
              <div class="bg-white rounded-lg p-4 border border-gray-100 shadow-sm">
                <div class="flex items-center gap-2 text-green-600 mb-3">
                  <FlaskIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Recommended Fertilizer</span>
                </div>
                <div class="space-y-2">
                  <div class="flex justify-between items-center">
                    <span class="text-sm font-medium text-gray-700">Type:</span>
                    <span class="text-sm text-gray-600">{{ selectedPrediction?.fertilizer?.type || 'N/A' }}</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="text-sm font-medium text-gray-700">Name:</span>
                    <span class="text-sm text-gray-600">{{ selectedPrediction?.fertilizer?.name || 'N/A' }}</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="text-sm font-medium text-gray-700">Amount:</span>
                    <span class="text-sm text-gray-600">
                      {{ selectedPrediction?.fertilizer?.adjusted_amount || 0 }} {{ selectedPrediction?.fertilizer?.unit || '' }}
                    </span>
                  </div>
                </div>
              </div>

              <!-- Status Management -->
              <div class="bg-white rounded-lg p-3 border border-gray-100 shadow-sm">
                <div class="flex items-center gap-2 text-green-600 mb-2">
                  <ActivityIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Status Management</span>
                </div>
                <div class="grid grid-cols-2 gap-2">
                  <button
                    v-for="status in ['Planted', 'Ongoing', 'Harvested', 'Cancelled']"
                    :key="status"
                    @click="updateStatus(status)"
                    :class="[
                      'px-3 py-1.5 rounded-lg text-xs font-medium transition-all duration-200',
                      editedStatus === status
                        ? getStatusButtonClass(status)
                        : 'bg-gray-50 text-gray-600 hover:bg-gray-100'
                    ]"
                  >
                    {{ status }}
                  </button>
                </div>
              </div>
            </div>

            <!-- Right Column -->
            <div class="space-y-3">
              <!-- Alternative Options with Fertilizers -->
              <div class="bg-white rounded-lg p-4 border border-gray-100 shadow-sm">
                <div class="flex items-center gap-2 text-green-600 mb-3">
                  <ListIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Alternative Options</span>
                </div>
                <div class="space-y-4">
                  <div v-for="option in alternativeCrops" :key="option.crop" class="space-y-2">
                    <!-- Crop Info -->
                    <div class="flex items-center justify-between">
                      <div>
                        <h4 class="text-sm font-medium text-gray-900">{{ option.crop }}</h4>
                        <p class="text-[10px] text-gray-500">Alternative crop</p>
                      </div>
                      <div class="text-right">
                        <div class="text-sm font-semibold text-gray-900">
                          {{ option.confidence }}%
                        </div>
                      </div>
                    </div>
                    <!-- Progress Bar -->
                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                      <div 
                        class="h-full bg-gradient-to-r from-green-500 to-emerald-500 rounded-full transition-all" 
                        :style="{ width: `${option.confidence}%` }"
                      ></div>
                    </div>
                    <!-- Fertilizer Info -->
                    <div class="bg-gray-50 rounded-lg p-2 mt-2">
                      <div class="text-[10px] font-medium text-gray-600 mb-1">Recommended Fertilizer:</div>
                      <div class="grid grid-cols-2 gap-1 text-[10px]">
                        <div class="text-gray-500">Type:</div>
                        <div class="text-gray-700 text-right">{{ option.fertilizer?.type || 'N/A' }}</div>
                        <div class="text-gray-500">Name:</div>
                        <div class="text-gray-700 text-right">{{ option.fertilizer?.name || 'N/A' }}</div>
                        <div class="text-gray-500">Amount:</div>
                        <div class="text-gray-700 text-right">
                          {{ option.fertilizer?.adjusted_amount || 0 }} {{ option.fertilizer?.unit || '' }}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Success Metrics -->
              <div class="bg-white rounded-lg p-4 border border-gray-100 shadow-sm">
                <div class="flex items-center gap-2 text-green-600 mb-3">
                  <TrendingUpIcon class="h-4 w-4" />
                  <span class="text-xs font-medium">Success Metrics</span>
                </div>
                <div class="space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs text-gray-600">Soil Compatibility</span>
                    <span class="text-xs font-medium text-gray-900">{{ selectedPrediction?.soilCompatibility }}%</span>
                  </div>
                  <div class="w-full bg-gray-100 rounded-full h-1.5 mb-1">
                    <div 
                      class="bg-green-500 h-1.5 rounded-full"
                      :style="{ width: `${selectedPrediction?.soilCompatibility}%` }"
                    />
                  </div>
                  
                  <div class="flex items-center justify-between">
                    <span class="text-xs text-gray-600">Growth Rate</span>
                    <span class="text-xs font-medium text-gray-900">{{ selectedPrediction?.growthRate }}%</span>
                  </div>
                  <div class="w-full bg-gray-100 rounded-full h-1.5 mb-1">
                    <div 
                      class="bg-blue-500 h-1.5 rounded-full"
                      :style="{ width: `${selectedPrediction?.growthRate}%` }"
                    />
                  </div>
                  
                  <div class="flex items-center justify-between">
                    <span class="text-xs text-gray-600">Yield Potential</span>
                    <span class="text-xs font-medium text-gray-900">{{ selectedPrediction?.yieldPotential }}%</span>
                  </div>
                  <div class="w-full bg-gray-100 rounded-full h-1.5 mb-1">
                    <div 
                      class="bg-purple-500 h-1.5 rounded-full"
                      :style="{ width: `${selectedPrediction?.yieldPotential}%` }"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex justify-end gap-2 p-4 pt-3 border-t border-gray-100">
            <button 
              @click="closeDetailsModal"
              class="px-3 py-1.5 text-sm font-medium text-gray-600 rounded-lg hover:bg-gray-100 hover:text-gray-900 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gray-200"
            >
              Close
            </button>
            <button 
              class="px-3 py-1.5 bg-gradient-to-r from-green-500 to-emerald-500 text-white text-sm font-medium rounded-lg hover:from-green-600 hover:to-emerald-600 transition-colors flex items-center gap-1.5 shadow-sm"
              @click="saveChanges"
            >
              <SaveIcon class="h-3.5 w-3.5" />
              Save Changes
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Script section remains the same as in the previous version
import { ref, computed, onMounted } from 'vue'
import { 
  ChartBarIcon,
  ClipboardListIcon,
  TrendingUpIcon,
  ActivityIcon,
  ActivitySquareIcon,
  BeakerIcon,
  TestTubesIcon,
  DropletIcon,
  WavesIcon,
  ThermometerIcon,
  CloudIcon,
  SproutIcon,
  XIcon,
  ListIcon,
  SearchIcon,
  FilterIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
  LayoutGridIcon,
  InfoIcon,
  DownloadIcon,
  ArrowUpIcon,
  ArrowDownIcon,
  WarehouseIcon,
  CalendarIcon,
  EyeIcon,
  BeakerIcon as FlaskIcon,
  SaveIcon,
  TableIcon
} from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'
// import Pagination from '../layout/Pagination.vue'
import api from '../../api/index.js'
import toastr from 'toastr'
import {
    getFirestore,
    collection,
    addDoc,
    getDocs,
    query,
    orderBy,
    limit,
    doc,
    setDoc,
    Timestamp,
    serverTimestamp,
    getDoc,
    updateDoc,
    deleteDoc,
    where
  } from 'firebase/firestore'
const db = getFirestore()

// Initialize all sensor data as reactive refs
const nitrogen = ref(0)
const phosphorus = ref(0)
const potassium = ref(0)
const soilpH = ref(0)
const soilMoisture = ref(0)
const temperature = ref(0)
const humidity = ref(0)

// Add new state for grid view and filter panel
const isGridView = ref(false)
const showFilterPanel = ref(false)

// Filter states
const filterSuccessRateMin = ref('')
const filterSuccessRateMax = ref('')
const filterDateStart = ref('')
const filterDateEnd = ref('')
const filterStatus = ref('')

const showModal = ref(false)
const recommendedCrop = ref('')
const successRate = ref(0)
const soilCompatibility = ref(0)
const growthRate = ref(0)
const yieldPotential = ref(0)
const alternativeOptions = ref([])
const fertilizer = ref({
  type: '',
  name: '',
  base_amount: 0,
  adjusted_amount: 0,
  unit: ''
})

const predictions = ref([])
const filteredPredictionsCache = ref([]) // Cache for filtered predictions
const searchQuery = ref('')
const currentPage = ref(1)
const itemsPerPage = ref(5)
const activeFilter = ref('All')

const showDetailsModal = ref(false)
const selectedPrediction = ref(null)
const alternativeCrops = ref([])
const recommendedFertilizers = ref([])
const editedStatus = ref(null)

const totalRecommendations = ref(0)
const previousRecommendationCount = ref(0)
const percentageChange = ref(0)
const isIncrease = ref(true)

const plantedCount = ref(0)
const plantedPercentageChange = ref(0)
const plantedIsIncrease = ref(true)

const harvestSuccessRate = ref(0)
const harvestedCount = ref(0)
const previousSuccessRate = ref(0)

const ongoingCount = ref(0) // Ongoing Count
const ongoingPercentageChange = ref(0) // Ongoing Percentage Change
const ongoingIsIncrease = ref(true) // Ongoing Increase or Decrease

// Function to toggle grid view
const toggleGridView = () => {
  isGridView.value = !isGridView.value
}

// Function to toggle filter panel
const toggleFilterPanel = () => {
  showFilterPanel.value = !showFilterPanel.value
}

// Function to reset filters
const resetFilters = () => {
  filterSuccessRateMin.value = ''
  filterSuccessRateMax.value = ''
  filterDateStart.value = ''
  filterDateEnd.value = ''
  filterStatus.value = ''
  
  // Reset to original predictions
  filteredPredictionsCache.value = [...predictions.value]
  currentPage.value = 1
}

// Function to apply filters
const applyFilters = () => {
  let filtered = [...predictions.value]
  
  // Apply success rate filter
  if (filterSuccessRateMin.value !== '') {
    filtered = filtered.filter(p => p.successRate >= parseFloat(filterSuccessRateMin.value))
  }
  
  if (filterSuccessRateMax.value !== '') {
    filtered = filtered.filter(p => p.successRate <= parseFloat(filterSuccessRateMax.value))
  }
  
  // Apply date filter
  if (filterDateStart.value !== '') {
    const startDate = new Date(filterDateStart.value)
    filtered = filtered.filter(p => new Date(p.date) >= startDate)
  }
  
  if (filterDateEnd.value !== '') {
    const endDate = new Date(filterDateEnd.value)
    endDate.setHours(23, 59, 59, 999) // Set to end of day
    filtered = filtered.filter(p => new Date(p.date) <= endDate)
  }
  
  // Apply status filter
  if (filterStatus.value !== '') {
    filtered = filtered.filter(p => p.status === filterStatus.value)
  }
  
  // Update filtered predictions cache
  filteredPredictionsCache.value = filtered
  
  // Reset to first page
  currentPage.value = 1
}

// Greenhouse data - now all parameters are dynamic
const greenhouse1Data = ref({
  nitrogen: '32',
  phosphorus: '121',
  potassium: '114',
  ph: '5.3',
  moisture: '0.0',
  temperature: '27.1',
  humidity: '81.7',
})

const greenhouse2Data = ref({
  nitrogen: '92.15',
  phosphorus: '25.32',
  potassium: '83.76',
  ph: '6.98',
  moisture: '48.50',
  temperature: '30.75',
  humidity: '72.34'
})

onMounted(async () => {
  await fetchLatestSensorDataFromFirebase()

  // Step 2: Start listening for real-time updates
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

    console.log("🔁 Real-time data:", data)
  }

  fetchSavedRecommendations()
  fetchRecommendationStats()
})

const fetchLatestSensorDataFromFirebase = async () => {
  try {
    const q = query(collection(db, "sensor_readings"), orderBy("timestamp", "desc"), limit(1))
    const snapshot = await getDocs(q)

    if (!snapshot.empty) {
      const latestDoc = snapshot.docs[0]
      const latestData = latestDoc.data()

      // ✅ Convert Firestore timestamp to JS Date
      const timestamp = latestData.timestamp
      latestData.timestamp = timestamp instanceof Timestamp ? timestamp.toDate() : new Date(timestamp.seconds * 1000)

      // Now assign the values
      nitrogen.value = latestData.nitrogen
      phosphorus.value = latestData.phosphorus
      potassium.value = latestData.potassium
      soilpH.value = latestData.soilPh
      temperature.value = latestData.temperature
      humidity.value = latestData.humidity
      soilMoisture.value = latestData.soilMoisture

      console.log("📥 Latest Firebase Data with Date:", latestData)
    }
  } catch (err) {
    console.error("❌ Error fetching from Firebase:", err)
  }
}

// Function to calculate percentage change between two periods
const calculatePercentageChange = (docs, status = '') => {
  let percentageChange = 0
  let isIncrease = true

  // Ensure there's more than one data point to calculate change
  if (docs.length > 1) {
    const firstDocCount = docs[0].length
    const lastDocCount = docs[docs.length - 1].length

    // Avoid division by zero
    if (firstDocCount === 0) {
      percentageChange = 0
      isIncrease = true
    } else {
      const change = lastDocCount - firstDocCount
      percentageChange = ((change / firstDocCount) * 100).toFixed(1)
      isIncrease = change >= 0
    }
  }

  // Return the percentage change and whether it increased or decreased
  return { percentageChange: isNaN(percentageChange) ? 0 : parseFloat(percentageChange), isIncrease }
}

const fetchRecommendationStats = async () => {
  try {
    // Fetch all crop recommendation records
    const snapshot = await getDocs(collection(db, 'crop_recommendations'))
    const allDocs = snapshot.docs.map(doc => doc.data())

    totalRecommendations.value = allDocs.length // Total count of all recommendations

    // Calculate Harvested Count and Success Rate
    harvestedCount.value = allDocs.filter(doc => doc.status === 'Harvested').length
    harvestSuccessRate.value = totalRecommendations.value > 0
      ? ((harvestedCount.value / totalRecommendations.value) * 100).toFixed(1)
      : 0

    // Calculate Planted Count and Percentage Change
    const plantedDocs = allDocs.filter(doc => doc.status === 'Planted')
    plantedCount.value = plantedDocs.length

    // Calculate the percentage change for Planted recommendations
    const plantedChanges = calculatePercentageChange(plantedDocs, 'Planted')

    plantedPercentageChange.value = plantedChanges.percentageChange
    plantedIsIncrease.value = plantedChanges.isIncrease

    // Calculate Ongoing Count and Percentage Change
    const ongoingDocs = allDocs.filter(doc => doc.status === 'Ongoing')
    ongoingCount.value = ongoingDocs.length

    const ongoingChanges = calculatePercentageChange(ongoingDocs, 'Ongoing')

    ongoingPercentageChange.value = ongoingChanges.percentageChange
    ongoingIsIncrease.value = ongoingChanges.isIncrease

    // Calculate the percentage change for all recommendations
    const recommendationChanges = calculatePercentageChange(allDocs)
    percentageChange.value = recommendationChanges.percentageChange
    isIncrease.value = recommendationChanges.isIncrease

  } catch (error) {
    console.error("❌ Error fetching recommendation stats:", error)
  }
}

const selectedGreenhouse = ref(1)

const currentGreenhouseData = computed(() => {
  return selectedGreenhouse.value === 1 ? greenhouse1Data.value : greenhouse2Data.value
})

const selectGreenhouse = (greenhouse) => {
  selectedGreenhouse.value = greenhouse
}

const submitForm = async () => {
  const payload = {
    nitrogen: parseFloat(nitrogen.value),
    phosphorus: parseFloat(phosphorus.value),
    potassium: parseFloat(potassium.value),
    soilpH: parseFloat(soilpH.value),
    soilMoisture: parseFloat(soilMoisture.value),
    temperature: parseFloat(temperature.value),
    humidity: parseFloat(humidity.value),
  }

  console.log("Payload being sent to backend:", payload)

  try {
    const res = await api.post('/crop/recommend', payload)
    console.log("Payload sent to backend:", payload)

    const result = res.data

    recommendedCrop.value = result.recommendedCrop
    successRate.value = result.successRate
    alternativeOptions.value = result.alternativeOptions
    soilCompatibility.value = result.soilCompatibility
    growthRate.value = result.growthRate
    yieldPotential.value = result.yieldPotential
    fertilizer.value = result.fertilizer
    showModal.value = true
  } catch (error) {
    console.error('Fetch error:', error)
  }
}

const saveRecommendation = async () => {
  const payload = {
    recommendedCrop: recommendedCrop.value,
    successRate: successRate.value,
    soilCompatibility: soilCompatibility.value,
    growthRate: growthRate.value,
    yieldPotential: yieldPotential.value,
    fertilizer: {
      type: fertilizer.value.type,
      name: fertilizer.value.name,
      base_amount: fertilizer.value.base_amount,
      adjusted_amount: fertilizer.value.adjusted_amount,
      unit: fertilizer.value.unit
    },
    alternativeOptions: alternativeOptions.value.map(alt => ({
      crop: alt.crop,
      confidence: alt.confidence,
      fertilizer: {
        type: alt.fertilizer.type,
        name: alt.fertilizer.name,
        base_amount: alt.fertilizer.base_amount,
        adjusted_amount: alt.fertilizer.adjusted_amount,
        unit: alt.fertilizer.unit
      }
    })),
    // Add soil reading data
    soilData: {
      nitrogen: nitrogen.value,
      phosphorus: phosphorus.value,
      potassium: potassium.value,
      soilpH: soilpH.value,
      soilMoisture: soilMoisture.value,
      temperature: temperature.value,
      humidity: humidity.value,
    }
  }

  try {
    // First save the soil reading
    const soilReadingRef = await addDoc(collection(db, "sensor_readings"), {
      nitrogen: nitrogen.value,
      phosphorus: phosphorus.value,
      potassium: potassium.value,
      soilPh: soilpH.value,
      soilMoisture: soilMoisture.value,
      temperature: temperature.value,
      humidity: humidity.value,
      timestamp: serverTimestamp()
    });

    // Add the soil reading reference to the payload
    payload.soilReadingId = soilReadingRef.id;

    const res = await api.post('/crop/save', payload)
    console.log("send to back:", payload)
    console.log("✅ Saved recommendation:", res.data)
    toastr.success('Recommendation Saved successfully')
    closeModal()
    fetchSavedRecommendations()
  } catch (error) {
    console.error('❌ Error saving recommendation:', error)
    toastr.error('Unexpected error, please try again')
  }
}

const closeModal = () => {
  showModal.value = false
}

const filters = [
  { name: 'All' },
  { name: 'Planted' },
  { name: 'Ongoing' },
  { name: 'Cancelled' },
  { name: 'Harvested' }
]

const tableHeaders = [
  { key: 'crop', label: 'Recommended Crop' },
  { key: 'date', label: 'Date & Time' },
  { key: 'successRate', label: 'Success Rate' },
  { key: 'status', label: 'Status' },
  { key: 'actions', label: 'Actions' }
]

const fetchSavedRecommendations = async () => {
  try {
    // Create a query to get all crop recommendations, ordered by timestamp
    const q = query(
      collection(db, 'crop_recommendations'),
      orderBy('timestamp', 'desc')
    )
    
    const querySnapshot = await getDocs(q)
    
    // Map the documents to include id and format the data
    predictions.value = querySnapshot.docs.map(doc => {
      const data = doc.data()
      let formattedDate = new Date().toLocaleString() // Default to current date
      
      try {
        if (data.timestamp) {
          // Handle Firestore Timestamp
          if (data.timestamp.toDate) {
            formattedDate = data.timestamp.toDate().toLocaleString()
          } 
          // Handle regular Date object
          else if (data.timestamp instanceof Date) {
            formattedDate = data.timestamp.toLocaleString()
          }
          // Handle timestamp as number
          else if (typeof data.timestamp === 'number') {
            formattedDate = new Date(data.timestamp).toLocaleString()
          }
        }
      } catch (error) {
        console.warn('Error formatting date:', error)
      }

      return {
        id: doc.id,
        crop: data.recommendedCrop,
        successRate: data.successRate,
        status: data.status || 'Recommended',
        date: formattedDate,
        soilCompatibility: data.soilCompatibility,
        growthRate: data.growthRate,
        yieldPotential: data.yieldPotential,
        alternativeOptions: data.alternativeOptions?.map(alt => ({
          ...alt,
          fertilizer: alt.fertilizer || {
            type: '',
            name: '',
            base_amount: 0,
            adjusted_amount: 0,
            unit: ''
          }
        })) || [],
        fertilizer: data.fertilizer || {
          type: '',
          name: '',
          base_amount: 0,
          adjusted_amount: 0,
          unit: ''
        }
      }
    })
    
    // Initialize filtered predictions cache
    filteredPredictionsCache.value = [...predictions.value]
    
    console.log("✅ Fetched recommendations:", predictions.value)
  } catch (error) {
    console.error("❌ Error fetching predictions from Firebase:", error)
    toastr.error('Failed to fetch crop recommendations')
  }
}

onMounted(fetchSavedRecommendations)

const filteredPredictions = computed(() => {
  // Start with the filtered cache if it exists, otherwise use all predictions
  let result = filteredPredictionsCache.value.length > 0 ? filteredPredictionsCache.value : predictions.value

  if (activeFilter.value !== 'All') {
    result = result.filter(p => p.status === activeFilter.value)
  }

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(p => p.crop.toLowerCase().includes(query))
  }

  return result
})

const paginatedPredictions = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return filteredPredictions.value.slice(start, end)
})

const totalPages = computed(() => Math.ceil(filteredPredictions.value.length / itemsPerPage.value))

const getStatusClass = (status) => {
  const classes = {
    'Planted': 'bg-green-100 text-green-700',
    'Ongoing': 'bg-blue-100 text-blue-700',
    'Cancelled': 'bg-red-100 text-red-700',
    'Harvested': 'bg-gray-100 text-gray-700',
    'Recommended': ''
  }
  return classes[status]
}

const showDetails = (prediction) => {
  selectedPrediction.value = prediction
  editedStatus.value = prediction.status  
  // Sort alternatives by confidence or successRate (whichever you save)
  const sortedAlternatives = [...(prediction.alternativeOptions || [])].sort(
    (a, b) => (b.confidence || b.successRate || 0) - (a.confidence || a.successRate || 0)
  )

  alternativeCrops.value = sortedAlternatives

  // If fertilizers were included
  recommendedFertilizers.value = prediction.recommendedFertilizers || []

  showDetailsModal.value = true
}

const updateStatus = (status) => {
  editedStatus.value = status
}

const getStatusButtonClass = (status) => {
  switch (status) {
    case 'Planted':
      return 'bg-green-100 text-green-700'
    case 'Ongoing':
      return 'bg-blue-100 text-blue-700'
    case 'Harvested':
      return 'bg-gray-100 text-gray-700'
    case 'Cancelled':
      return 'bg-red-100 text-red-700'
    default:
      return 'bg-gray-50 text-gray-600'
  }
}

const closeDetailsModal = () => {
  showDetailsModal.value = false
  selectedPrediction.value = null
  alternativeCrops.value = []
  recommendedFertilizers.value = []
  editedStatus.value = null
}

const saveChanges = async () => {
  if (!selectedPrediction.value) return

  try {
    await api.post(`/crop/recommendations/${selectedPrediction.value.id}/status`, null, {
      params: { status: editedStatus.value }
    })

    selectedPrediction.value.status = editedStatus.value // update locally too

    // Optional: update in the main table
    const index = predictions.value.findIndex(p => p.id === selectedPrediction.value.id)
    if (index !== -1) predictions.value[index].status = editedStatus.value

    toastr.success('Status updated successfully')
    closeDetailsModal()
  } catch (err) {
    console.error('Error saving changes:', err)
    toastr.error('Failed to save changes')
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Smooth transitions */
* {
  transition: all 200ms ease-in-out;
}

/* Enhanced hover effects */
.hover\:shadow-md:hover {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

/* Custom scrollbar styling */
.scrollbar-thin {
  scrollbar-width: thin;
  scrollbar-color: rgba(156, 163, 175, 0.5) transparent;
}

.scrollbar-thin::-webkit-scrollbar {
  height: 6px;
  width: 6px;
}

.scrollbar-thin::-webkit-scrollbar-track {
  background: transparent;
}

.scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.5);
  border-radius: 3px;
}

.scrollbar-thumb-gray-200::-webkit-scrollbar-thumb {
  background-color: rgba(229, 231, 235, 0.8);
}

.scrollbar-thumb-gray-200:hover::-webkit-scrollbar-thumb {
  background-color: rgba(209, 213, 219, 1);
}

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

.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(20, 83, 45, 0.5) transparent;
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgba(20, 83, 45, 0.5);
  border-radius: 9999px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
  background-color: rgba(20, 83, 45, 0.7);
}

/* Card animations */
.bg-white {
  transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.bg-white:hover {
  transform: translateY(-2px);
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .text-xl {
    font-size: 1.1rem;
  }
  
  .p-6 {
    padding: 1rem;
  }
}

/* Gradient animations */
.bg-gradient-to-r {
  background-size: 200% 200%;
  animation: gradientShift 8s ease infinite;
}

@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>