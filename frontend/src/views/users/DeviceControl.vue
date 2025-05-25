<template>
  <div class="h-screen flex bg-white font-poppins overflow-hidden">
    <Sidebar />
    <main class="flex-1 flex flex-col h-screen pt-32">
      <div class="flex-1 w-full px-4 sm:px-6 md:px:8 lg:px-10 overflow-hidden">
        <!-- Enhanced main container with more appealing design -->
        <div class="bg-white rounded-lg shadow-lg border border-gray-100 h-[calc(100vh-140px)] flex flex-col overflow-hidden">
          <!-- Gradient header for visual appeal -->
          <div class="bg-gradient-to-r from-emerald-50 to-white p-6 border-b border-gray-100 rounded-t-lg">
            <!-- Header with controls aligned side by side -->
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <!-- Title and breadcrumb with enhanced styling -->
              <div>
                <h1 class="text-xl font-semibold text-gray-800 mb-1">Device Control</h1>
                <div class="flex items-center text-sm text-gray-500">
                  <span class="text-emerald-600 font-medium">Device Setup</span>
                  <ChevronRight class="h-3.5 w-3.5 mx-1 text-gray-400" />
                  <span class="text-gray-600">{{ currentView === 'history' ? 'Schedule History' : 'Overview' }}</span>
                </div>
              </div>
              
              <!-- Controls aligned horizontally with improved styling -->
              <div v-if="currentView === 'history'" class="flex items-center gap-2 flex-wrap md:flex-nowrap">
                <!-- Back to overview button -->
                <button 
                  @click="backToOverview()" 
                  class="flex items-center gap-1.5 bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium rounded-full px-4 py-2 transition-all duration-300 shadow-sm hover:shadow-md text-sm"
                >
                  <ArrowLeft class="w-4 h-4" />
                  <span>Back to Overview</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Content Wrapper - ONLY THIS SHOULD BE SCROLLABLE -->
          <div v-if="currentView === 'overview'" class="p-6 md:p-8 overflow-y-auto">
            <!-- System Controls Section - KEEPING ORIGINAL 3-COLUMN GRID -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <!-- Motor Control Card - Left Position (COMPLETELY UNTOUCHED) -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                <div class="flex items-center justify-between mb-6">
                  <div class="flex items-center gap-2">
                    <!-- Changed icon color from purple to green -->
                    <div class="text-green-500">
                      <Droplet class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Motor Control</h2>
                  </div>
                </div>
                
                <!-- Motor Status and Toggle - Ultra Modern Design -->
                <div class="mt-6">
                  <div class="flex items-center justify-between mb-4">
                    <span class="text-sm font-medium text-gray-700">Motor Status</span>
                    <div class="flex items-center gap-2">
                      <div class="w-2.5 h-2.5 rounded-full" :class="waterPumpActive ? 'bg-green-500' : 'bg-gray-300'"></div>
                      <span 
                        class="text-xs font-medium tracking-wider px-2 py-1 rounded-full"
                        :class="waterPumpActive ? 'bg-green-100 text-green-600' : 'bg-gray-100 text-gray-500'"
                      >
                        {{ waterPumpActive ? 'ACTIVE' : 'INACTIVE' }}
                      </span>
                    </div>
                  </div>
                  
                  <!-- Ultra Modern Power Button - FIXED CLICKABLE AREA -->
                  <div class="flex justify-center mb-8">
                    <!-- Entire button container is now clickable -->
                    <div 
                      class="relative w-48 h-48 cursor-pointer"
                      @click="showToggleConfirmation()"
                    >
                      <!-- Outer glow effect -->
                      <div 
                        class="absolute inset-0 rounded-full blur-xl transition-all duration-500 pointer-events-none"
                        :class="waterPumpActive ? 'bg-green-300 opacity-40' : 'bg-orange-300 opacity-30'"
                      ></div>
                      
                      <!-- Subtle background pattern -->
                      <div class="absolute inset-0 rounded-full overflow-hidden opacity-10 pointer-events-none">
                        <div class="absolute inset-0 bg-gradient-to-br from-white to-transparent"></div>
                        <div v-for="i in 8" :key="`pattern-${i}`" class="absolute w-full h-0.5 bg-white opacity-30"
                          :style="{
                            transform: `rotate(${i * 22.5}deg)`,
                            top: '50%'
                          }"
                        ></div>
                      </div>
                      
                      <!-- Outer ring with subtle gradient -->
                      <div 
                        class="absolute inset-0 rounded-full border-2 transition-all duration-500 pointer-events-none"
                        :class="waterPumpActive ? 'border-green-300 opacity-80' : 'border-orange-300 opacity-60'"
                      >
                        <div class="absolute inset-0 rounded-full bg-gradient-to-b from-white to-transparent opacity-30"></div>
                      </div>
                      
                      <!-- Tick marks around the button - Properly positioned -->
                      <div class="absolute inset-0 pointer-events-none">
                        <div v-for="i in 12" :key="`tick-${i}`" 
                          class="absolute w-1 h-3 rounded-full transition-all duration-300" 
                          :class="waterPumpActive ? 'bg-green-200' : 'bg-orange-200'"
                          :style="{
                            transform: `rotate(${i * 30}deg) translateY(-22px)`,
                            left: 'calc(50% - 0.5px)',
                            top: '50%',
                            transformOrigin: 'center calc(100% + 22px)',
                            opacity: i % 3 === 0 ? '0.8' : '0.4'
                          }"
                        ></div>
                      </div>
                      
                      <!-- Main button with glass morphism effect -->
                      <div 
                        class="absolute inset-6 rounded-full overflow-hidden transition-all duration-500 z-10 glass-button pointer-events-none"
                        :class="waterPumpActive ? 'active-button' : 'inactive-button'"
                      >
                        <!-- Background gradient -->
                        <div 
                          class="absolute inset-0 transition-all duration-500"
                          :class="waterPumpActive ? 'bg-gradient-to-br from-green-400 to-green-600' : 'bg-gradient-to-br from-orange-400 to-orange-600'"
                        ></div>
                        
                        <!-- Glass effect overlay -->
                        <div class="absolute inset-0 bg-white opacity-10"></div>
                        <div class="absolute inset-0 bg-gradient-to-b from-white to-transparent opacity-20"></div>
                        
                        <!-- Highlight effect -->
                        <div class="absolute inset-x-0 top-0 h-1/3 bg-gradient-to-b from-white to-transparent opacity-30 rounded-t-full"></div>
                        
                        <!-- Center content with modern icon -->
                        <div class="absolute inset-0 flex items-center justify-center">
                          <div class="text-center z-20">
                            <!-- Power icon with glow effect -->
                            <div class="relative">
                              <Power class="w-12 h-12 text-white drop-shadow-lg" :class="waterPumpActive ? 'power-icon-on' : 'power-icon-off'" />
                            </div>
                            
                            <!-- Status text with modern font -->
                            <div class="mt-2">
                              <span class="text-2xl font-bold text-white drop-shadow-lg tracking-wider">
                                {{ waterPumpActive ? 'ON' : 'OFF' }}
                              </span>
                            </div>
                          </div>
                        </div>
                        
                        <!-- Animated pulse effect when active -->
                        <div 
                          v-if="waterPumpActive" 
                          class="absolute inset-0 bg-white opacity-0 pulse-animation"
                        ></div>
                      </div>
                      
                      <!-- Inner ring glow -->
                      <div 
                        class="absolute pointer-events-none"
                        :class="waterPumpActive ? 'inset-5 rounded-full border border-green-200 opacity-60' : 'inset-5 rounded-full border border-orange-200 opacity-40'"
                      ></div>
                    </div>
                  </div>
                  
                  <!-- Motor Activity History - Modern Clean Design with scrolling -->
                  <div class="mt-6 space-y-3">
                    <h3 class="text-sm font-medium text-gray-700">Recent Activity</h3>
                    <div class="max-h-[200px] overflow-y-auto pr-1 space-y-2">
                      <!-- Loading state -->
                      <div v-if="isLoadingActivities" class="py-8 flex flex-col items-center justify-center">
                        <div class="w-8 h-8 border-2 border-green-500 border-t-transparent rounded-full animate-spin mb-2"></div>
                        <p class="text-sm text-gray-500">Loading activities...</p>
                      </div>
                      
                      <!-- Empty state -->
                      <div v-else-if="filteredMotorActivities.length === 0" class="flex flex-col items-center justify-center py-4 text-center">
                        <p class="text-gray-400 text-sm">No recent activities</p>
                      </div>
                      
                      <!-- Activities list -->
                      <div 
                        v-else
                        v-for="(activity, index) in filteredMotorActivities" 
                        :key="index" 
                        class="flex items-center justify-between bg-gray-50 rounded-lg p-3 hover:bg-gray-100 transition-colors"
                      >
                        <div class="flex items-center gap-2">
                          <div class="w-2 h-2 rounded-full" :class="activity.status ? 'bg-green-500' : 'bg-gray-400'"></div>
                          <span class="text-xs text-gray-600">{{ activity.timestamp }}</span>
                        </div>
                        <span 
                          class="text-xs font-medium px-2 py-1 rounded-full"
                          :class="activity.status ? 'bg-green-50 text-green-600' : 'bg-gray-100 text-gray-600'"
                        >
                          {{ activity.status ? 'Turned ON' : 'Turned OFF' }}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Saved Schedules Card - Expanded to take 2/3 of the space (col-span-2) -->
              <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 md:col-span-2">
                <div class="flex items-center justify-between mb-2">
                  <div class="flex items-center gap-2">
                    <div class="text-green-500">
                      <CalendarClock class="w-5 h-5" />
                    </div>
                    <h2 class="text-lg font-medium text-gray-800">Saved Schedules</h2>
                  </div>
                  <div class="flex items-center gap-2">
                    <!-- View History Button -->
                    <button 
                      @click="viewScheduleHistory()" 
                      class="flex items-center gap-1.5 bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium rounded-full px-4 py-2 transition-all duration-300 shadow-sm hover:shadow-md text-sm"
                    >
                      <History class="w-4 h-4" />
                      <span>View History</span>
                    </button>
                    <!-- Add Schedule Button - Slightly larger but not too large -->
                    <button 
                      @click="openScheduleModal()" 
                      class="flex items-center gap-1.5 bg-green-500 hover:bg-green-600 text-white font-medium rounded-full px-4 py-2 transition-all duration-300 shadow-sm hover:shadow-md text-sm"
                    >
                      <Plus class="w-4 h-4" />
                      <span>Add Schedule</span>
                    </button>
                  </div>
                </div>
                
                <!-- "Upcoming Waterings" text positioned below the heading -->
                <div class="text-xs text-gray-500 mb-4">
                  Upcoming Waterings
                </div>
                
                <!-- Next Scheduled Watering - Enhanced with modern design -->
                <div class="mb-5 bg-green-50 rounded-xl p-4 flex items-center justify-between border border-green-100 shadow-sm">
                  <div class="flex items-center gap-2">
                    <div class="bg-green-100 p-1.5 rounded-full">
                      <CalendarClock class="w-4 h-4 text-green-600" />
                    </div>
                    <span class="text-sm text-gray-700">Next scheduled watering</span>
                  </div>
                  <span 
                    v-if="isLoadingNextWatering" 
                    class="text-sm font-medium text-gray-500 bg-gray-100 px-3 py-1 rounded-full flex items-center gap-2"
                  >
                    <div class="w-3 h-3 border-2 border-gray-300 border-t-gray-600 rounded-full animate-spin"></div>
                    Loading...
                  </span>
                  <span 
                    v-else 
                    class="text-sm font-medium text-green-700 bg-green-100 px-3 py-1 rounded-full"
                  >
                    {{ nextWateringTime }}
                  </span>
                </div>
                
                <div class="flex items-center justify-between mb-4">
                  <div class="text-sm text-gray-500">All scheduled waterings:</div>
                  <div class="h-0.5 flex-grow mx-4 bg-gray-100"></div>
                </div>
                
                <!-- Saved Schedules List - Enhanced with better spacing and modern design -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 pr-1 mb-4">
                  <div v-if="upcomingSchedules.length === 0" class="flex flex-col items-center justify-center py-12 text-center md:col-span-2 lg:col-span-3">
                    <div class="bg-gray-50 p-6 rounded-full mb-4">
                      <CalendarClock class="w-16 h-16 text-gray-200" />
                    </div>
                    <p class="text-gray-400 font-medium">No upcoming schedules</p>
                    <p class="text-xs text-gray-400 mt-2">Add a schedule to see it here</p>
                  </div>
                  
                  <div 
                    v-for="(schedule, index) in upcomingSchedules" 
                    :key="index"
                    class="bg-white rounded-xl p-5 border border-gray-100 hover:border-green-200 transition-all duration-300 hover:shadow-md group relative overflow-hidden"
                  >
                    <!-- Decorative accent -->
                    <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-green-400 to-green-500"></div>
                    
                    <div class="flex items-center justify-between mb-3">
                      <div class="flex items-center gap-2">
                        <div class="w-2.5 h-2.5 rounded-full bg-green-500"></div>
                        <span class="text-sm font-medium text-gray-700">{{ schedule.dateTime }}</span>
                      </div>
                      <div class="flex items-center gap-1">
                        <!-- Edit button -->
                        <button 
                          @click="editSchedule(getOriginalIndex(schedule.id))" 
                          class="text-gray-300 group-hover:text-green-500 transition-colors p-1 rounded-full hover:bg-green-50"
                          title="Edit schedule"
                        >
                          <Edit2 class="w-4 h-4" />
                        </button>
                        <!-- Delete button -->
                        <button 
                          @click="removeSchedule(getOriginalIndex(schedule.id))" 
                          class="text-gray-300 group-hover:text-red-500 transition-colors p-1 rounded-full hover:bg-red-50"
                          title="Delete schedule"
                        >
                          <Trash2 class="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                    
                    <div class="flex items-center gap-4 text-xs text-gray-500 mt-3">
                      <div class="flex items-center gap-1.5 bg-gray-50 px-2.5 py-1.5 rounded-full border border-gray-100">
                        <Clock class="w-3.5 h-3.5 text-green-500" />
                        <span>{{ schedule.duration }} min</span>
                      </div>
                      
                      <div class="flex items-center gap-1.5 bg-gray-50 px-2.5 py-1.5 rounded-full border border-gray-100">
                        <Calendar class="w-3.5 h-3.5 text-green-500" />
                        <span>{{ schedule.mode }}</span>
                      </div>
                    </div>
                    
                    <div v-if="schedule.mode === 'weekly'" class="flex flex-wrap gap-1.5 mt-4">
                      <span 
                        v-for="(day, dayIndex) in weekDays" 
                        :key="dayIndex"
                        :class="[
                          'text-xs px-2 py-1 rounded-md transition-colors',
                          schedule.days[dayIndex] 
                            ? 'bg-green-100 text-green-700 border border-green-200' 
                            : 'bg-gray-50 text-gray-400 border border-gray-100'
                        ]"
                      >
                        {{ day.substring(0, 3) }}
                      </span>
                    </div>
                    
                    <!-- Additional settings indicators -->
                    <div class="flex items-center gap-2 mt-3">
                      <div v-if="schedule.skipIfRain" class="flex items-center gap-1 text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded-full">
                        <CloudRain class="w-3 h-3" />
                        <span>Skip if rain</span>
                      </div>
                      <div v-if="schedule.notifyWatering" class="flex items-center gap-1 text-xs text-amber-600 bg-amber-50 px-2 py-1 rounded-full">
                        <Bell class="w-3 h-3" />
                        <span>Notify</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Schedule History View (MODIFIED to use 1/4 - 3/4 layout) -->
          <div v-else-if="currentView === 'history'" class="flex-1 flex flex-col overflow-hidden">
            
            <!-- Modified layout - 1/4 and 3/4 split -->
            <div class="flex-1 flex flex-col md:flex-row overflow-hidden">
              
              <!-- LEFT SIDE (1/4) - Filters, Search, Export -->
              <div class="w-full md:w-1/4 border-r border-gray-100 bg-white p-4 flex flex-col overflow-y-auto">
                
                <!-- Search Bar -->
                <div class="mb-4">
                  <div class="relative">
                    <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                    <input
                      type="text"
                      placeholder="Search schedules..."
                      class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500 text-sm"
                      v-model="searchQuery"
                    />
                  </div>
                </div>
                
                <!-- Filters Section -->
                <div class="space-y-4 mb-4">
                  <h3 class="text-sm font-medium text-gray-700">Filters</h3>
                  
                  <!-- Date Range -->
                  <div class="space-y-2">
                    <label class="text-xs text-gray-500">Date Range</label>
                    <div class="flex flex-col space-y-2">
                      <div class="flex items-center">
                        <span class="text-xs text-gray-500 w-14">From:</span>
                        <input 
                          type="date" 
                          v-model="historyFilters.startDate" 
                          class="flex-1 border border-gray-200 rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500"
                        />
                      </div>
                      <div class="flex items-center">
                        <span class="text-xs text-gray-500 w-14">To:</span>
                        <input 
                          type="date" 
                          v-model="historyFilters.endDate" 
                          class="flex-1 border border-gray-200 rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500"
                        />
                      </div>
                    </div>
                  </div>
                  
                  <!-- Schedule Type -->
                  <div class="space-y-2">
                    <label class="text-xs text-gray-500">Schedule Type</label>
                    <select 
                      v-model="historyFilters.scheduleType" 
                      class="w-full border border-gray-200 rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500"
                    >
                      <option value="all">All Types</option>
                      <option value="one-time">One-time</option>
                      <option value="daily">Daily</option>
                      <option value="weekly">Weekly</option>
                      <option value="custom">Custom</option>
                    </select>
                  </div>
                  
                  <!-- Duration -->
                  <div class="space-y-2">
                    <label class="text-xs text-gray-500">Duration</label>
                    <select 
                      v-model="historyFilters.duration" 
                      class="w-full border border-gray-200 rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:ring-1 focus:ring-emerald-500"
                    >
                      <option value="all">All Durations</option>
                      <option value="short">Short (< 10 min)</option>
                      <option value="medium">Medium (10-30 min)</option>
                      <option value="long">Long (> 30 min)</option>
                    </select>
                  </div>
                  
                  <!-- Apply Filters Button -->
                  <button 
                    @click="applyHistoryFilters" 
                    class="w-full flex items-center justify-center gap-1.5 px-4 py-2 bg-emerald-500 text-white rounded-lg text-sm font-medium hover:bg-emerald-600 transition-colors"
                  >
                    <Filter class="h-4 w-4" />
                    Apply Filters
                  </button>
                  
                  <!-- Clear All Filters (only shown when filters are active) -->
                  <button 
                    v-if="hasActiveFilters"
                    @click="clearAllFilters" 
                    class="w-full text-xs text-gray-500 hover:text-gray-700 underline py-1 text-center"
                  >
                    Clear all filters
                  </button>
                </div>
                
                <!-- Active Filters Display -->
                <div v-if="hasActiveFilters" class="mb-4">
                  <h3 class="text-xs font-medium text-gray-500 mb-2">Active filters:</h3>
                  <div class="flex flex-wrap gap-2">
                    <!-- Date Range Filter Tag -->
                    <div v-if="historyFilters.startDate || historyFilters.endDate" class="flex items-center gap-1 bg-emerald-50 text-emerald-700 text-xs px-2 py-1 rounded-full">
                      <Calendar class="w-3 h-3" />
                      <span>{{ formatDateRange }}</span>
                      <button @click="clearDateFilter" class="ml-1 text-emerald-600 hover:text-emerald-800">
                        <X class="w-3 h-3" />
                      </button>
                    </div>
                    
                    <!-- Schedule Type Filter Tag -->
                    <div v-if="historyFilters.scheduleType !== 'all'" class="flex items-center gap-1 bg-emerald-50 text-emerald-700 text-xs px-2 py-1 rounded-full">
                      <CalendarClock class="w-3 h-3" />
                      <span>{{ formatScheduleType }}</span>
                      <button @click="clearTypeFilter" class="ml-1 text-emerald-600 hover:text-emerald-800">
                        <X class="w-3 h-3" />
                      </button>
                    </div>
                    
                    <!-- Duration Filter Tag -->
                    <div v-if="historyFilters.duration !== 'all'" class="flex items-center gap-1 bg-emerald-50 text-emerald-700 text-xs px-2 py-1 rounded-full">
                      <Clock class="w-3 h-3" />
                      <span>{{ formatDuration }}</span>
                      <button @click="clearDurationFilter" class="ml-1 text-emerald-600 hover:text-emerald-800">
                        <X class="w-3 h-3" />
                      </button>
                    </div>
                  </div>
                </div>
                
                <!-- Export Section -->
                <div class="mt-auto">
                  <h3 class="text-sm font-medium text-gray-700 mb-2">Export Data</h3>
                  <div class="relative">
                    <button 
                      @click.stop="toggleDropdown('export')"
                      class="w-full flex items-center justify-between gap-1.5 px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg text-sm font-medium transition-colors"
                    >
                      <div class="flex items-center gap-1.5">
                        <Download class="h-4 w-4" />
                        <span>Export History</span>
                      </div>
                      <ChevronDown class="h-3.5 w-3.5" :class="{ 'transform rotate-180': activeDropdown === 'export' }" />
                    </button>
                    
                    <div 
                      v-show="activeDropdown === 'export'"
                      class="absolute left-0 right-0 mt-1 bg-white rounded-lg shadow-lg border border-gray-200 z-50 overflow-hidden"
                      @click.stop
                    >
                      <div class="py-1">
                        <button
                          v-for="format in exportFormats"
                          :key="format"
                          @click="exportData(format)"
                          class="w-full px-3 py-1.5 text-left text-sm text-gray-700 hover:bg-gray-50 flex items-center"
                        >
                          <span v-if="format === 'csv'" class="mr-2 text-emerald-500"><FileText class="h-3.5 w-3.5" /></span>
                          <span v-else-if="format === 'pdf'" class="mr-2 text-red-500"><FileText class="h-3.5 w-3.5" /></span>
                          <span v-else class="mr-2 text-blue-500"><FileText class="h-3.5 w-3.5" /></span>
                          {{ format.toUpperCase() }}
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- RIGHT SIDE (3/4) - Table Display -->
              <div class="w-full md:w-3/4 flex-1 flex flex-col overflow-hidden">
                <!-- Fixed Table Header - Will not scroll -->
                <div class="bg-gray-50 border-b border-gray-200">
                  <table class="min-w-full">
                    <thead>
                      <tr>
                        <th class="w-[25%] py-3 px-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          <div class="text-gray-600">Date & Time</div>
                          <div class="text-gray-400 text-[10px] normal-case">MMM DD, YYYY HH:MM</div>
                        </th>
                        <th class="w-[20%] py-3 px-4 text-left text-xs font-medium uppercase tracking-wider">
                          <div class="text-blue-600">Duration</div>
                          <div class="text-gray-400 text-[10px] normal-case">Minutes</div>
                        </th>
                        <th class="w-[20%] py-3 px-4 text-left text-xs font-medium uppercase tracking-wider">
                          <div class="text-emerald-600">Schedule Type</div>
                          <div class="text-gray-400 text-[10px] normal-case">Mode</div>
                        </th>
                        <th class="w-[15%] py-3 px-4 text-left text-xs font-medium uppercase tracking-wider">
                          <div class="text-gray-600">Status</div>
                          <div class="text-gray-400 text-[10px] normal-case">Completion</div>
                        </th>
                        <th class="w-[20%] py-3 px-4 text-left text-xs font-medium uppercase tracking-wider">
                          <div class="text-gray-600">Additional Info</div>
                          <div class="text-gray-400 text-[10px] normal-case">Settings</div>
                        </th>
                      </tr>
                    </thead>
                  </table>
                </div>
                
                <!-- Scrollable Table Body -->
                <div class="flex-1 overflow-y-auto">
                  <table class="min-w-full">
                    <tbody>
                      <!-- Loading state -->
                      <tr v-if="isLoadingHistory" class="border-b border-gray-50 last:border-0">
                        <td colspan="5" class="px-4 py-20 text-center">
                          <div class="flex flex-col items-center justify-center">
                            <div class="w-10 h-10 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin mb-4"></div>
                            <p class="text-gray-500">Loading schedule history...</p>
                          </div>
                        </td>
                      </tr>
                      
                      <!-- Empty state -->
                      <tr v-else-if="filteredPastSchedules.length === 0" class="border-b border-gray-50 last:border-0">
                        <td colspan="5" class="px-4 py-20 text-center">
                          <div class="flex flex-col items-center justify-center">
                            <History class="h-16 w-16 text-gray-200 mb-4" />
                            <p class="text-gray-400 font-medium">No schedule history found</p>
                            <p class="text-xs text-gray-400 mt-2">Completed schedules will appear here</p>
                          </div>
                        </td>
                      </tr>
                      
                      <!-- Data rows -->
                      <tr 
                        v-else
                        v-for="(schedule, index) in paginatedPastSchedules" 
                        :key="index"
                        class="border-b border-gray-50 hover:bg-gray-50 transition-colors last:border-0"
                      >
                        <!-- Date & Time -->
                        <td class="w-[25%] px-4 py-3 whitespace-nowrap">
                          <div class="flex items-center gap-2">
                            <div class="w-2 h-2 rounded-full bg-gray-400"></div>
                            <div class="text-sm font-medium text-gray-700">{{ schedule.dateTime }}</div>
                          </div>
                        </td>
                        
                        <!-- Duration -->
                        <td class="w-[20%] px-4 py-3 whitespace-nowrap">
                          <div class="text-sm font-medium text-blue-600">
                            {{ schedule.duration }} minutes
                          </div>
                        </td>
                        
                        <!-- Schedule Type -->
                        <td class="w-[20%] px-4 py-3 whitespace-nowrap">
                          <span class="px-3 py-1 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800 capitalize">
                            {{ schedule.mode }}
                          </span>
                        </td>
                        
                        <!-- Status -->
                        <td class="w-[15%] px-4 py-3 whitespace-nowrap">
                          <span class="px-3 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                            Completed
                          </span>
                        </td>
                        
                        <!-- Additional Info -->
                        <td class="w-[20%] px-4 py-3">
                          <div class="flex flex-wrap gap-1">
                            <div v-if="schedule.skipIfRain" class="flex items-center gap-1 text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded-full">
                              <CloudRain class="w-3 h-3" />
                              <span>Rain skip</span>
                            </div>
                            <div v-if="schedule.notifyWatering" class="flex items-center gap-1 text-xs text-amber-600 bg-amber-50 px-2 py-1 rounded-full">
                              <Bell class="w-3 h-3" />
                              <span>Notify</span>
                            </div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              
                <!-- Pagination - At the bottom of right side -->
                <div class="border-t border-gray-100 py-3 px-6 bg-white">
                  <div class="flex flex-col sm:flex-row items-center justify-between gap-3">
                    <div class="text-sm text-gray-600 flex items-center gap-2">
                      <span>Showing</span>
                      <select 
                        v-model="itemsPerPage" 
                        class="bg-white border border-gray-200 rounded-lg px-2 py-1 text-sm font-medium text-gray-700 focus:outline-none focus:ring-1 focus:ring-emerald-500"
                        @change="updatePagination"
                      >
                        <option value="10">10</option>
                        <option value="20">20</option>
                        <option value="50">50</option>
                      </select>
                      <span>of {{ filteredPastSchedules.length }}</span>
                    </div>
                    
                    <div class="flex items-center gap-1">
                      <button 
                        @click="prevPage"
                        :disabled="currentPage === 1"
                        class="inline-flex items-center justify-center px-3 py-1.5 text-sm font-medium transition-colors rounded-md
                          disabled:opacity-50 disabled:cursor-not-allowed disabled:text-gray-400
                          enabled:text-gray-700 enabled:hover:text-emerald-600 enabled:hover:bg-emerald-50"
                      >
                        <ChevronLeft class="w-4 h-4 mr-1" />
                        Prev
                      </button>
                      
                      <div class="flex items-center">
                        <button
                          v-for="page in displayedPages"
                          :key="page"
                          @click="goToPage(page)"
                          :class="[
                            'relative inline-flex items-center justify-center w-8 h-8 text-sm transition-colors mx-0.5 rounded-md',
                            page === currentPage
                              ? 'text-white bg-emerald-500 font-semibold'
                              : page === '...'
                                ? 'cursor-default text-gray-400'
                                : 'text-gray-700 hover:text-emerald-600 hover:bg-emerald-50'
                          ]"
                        >
                          {{ page }}
                        </button>
                      </div>
                      
                      <button 
                        @click="nextPage"
                        :disabled="currentPage >= totalPages"
                        class="inline-flex items-center justify-center px-3 py-1.5 text-sm font-medium transition-colors rounded-md
                          disabled:opacity-50 disabled:cursor-not-allowed disabled:text-gray-400
                          enabled:text-gray-700 enabled:hover:text-emerald-600 enabled:hover:bg-emerald-50"
                      >
                        Next
                        <ChevronRight class="w-4 h-4 ml-1" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Toggle Confirmation Dialog -->
    <Transition name="modal">
      <div v-if="showToggleConfirmationDialog" class="fixed inset-0 z-[10000] flex items-center justify-center p-4 sm:p-0">
        <div 
          class="fixed inset-0 bg-black/50 backdrop-blur-sm" 
          @click="showToggleConfirmationDialog = false"
        ></div>
        
        <div class="relative bg-white rounded-xl shadow-xl w-full max-w-md p-6 z-[10001]">
          <div class="flex items-center gap-4 mb-4">
            <div :class="waterPumpActive ? 'bg-red-100' : 'bg-green-100'" class="p-2 rounded-full">
              <Power :class="waterPumpActive ? 'text-red-600' : 'text-green-600'" class="w-6 h-6" />
            </div>
            <h3 class="text-lg font-medium text-gray-900">
              {{ waterPumpActive ? 'Turn OFF Water Pump?' : 'Turn ON Water Pump?' }}
            </h3>
          </div>
          
          <p class="text-gray-600 mb-6">
            {{ waterPumpActive 
              ? 'Are you sure you want to turn OFF the water pump?' 
              : 'Are you sure you want to turn ON the water pump?' 
            }}
          </p>
          
          <div class="flex justify-end gap-3">
            <button 
              @click="showToggleConfirmationDialog = false" 
              class="bg-white border border-gray-300 text-gray-700 hover:bg-gray-50 text-sm font-medium rounded-lg px-4 py-2 transition-colors"
            >
              Cancel
            </button>
            <button 
              @click="confirmToggleWaterPump" 
              :class="waterPumpActive 
                ? 'bg-red-600 hover:bg-red-700' 
                : 'bg-green-600 hover:bg-green-700'"
              class="text-white text-sm font-medium rounded-lg px-4 py-2 transition-colors flex items-center gap-2"
            >
              <Power class="w-4 h-4" />
              <span>{{ waterPumpActive ? 'Turn OFF' : 'Turn ON' }}</span>
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Modern Watering Schedule Modal with Calendar -->
    <Transition name="modal">
      <div v-if="showScheduleModal" class="fixed inset-0 z-[9999] flex items-center justify-center p-4 sm:p-0">
        <!-- Backdrop with blur effect -->
        <div 
          class="fixed inset-0 bg-black/50 backdrop-blur-sm" 
          @click="closeScheduleModal"
        ></div>
        
        <!-- Modal Content - Redesigned with modern UI and fixed header and rounded bottom corners -->
        <div class="relative bg-white rounded-2xl shadow-xl w-full max-w-2xl max-h-[90vh] flex flex-col m-4 z-[10000] overflow-hidden">
          <!-- Modal Header with gradient background - FIXED -->
          <div class="bg-gradient-to-r from-green-500 to-emerald-600 p-6 rounded-t-2xl flex items-center justify-between sticky top-0 z-10">
            <div class="flex items-center gap-3">
              <div class="bg-white/20 p-2 rounded-full">
                <CalendarClock class="w-6 h-6 text-white" />
              </div>
              <h2 class="text-xl font-semibold text-white">
                {{ editingScheduleIndex !== null ? 'Edit Schedule' : 'New Watering Schedule' }}
              </h2>
            </div>
            <button 
              @click="closeScheduleModal" 
              class="text-white/80 hover:text-white transition-colors bg-white/10 hover:bg-white/20 rounded-full p-1.5"
            >
              <X class="w-5 h-5" />
            </button>
          </div>
          
          <!-- Schedule Type Tabs - FIXED -->
          <div class="px-6 pt-6 pb-2 border-b border-gray-100 bg-white sticky top-[76px] z-10">
            <div class="flex space-x-2">
              <button 
                @click="wateringMode = 'weekly'" 
                :class="[
                  'px-4 py-2 rounded-full text-sm font-medium transition-all',
                  wateringMode === 'weekly' 
                    ? 'bg-green-500 text-white shadow-sm' 
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                ]"
              >
                Weekly
              </button>
              <button 
                @click="wateringMode = 'daily'" 
                :class="[
                  'px-4 py-2 rounded-full text-sm font-medium transition-all',
                  wateringMode === 'daily' 
                    ? 'bg-green-500 text-white shadow-sm' 
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                ]"
              >
                Daily
              </button>
              <button 
                @click="wateringMode = 'custom'" 
                :class="[
                  'px-4 py-2 rounded-full text-sm font-medium transition-all',
                  wateringMode === 'custom' 
                    ? 'bg-green-500 text-white shadow-sm' 
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                ]"
              >
                Custom
              </button>
              <button 
                @click="wateringMode = 'one-time'" 
                :class="[
                  'px-4 py-2 rounded-full text-sm font-medium transition-all',
                  wateringMode === 'one-time' 
                    ? 'bg-green-500 text-white shadow-sm' 
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                ]"
              >
                One-time
              </button>
            </div>
          </div>
          
          <!-- Scrollable Content Area -->
          <div class="overflow-y-auto flex-1">
            <!-- Modal Body -->
            <div class="p-6">
              <!-- Calendar for One-time and Custom scheduling -->
              <div v-if="wateringMode === 'one-time' || wateringMode === 'custom'" class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">Select Date</label>
                <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
                  <!-- Calendar Header -->
                  <div class="flex items-center justify-between p-4 bg-gray-50 border-b border-gray-200">
                    <button @click="prevMonth" class="p-1 rounded-full hover:bg-gray-200 transition-colors">
                      <ChevronLeft class="w-5 h-5 text-gray-600" />
                    </button>
                    <h3 class="text-sm font-medium text-gray-700">{{ currentMonthName }} {{ currentYear }}</h3>
                    <button @click="nextMonth" class="p-1 rounded-full hover:bg-gray-200 transition-colors">
                      <ChevronRight class="w-5 h-5 text-gray-600" />
                    </button>
                  </div>
                  
                  <!-- Calendar Grid -->
                  <div class="p-4">
                    <!-- Day headers -->
                    <div class="grid grid-cols-7 mb-2">
                      <div v-for="day in ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']" :key="day" class="text-xs font-medium text-gray-500 text-center py-2">
                        {{ day }}
                      </div>
                    </div>
                    
                    <!-- Calendar days -->
                    <div class="grid grid-cols-7 gap-1">
                      <div 
                        v-for="(day, index) in calendarDays" 
                        :key="index"
                        @click="selectCalendarDate(day)"
                        :class="[
                          'h-9 flex items-center justify-center rounded-full text-sm transition-all cursor-pointer',
                          day.isCurrentMonth ? 'hover:bg-green-50' : 'text-gray-400',
                          isSelectedDate(day) ? 'bg-green-500 text-white font-medium hover:bg-green-600' : '',
                          isToday(day) && !isSelectedDate(day) ? 'border border-green-500 text-green-600' : ''
                        ]"
                      >
                        {{ day.day }}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Weekly Schedule - Enhanced UI -->
              <div v-if="wateringMode === 'weekly'" class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">Select Days</label>
                <div class="grid grid-cols-7 gap-2">
                  <button 
                    v-for="(day, index) in weekDays" 
                    :key="day"
                    @click="toggleWateringDay(index)"
                    :class="[
                      'py-3 rounded-xl transition-all text-sm font-medium relative overflow-hidden',
                      wateringDays[index] 
                        ? 'bg-green-500 text-white shadow-sm' 
                        : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                    ]"
                  >
                    <span class="relative z-10">{{ day.substring(0, 3) }}</span>
                    <div 
                      v-if="wateringDays[index]" 
                      class="absolute bottom-0 left-0 w-full h-1 bg-green-600"
                    ></div>
                  </button>
                </div>
              </div>
              
              <!-- Time of Day - Enhanced UI -->
              <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">Time of Day</label>
                <div class="flex items-center">
                  <div class="bg-gray-50 rounded-xl px-4 py-3 w-full flex items-center justify-center border border-gray-200">
                    <div class="relative">
                      <input 
                        type="text" 
                        v-model="formattedHour" 
                        class="w-16 text-center bg-transparent border-0 text-xl font-medium focus:outline-none focus:ring-0"
                        @blur="validateHour"
                      />
                      <div class="absolute -top-3 left-0 w-full flex justify-center">
                        <button @click="incrementHour" class="text-gray-400 hover:text-gray-600">
                          <ChevronUp class="w-4 h-4" />
                        </button>
                      </div>
                      <div class="absolute -bottom-3 left-0 w-full flex justify-center">
                        <button @click="decrementHour" class="text-gray-400 hover:text-gray-600">
                          <ChevronDown class="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                    
                    <span class="text-gray-400 mx-2 text-2xl">:</span>
                    
                    <div class="relative">
                      <input 
                        type="text" 
                        v-model="formattedMinute" 
                        class="w-16 text-center bg-transparent border-0 text-xl font-medium focus:outline-none focus:ring-0"
                        @blur="validateMinute"
                      />
                      <div class="absolute -top-3 left-0 w-full flex justify-center">
                        <button @click="incrementMinute" class="text-gray-400 hover:text-gray-600">
                          <ChevronUp class="w-4 h-4" />
                        </button>
                      </div>
                      <div class="absolute -bottom-3 left-0 w-full flex justify-center">
                        <button @click="decrementMinute" class="text-gray-400 hover:text-gray-600">
                          <ChevronDown class="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                    
                    <!-- AM/PM selector -->
                    <div class="ml-4 flex flex-col bg-white rounded-lg border border-gray-200 overflow-hidden">
                      <button 
                        @click="setAmPm('AM')"
                        :class="[
                          'px-3 py-1 text-xs font-medium transition-colors',
                          isAm ? 'bg-green-500 text-white' : 'bg-white text-gray-600 hover:bg-gray-100'
                        ]"
                      >
                        AM
                      </button>
                      <button 
                        @click="setAmPm('PM')"
                        :class="[
                          'px-3 py-1 text-xs font-medium transition-colors',
                          !isAm ? 'bg-green-500 text-white' : 'bg-white text-gray-600 hover:bg-gray-100'
                        ]"
                      >
                        PM
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Duration - Enhanced UI -->
              <div class="mb-6">
                <div class="flex items-center justify-between mb-2">
                  <label class="text-sm font-medium text-gray-700">Duration</label>
                  <div class="flex items-center gap-2">
                    <span class="text-sm text-gray-500">{{ wateringDuration }} minutes</span>
                  </div>
                </div>
                
                <div class="relative">
                  <input
                    type="range"
                    v-model.number="wateringDuration"
                    min="1"
                    max="120"
                    step="1"
                    class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-green-500"
                  />
                  <div class="absolute -top-2 left-0 right-0 flex justify-between px-2 text-xs text-gray-500">
                    <span>1m</span>
                    <span>30m</span>
                    <span>60m</span>
                    <span>90m</span>
                    <span>120m</span>
                  </div>
                </div>
                
                <div class="flex items-center justify-between mt-6">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="decreaseDuration" 
                      class="bg-gray-100 hover:bg-gray-200 rounded-lg p-2 transition-colors"
                    >
                      <Minus class="w-4 h-4 text-gray-600" />
                    </button>
                    <div class="bg-gray-50 rounded-lg px-4 py-2 w-20 text-center border border-gray-200">
                      <span class="text-lg font-medium">{{ wateringDuration }}</span>
                    </div>
                    <button 
                      @click="increaseDuration" 
                      class="bg-gray-100 hover:bg-gray-200 rounded-lg p-2 transition-colors"
                    >
                      <Plus class="w-4 h-4 text-gray-600" />
                    </button>
                  </div>
                  <div class="text-sm text-gray-500">
                    Watering duration in minutes
                  </div>
                </div>
              </div>
              
              <!-- Custom Schedule - Interval Settings -->
              <div v-if="wateringMode === 'custom'" class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">Repeat Every</label>
                <div class="flex items-center gap-3">
                  <div class="flex-1">
                    <div class="flex items-center">
                      <button 
                        @click="decreaseInterval" 
                        class="bg-gray-100 hover:bg-gray-200 rounded-l-lg p-2.5"
                      >
                        <Minus class="w-4 h-4 text-gray-600" />
                      </button>
                      <input 
                        type="number" 
                        v-model.number="wateringInterval"
                        min="1"
                        max="30"
                        class="w-full bg-gray-50 py-2.5 text-center border-y border-gray-200 text-lg focus:outline-none focus:ring-0"
                      />
                      <button
                        @click="increaseInterval"
                        class="bg-gray-100 hover:bg-gray-200 rounded-r-lg p-2.5"
                      >
                        <Plus class="w-4 h-4 text-gray-600" />
                      </button>
                    </div>
                  </div>
                  <select
                    v-model="wateringIntervalUnit"
                    class="bg-gray-50 rounded-lg border border-gray-200 text-base text-gray-700 focus:outline-none focus:ring-1 focus:ring-green-500 px-4 py-2.5 flex-1"
                  >
                    <option value="hours">Hours</option>
                    <option value="days">Days</option>
                    <option value="weeks">Weeks</option>
                  </select>
                </div>
              </div>
              
              <!-- Additional Settings -->
              <div class="mb-6">
                <h3 class="text-sm font-medium text-gray-700 mb-3">Additional Settings</h3>
              
                <div class="space-y-3">
                  <!-- Weather-based Skip -->
                  <div class="flex items-center justify-between bg-gray-50 rounded-xl p-4 border border-gray-200">
                    <div class="flex items-center gap-3">
                      <div class="bg-blue-100 p-1.5 rounded-full">
                        <CloudRain class="w-5 h-5 text-blue-600" />
                      </div>
                      <div>
                        <p class="text-sm font-medium text-gray-700">Skip if rain is forecasted</p>
                        <p class="text-xs text-gray-500 mt-0.5">Automatically skip watering if rain is expected</p>
                      </div>
                    </div>
                    <label class="relative inline-flex items-center cursor-pointer">
                      <input type="checkbox" v-model="skipIfRain" class="sr-only peer">
                      <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-green-500"></div>
                    </label>
                  </div>
                
                  <!-- Notification -->
                  <div class="flex items-center justify-between bg-gray-50 rounded-xl p-4 border border-gray-200">
                    <div class="flex items-center gap-3">
                      <div class="bg-amber-100 p-1.5 rounded-full">
                        <Bell class="w-5 h-5 text-amber-600" />
                      </div>
                      <div>
                        <p class="text-sm font-medium text-gray-700">Receive notifications</p>
                        <p class="text-xs text-gray-500 mt-0.5">Get notified when watering starts and ends</p>
                      </div>
                    </div>
                    <label class="relative inline-flex items-center cursor-pointer">
                      <input type="checkbox" v-model="notifyWatering" class="sr-only peer">
                      <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-green-500"></div>
                    </label>
                  </div>
                
                  <!-- Water Flow Rate -->
                  <div v-if="showAdvancedSettings" class="flex items-center justify-between bg-gray-50 rounded-xl p-4 border border-gray-200">
                    <div class="flex items-center gap-3">
                      <div class="bg-cyan-100 p-1.5 rounded-full">
                        <Droplets class="w-5 h-5 text-cyan-600" />
                      </div>
                      <div>
                        <p class="text-sm font-medium text-gray-700">Water flow rate</p>
                        <p class="text-xs text-gray-500 mt-0.5">Set the water flow intensity</p>
                      </div>
                    </div>
                    <select
                      v-model="waterFlowRate"
                      class="bg-white rounded-lg border border-gray-200 text-sm text-gray-700 focus:outline-none focus:ring-1 focus:ring-green-500 px-3 py-1.5"
                    >
                      <option value="low">Low</option>
                      <option value="medium">Medium</option>
                      <option value="high">High</option>
                    </select>
                  </div>
                </div>
              
                <button
                  @click="showAdvancedSettings = !showAdvancedSettings"
                  class="mt-3 text-sm text-green-600 hover:text-green-700 flex items-center gap-1"
                >
                  <span>{{ showAdvancedSettings ? 'Hide' : 'Show' }} advanced settings</span>
                  <ChevronDown v-if="!showAdvancedSettings" class="w-4 h-4" />
                  <ChevronUp v-else class="w-4 h-4" />
                </button>
              </div>
            
              <!-- Schedule Summary -->
              <div class="bg-gray-50 rounded-xl p-4 border border-gray-200 mb-6">
                <h3 class="text-sm font-medium text-gray-700 mb-2">Schedule Summary</h3>
                <div class="space-y-2 text-sm text-gray-600">
                  <div class="flex items-center gap-2">
                    <Calendar class="w-4 h-4 text-gray-500" />
                    <span>{{ scheduleSummary }}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <Clock class="w-4 h-4 text-gray-500" />
                    <span>{{ timeDisplay }} for {{ wateringDuration }} minutes</span>
                  </div>
                  <div v-if="skipIfRain" class="flex items-center gap-2">
                    <CloudRain class="w-4 h-4 text-gray-500" />
                    <span>Will skip if rain is forecasted</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Modal Footer - FIXED with rounded bottom corners -->
          <div class="p-6 border-t border-gray-100 flex justify-end gap-3 bg-white sticky bottom-0 z-10 rounded-b-2xl">
            <button
              @click="closeScheduleModal"
              class="bg-white border border-gray-300 text-gray-700 hover:bg-gray-50 text-sm font-medium rounded-lg px-5 py-2.5 transition-colors shadow-sm"
            >
              Cancel
            </button>
            <button
              @click="saveWateringSchedule"
              class="bg-gradient-to-r from-green-500 to-emerald-600 hover:from-green-600 hover:to-emerald-700 text-white text-sm font-medium rounded-lg px-5 py-2.5 transition-colors shadow-sm flex items-center gap-2"
            >
              <Save class="w-4 h-4" />
              <span>{{ editingScheduleIndex !== null ? 'Update Schedule' : 'Save Schedule' }}</span>
            </button>
          </div>
        </div>
      </div>
    </Transition>
  
    <!-- Confirmation Dialog for Delete -->
    <Transition name="modal">
      <div v-if="showDeleteConfirmation" class="fixed inset-0 z-[10000] flex items-center justify-center p-4 sm:p-0">
        <div
          class="fixed inset-0 bg-black/50 backdrop-blur-sm"
          @click="showDeleteConfirmation = false"
        ></div>
      
        <div class="relative bg-white rounded-xl shadow-xl w-full max-w-md p-6 z-[10001]">
          <div class="flex items-center gap-4 mb-4">
            <div class="bg-red-100 p-2 rounded-full">
              <AlertTriangle class="w-6 h-6 text-red-600" />
            </div>
            <h3 class="text-lg font-medium text-gray-900">Delete Schedule</h3>
          </div>
        
          <p class="text-gray-600 mb-6">
            Are you sure you want to delete this watering schedule? This action cannot be undone.
          </p>
        
          <div class="flex justify-end gap-3">
            <button
              @click="showDeleteConfirmation = false"
              class="bg-white border border-gray-300 text-gray-700 hover:bg-gray-50 text-sm font-medium rounded-lg px-4 py-2 transition-colors"
            >
              Cancel
            </button>
            <button
              @click="confirmDeleteSchedule"
              class="bg-red-600 hover:bg-red-700 text-white text-sm font-medium rounded-lg px-4 py-2 transition-colors flex items-center gap-2"
            >
              <Trash2 class="w-4 h-4" />
              <span>Delete</span>
            </button>
          </div>
        </div>
      </div>
    </Transition>
  
    <!-- Success Toast Notification -->
    <Transition name="toast">
      <div
        v-if="showToast"
        class="fixed bottom-4 right-4 bg-white rounded-lg shadow-lg border border-gray-200 p-4 flex items-center gap-3 z-[10001] max-w-md"
      >
        <div class="bg-green-100 p-2 rounded-full">
          <CheckCircle class="w-5 h-5 text-green-600" />
        </div>
        <div>
          <p class="text-sm font-medium text-gray-800">{{ toastMessage }}</p>
        </div>
        <button
          @click="showToast = false"
          class="ml-auto text-gray-400 hover:text-gray-600"
        >
          <X class="w-4 h-4" />
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import {
  Droplet,
  Droplets,
  Clock,
  CalendarClock,
  Plus,
  Minus,
  X,
  Calendar,
  ChevronRight,
  ChevronLeft,
  ChevronUp,
  ChevronDown,
  Power,
  CloudRain,
  Bell,
  Save,
  Edit2,
  Trash2,
  AlertTriangle,
  CheckCircle,
  History,
  ArrowLeft,
  Filter,
  Search,
  Download,
  ArrowUpDown,
  FileText,
  FileSearch
} from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'
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
import axios from 'axios'

// Get Firestore instance - using the existing instance from your backend
const db = getFirestore()

// View state
const currentView = ref('overview')

// System control values
const waterPumpActive = ref(false)
const motorActivities = ref([])
const isLoadingActivities = ref(true)
const isLoadingNextWatering = ref(true)
const isLoadingHistory = ref(false)

// Search query for history
const searchQuery = ref('')

// Active dropdown for export
const activeDropdown = ref(null)
const exportFormats = ['csv', 'pdf', 'excel']

// Filter panel state
const showFilterPanel = ref(false)

// Pagination for history view
const itemsPerPage = ref(10)
const currentPage = ref(1)
const totalPages = computed(() => Math.ceil(filteredPastSchedules.value.length / itemsPerPage.value))
const paginationStart = computed(() => ((currentPage.value - 1) * itemsPerPage.value) + 1)
const paginationEnd = computed(() => Math.min(currentPage.value * itemsPerPage.value, filteredPastSchedules.value.length))

// Display pagination buttons
const displayedPages = computed(() => {
  const total = totalPages.value
  const current = currentPage.value
  const pages = []

  if (total <= 7) {
    // If 7 or fewer pages, show all
    for (let i = 1; i <= total; i++) {
      pages.push(i)
    }
  } else {
    // Always show first page
    pages.push(1)

    if (current <= 3) {
      // If near start, show 2-5 then ellipsis
      pages.push(2, 3, 4, 5, '...', total)
    } else if (current >= total - 2) {
      // If near end, show ellipsis then last 4
      pages.push('...', total - 4, total - 3, total - 2, total - 1, total)
    } else {
      // Otherwise show ellipsis, current -1, current, current + 1, ellipsis
      pages.push('...', current - 1, current, current + 1, '...', total)
    }
  }

  return pages
})

// History filters
const historyFilters = ref({
  startDate: '',
  endDate: '',
  scheduleType: 'all',
  duration: 'all'
})

// Check if any filters are active
const hasActiveFilters = computed(() => {
  return historyFilters.value.startDate || 
         historyFilters.value.endDate || 
         historyFilters.value.scheduleType !== 'all' || 
         historyFilters.value.duration !== 'all'
})

// Format date range for display
const formatDateRange = computed(() => {
  if (historyFilters.value.startDate && historyFilters.value.endDate) {
    return `${formatShortDate(historyFilters.value.startDate)} - ${formatShortDate(historyFilters.value.endDate)}`
  } else if (historyFilters.value.startDate) {
    return `From ${formatShortDate(historyFilters.value.startDate)}`
  } else if (historyFilters.value.endDate) {
    return `Until ${formatShortDate(historyFilters.value.endDate)}`
  }
  return ''
})

// Format schedule type for display
const formatScheduleType = computed(() => {
  return historyFilters.value.scheduleType.charAt(0).toUpperCase() + historyFilters.value.scheduleType.slice(1)
})

// Format duration for display
const formatDuration = computed(() => {
  const duration = historyFilters.value.duration
  if (duration === 'short') return 'Short (< 10 min)'
  if (duration === 'medium') return 'Medium (10-30 min)'
  if (duration === 'long') return 'Long (> 30 min)'
  return ''
})

// Helper function to format date for display
const formatShortDate = (dateStr) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

// Clear filter functions
const clearDateFilter = () => {
  historyFilters.value.startDate = ''
  historyFilters.value.endDate = ''
  applyHistoryFilters()
}

const clearTypeFilter = () => {
  historyFilters.value.scheduleType = 'all'
  applyHistoryFilters()
}

const clearDurationFilter = () => {
  historyFilters.value.duration = 'all'
  applyHistoryFilters()
}

const clearAllFilters = () => {
  historyFilters.value.startDate = ''
  historyFilters.value.endDate = ''
  historyFilters.value.scheduleType = 'all'
  historyFilters.value.duration = 'all'
  applyHistoryFilters()
}

// Toggle filter panel
const toggleFilterPanel = () => {
  showFilterPanel.value = !showFilterPanel.value
}

// Filter activities to only show those from the last 7 days
const filteredMotorActivities = computed(() => {
  const sevenDaysAgo = new Date();
  sevenDaysAgo.setDate(sevenDaysAgo.getDate() - 7);
  
  return motorActivities.value.filter(activity => {
    // Parse the timestamp to a Date object
    const activityDate = parseActivityTimestamp(activity.timestamp);
    // Only include activities from the last 7 days
    return activityDate >= sevenDaysAgo;
  });
});

// NEW: Computed properties to separate upcoming and past schedules
const upcomingSchedules = computed(() => {
  const now = new Date().getTime();
  return savedSchedules.value.filter(schedule => {
    // Check if the schedule has a scheduledTime property and it's in the future
    return schedule.scheduledTime && schedule.scheduledTime > now;
  });
});

// FIXED: Modified to properly identify past schedules
const pastSchedules = computed(() => {
  // Get all schedules that are not in upcomingSchedules
  // This ensures we include all schedules that have passed their scheduled time
  return savedSchedules.value.filter(schedule => {
    // A schedule is considered "past" if:
    // 1. It has a scheduledTime and it's in the past, OR
    // 2. It has a completed status flag
    const now = new Date().getTime();
    return (schedule.scheduledTime && schedule.scheduledTime <= now) || 
           (schedule.completed === true) ||
           // For one-time schedules, check if the date has passed
           (schedule.mode === 'one-time' && schedule.scheduledTime && schedule.scheduledTime <= now);
  });
});

// FIXED: Modified to properly filter past schedules based on history filters
const filteredPastSchedules = computed(() => {
  let filtered = [...pastSchedules.value];
  
  // Apply search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(schedule => {
      return Object.values(schedule).some(value => 
        String(value).toLowerCase().includes(query)
      )
    })
  }
  
  // Apply date range filter
  if (historyFilters.value.startDate) {
    const startDate = new Date(historyFilters.value.startDate).getTime();
    filtered = filtered.filter(schedule => {
      // If scheduledTime exists, use it for filtering
      if (schedule.scheduledTime) {
        return schedule.scheduledTime >= startDate;
      }
      // Fallback to parsing dateTime if available
      if (schedule.dateTime) {
        const scheduleDate = parseScheduleDateTime(schedule.dateTime);
        return scheduleDate.getTime() >= startDate;
      }
      return true; // Include if we can't determine the date
    });
  }
  
  if (historyFilters.value.endDate) {
    const endDate = new Date(historyFilters.value.endDate);
    endDate.setHours(23, 59, 59, 999); // End of the day
    const endTime = endDate.getTime();
    filtered = filtered.filter(schedule => {
      // If scheduledTime exists, use it for filtering
      if (schedule.scheduledTime) {
        return schedule.scheduledTime <= endTime;
      }
      // Fallback to parsing dateTime if available
      if (schedule.dateTime) {
        const scheduleDate = parseScheduleDateTime(schedule.dateTime);
        return scheduleDate.getTime() <= endTime;
      }
      return true; // Include if we can't determine the date
    });
  }
  
  // Apply schedule type filter
  if (historyFilters.value.scheduleType !== 'all') {
    filtered = filtered.filter(schedule => schedule.mode === historyFilters.value.scheduleType);
  }
  
  // Apply duration filter
  if (historyFilters.value.duration !== 'all') {
    if (historyFilters.value.duration === 'short') {
      filtered = filtered.filter(schedule => schedule.duration < 10);
    } else if (historyFilters.value.duration === 'medium') {
      filtered = filtered.filter(schedule => schedule.duration >= 10 && schedule.duration <= 30);
    } else if (historyFilters.value.duration === 'long') {
      filtered = filtered.filter(schedule => schedule.duration > 30);
    }
  }
  
  return filtered;
});

// Paginated past schedules for display
const paginatedPastSchedules = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage.value;
  const endIndex = startIndex + itemsPerPage.value;
  return filteredPastSchedules.value.slice(startIndex, endIndex);
});

// ADDED: Helper function to parse schedule dateTime strings
const parseScheduleDateTime = (dateTimeStr) => {
  if (!dateTimeStr) return new Date();
  
  try {
    // Handle formats like "Mon, May 12, 01:35 AM"
    const parts = dateTimeStr.split(', ');
    if (parts.length >= 3) {
      const datePart = parts[0] + ', ' + parts[1];
      const timePart = parts[2];
      
      // Create a date from the combined string
      return new Date(datePart + ', ' + new Date().getFullYear() + ' ' + timePart);
    }
    
    // Fallback to direct parsing
    return new Date(dateTimeStr);
  } catch (error) {
    console.error('Error parsing schedule dateTime:', error, dateTimeStr);
    return new Date(); // Return current date as fallback
  }
};

// FIXED: Helper function to parse activity timestamps into Date objects
const parseActivityTimestamp = (timestamp) => {
  // Check if timestamp is already a Date object
  if (timestamp instanceof Date) {
    return timestamp;
  }
  
  if (typeof timestamp !== 'string') {
    console.error('Invalid timestamp format:', timestamp);
    return new Date(); // Return current date as fallback
  }
  
  // Handle Firebase formatted timestamps (e.g., "Sun, May 4, 06:32 PM")
  if (timestamp.includes(',')) {
    try {
      // Parse the full date string
      const dateParts = timestamp.split(', ');
      
      // If it's a full date with day of week, month, day, and time
      if (dateParts.length >= 2) {
        // For format like "Sun, May 4, 06:32 PM"
        const fullDateStr = timestamp;
        const date = new Date(fullDateStr);
        
        // Check if date is valid
        if (!isNaN(date.getTime())) {
          return date;
        }
        
        // If direct parsing failed, try manual parsing
        const monthDayPart = dateParts[1];
        let timePart = '';
        
        if (dateParts.length > 2) {
          timePart = dateParts[2];
        }
        
        // Extract month and day
        const monthDayMatch = monthDayPart.match(/([A-Za-z]+)\s+(\d+)/);
        if (monthDayMatch) {
          const monthName = monthDayMatch[1];
          const day = parseInt(monthDayMatch[2]);
          
          // Convert month name to month index
          const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
          const monthIndex = months.findIndex(m => m === monthName);
          
          if (monthIndex !== -1) {
            // Create date with current year (or adjust if needed)
            const currentYear = new Date().getFullYear();
            const newDate = new Date(currentYear, monthIndex, day);
            
            // Add time if available
            if (timePart) {
              const timeMatch = timePart.match(/(\d+):(\d+)\s+(AM|PM)/i);
              if (timeMatch) {
                let hours = parseInt(timeMatch[1]);
                const minutes = parseInt(timeMatch[2]);
                const ampm = timeMatch[3].toUpperCase();
                
                // Convert to 24-hour format
                if (ampm === 'PM' && hours < 12) {
                  hours += 12;
                } else if (ampm === 'AM' && hours === 12) {
                  hours = 0;
                }
                
                newDate.setHours(hours, minutes, 0, 0);
              }
            }
            
            return newDate;
          }
        }
      }
    } catch (error) {
      console.error('Error parsing timestamp:', error, timestamp);
    }
  }
  
  // Handle "Today" and "Yesterday" formats
  if (timestamp.startsWith('Today')) {
    const today = new Date();
    const timeStr = timestamp.split(', ')[1];
    const [hours, minutes] = timeStr.split(':');
    const isPM = timeStr.includes('PM');
    
    today.setHours(
      isPM && hours !== '12' ? parseInt(hours) + 12 : (hours === '12' && !isPM ? 0 : parseInt(hours)),
      parseInt(minutes),
      0,
      0
    );
    return today;
  } else if (timestamp.startsWith('Yesterday')) {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const timeStr = timestamp.split(', ')[1];
    const [hours, minutes] = timeStr.split(':');
    const isPM = timeStr.includes('PM');
    
    yesterday.setHours(
      isPM && hours !== '12' ? parseInt(hours) + 12 : (hours === '12' && !isPM ? 0 : parseInt(hours)),
      parseInt(minutes),
      0,
      0
    );
    return yesterday;
  }
  
  // If all parsing attempts fail, return current date as fallback
  console.warn('Could not parse timestamp, using current date as fallback:', timestamp);
  return new Date();
};

// Modal control
const showScheduleModal = ref(false)
const showAdvancedSettings = ref(false)
const showDeleteConfirmation = ref(false)
const showToast = ref(false)
const toastMessage = ref('')
const toastTimeout = ref(null)

// NEW: Toggle confirmation dialog control
const showToggleConfirmationDialog = ref(false)

// Editing state
const editingScheduleIndex = ref(null)
const scheduleToDeleteIndex = ref(null)
const editingScheduleId = ref(null) // NEW: Store the Firestore document ID when editing

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
const isAm = ref(true)

// Additional settings
const skipIfRain = ref(false)
const notifyWatering = ref(true)
const waterFlowRate = ref('medium')

// Calendar state
const currentDate = ref(new Date())
const selectedDate = ref(new Date())

// Saved schedules array
const savedSchedules = ref([])
const isLoadingSchedules = ref(false)
const nextWateringTime = ref('No schedules set')

// NEW: Helper function to get the original index from the savedSchedules array
const getOriginalIndex = (scheduleId) => {
  return savedSchedules.value.findIndex(schedule => schedule.id === scheduleId);
};

// Function to toggle dropdown
const toggleDropdown = (dropdown) => {
  if (activeDropdown.value === dropdown) {
    activeDropdown.value = null;
  } else {
    activeDropdown.value = dropdown;
  }
};

// NEW: Function to view schedule history
const viewScheduleHistory = () => {
  currentView.value = 'history';
  // Initialize date filters to last 30 days by default
  const today = new Date();
  const thirtyDaysAgo = new Date();
  thirtyDaysAgo.setDate(today.getDate() - 30);
  
  historyFilters.value.startDate = thirtyDaysAgo.toISOString().split('T')[0];
  historyFilters.value.endDate = today.toISOString().split('T')[0];
  
  // Reset pagination
  currentPage.value = 1;
  
  // Fetch all schedules to ensure we have the latest data
  fetchWateringSchedules();
};

// NEW: Function to go back to overview
const backToOverview = () => {
  currentView.value = 'overview';
};

// NEW: Function to apply history filters
const applyHistoryFilters = () => {
  // Reset pagination when filters change
  currentPage.value = 1;
};

// Export data function
const exportData = (format) => {
  console.log(`Exporting data in ${format} format`);
  showToastMessage(`Schedule history exported as ${format.toUpperCase()}`);
  activeDropdown.value = null;
};

// NEW: Pagination functions
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const updatePagination = () => {
  currentPage.value = 1;
};

const goToPage = (page) => {
  if (typeof page === 'number') {
    currentPage.value = page;
  }
};

// NEW: Function to show toggle confirmation dialog
const showToggleConfirmation = () => {
  // Only show confirmation dialog if user is trying to change the current state
  showToggleConfirmationDialog.value = true
}

// NEW: Function to confirm and execute water pump toggle
const confirmToggleWaterPump = async () => {
try {
  // Toggle the state
  waterPumpActive.value = !waterPumpActive.value

  console.log('Toggling water pump to:', waterPumpActive.value ? 'ON' : 'OFF')

  // Get current timestamp
  const now = new Date()
  const formattedTime = now.toLocaleString('en-US', {
    weekday: 'short',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  })

  // Create the status document
  const statusData = {
    status: waterPumpActive.value,
    timestamp: serverTimestamp(),
    device_id: 'main_motor',
    user: 'system',
    formattedTime: formattedTime
  }

  console.log('Saving data to Firebase motor_status collection:', statusData)

  // Save to Firebase
  await setDoc(doc(db, 'motor_status', 'current'), statusData)
  console.log('Successfully saved current status to Firebase')

  const historyRef = collection(db, 'motor_status', 'history', 'logs')
  await addDoc(historyRef, statusData)
  console.log('Successfully added to history logs')

  // Add to UI activity log
  const newActivity = {
    status: waterPumpActive.value,
    timestamp: `Today, ${now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
  }
  motorActivities.value.unshift(newActivity)

  // Show toast
  showToastMessage(`Motor turned ${waterPumpActive.value ? 'ON' : 'OFF'} successfully`)
  showToggleConfirmationDialog.value = false

  // ✅ Send motor status to FastAPI backend here
  try {
    const response = await axios.post('http://localhost:8000/api/motor_status/', {
      status: waterPumpActive.value,
      device_id: 'main_motor',
      user: 'system',
      timestamp: now.toISOString(),
      formatted_time: formattedTime  // ✅ FIXED: was `formattedTime`
    })

    console.log('Motor status sent to FastAPI backend:', response.data)
  } catch (error) {
    console.error('Error sending motor status to FastAPI:', error)
  }

} catch (error) {
  console.error('Error saving motor status to Firebase:', error)
  console.error('Error details:', {
    code: error.code,
    message: error.message,
    stack: error.stack
  })

  waterPumpActive.value = !waterPumpActive.value
  showToastMessage('Error saving motor status. Please check console for details.')
  showToggleConfirmationDialog.value = false
}
}

// Function to fetch motor status from Firebase
const fetchMotorStatus = async () => {
  try {
    console.log('Fetching motor status from Firebase...')
    isLoadingActivities.value = true
    
    // First try to get the current status document
    try {
      const currentStatusDoc = await getDoc(doc(db, 'motor_status', 'current'))
      if (currentStatusDoc.exists()) {
        const data = currentStatusDoc.data()
        waterPumpActive.value = data.status
        console.log('Fetched current motor status:', data.status)
      } else {
        console.log('No current status document found')
      }
    } catch (err) {
      console.warn('Error fetching current status, will try collection query instead:', err)
    }
    
    // Calculate date 7 days ago for filtering
    const sevenDaysAgo = new Date()
    sevenDaysAgo.setDate(sevenDaysAgo.getDate() - 7)
    
    // Fetch recent activities from the history subcollection
    try {
      const historyRef = collection(db, 'motor_status', 'history', 'logs')
      // Add where clause to filter by timestamp
      const activitiesQuery = query(
        historyRef, 
        orderBy('timestamp', 'desc'),
        // No need to limit here as we'll filter in the computed property
      )
      const activitiesSnapshot = await getDocs(activitiesQuery)
      
      const activities = []
      activitiesSnapshot.forEach(doc => {
        const data = doc.data()
        
        // FIXED: Format the timestamp correctly based on the actual date
        let formattedTimestamp;
        if (data.timestamp) {
          const timestampDate = data.timestamp.toDate();
          formattedTimestamp = formatFirebaseTimestamp(timestampDate);
        } else {
          formattedTimestamp = data.formattedTime || 'Unknown time';
        }
        
        activities.push({
          status: data.status,
          timestamp: formattedTimestamp
        })
      })
      
      if (activities.length > 0) {
        motorActivities.value = activities
        console.log('Fetched motor activities:', activities.length)
      }
    } catch (err) {
      console.warn('Error fetching history logs:', err)
    } finally {
      isLoadingActivities.value = false
    }
    
  } catch (error) {
    console.error('Error in fetchMotorStatus:', error)
    isLoadingActivities.value = false
  }
}

// ADDED: New function to format Firebase timestamp with proper date comparison
const formatFirebaseTimestamp = (date) => {
  if (!date || !(date instanceof Date)) {
    return 'Invalid date';
  }
  
  const now = new Date();
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);
  const dateOnly = new Date(date.getFullYear(), date.getMonth(), date.getDate());
  
  // Format the time part
  const timeStr = date.toLocaleTimeString([], { 
    hour: '2-digit', 
    minute: '2-digit',
    hour12: true 
  });
  
  // Check if the date is in the future (which would be incorrect)
  if (dateOnly > today) {
    // Return the full date for future dates (likely a timestamp issue)
    return date.toLocaleString('en-US', {
      weekday: 'short',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      hour12: true
    });
  }
  
  // Check if it's today
  if (dateOnly.getTime() === today.getTime()) {
    return `Today, ${timeStr}`;
  }
  
  // Check if it's yesterday
  if (dateOnly.getTime() === yesterday.getTime()) {
    return `Yesterday, ${timeStr}`;
  }
  
  // Otherwise return the full date
  return date.toLocaleString('en-US', {
    weekday: 'short',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  });
}

// FIXED: Function to fetch watering schedules from Firebase
const fetchWateringSchedules = async () => {
  try {
    console.log('Fetching watering schedules from Firebase...')
    isLoadingSchedules.value = true
    isLoadingNextWatering.value = true
    isLoadingHistory.value = true
    
    // Reference to the watering_schedules collection
    const schedulesRef = collection(db, 'watering_schedules')
    const schedulesQuery = query(schedulesRef, orderBy('createdAt', 'desc'))
    
    const schedulesSnapshot = await getDocs(schedulesQuery)
    
    const schedules = []
    schedulesSnapshot.forEach(doc => {
      const data = doc.data()
      
      // FIXED: Add a completed flag for schedules that have passed their time
      const now = new Date().getTime()
      const isCompleted = data.scheduledTime && data.scheduledTime <= now
      
      schedules.push({
        id: doc.id, // Store the document ID for later updates/deletes
        dateTime: data.dateTime,
        duration: data.duration,
        mode: data.mode,
        days: data.days || [],
        skipIfRain: data.skipIfRain || false,
        notifyWatering: data.notifyWatering || false,
        waterFlowRate: data.waterFlowRate || 'medium',
        interval: data.interval || null,
        scheduledTime: data.scheduledTime || null,
        completed: isCompleted, // Add completed flag
        createdAt: data.createdAt || null
      })
    })
    
    savedSchedules.value = schedules
    console.log('Fetched watering schedules:', schedules.length)
    
    // Calculate the next watering time based on the schedules
    await calculateNextWateringTime()
    
  } catch (error) {
    console.error('Error fetching watering schedules:', error)
    showToastMessage('Error loading schedules. Please try again.')
  } finally {
    isLoadingSchedules.value = false
    isLoadingHistory.value = false
  }
}

// MODIFIED: Function to calculate the next watering time from the database
const calculateNextWateringTime = async () => {
  try {
    if (savedSchedules.value.length === 0) {
      nextWateringTime.value = 'No schedules set'
      isLoadingNextWatering.value = false
      return
    }

    const now = new Date()
    
    // Query for the next scheduled watering that is in the future
    const schedulesRef = collection(db, 'watering_schedules')
    const nextWateringQuery = query(
      schedulesRef,
      where('scheduledTime', '>=', now.getTime()),
      orderBy('scheduledTime', 'asc'),
      limit(1)
    )
    
    try {
      const nextWateringSnapshot = await getDocs(nextWateringQuery)
      
      if (!nextWateringSnapshot.empty) {
        // Get the first (and only) document from the query result
        const nextWateringDoc = nextWateringSnapshot.docs[0]
        const nextWateringData = nextWateringDoc.data()
        
        // Use the dateTime field which contains the formatted date and time
        if (nextWateringData.dateTime) {
          nextWateringTime.value = nextWateringData.dateTime
          console.log('Next watering time set from database:', nextWateringData.dateTime)
        } else {
          nextWateringTime.value = 'No upcoming waterings'
          console.log('Next watering document found but no dateTime field')
        }
      } else {
        // If no future schedules found in the database, set to "No upcoming waterings"
        nextWateringTime.value = 'No upcoming waterings'
        console.log('No upcoming waterings found in database')
      }
    } catch (error) {
      console.error('Error querying next watering schedule:', error)
      nextWateringTime.value = 'Error loading next watering'
    }
  } catch (error) {
    console.error('Error calculating next watering time:', error)
    nextWateringTime.value = 'Error calculating next watering'
  } finally {
    isLoadingNextWatering.value = false
  }
}

// Calendar functions
const currentMonthName = computed(() => {
  return new Intl.DateTimeFormat('en-US', { month: 'long' }).format(currentDate.value)
})

const currentYear = computed(() => {
  return currentDate.value.getFullYear()
})

const calendarDays = computed(() => {
  const year = currentDate.value.getFullYear()
  const month = currentDate.value.getMonth()

  // First day of the month
  const firstDay = new Date(year, month, 1)
  // Last day of the month
  const lastDay = new Date(year, month + 1, 0)

  // Get the day of the week for the first day (0 = Sunday, 6 = Saturday)
  const firstDayOfWeek = firstDay.getDay()

  // Array to hold all calendar days
  const days = []

  // Add days from previous month
  const prevMonthLastDay = new Date(year, month, 0).getDate()
  for (let i = firstDayOfWeek - 1; i >= 0; i--) {
    days.push({
      day: prevMonthLastDay - i,
      month: month - 1,
      year: month === 0 ? year - 1 : year,
      isCurrentMonth: false
    })
  }

  // Add days from current month
  for (let i = 1; i <= lastDay.getDate(); i++) {
    days.push({
      day: i,
      month,
      year,
      isCurrentMonth: true
    })
  }

  // Add days from next month
  const remainingDays = 42 - days.length // 6 rows of 7 days
  for (let i = 1; i <= remainingDays; i++) {
    days.push({
      day: i,
      month: month + 1,
      year: month === 11 ? year + 1 : year,
      isCurrentMonth: false
    })
  }

  return days
})

const prevMonth = () => {
  currentDate.value = new Date(
    currentDate.value.getFullYear(),
    currentDate.value.getMonth() - 1,
    1
  )
}

const nextMonth = () => {
  currentDate.value = new Date(
    currentDate.value.getFullYear(),
    currentDate.value.getMonth() + 1,
    1
  )
}

const selectCalendarDate = (day) => {
  selectedDate.value = new Date(day.year, day.month, day.day)
}

const isSelectedDate = (day) => {
  const selected = selectedDate.value
  return day.day === selected.getDate() &&
         day.month === selected.getMonth() &&
         day.year === selected.getFullYear()
}

const isToday = (day) => {
  const today = new Date()
  return day.day === today.getDate() &&
         day.month === today.getMonth() &&
         day.year === today.getFullYear()
}

// Time functions
const incrementHour = () => {
  let hour = parseInt(wateringHour.value)
  hour = (hour + 1) % 24
  wateringHour.value = hour
  updateAmPm()
}

const decrementHour = () => {
  let hour = parseInt(wateringHour.value)
  hour = (hour - 1 + 24) % 24
  wateringHour.value = hour
  updateAmPm()
}

const incrementMinute = () => {
  let minute = parseInt(wateringMinute.value)
  minute = (minute + 5) % 60
  wateringMinute.value = minute
}

const decrementMinute = () => {
  let minute = parseInt(wateringMinute.value)
  minute = (minute - 5 + 60) % 60
  wateringMinute.value = minute
}

const updateAmPm = () => {
  // Update isAm based on the 24-hour format hour
  isAm.value = wateringHour.value < 12

  // Log the current time state for debugging
  console.log(`Time updated: ${wateringHour.value}:${wateringMinute.value} (${isAm.value ? "AM" : "PM"})`)
}

// COMPLETELY REWRITTEN: Function to set AM/PM
const setAmPm = (value) => {
  console.log(`setAmPm called with value: ${value}, current hour: ${wateringHour.value}, current isAm: ${isAm.value}`);
  
  // Only update if we're actually changing the AM/PM state
  if (value === 'AM' && !isAm.value) {
    // Switching from PM to AM
    if (wateringHour.value >= 12) {
      wateringHour.value = wateringHour.value - 12;
    }
    isAm.value = true;
  } else if (value === 'PM' && isAm.value) {
    // Switching from AM to PM
    if (wateringHour.value < 12) {
      wateringHour.value = wateringHour.value + 12;
    }
    isAm.value = false;
  }
  
  console.log(`After setAmPm: hour=${wateringHour.value}, isAm=${isAm.value}`);
}

// Validation functions
const validateHour = () => {
  let hour = parseInt(formattedHour.value)
  if (isNaN(hour) || hour < 0) hour = 0
  if (hour > 23) hour = 23
  wateringHour.value = hour
  updateAmPm()
}

const validateMinute = () => {
  let minute = parseInt(formattedMinute.value)
  if (isNaN(minute) || minute < 0) minute = 0
  if (minute > 59) minute = 59
  wateringMinute.value = minute
}

// Formatted time inputs
const formattedHour = computed({
  get: () => {
    const hour = wateringHour.value % 12
    return (hour === 0 ? 12 : hour).toString().padStart(2, '0')
  },
  set: (value) => {
    let hour = parseInt(value)
    if (!isNaN(hour)) {
      if (hour === 12) hour = 0
      if (!isAm.value) hour += 12
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

// Toggle watering day
const toggleWateringDay = (index) => {
  wateringDays.value[index] = !wateringDays.value[index]
}

// Function to open the schedule modal for creating a new schedule
const openScheduleModal = (index = null) => {
  if (index === null) {
    // Creating a new schedule - reset form
    editingScheduleIndex.value = null
    editingScheduleId.value = null
    resetScheduleForm()
  } else {
    // Editing existing schedule - load data
    editingScheduleIndex.value = index
    editingScheduleId.value = savedSchedules.value[index].id // Store the document ID
    loadScheduleData(index)
  }
  showScheduleModal.value = true
}

// COMPLETELY REWRITTEN: Function to load schedule data for editing
const loadScheduleData = (index) => {
  const schedule = savedSchedules.value[index];
  console.log("Loading schedule data:", schedule);

  // Set mode
  wateringMode.value = schedule.mode;

  // Set days for weekly mode
  if (schedule.days) {
    wateringDays.value = [...schedule.days];
  }

  // Set time - CRITICAL FIX
  const timeMatch = schedule.dateTime.match(/(\d+):(\d+)\s+(AM|PM)/);
  if (timeMatch) {
    const hour12 = parseInt(timeMatch[1]);
    const minute = parseInt(timeMatch[2]);
    const ampm = timeMatch[3];

    console.log(`Parsed time from schedule: ${hour12}:${minute} ${ampm}`);

    // Set AM/PM state first
    isAm.value = ampm === 'AM';

    // Convert to 24-hour format for internal storage
    let hour24;
    if (ampm === 'PM' && hour12 < 12) {
      hour24 = hour12 + 12;
    } else if (ampm === 'AM' && hour12 === 12) {
      hour24 = 0;
    } else {
      hour24 = hour12;
    }

    wateringHour.value = hour24;
    wateringMinute.value = minute;

    console.log(`Loaded time: ${hour24}:${minute} (${ampm}), isAm set to ${isAm.value}`);
  }

  // Set duration
  wateringDuration.value = schedule.duration;

  // Set additional settings
  skipIfRain.value = schedule.skipIfRain || false;
  notifyWatering.value = schedule.notifyWatering || false;
  waterFlowRate.value = schedule.waterFlowRate || 'medium';

  // Set interval for custom mode
  if (schedule.interval) {
    wateringInterval.value = schedule.interval.value;
    wateringIntervalUnit.value = schedule.interval.unit;
  }

  // Set date for one-time mode
  if (schedule.mode === 'one-time' && schedule.dateTime) {
    const dateMatch = schedule.dateTime.match(/([A-Za-z]+),\s+([A-Za-z]+)\s+(\d+)/);
    if (dateMatch) {
      const monthName = dateMatch[2];
      const day = parseInt(dateMatch[3]);

      // Create a date object
      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      const monthIndex = months.findIndex(m => m === monthName);

      if (monthIndex !== -1) {
        selectedDate.value = new Date(new Date().getFullYear(), monthIndex, day);
        currentDate.value = new Date(selectedDate.value);
      }
    }
  }
};

// Function to reset the schedule form
const resetScheduleForm = () => {
  wateringMode.value = 'weekly'
  wateringDays.value = [true, false, true, false, true, false, false]
  wateringHour.value = 6
  wateringMinute.value = 30
  wateringDuration.value = 20
  wateringInterval.value = 2
  wateringIntervalUnit.value = 'days'
  skipIfRain.value = false
  notifyWatering.value = true
  waterFlowRate.value = 'medium'
  selectedDate.value = new Date()
  currentDate.value = new Date()
  isAm.value = true
}

// Function to close the schedule modal
const closeScheduleModal = () => {
  showScheduleModal.value = false
  editingScheduleIndex.value = null
  editingScheduleId.value = null
}

// Function to increase duration
const increaseDuration = () => {
  if (wateringDuration.value < 120) {
    wateringDuration.value++
  }
}

// Function to decrease duration
const decreaseDuration = () => {
  if (wateringDuration.value > 1) {
    wateringDuration.value--
  }
}

// Function to increase interval
const increaseInterval = () => {
  if (wateringInterval.value < 30) {
    wateringInterval.value++
  }
}

// Function to decrease interval
const decreaseInterval = () => {
  if (wateringInterval.value > 1) {
    wateringInterval.value--
  }
}

// Function to edit a schedule
const editSchedule = (index) => {
  openScheduleModal(index)
}

// Function to initiate schedule deletion
const removeSchedule = (index) => {
  scheduleToDeleteIndex.value = index
  showDeleteConfirmation.value = true
}

// UPDATED: Function to confirm and execute schedule deletion
const confirmDeleteSchedule = async () => {
  if (scheduleToDeleteIndex.value !== null) {
    try {
      const scheduleId = savedSchedules.value[scheduleToDeleteIndex.value].id
      
      // Delete from Firebase
      await deleteDoc(doc(db, 'watering_schedules', scheduleId))
      
      // Remove from local array
      savedSchedules.value.splice(scheduleToDeleteIndex.value, 1)
      
      // Recalculate next watering time
      await calculateNextWateringTime()
      
      showToastMessage('Schedule deleted successfully')
    } catch (error) {
      console.error('Error deleting schedule:', error)
      showToastMessage('Error deleting schedule. Please try again.')
    } finally {
      showDeleteConfirmation.value = false
      scheduleToDeleteIndex.value = null
    }
  }
}

// Function to show toast message
const showToastMessage = (message) => {
  // Clear any existing timeout
  if (toastTimeout.value) {
    clearTimeout(toastTimeout.value)
  }

  // Set message and show toast
  toastMessage.value = message
  showToast.value = true

  // Auto-hide after 3 seconds
  toastTimeout.value = setTimeout(() => {
    showToast.value = false
  }, 3000)
}

// Schedule summary
const scheduleSummary = computed(() => {
  if (wateringMode.value === 'weekly') {
    const selectedDays = weekDays
      .filter((_, index) => wateringDays.value[index])
      .map(day => day.substring(0, 3))
      .join(', ')
    return `Every ${selectedDays || 'day'}`
  } else if (wateringMode.value === 'daily') {
    return 'Every day'
  } else if (wateringMode.value === 'custom') {
    return `Every ${wateringInterval.value} ${wateringIntervalUnit.value}`
  } else if (wateringMode.value === 'one-time') {
    return selectedDate.value.toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: 'numeric'
    })
  }
  return ''
})

// COMPLETELY REWRITTEN: Time display computed property
const timeDisplay = computed(() => {
  // Convert 24-hour format to 12-hour format for display
  let hour12 = wateringHour.value % 12;
  if (hour12 === 0) hour12 = 12; // 0 should display as 12 in 12-hour format
  
  const minute = wateringMinute.value.toString().padStart(2, '0');
  const ampm = wateringHour.value < 12 ? 'AM' : 'PM';
  
  console.log(`timeDisplay computed: ${hour12}:${minute} ${ampm} (from hour: ${wateringHour.value}, isAm: ${isAm.value})`);
  return `${hour12}:${minute} ${ampm}`;
});

const saveWateringSchedule = async () => {
  try {
    console.log("🚀 Starting saveWateringSchedule...");
    console.log(`Selected Hour: ${wateringHour.value}, Minute: ${wateringMinute.value}, isAm: ${isAm.value}`);

    const scheduledTime = new Date();

    // If one-time, set full date
    if (wateringMode.value === 'one-time') {
      scheduledTime.setFullYear(
        selectedDate.value.getFullYear(),
        selectedDate.value.getMonth(),
        selectedDate.value.getDate()
      );
    }

    // Convert time to 24-hour format
    let hour24 = wateringHour.value;
    if (isAm.value && hour24 === 12) {
      hour24 = 0;
    } else if (!isAm.value && hour24 < 12) {
      hour24 = hour24 + 12;
    }
    scheduledTime.setHours(hour24, wateringMinute.value, 0, 0);

    // Format for user-friendly display
    const formattedDateTime = (() => {
      const timeDate = new Date();
      if (wateringMode.value === 'one-time') {
        timeDate.setFullYear(
          selectedDate.value.getFullYear(),
          selectedDate.value.getMonth(),
          selectedDate.value.getDate()
        );
      }
      timeDate.setHours(hour24, wateringMinute.value, 0, 0);
      return timeDate.toLocaleString('en-US', {
        weekday: 'short',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
      });
    })();

    const now = new Date().getTime();
    const isCompleted = scheduledTime.getTime() <= now;

    const scheduleData = {
      dateTime: formattedDateTime,
      duration: wateringDuration.value,
      mode: wateringMode.value,
      days: [...wateringDays.value],
      skipIfRain: skipIfRain.value,
      notifyWatering: notifyWatering.value,
      waterFlowRate: waterFlowRate.value,
      interval: wateringMode.value === 'custom' ? {
        value: wateringInterval.value,
        unit: wateringIntervalUnit.value,
      } : null,
      scheduledTime: scheduledTime.getTime(),
      completed: isCompleted
    };

    console.log("📦 Sending schedule to backend:", scheduleData);

    const response = await axios.post("http://127.0.0.1:8000/api/watering-schedule", scheduleData);

    if (response.status === 200) {
      console.log("✅ Schedule successfully saved to backend.");
      showToastMessage("Schedule saved successfully");

      savedSchedules.value.push({
        ...scheduleData,
        id: response.data.id || 'temp-' + Date.now(),
        createdAt: new Date().toISOString()
      });

      await calculateNextWateringTime();
      closeScheduleModal();

      if (currentView.value === 'history') {
        await fetchWateringSchedules();
      }
    } else {
      console.error("❌ Backend responded with an error:", response);
      showToastMessage("Error: Backend responded with an error.");
    }
  } catch (error) {
    console.error("❌ Error saving watering schedule:", error);
    showToastMessage("Error saving schedule. Please try again.");
  }
};

// Initialize AM/PM based on hour
watch(() => wateringHour.value, updateAmPm, { immediate: true })

onMounted(() => {
  console.log('Component mounted, fetching data...')
  // Fetch initial motor status from Firebase
  fetchMotorStatus()
  // Fetch watering schedules from Firebase
  fetchWateringSchedules()
  
  // Initialize history date filters to last 30 days by default
  const today = new Date()
  const thirtyDaysAgo = new Date()
  thirtyDaysAgo.setDate(today.getDate() - 30)
  
  historyFilters.value.startDate = thirtyDaysAgo.toISOString().split('T')[0]
  historyFilters.value.endDate = today.toISOString().split('T')[0]
})

onUnmounted(() => {
  if (toastTimeout.value) clearTimeout(toastTimeout.value)
})
</script>

<style>
/* Keep your existing styles */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Modal animations */
.modal-enter-active,
.modal-leave-active {
  transition: all 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

/* Toast animations */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Power button styles */
.glass-button {
  backdrop-filter: blur(4px);
  transform: translateZ(0);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 
    0 10px 25px -5px rgba(0, 0, 0, 0.1), 
    0 10px 10px -5px rgba(0, 0, 0, 0.04),
    inset 0 -5px 10px -5px rgba(0, 0, 0, 0.1);
}

.active-button {
  box-shadow: 
    0 0 0 2px rgba(34, 197, 94, 0.5),
    0 0 20px 5px rgba(34, 197, 94, 0.5),
    0 0 0 4px rgba(34, 197, 94, 0.3),
    inset 0 -5px 15px -5px rgba(0, 0, 0, 0.2);
}

.inactive-button {
  box-shadow: 
    0 0 0 2px rgba(249, 115, 22, 0.3),
    0 0 15px 2px rgba(249, 115, 22, 0.2),
    0 0 0 4px rgba(249, 115, 22, 0.1),
    inset 0 -5px 15px -5px rgba(0, 0, 0, 0.2);
}

/* Power icon animations */
.power-icon-on {
  filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.8));
  animation: glow 2s ease-in-out infinite alternate;
}

.power-icon-off {
  filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
}

@keyframes glow {
  from {
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.8));
  }
  to {
    filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.9));
  }
}

/* Pulse animation for active button */
.pulse-animation {
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 0.1;
  }
  100% {
    opacity: 0;
  }
}
</style>