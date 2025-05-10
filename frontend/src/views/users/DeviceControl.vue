<template>
<<<<<<< HEAD
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen pt-32">
      <!-- Container Wrapper with proper spacing -->
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Main Container with adjusted width -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border borderc-green-100 h-[calc(100vh-140px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
          <!-- Title Section with breadcrumb navigation -->
          <div class="p-6 pb-0">
            <div>
              <h1 class="text-2xl font-bold text-gray-800 mb-2">Device Control</h1>
              <div class="flex items-center text-sm text-gray-500">
                <span class="text-green-600">Device Setup</span>
                <ChevronRight class="h-4 w-4 mx-1" />
                <span>{{ currentView === 'history' ? 'Schedule History' : 'Overview' }}</span>
              </div>
            </div>
          </div>
          
          <!-- Content Wrapper -->
          <div class="p-6 md:p-8">
            <!-- Main View Switcher -->
            <div v-if="currentView === 'overview'">
=======
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
              <div>
                <h1 class="text-2xl font-bold text-gray-800 mb-2">Device Control</h1>
                <div class="flex items-center text-sm text-gray-500">
                  <span class="text-green-600">Device Setup</span>
                  <ChevronRight class="h-4 w-4 mx-1" />
                  <span>Overview</span>
                </div>
              </div>
            </div>
            
            <!-- Content Wrapper -->
            <div class="p-6 md:p-8">
>>>>>>> cy
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
<<<<<<< HEAD

=======
  
>>>>>>> cy
                <!-- Saved Schedules Card - Expanded to take 2/3 of the space (col-span-2) -->
                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 md:col-span-2">
                  <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                      <div class="text-green-500">
                        <CalendarClock class="w-5 h-5" />
                      </div>
                      <h2 class="text-lg font-medium text-gray-800">Saved Schedules</h2>
                    </div>
<<<<<<< HEAD
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
=======
                    <!-- Add Schedule Button - Slightly larger but not too large -->
                    <button 
                      @click="openScheduleModal()" 
                      class="flex items-center gap-1.5 bg-green-500 hover:bg-green-600 text-white font-medium rounded-full px-4 py-2 transition-all duration-300 shadow-sm hover:shadow-md text-sm"
                    >
                      <Plus class="w-4 h-4" />
                      <span>Add Schedule</span>
                    </button>
>>>>>>> cy
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
                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-[400px] overflow-y-auto pr-1 mb-4">
<<<<<<< HEAD
                    <div v-if="upcomingSchedules.length === 0" class="flex flex-col items-center justify-center py-12 text-center md:col-span-2 lg:col-span-3">
                      <div class="bg-gray-50 p-6 rounded-full mb-4">
                        <CalendarClock class="w-16 h-16 text-gray-200" />
                      </div>
                      <p class="text-gray-400 font-medium">No upcoming schedules</p>
=======
                    <div v-if="savedSchedules.length === 0" class="flex flex-col items-center justify-center py-12 text-center md:col-span-2 lg:col-span-3">
                      <div class="bg-gray-50 p-6 rounded-full mb-4">
                        <CalendarClock class="w-16 h-16 text-gray-200" />
                      </div>
                      <p class="text-gray-400 font-medium">No schedules saved yet</p>
>>>>>>> cy
                      <p class="text-xs text-gray-400 mt-2">Add a schedule to see it here</p>
                    </div>
                    
                    <div 
<<<<<<< HEAD
                      v-for="(schedule, index) in upcomingSchedules" 
=======
                      v-for="(schedule, index) in savedSchedules" 
>>>>>>> cy
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
<<<<<<< HEAD
                            @click="editSchedule(getOriginalIndex(schedule.id))" 
=======
                            @click="editSchedule(index)" 
>>>>>>> cy
                            class="text-gray-300 group-hover:text-green-500 transition-colors p-1 rounded-full hover:bg-green-50"
                            title="Edit schedule"
                          >
                            <Edit2 class="w-4 h-4" />
                          </button>
                          <!-- Delete button -->
                          <button 
<<<<<<< HEAD
                            @click="removeSchedule(getOriginalIndex(schedule.id))" 
=======
                            @click="removeSchedule(index)" 
>>>>>>> cy
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
<<<<<<< HEAD

            <!-- Schedule History View -->
            <div v-else-if="currentView === 'history'" class="animate-fadeIn">
              <div class="flex items-center justify-between mb-6">
                <div class="flex items-center gap-3">
                  <div class="bg-gray-100 p-2 rounded-full">
                    <History class="w-5 h-5 text-gray-600" />
                  </div>
                  <h2 class="text-xl font-medium text-gray-800">Schedule History</h2>
                </div>
                <button 
                  @click="backToOverview()" 
                  class="flex items-center gap-1.5 bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium rounded-full px-4 py-2 transition-all duration-300 shadow-sm hover:shadow-md text-sm"
                >
                  <ArrowLeft class="w-4 h-4" />
                  <span>Back to Overview</span>
                </button>
              </div>

              <!-- History Filters -->
              <div class="bg-white rounded-xl p-4 border border-gray-200 mb-6">
                <div class="flex flex-wrap items-center gap-4">
                  <div class="flex-1 min-w-[200px]">
                    <label class="block text-xs font-medium text-gray-500 mb-1">Date Range</label>
                    <div class="flex items-center gap-2">
                      <div class="relative flex-1">
                        <input 
                          type="date" 
                          v-model="historyFilters.startDate" 
                          class="w-full bg-gray-50 border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-green-500"
                        />
                        <Calendar class="absolute right-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400 pointer-events-none" />
                      </div>
                      <span class="text-gray-400">to</span>
                      <div class="relative flex-1">
                        <input 
                          type="date" 
                          v-model="historyFilters.endDate" 
                          class="w-full bg-gray-50 border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-green-500"
                        />
                        <Calendar class="absolute right-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400 pointer-events-none" />
                      </div>
                    </div>
                  </div>
                  <div class="w-[150px]">
                    <label class="block text-xs font-medium text-gray-500 mb-1">Schedule Type</label>
                    <select 
                      v-model="historyFilters.scheduleType" 
                      class="w-full bg-gray-50 border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-green-500"
                    >
                      <option value="all">All Types</option>
                      <option value="one-time">One-time</option>
                      <option value="daily">Daily</option>
                      <option value="weekly">Weekly</option>
                      <option value="custom">Custom</option>
                    </select>
                  </div>
                  <div class="w-[150px]">
                    <label class="block text-xs font-medium text-gray-500 mb-1">Duration</label>
                    <select 
                      v-model="historyFilters.duration" 
                      class="w-full bg-gray-50 border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-green-500"
                    >
                      <option value="all">All Durations</option>
                      <option value="short">Short (< 10 min)</option>
                      <option value="medium">Medium (10-30 min)</option>
                      <option value="long">Long (> 30 min)</option>
                    </select>
                  </div>
                  <div class="flex items-end">
                    <button 
                      @click="applyHistoryFilters" 
                      class="bg-green-500 hover:bg-green-600 text-white font-medium rounded-lg px-4 py-2 transition-all duration-300 text-sm flex items-center gap-1.5"
                    >
                      <Filter class="w-4 h-4" />
                      <span>Apply Filters</span>
                    </button>
                  </div>
                </div>
              </div>

              <!-- History Table -->
              <div class="bg-white rounded-xl border border-gray-200 overflow-hidden">
                <!-- Table Header -->
                <div class="bg-gray-50 border-b border-gray-200 grid grid-cols-12 gap-4 px-6 py-3">
                  <div class="col-span-3 font-medium text-gray-600 text-sm">Date & Time</div>
                  <div class="col-span-2 font-medium text-gray-600 text-sm">Duration</div>
                  <div class="col-span-2 font-medium text-gray-600 text-sm">Schedule Type</div>
                  <div class="col-span-2 font-medium text-gray-600 text-sm">Status</div>
                  <div class="col-span-3 font-medium text-gray-600 text-sm">Additional Info</div>
                </div>

                <!-- Loading State -->
                <div v-if="isLoadingHistory" class="py-20 flex flex-col items-center justify-center">
                  <div class="w-10 h-10 border-2 border-green-500 border-t-transparent rounded-full animate-spin mb-3"></div>
                  <p class="text-gray-500">Loading schedule history...</p>
                </div>

                <!-- Empty State -->
                <div v-else-if="filteredPastSchedules.length === 0" class="py-20 flex flex-col items-center justify-center">
                  <div class="bg-gray-50 p-6 rounded-full mb-4">
                    <History class="w-16 h-16 text-gray-200" />
                  </div>
                  <p class="text-gray-400 font-medium">No past schedules found</p>
                  <p class="text-xs text-gray-400 mt-2">Completed schedules will appear here</p>
                </div>

                <!-- Table Content -->
                <div v-else class="divide-y divide-gray-100 max-h-[500px] overflow-y-auto">
                  <div 
                    v-for="(schedule, index) in filteredPastSchedules" 
                    :key="index"
                    class="grid grid-cols-12 gap-4 px-6 py-4 hover:bg-gray-50 transition-colors"
                  >
                    <!-- Date & Time -->
                    <div class="col-span-3 flex items-center gap-2">
                      <div class="w-2 h-2 rounded-full bg-gray-400"></div>
                      <span class="text-sm text-gray-700">{{ schedule.dateTime }}</span>
                    </div>
                    
                    <!-- Duration -->
                    <div class="col-span-2 flex items-center gap-1.5">
                      <Clock class="w-4 h-4 text-gray-400" />
                      <span class="text-sm text-gray-600">{{ schedule.duration }} minutes</span>
                    </div>
                    
                    <!-- Schedule Type -->
                    <div class="col-span-2 flex items-center gap-1.5">
                      <Calendar class="w-4 h-4 text-gray-400" />
                      <span class="text-sm text-gray-600 capitalize">{{ schedule.mode }}</span>
                    </div>
                    
                    <!-- Status -->
                    <div class="col-span-2">
                      <span class="text-xs font-medium px-2.5 py-1 rounded-full bg-gray-200 text-gray-700">
                        Completed
                      </span>
                    </div>
                    
                    <!-- Additional Info -->
                    <div class="col-span-3 flex items-center gap-2 flex-wrap">
                      <div v-if="schedule.skipIfRain" class="flex items-center gap-1 text-xs text-blue-600 bg-blue-50 px-2 py-1 rounded-full">
                        <CloudRain class="w-3 h-3" />
                        <span>Rain skip enabled</span>
                      </div>
                      <div v-if="schedule.notifyWatering" class="flex items-center gap-1 text-xs text-amber-600 bg-amber-50 px-2 py-1 rounded-full">
                        <Bell class="w-3 h-3" />
                        <span>Notification sent</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Pagination -->
                <div class="bg-gray-50 border-t border-gray-200 px-6 py-3 flex items-center justify-between">
                  <div class="text-sm text-gray-500">
                    Showing <span class="font-medium">{{ paginationStart }}</span> to <span class="font-medium">{{ paginationEnd }}</span> of <span class="font-medium">{{ filteredPastSchedules.length }}</span> entries
                  </div>
                  <div class="flex items-center gap-2">
                    <button 
                      @click="prevPage" 
                      :disabled="currentPage === 1"
                      :class="[
                        'px-3 py-1 rounded-md text-sm border',
                        currentPage === 1 
                          ? 'bg-gray-100 text-gray-400 border-gray-200 cursor-not-allowed' 
                          : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'
                      ]"
                    >
                      <ChevronLeft class="w-4 h-4" />
                    </button>
                    <div class="text-sm text-gray-600 font-medium">
                      Page {{ currentPage }} of {{ totalPages }}
                    </div>
                    <button 
                      @click="nextPage" 
                      :disabled="currentPage === totalPages"
                      :class="[
                        'px-3 py-1 rounded-md text-sm border',
                        currentPage === totalPages 
                          ? 'bg-gray-100 text-gray-400 border-gray-200 cursor-not-allowed' 
                          : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'
                      ]"
                    >
                      <ChevronRight class="w-4 h-4" />
                    </button>
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
=======
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
>>>>>>> cy
                      >
                        <Plus class="w-4 h-4 text-gray-600" />
                      </button>
                    </div>
<<<<<<< HEAD
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
=======
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
>>>>>>> cy
                  </div>
                </div>
              </div>
            </div>
<<<<<<< HEAD
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
  Filter
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

// Pagination for history view
const itemsPerPage = 10
const currentPage = ref(1)
const totalPages = computed(() => Math.ceil(filteredPastSchedules.value.length / itemsPerPage))
const paginationStart = computed(() => ((currentPage.value - 1) * itemsPerPage) + 1)
const paginationEnd = computed(() => Math.min(currentPage.value * itemsPerPage, filteredPastSchedules.value.length))

// History filters
const historyFilters = ref({
  startDate: '',
  endDate: '',
  scheduleType: 'all',
  duration: 'all'
})

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

const pastSchedules = computed(() => {
  const now = new Date().getTime();
  return savedSchedules.value.filter(schedule => {
    // Check if the schedule has a scheduledTime property and it's in the past
    return schedule.scheduledTime && schedule.scheduledTime <= now;
  });
});

// NEW: Filtered past schedules based on history filters
const filteredPastSchedules = computed(() => {
  let filtered = [...pastSchedules.value];
  
  // Apply date range filter
  if (historyFilters.value.startDate) {
    const startDate = new Date(historyFilters.value.startDate).getTime();
    filtered = filtered.filter(schedule => schedule.scheduledTime >= startDate);
  }
  
  if (historyFilters.value.endDate) {
    const endDate = new Date(historyFilters.value.endDate);
    endDate.setHours(23, 59, 59, 999); // End of the day
    const endTime = endDate.getTime();
    filtered = filtered.filter(schedule => schedule.scheduledTime <= endTime);
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

// Helper function to parse activity timestamps into Date objects
const parseActivityTimestamp = (timestamp) => {
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
  } else {
    // Handle other date formats (e.g., "Mon, Apr 29, 02:11 AM")
    try {
      const dateParts = timestamp.split(', ');
      if (dateParts.length >= 3) {
        const monthDay = dateParts[1].split(' ');
        const month = monthToNumber(monthDay[0]);
        const day = parseInt(monthDay[1]);
        
        const timeStr = dateParts[2];
        const [timePart, ampm] = timeStr.split(' ');
        const [hours, minutes] = timePart.split(':');
        const isPM = ampm === 'PM';
        
        const date = new Date();
        date.setMonth(month);
        date.setDate(day);
        date.setHours(
          isPM && hours !== '12' ? parseInt(hours) + 12 : (hours === '12' && !isPM ? 0 : parseInt(hours)),
          parseInt(minutes),
          0,
          0
        );
        return date;
      }
    } catch (error) {
      console.error('Error parsing timestamp:', error);
    }
    
    // If parsing fails, return a date object for the timestamp
    // This is a fallback that will include the activity in the list
    return new Date();
  }
};

// Helper function to convert month name to month number (0-11)
const monthToNumber = (monthName) => {
  const months = {
    'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
    'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
  };
  return months[monthName] || 0;
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
      device_id: 'main_motor',      user: 'system',
      timestamp: now.toISOString(),
      formatted_time: formattedTime
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
        // Only include activities from the last 7 days
        if (data.timestamp && data.timestamp.toDate() >= sevenDaysAgo) {
          activities.push({
            status: data.status,
            timestamp: data.formattedTime || formatTimestamp(data.timestamp)
          })
        }
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

// Function to fetch watering schedules from Firebase
const fetchWateringSchedules = async () => {
  try {
    console.log('Fetching watering schedules from Firebase...')
    isLoadingSchedules.value = true
    isLoadingNextWatering.value = true
    
    // Reference to the watering_schedules collection
    const schedulesRef = collection(db, 'watering_schedules')
    const schedulesQuery = query(schedulesRef, orderBy('createdAt', 'desc'))
    
    const schedulesSnapshot = await getDocs(schedulesQuery)
    
    const schedules = []
    schedulesSnapshot.forEach(doc => {
      const data = doc.data()
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
        scheduledTime: data.scheduledTime || null
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

// Function to format Firestore timestamp
const formatTimestamp = (timestamp) => {
  if (!timestamp) return ''

  const date = timestamp.toDate()
  const now = new Date()
  const yesterday = new Date(now)
  yesterday.setDate(yesterday.getDate() - 1)

  // Check if it's today
  if (date.toDateString() === now.toDateString()) {
    return `Today, ${date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
  }

  // Check if it's yesterday
  if (date.toDateString() === yesterday.toDateString()) {
    return `Yesterday, ${date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
  }

  // Otherwise return the full date
  return date.toLocaleString([], {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
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

// COMPLETELY REWRITTEN: Save or update watering schedule
const saveWateringSchedule = async () => {
  try {
    console.log("Starting saveWateringSchedule with current values:");
    console.log(`Hour: ${wateringHour.value}, Minute: ${wateringMinute.value}, isAm: ${isAm.value}`);
    
    // Create scheduled time as a timestamp for easier querying
    const scheduledTime = new Date();

    if (wateringMode.value === 'one-time') {
      // Use the selected date for one-time schedules
      scheduledTime.setFullYear(
        selectedDate.value.getFullYear(),
        selectedDate.value.getMonth(),
        selectedDate.value.getDate()
      );
    }

    // CRITICAL FIX: Properly convert 12-hour format to 24-hour format
    let hour24 = wateringHour.value;
    
    // Debug the current state
    console.log(`Before conversion - hour24: ${hour24}, isAm: ${isAm.value}`);
    
    // Handle 12 AM special case
    if (isAm.value && hour24 === 12) {
      hour24 = 0;
    } 
    // Handle PM conversion (except 12 PM which stays as 12)
    else if (!isAm.value && hour24 < 12) {
      hour24 = hour24 + 12;
    }
    
    console.log(`After conversion - hour24: ${hour24}, isAm: ${isAm.value}`);
    
    // Set the time component
    scheduledTime.setHours(hour24, wateringMinute.value, 0, 0);
    
    // Format the time string for display
    const formattedDateTime = (() => {
      const timeDate = new Date();
      
      // Set the date part if it's a one-time schedule
      if (wateringMode.value === 'one-time') {
        timeDate.setFullYear(
=======
            
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
    CheckCircle
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
  
  // System control values
  const waterPumpActive = ref(false)
  const motorActivities = ref([])
  const isLoadingActivities = ref(true)
  const isLoadingNextWatering = ref(true)
  
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
  
  // Helper function to parse activity timestamps into Date objects
  const parseActivityTimestamp = (timestamp) => {
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
    } else {
      // Handle other date formats (e.g., "Mon, Apr 29, 02:11 AM")
      try {
        const dateParts = timestamp.split(', ');
        if (dateParts.length >= 3) {
          const monthDay = dateParts[1].split(' ');
          const month = monthToNumber(monthDay[0]);
          const day = parseInt(monthDay[1]);
          
          const timeStr = dateParts[2];
          const [timePart, ampm] = timeStr.split(' ');
          const [hours, minutes] = timePart.split(':');
          const isPM = ampm === 'PM';
          
          const date = new Date();
          date.setMonth(month);
          date.setDate(day);
          date.setHours(
            isPM && hours !== '12' ? parseInt(hours) + 12 : (hours === '12' && !isPM ? 0 : parseInt(hours)),
            parseInt(minutes),
            0,
            0
          );
          return date;
        }
      } catch (error) {
        console.error('Error parsing timestamp:', error);
      }
      
      // If parsing fails, return a date object for the timestamp
      // This is a fallback that will include the activity in the list
      return new Date();
    }
  };
  
  // Helper function to convert month name to month number (0-11)
  const monthToNumber = (monthName) => {
    const months = {
      'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
      'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
    };
    return months[monthName] || 0;
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
  
  // NEW: Function to show toggle confirmation dialog
  const showToggleConfirmation = () => {
    // Only show confirmation dialog if user is trying to change the current state
    showToggleConfirmationDialog.value = true
  }
  
  // NEW: Function to confirm and execute water pump toggle
//   const confirmToggleWaterPump = async () => {
//     try {
//       // Toggle the state
//       waterPumpActive.value = !waterPumpActive.value
      
//       console.log('Toggling water pump to:', waterPumpActive.value ? 'ON' : 'OFF')
      
//       // Get current timestamp
//       const now = new Date()
//       const formattedTime = now.toLocaleString('en-US', {
//         weekday: 'short',
//         month: 'short',
//         day: 'numeric',
//         hour: '2-digit',
//         minute: '2-digit',
//         hour12: true
//       })
      
//       // Create the status document with all required fields
//       const statusData = {
//         status: waterPumpActive.value,
//         timestamp: serverTimestamp(), // Use serverTimestamp for consistent server-side timestamps
//         device_id: 'main_motor',
//         user: 'system',
//         formattedTime: formattedTime
//       }
      
//       console.log('Saving data to Firebase motor_status collection:', statusData)
      
//       // Save current status to a specific document
//       await setDoc(doc(db, 'motor_status', 'current'), statusData)
//       console.log('Successfully saved current status to Firebase')
      
//       // Also add to history collection
//       const historyRef = collection(db, 'motor_status', 'history', 'logs')
//       await addDoc(historyRef, statusData)
//       console.log('Successfully added to history logs')
      
//       // Update the activity log in the UI
//       const newActivity = {
//         status: waterPumpActive.value,
//         timestamp: `Today, ${now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
//       }
      
//       // Add to the beginning of the array
//       motorActivities.value.unshift(newActivity)
      
//       // Keep only the most recent activities (no need to limit here as we'll filter in the computed property)
      
//       // Show success toast
//       showToastMessage(`Motor turned ${waterPumpActive.value ? 'ON' : 'OFF'} successfully`)
      
//       // Close the confirmation dialog
//       showToggleConfirmationDialog.value = false
      
//     } catch (error) {
//       console.error('Error saving motor status to Firebase:', error)
//       // Show detailed error information for debugging
//       console.error('Error details:', {
//         code: error.code,
//         message: error.message,
//         stack: error.stack
//       })
      
//       // Revert the state if there was an error
//       waterPumpActive.value = !waterPumpActive.value
//       showToastMessage('Error saving motor status. Please check console for details.')
      
//       // Close the confirmation dialog
//       showToggleConfirmationDialog.value = false

//      // Send motor status to FastAPI backend
//     try {
//     const response = await axios.post('http://localhost:8000/api/motor-status/', {
//         status: waterPumpActive.value,
//         device_id: 'main_motor',
//         user: 'system',
//         timestamp: now.toISOString(),
//         formatted_time: formattedTime
//     })

//     console.log('Motor status sent to FastAPI backend:', response.data)
//     } catch (error) {
//     console.error('Error sending motor status to FastAPI:', error)
//     }

//     }
//   }
  
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
      const response = await axios.post('http://localhost:8000/api/motor-status/', {
        status: waterPumpActive.value,
        device_id: 'main_motor',
        user: 'system',
        timestamp: now.toISOString(),
        formatted_time: formattedTime
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
          // Only include activities from the last 7 days
          if (data.timestamp && data.timestamp.toDate() >= sevenDaysAgo) {
            activities.push({
              status: data.status,
              timestamp: data.formattedTime || formatTimestamp(data.timestamp)
            })
          }
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
  
  // Function to fetch watering schedules from Firebase
  const fetchWateringSchedules = async () => {
    try {
      console.log('Fetching watering schedules from Firebase...')
      isLoadingSchedules.value = true
      isLoadingNextWatering.value = true
      
      // Reference to the watering_schedules collection
      const schedulesRef = collection(db, 'watering_schedules')
      const schedulesQuery = query(schedulesRef, orderBy('createdAt', 'desc'))
      
      const schedulesSnapshot = await getDocs(schedulesQuery)
      
      const schedules = []
      schedulesSnapshot.forEach(doc => {
        const data = doc.data()
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
          scheduledTime: data.scheduledTime || null
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
    }
  }
  
  // Function to calculate the next watering time from the database
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
          nextWateringTime.value = nextWateringData.dateTime
        } else {
          // If no future schedules found, check for recurring schedules that need to be adjusted
          let closestSchedule = null
          let nextDate = null
          
          // Process each schedule to find the next occurrence
          savedSchedules.value.forEach(schedule => {
            let scheduleDate = null
            
            // Extract time from the dateTime field
            const timeMatch = schedule.dateTime.match(/(\d+):(\d+)\s+(AM|PM)/)
            if (!timeMatch) return
            
            let hour = parseInt(timeMatch[1])
            const minute = parseInt(timeMatch[2])
            const ampm = timeMatch[3]
            
            // Convert to 24-hour format
            if (ampm === 'PM' && hour < 12) hour += 12
            if (ampm === 'AM' && hour === 12) hour = 0
            
            // Handle different schedule modes
            if (schedule.mode === 'daily') {
              // For daily schedules, set to tomorrow if today's time has passed
              scheduleDate = new Date()
              scheduleDate.setHours(hour, minute, 0, 0)
              
              if (scheduleDate < now) {
                scheduleDate.setDate(scheduleDate.getDate() + 1)
              }
            } else if (schedule.mode === 'weekly' && schedule.days) {
              // For weekly schedules, find the next occurrence
              const currentDay = now.getDay() // 0 = Sunday, 1 = Monday, etc.
              const adjustedCurrentDay = currentDay === 0 ? 6 : currentDay - 1 // Convert to 0 = Monday, 6 = Sunday
              
              // Check if there's a watering day enabled
              if (!schedule.days.some(day => day)) return
              
              // Find the next watering day
              let daysToAdd = 0
              let foundNextDay = false
              
              for (let i = 0; i < 7; i++) {
                const checkDay = (adjustedCurrentDay + i) % 7
                if (schedule.days[checkDay]) {
                  daysToAdd = i
                  foundNextDay = true
                  break
                }
              }
              
              if (!foundNextDay) return
              
              scheduleDate = new Date()
              scheduleDate.setDate(now.getDate() + daysToAdd)
              scheduleDate.setHours(hour, minute, 0, 0)
              
              // If today is the day but time has passed, find the next occurrence
              if (daysToAdd === 0 && scheduleDate < now) {
                // Look for the next enabled day
                for (let i = 1; i < 7; i++) {
                  const checkDay = (adjustedCurrentDay + i) % 7
                  if (schedule.days[checkDay]) {
                    scheduleDate.setDate(now.getDate() + i)
                    break
                  }
                }
              }
            } else if (schedule.mode === 'custom' && schedule.interval) {
              // For custom schedules, calculate the next occurrence based on interval
              const dateMatch = schedule.dateTime.match(/([A-Za-z]+),\s+([A-Za-z]+)\s+(\d+)/)
              if (!dateMatch) return
              
              const monthName = dateMatch[2]
              const day = parseInt(dateMatch[3])
              
              const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
              const monthIndex = months.findIndex(m => m === monthName)
              
              if (monthIndex === -1) return
              
              // Start with the base date from the schedule
              scheduleDate = new Date(new Date().getFullYear(), monthIndex, day, hour, minute, 0, 0)
              
              // If the date is in the past, add intervals until it's in the future
              while (scheduleDate < now) {
                if (schedule.interval.unit === 'hours') {
                  scheduleDate.setHours(scheduleDate.getHours() + schedule.interval.value)
                } else if (schedule.interval.unit === 'days') {
                  scheduleDate.setDate(scheduleDate.getDate() + schedule.interval.value)
                } else if (schedule.interval.unit === 'weeks') {
                  scheduleDate.setDate(scheduleDate.getDate() + (schedule.interval.value * 7))
                }
              }
            } else if (schedule.mode === 'one-time') {
              // For one-time schedules, parse the date
              const dateMatch = schedule.dateTime.match(/([A-Za-z]+),\s+([A-Za-z]+)\s+(\d+)/)
              if (!dateMatch) return
              
              const monthName = dateMatch[2]
              const day = parseInt(dateMatch[3])
              
              const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
              const monthIndex = months.findIndex(m => m === monthName)
              
              if (monthIndex === -1) return
              
              scheduleDate = new Date(new Date().getFullYear(), monthIndex, day, hour, minute, 0, 0)
              
              // Skip if it's in the past
              if (scheduleDate < now) return
            }
            
            // Update the closest schedule if this one is sooner
            if (scheduleDate && (!nextDate || scheduleDate < nextDate)) {
              nextDate = scheduleDate
              closestSchedule = schedule
            }
          })
          
          if (nextDate) {
            // Format the date for display
            nextWateringTime.value = nextDate.toLocaleString('en-US', {
              weekday: 'short',
              month: 'short',
              day: 'numeric',
              hour: '2-digit',
              minute: '2-digit',
              hour12: true
            })
          } else {
            nextWateringTime.value = 'No upcoming waterings'
          }
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
  
  // Function to format Firestore timestamp
  const formatTimestamp = (timestamp) => {
    if (!timestamp) return ''
  
    const date = timestamp.toDate()
    const now = new Date()
    const yesterday = new Date(now)
    yesterday.setDate(yesterday.getDate() - 1)
  
    // Check if it's today
    if (date.toDateString() === now.toDateString()) {
      return `Today, ${date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
    }
  
    // Check if it's yesterday
    if (date.toDateString() === yesterday.toDateString()) {
      return `Yesterday, ${date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`
    }
  
    // Otherwise return the full date
    return date.toLocaleString([], {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
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
  
  // COMPLETELY REWRITTEN: Save or update watering schedule
  const saveWateringSchedule = async () => {
    try {
      console.log("Starting saveWateringSchedule with current values:");
      console.log(`Hour: ${wateringHour.value}, Minute: ${wateringMinute.value}, isAm: ${isAm.value}`);
      
      // Create scheduled time as a timestamp for easier querying
      const scheduledTime = new Date();
  
      if (wateringMode.value === 'one-time') {
        // Use the selected date for one-time schedules
        scheduledTime.setFullYear(
>>>>>>> cy
          selectedDate.value.getFullYear(),
          selectedDate.value.getMonth(),
          selectedDate.value.getDate()
        );
      }
<<<<<<< HEAD
      
      // Set the time part
      timeDate.setHours(hour24, wateringMinute.value, 0, 0);
      
      // Format with explicit AM/PM
      const formattedTime = timeDate.toLocaleString('en-US', {
        weekday: 'short',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
      });
      
      console.log(`Formatted time for Firebase: ${formattedTime}`);
      return formattedTime;
    })();

    // Create a new schedule object with all the data
    const scheduleData = {
      dateTime: formattedDateTime,
      duration: wateringDuration.value,
      mode: wateringMode.value,
      days: [...wateringDays.value], // Create a copy of the array
      skipIfRain: skipIfRain.value,
      notifyWatering: notifyWatering.value,
      waterFlowRate: waterFlowRate.value,
      interval:
        wateringMode.value === 'custom'
          ? {
              value: wateringInterval.value,
              unit: wateringIntervalUnit.value,
            }
          : null,
      updatedAt: serverTimestamp(),
      // Add a scheduled time as a numeric timestamp for easier querying
      scheduledTime: scheduledTime.getTime(),
    };

    console.log('Saving schedule to Firebase:', scheduleData);
    console.log(`DateTime being saved: ${scheduleData.dateTime}`);

    // If editing, update existing schedule
    if (editingScheduleId.value) {
      // Update in Firebase - only update the fields we have in scheduleData
      await updateDoc(doc(db, 'watering_schedules', editingScheduleId.value), scheduleData);

      // Update in local array
      if (editingScheduleIndex.value !== null) {
        // Preserve the original createdAt when updating the local array
        const originalCreatedAt = savedSchedules.value[editingScheduleIndex.value].createdAt;

        savedSchedules.value[editingScheduleIndex.value] = {
          ...scheduleData,
          id: editingScheduleId.value,
          createdAt: originalCreatedAt, // Keep the original createdAt
        };
      }

      showToastMessage('Schedule updated successfully');
    } else {
      // Add createdAt only for new schedules
      const newScheduleData = {
        ...scheduleData,
        createdAt: serverTimestamp(),
      };

      // Add new schedule to Firebase
      const docRef = await addDoc(collection(db, 'watering_schedules'), newScheduleData);

      // Add to local array with the document ID
      savedSchedules.value.push({
        ...newScheduleData,
        id: docRef.id,
      });

      showToastMessage('New schedule saved successfully');
    }

    // Recalculate next watering time
    await calculateNextWateringTime();

    // Close the modal after saving
    closeScheduleModal();
  } catch (error) {
    console.error('Error saving watering schedule:', error);
    showToastMessage('Error saving schedule. Please try again.');
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
  if (timerInterval) clearInterval(timerInterval)
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
  transition: all 0.3s ease;
}

@keyframes glow {
  from {
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
  }
  to {
    filter: drop-shadow(0 0 12px rgba(255, 255, 255, 0.9));
  }
}

@keyframes pulse-animation {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 0.3;
  }
  100% {
    opacity: 0;
  }
}

.pulse-animation {
  animation: pulse-animation 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* Animation for page transitions */
.animate-fadeIn {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
=======
  
      // CRITICAL FIX: Properly convert 12-hour format to 24-hour format
      let hour24 = wateringHour.value;
      
      // Debug the current state
      console.log(`Before conversion - hour24: ${hour24}, isAm: ${isAm.value}`);
      
      // Handle 12 AM special case
      if (isAm.value && hour24 === 12) {
        hour24 = 0;
      } 
      // Handle PM conversion (except 12 PM which stays as 12)
      else if (!isAm.value && hour24 < 12) {
        hour24 = hour24 + 12;
      }
      
      console.log(`After conversion - hour24: ${hour24}, isAm: ${isAm.value}`);
      
      // Set the time component
      scheduledTime.setHours(hour24, wateringMinute.value, 0, 0);
      
      // Format the time string for display
      const formattedDateTime = (() => {
        const timeDate = new Date();
        
        // Set the date part if it's a one-time schedule
        if (wateringMode.value === 'one-time') {
          timeDate.setFullYear(
            selectedDate.value.getFullYear(),
            selectedDate.value.getMonth(),
            selectedDate.value.getDate()
          );
        }
        
        // Set the time part
        timeDate.setHours(hour24, wateringMinute.value, 0, 0);
        
        // Format with explicit AM/PM
        const formattedTime = timeDate.toLocaleString('en-US', {
          weekday: 'short',
          month: 'short',
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit',
          hour12: true
        });
        
        console.log(`Formatted time for Firebase: ${formattedTime}`);
        return formattedTime;
      })();
  
      // Create a new schedule object with all the data
      const scheduleData = {
        dateTime: formattedDateTime,
        duration: wateringDuration.value,
        mode: wateringMode.value,
        days: [...wateringDays.value], // Create a copy of the array
        skipIfRain: skipIfRain.value,
        notifyWatering: notifyWatering.value,
        waterFlowRate: waterFlowRate.value,
        interval:
          wateringMode.value === 'custom'
            ? {
                value: wateringInterval.value,
                unit: wateringIntervalUnit.value,
              }
            : null,
        updatedAt: serverTimestamp(),
        // Add a scheduled time as a numeric timestamp for easier querying
        scheduledTime: scheduledTime.getTime(),
      };
  
      console.log('Saving schedule to Firebase:', scheduleData);
      console.log(`DateTime being saved: ${scheduleData.dateTime}`);
  
      // If editing, update existing schedule
      if (editingScheduleId.value) {
        // Update in Firebase - only update the fields we have in scheduleData
        await updateDoc(doc(db, 'watering_schedules', editingScheduleId.value), scheduleData);
  
        // Update in local array
        if (editingScheduleIndex.value !== null) {
          // Preserve the original createdAt when updating the local array
          const originalCreatedAt = savedSchedules.value[editingScheduleIndex.value].createdAt;
  
          savedSchedules.value[editingScheduleIndex.value] = {
            ...scheduleData,
            id: editingScheduleId.value,
            createdAt: originalCreatedAt, // Keep the original createdAt
          };
        }
  
        showToastMessage('Schedule updated successfully');
      } else {
        // Add createdAt only for new schedules
        const newScheduleData = {
          ...scheduleData,
          createdAt: serverTimestamp(),
        };
  
        // Add new schedule to Firebase
        const docRef = await addDoc(collection(db, 'watering_schedules'), newScheduleData);
  
        // Add to local array with the document ID
        savedSchedules.value.push({
          ...newScheduleData,
          id: docRef.id,
        });
  
        showToastMessage('New schedule saved successfully');
      }
  
      // Recalculate next watering time
      await calculateNextWateringTime();
  
      // Close the modal after saving
      closeScheduleModal();
    } catch (error) {
      console.error('Error saving watering schedule:', error);
      showToastMessage('Error saving schedule. Please try again.');
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
  })
  
  onUnmounted(() => {
    if (toastTimeout.value) clearTimeout(toastTimeout.value)
    if (timerInterval) clearInterval(timerInterval)
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
    transition: all 0.3s ease;
  }
  
  @keyframes glow {
    from {
      filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
    }
    to {
      filter: drop-shadow(0 0 12px rgba(255, 255, 255, 0.9));
    }
  }
  
  @keyframes pulse-animation {
    0% {
      opacity: 0;
    }
    50% {
      opacity: 0.3;
    }
    100% {
      opacity: 0;
    }
  }
  
  .pulse-animation {
    animation: pulse-animation 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }
  </style>
>>>>>>> cy
