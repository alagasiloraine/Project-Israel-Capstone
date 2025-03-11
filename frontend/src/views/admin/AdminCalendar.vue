<template>
  <div class="min-h-screen bg-gray-100 max-w-[2000px] mx-auto">
    <AdminHeader />
    <!-- Main container with fixed width to match navbar -->
    <div class="w-full px-4 py-4">
      <div class="bg-white rounded-xl shadow-sm h-full overflow-hidden">
        <!-- Main content area with scrollable content -->
        <div class="flex h-full overflow-auto">
          <!-- Sidebar with fixed height -->
          <div class="w-72 bg-gradient-to-b from-[#00A76F] to-[#00A76F]/90 text-white relative rounded-r-3xl shadow-xl flex-shrink-0">
            <!-- User Profile -->
            <div class="p-4 border-b border-white/10">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="relative group">
                    <img 
                      :src="profilePicture"
                      alt="Profile"
                      class="w-10 h-10 rounded-full cursor-pointer"
                    />
                    <div class="absolute inset-0 bg-black bg-opacity-50 rounded-full opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity">
                      <label class="cursor-pointer">
                        <input 
                          type="file" 
                          class="hidden" 
                          @change="handleProfilePictureChange" 
                          accept="image/*"
                        />
                        <CameraIcon class="w-5 h-5 text-white" />
                      </label>
                    </div>
                    <span class="absolute -top-1 -right-1 w-4 h-4 bg-[#00A76F] rounded-full border-2 border-white/30"></span>
                  </div>
                  <div class="flex-1">
                    <h3 class="font-medium text-white">Admin 1 Profile </h3>
                    <p class="text-sm text-white/70">Admin 1</p>
                  </div>
                </div>
                <div class="flex gap-2">
                  <button 
                    @click="showNotifications = !showNotifications"
                    class="p-2 hover:bg-white/10 rounded-lg relative transition-colors"
                  >
                    <BellIcon class="w-5 h-5" />
                    <span class="absolute -top-1 -right-1 w-4 h-4 bg-red-500 rounded-full text-xs flex items-center justify-center">3</span>
                  </button>
                  <!-- <div class="relative">
                    <button 
                      @click="showSettingsDropdown = !showSettingsDropdown"
                      class="p-2 hover:bg-white/10 rounded-lg transition-colors"
                    >
                      <Settings2Icon class="w-5 h-5" />
                    </button>
                    <div v-if="showSettingsDropdown" 
                         class="absolute right-0 mt-2 w-48 bg-[#00A76F] rounded-lg shadow-lg p-2 z-50">
                      <a href="/profile" class="block px-4 py-2 text-sm hover:bg-white/10 rounded-lg transition-colors">
                        Edit Profile
                      </a>
                      <button @click="handleLogout" 
                              class="block w-full text-left px-4 py-2 text-sm hover:bg-white/10 rounded-lg text-red-400 transition-colors">
                        Logout
                      </button>
                    </div>
                  </div> -->
                </div>
              </div>
            </div>
        
            <!-- Mini Calendar -->
            <div class="p-4 border border-white/10 rounded-lg mx-4 mt-4 bg-white/5">
              <div class="flex items-center justify-between mb-4">
                <h2 class="text-lg font-medium">{{ miniCalendarMonth }} {{ miniCalendarYear }}</h2>
                <div class="flex gap-1">
                  <button class="p-1 hover:bg-white/10 rounded-lg transition-colors" @click="navigateMonth(-1)">
                    <ChevronLeftIcon class="w-4 h-4" />
                  </button>
                  <button class="p-1 hover:bg-white/10 rounded-lg transition-colors" @click="navigateMonth(1)">
                    <ChevronRightIcon class="w-4 h-4" />
                  </button>
                </div>
              </div>
        
              <div class="grid grid-cols-7 text-center text-sm">
                <div v-for="day in ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']" 
                     :key="day" 
                     class="py-1 text-white/50">
                  {{ day }}
                </div>
        
                <template v-for="date in calendarDays" :key="date.value">
                  <button 
                    :class="[
                      'p-1 rounded-full hover:bg-white/20 transition-colors',
                      date.isToday ? 'bg-white/20' : '',
                      date.isSelected ? 'bg-[#FFA500]' : '',
                      date.isCurrentMonth ? 'text-white' : 'text-white/30',
                      'text-sm'
                    ]"
                    @click="selectMiniCalendarDate(date)"
                  >
                    {{ date.day }}
                  </button>
                </template>
              </div>
            </div>
        
            <!-- My Tasks -->
            <div class="p-4 border border-white/10 rounded-lg mx-4 mt-4 bg-white/5">
              <div class="flex items-center justify-between mb-4">
                <h2 class="font-medium">My Tasks</h2>
                <button @click="showTasks = !showTasks">
                  <ChevronDownIcon class="w-5 h-5 text-white/50" :class="{ 'transform rotate-180': showTasks }" />
                </button>
              </div>
              <div v-show="showTasks" class="space-y-3">
                <div v-for="task in tasks" :key="task.id" class="flex items-center gap-3 cursor-pointer group">
                  <input 
                    type="checkbox" 
                    v-model="task.completed" 
                    class="rounded border-white/30 text-[#00A76F] focus:ring-[#00A76F] bg-white/10" 
                  />
                  <span :class="{ 'line-through': task.completed }">{{ task.title }}</span>
                  <div class="flex items-center ml-auto">
                    <span 
                      class="w-5 h-5 rounded-full block mr-2"
                      :class="task.completed ? 'bg-[#00A76F]' : 'bg-[#FFA500]'"
                    ></span>
                    <button @click="viewTask(task)" class="p-1 hover:bg-white/10 rounded-full transition-colors">
                      <EyeIcon class="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        
          <!-- Main Calendar Content with scrollable area -->
          <div class="flex-1 flex flex-col overflow-auto">
            <!-- Calendar Header stays fixed -->
            <div class="p-6 bg-white sticky top-0 z-10">
              <div class="flex flex-col space-y-6">
                <div class="flex items-center justify-between">
                  <h1 class="text-3xl font-medium text-gray-900">{{ currentMonth }} {{ currentDay }}, {{ currentYear }}</h1>
                  
                  <!-- Month/Week/Day buttons section -->
                  <div class="flex items-center space-x-4">
                    <div class="bg-gray-100 rounded-2xl inline-flex p-1">
                      <div class="relative">
                        <button 
                          :class="[
                            'px-8 py-2 rounded-xl text-sm font-medium transition-colors',
                            currentView === 'month' 
                              ? 'bg-white shadow-sm text-gray-900' 
                              : 'text-gray-600 hover:bg-gray-50'
                          ]"
                          @click="toggleMonthDropdown"
                        >
                          Month
                        </button>
                        <!-- Month Dropdown -->
                        <div v-if="showMonthDropdown" 
                             class="absolute top-full mt-1 w-48 bg-white rounded-lg shadow-lg py-1 z-50">
                          <button 
                            v-for="(month, index) in months" 
                            :key="month"
                            class="w-full px-4 py-2 text-left text-sm hover:bg-gray-50"
                            @click="selectMonth(index)"
                          >
                            {{ month }}
                          </button>
                        </div>
                      </div>
                      <button 
                        :class="[
                          'px-8 py-2 rounded-xl text-sm font-medium transition-colors',
                          currentView === 'week' 
                            ? 'bg-white shadow-sm text-gray-900' 
                            : 'text-gray-600 hover:bg-gray-50'
                        ]"
                        @click="goToFirstWeek"
                      >
                        Week
                      </button>
                      <button 
                        :class="[
                          'px-8 py-2 rounded-xl text-sm font-medium transition-colors',
                          currentView === 'day' 
                            ? 'bg-white shadow-sm text-gray-900' 
                            : 'text-gray-600 hover:bg-gray-50'
                        ]"
                        @click="goToMiniCalendarDate"
                      >
                        Day
                      </button>
                    </div>
                  </div>
        
                  <div class="flex items-center space-x-2">
                    <button class="p-2 rounded-lg bg-gray-100 hover:bg-gray-200 transition-colors" @click="navigateDate(-1)">
                      <ChevronLeftIcon class="w-5 h-5" />
                    </button>
                    <button class="px-4 py-2 rounded-lg bg-[#00A76F] text-white hover:bg-[#00A76F]/90 transition-colors" @click="goToToday">
                      Today
                    </button>
                    <button class="p-2 rounded-lg bg-gray-100 hover:bg-gray-200 transition-colors" @click="navigateDate(1)">
                      <ChevronRightIcon class="w-5 h-5" />
                    </button>
                  </div>
                </div>
        
                <!-- Calendar Days -->
                <div class="flex items-center">
                  <CalendarIcon class="w-6 h-6 text-gray-400 mr-4" />
                  <div class="grid grid-cols-7 gap-4 flex-1">
                    <div 
                      v-for="(day, index) in weekDays" 
                      :key="index"
                      class="border border-gray-200 rounded-xl p-4 cursor-pointer transition-colors"
                      :class="{'bg-[#00A76F] text-white': selectedDay === day.date, 'hover:bg-[#FFA500] hover:text-white': selectedDay !== day.date}"
                      @click="selectDay(day)"
                    >
                      <div class="text-sm font-medium mb-1">{{ day.name }}</div>
                      <div class="text-[32px] font-medium">{{ day.date }}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        
            <!-- Scrollable calendar content -->
            <div class="flex-1 overflow-auto">
              <!-- Time Grid -->
              <div class="grid grid-cols-[50px_1fr] divide-x h-[540px] overflow-y-auto">
                <!-- Time Labels -->
                <div class="divide-y">
                  <div 
                    v-for="hour in timeSlots" 
                    :key="hour"
                    class="h-16 p-2 text-xs text-gray-500 sticky left-0 bg-white"
                  >
                    {{ formatHour(hour) }}
                  </div>
                </div>
        
                <!-- Events Grid -->
                <div class="divide-y">
                  <div 
                    v-for="hour in timeSlots" 
                    :key="hour"
                    class="h-16 grid grid-cols-7 divide-x"
                  >
                    <div 
                      v-for="day in 7" 
                      :key="day"
                      class="relative group"
                      @mouseenter="!hasEventsInTimeSlot(hour, day) && hoverCell(hour, day)"
                      @mouseleave="clearHover()"
                    >
                      <!-- Hover Grid with Dashed Lines and Add Button -->
                      <div 
                        v-if="hoveredCell.hour === hour && hoveredCell.day === day && !hasEventsInTimeSlot(hour, day)"
                        class="absolute inset-0 border-2 border-dashed border-green-500 rounded-md z-10 transition-all duration-200"
                      >
                        <!-- Add Button -->
                        <button 
                          @click.stop="openAddEventModal(hour, day)"
                          class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-8 h-8 bg-green-500 hover:bg-green-600 text-white rounded-full flex items-center justify-center shadow-md transition-all duration-200"
                        >
                          <PlusIcon class="w-5 h-5" />
                        </button>
                      </div>
        
                      <!-- Event Block -->
                      <template v-for="event in getEventsForTimeSlot(hour, day)" :key="event.id">
                        <div 
                          :style="{
                            top: `${getEventOffset(event)}px`,
                            height: `${getEventHeight(event)}px`,
                            backgroundColor: event.color + '15',
                            borderColor: event.color
                          }"
                          class="absolute left-1 right-1 rounded-xl p-2 border-l-4 flex flex-col gap-1 z-20 cursor-pointer hover:shadow-md transition-shadow"
                          @click="showEventDetailsModal(event)"
                        >
                          <div class="text-xs font-medium">{{ event.title }}</div>
                          <div class="text-xs text-gray-500">
                            {{ formatEventTime(event) }}
                          </div>
                          <div class="flex -space-x-2">
                            <img 
                              v-for="staff in event.staff.slice(0, 3)" 
                              :key="staff.id"
                              :src="staff.avatar"
                              :alt="staff.name"
                              class="w-5 h-5 rounded-full border-2 border-white"
                            />
                          </div>
                        </div>
                      </template>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Event Details Modal -->
    <div 
      v-if="showEventDetails"
      class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center"
      @click="showEventDetails = false"
    >
      <div class="bg-white rounded-xl p-6 w-full max-w-md mx-4 text-gray-900" @click.stop>
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-xl font-bold">{{ isEditing ? 'Edit Event' : 'Task Details' }}</h2>
          <button @click="showEventDetails = false">
            <XIcon class="w-6 h-6" />
          </button>
        </div>
        
        <div class="space-y-4">
          <div>
            <h3 v-if="!isEditing" class="font-medium text-lg">{{ currentTask.title }}</h3>
            <input
              v-else
              v-model="editingTask.title"
              type="text"
              class="w-full px-3 py-2 border rounded-lg"
              placeholder="Event title"
            />
            <p class="text-gray-500">12:00 - 13:30</p>
          </div>

          <div>
            <h4 class="text-sm font-medium text-gray-700 mb-2">Staff In Charge</h4>
            <div v-if="!isEditing" class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg">
              <img 
                src="/images/tg1.jpg"
                alt="Staff"
                class="w-10 h-10 rounded-full"
              />
              <div>
                <p class="font-medium">Staff 1- Profile</p>
                <p class="text-sm text-gray-500">Staff 1</p>
              </div>
            </div>
            <div v-else class="space-y-2">
              <div class="flex flex-wrap gap-2">
                <div 
                  v-for="staff in editingTask.staff" 
                  :key="staff.id"
                  class="flex items-center gap-2 bg-gray-100 px-2 py-1 rounded-md"
                >
                  <img 
                    :src="staff.avatar"
                    :alt="staff.name"
                    class="w-6 h-6 rounded-full"
                  />
                  <span class="text-sm">{{ staff.name }}</span>
                  <button @click="removeStaffFromEdit(staff.id)" class="text-gray-500 hover:text-gray-700">
                    <XIcon class="w-4 h-4" />
                  </button>
                </div>
              </div>
              <button 
                @click="showStaffModal = true"
                class="text-sm text-[#00A76F] hover:text-[#00A76F]/80"
              >
                + Add Staff
              </button>
            </div>
          </div>

          <div>
            <h4 class="text-sm font-medium text-gray-700 mb-2">Description</h4>
            <p v-if="!isEditing" class="text-gray-600">
              {{ currentTask.description || 'Meeting to discuss the new library management system implementation and timeline.' }}
            </p>
            <textarea
              v-else
              v-model="editingTask.description"
              class="w-full px-3 py-2 border rounded-lg"
              rows="3"
              placeholder="Enter event description"
            ></textarea>
          </div>

          <div>
            <h4 class="text-sm font-medium text-gray-700 mb-2">Plot</h4>
            <div v-if="!isEditing" class="text-gray-600">Plot {{ currentTask.plot || '1' }}</div>
            <select
              v-else
              v-model="editingTask.plot"
              class="w-full px-3 py-2 border rounded-lg"
            >
              <option value="1">Plot 1</option>
              <option value="2">Plot 2</option>
              <option value="3">Plot 3</option>
            </select>
          </div>

          <div class="flex justify-end gap-2">
            <button 
              v-if="!isEditing"
              @click="startEditing"
              class="px-4 py-2 bg-[#00A76F] text-white rounded-lg hover:bg-[#00A76F]/90 transition-colors"
            >
              Edit Details
            </button>
            <template v-else>
              <button 
                @click="cancelEditing"
                class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors"
              >
                Cancel
              </button>
              <button 
                @click="saveEditing"
                class="px-4 py-2 bg-[#00A76F] text-white rounded-lg hover:bg-[#00A76F]/90 transition-colors"
              >
                Save Changes
              </button>
            </template>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Event Modal Backdrop -->
    <div 
      v-if="showAddEventModal"
      class="fixed inset-0 bg-black/50 backdrop-blur-sm z-[100]"
      @click="showAddEventModal = false"
    />

    <!-- Add Event Modal Content -->
    <div 
      v-if="showAddEventModal"
      class="fixed inset-0 flex items-center justify-center z-[100]"
      @click.stop
    >
      <div class="bg-white rounded-xl p-6 w-full max-w-md mx-4 shadow-xl">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-xl font-semibold text-gray-800">Add New Task</h2>
          <button @click="closeAddEventModal" class="hover:bg-gray-100 p-2 rounded-lg transition-colors">
            <XIcon class="w-5 h-5" />
          </button>
        </div>
      
        <div class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Task Title
            </label>
            <input 
              v-model="newEvent.title"
              type="text"
              class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent"
              placeholder="Enter task title"
            />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Start Time
              </label>
              <select 
                v-model="newEvent.startHour"
                class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent bg-white"
              >
                <option v-for="hour in timeSlots" :key="hour" :value="hour">
                  {{ formatHour(hour) }}
                </option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Duration
              </label>
              <select 
                v-model="newEvent.duration"
                class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent bg-white"
              >
                <option v-for="n in 8" :key="n" :value="n">
                  {{ n }} {{ n === 1 ? 'hour' : 'hours' }}
                </option>
              </select>
            </div>
          </div>

          <!-- Staff Members Selection -->
          <div class="relative">
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Staff Members
            </label>
            <div 
              class="w-full px-4 py-2.5 border border-gray-200 rounded-lg flex items-center justify-between cursor-pointer hover:border-[#00A76F]"
              @click="openStaffModal"
            >
              <span class="text-gray-500">
                {{ selectedStaffDisplay || 'Select staff members' }}
              </span>
              <span class="text-[#00A76F] font-medium hover:text-[#00A76F]/80 transition-colors">
                + Add Staff
              </span>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Choose Color
            </label>
            <div class="flex gap-3">
              <button
                v-for="color in eventColors"
                :key="color.name"
                :class="[
                  'w-8 h-8 rounded-full border-2 transition-all duration-200',
                  newEvent.color === color.value ? 'border-gray-900 scale-110' : 'border-transparent hover:scale-110'
                ]"
                :style="{
                  backgroundColor: color.value,
                  opacity: newEvent.color === color.value ? 1 : 0.5
                }"
                @click="newEvent.color = color.value"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Details
            </label>
            <textarea 
              v-model="newEvent.details"
              class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent"
              rows="3"
              placeholder="Enter event details"
            ></textarea>
          </div>

          <div class="flex justify-end gap-3 pt-2">
            <button 
              @click="closeAddEventModal"
              class="px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition-colors"
            >
              Cancel
            </button>
            <button 
              @click="addEvent"
              class="px-4 py-2 bg-[#00A76F] text-white rounded-lg hover:bg-[#00A76F]/90 transition-colors"
            >
              Add Task
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Staff Selection Modal -->
    <div v-if="showStaffModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-[200]">
      <div class="bg-white rounded-lg shadow-xl w-full max-w-md p-6" @click.stop>
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-medium">Select Staff</h3>
          <button @click="showStaffModal = false" class="text-gray-500 hover:text-gray-700">
            <XIcon class="w-5 h-5" />
          </button>
        </div>
        
        <div class="mb-4">
          <input 
            type="text"
            v-model="staffSearchQuery"
            placeholder="Search staff..."
            class="w-full px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent"
          />
        </div>
        
        <div class="max-h-60 overflow-y-auto">
          <div 
            v-for="staff in filteredAvailableStaff" 
            :key="staff.id"
            class="flex items-center p-3 rounded-lg cursor-pointer transition-colors"
            :class="modalSelectedStaff.some(s => s.id === staff.id) ? 'bg-gray-100' : 'hover:bg-gray-100'"
            @click="selectStaff(staff)"
          >
            <img 
              :src="staff.avatar"
              :alt="staff.name"
              class="w-10 h-10 rounded-full mr-3"
            />
            <div>
              <div class="font-medium">{{ staff.name }}</div>
              <div class="text-sm text-gray-500">{{ staff.role }}</div>
            </div>
          </div>
        </div>
        
        <div class="mt-4 flex justify-end">
          <button 
            @click="closeStaffModal"
            class="px-4 py-2 bg-[#00A76F] text-white rounded-lg hover:bg-[#00A76F]/90 transition-colors"
          >
            Done
          </button>
        </div>
      </div>
    </div>

    <!-- Notification Modal -->
    <div 
      v-if="showNotifications" 
      class="fixed inset-y-0 right-0 w-96 bg-white shadow-lg transform transition-transform duration-300 ease-in-out z-50"
      :class="showNotifications ? 'translate-x-0' : 'translate-x-full'"
    >
      <div class="h-full flex flex-col">
        <div class="p-6 border-b border-gray-200">
          <div class="flex items-center justify-between">
            <h2 class="text-lg font-semibold text-gray-900">Notifications</h2>
            <button 
              @click="showNotifications = false"
              class="text-gray-500 hover:text-gray-700"
            >
              <X class="h-5 w-5" />
            </button>
          </div>
        </div>
        
        <div class="flex-1 overflow-y-auto p-6">
          <div class="space-y-4">
            <!-- Water Level Alert -->
            <div class="bg-red-50 border-l-4 border-red-500 p-4 rounded-r-lg">
              <div class="flex items-center">
                <AlertTriangle class="h-5 w-5 text-red-500 mr-2" />
                <div>
                  <h3 class="text-sm font-medium text-red-800">Water Level Alert</h3>
                  <p class="text-sm text-red-700 mt-1">Water level is critically low in Plot A</p>
                  <p class="text-xs text-red-600 mt-1">2 minutes ago</p>
                </div>
              </div>
            </div>

            <!-- Motor Toggle Notification -->
            <div class="bg-blue-50 border-l-4 border-blue-500 p-4 rounded-r-lg">
              <div class="flex items-center">
                <Activity class="h-5 w-5 text-blue-500 mr-2" />
                <div>
                  <h3 class="text-sm font-medium text-blue-800">System Update</h3>
                  <p class="text-sm text-blue-700 mt-1">Staff John Smith toggled motor ON in Plot B</p>
                  <p class="text-xs text-blue-600 mt-1">5 minutes ago</p>
                </div>
              </div>
            </div>

            <!-- Task Completion -->
            <div class="bg-green-50 border-l-4 border-green-500 p-4 rounded-r-lg">
              <div class="flex items-center">
                <CheckCircle class="h-5 w-5 text-green-500 mr-2" />
                <div>
                  <h3 class="text-sm font-medium text-green-800">Task Completed</h3>
                  <p class="text-sm text-green-700 mt-1">Daily water level check completed by Maria Garcia</p>
                  <p class="text-xs text-green-600 mt-1">15 minutes ago</p>
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
import { ref, computed, onMounted } from 'vue'
import { 
  ChevronLeftIcon, 
  ChevronRightIcon, 
  ChevronDownIcon,
  PlusIcon, 
  XIcon,
  CalendarIcon,
  BellIcon,
  Settings2Icon,
  CameraIcon,
  EyeIcon,
  AlertTriangle,
  Activity,
  CheckCircle,
  X
} from 'lucide-vue-next'
import AdminHeader from './AdminHeader.vue'

// Profile related
const profilePicture = ref('/images/tg1.jpg')
const showSettingsDropdown = ref(false)
const showNotifications = ref(false)

// Calendar state
const currentView = ref('week')
const miniCalendarDate = ref(new Date())
const selectedDate = ref(null)
const selectedDay = ref(new Date().getDate().toString())
const showAddEventModal = ref(false)
const showStaffModal = ref(false)
const staffSearchQuery = ref('')

// Add this to the reactive variables section
const modalSelectedStaff = ref([])

// Update the newEvent object to include staff
const newEvent = ref({
  title: '',
  startHour: null,
  duration: 1,
  color: '#00A76F',
  details: '',
  day: null,
  staff: []
})

// Hover state for calendar cells
const hoveredCell = ref({ hour: null, day: null })

// Other reactive variables
const showTasks = ref(true)
const showEventDetails = ref(false)
const isEditing = ref(false)
const editingTask = ref({
  title: '',
  description: '',
  plot: '1',
  staff: []
})

const tasks = ref([
  { id: 1, title: 'Assign Task', completed: false },
  { id: 2, title: 'Add Staff Profile', completed: true },
  { id: 3, title: 'Check Report', completed: false }
])

const weekDays = ref([
  { name: 'Sunday', date: '16' },
  { name: 'Monday', date: '17' },
  { name: 'Tuesday', date: '18' },
  { name: 'Wednesday', date: '19' },
  
])

const timeSlots = ref(Array.from({ length: 13 }, (_, i) => i + 5)) // 5 AM to 5 PM
const events = ref([]) // Start with empty events array

const eventColors = [
  { name: 'Green', value: '#00A76F' },
  { name: 'Blue', value: '#60A5FA' },
  { name: 'Purple', value: '#8B5CF6' },
  { name: 'Yellow', value: '#FBBF24' },
  { name: 'Pink', value: '#EC4899' }
]

const availableStaff = [
  { id: 1, name: 'John Doe', role: 'Manager', avatar: '/images/tg1.jpg' },
  { id: 2, name: 'Jane Smith', role: 'Assistant', avatar: '/images/tg1.jpg' },
  { id: 3, name: 'Mike Johnson', role: 'Supervisor', avatar: '/images/tg1.jpg' },
  { id: 4, name: 'Sarah Williams', role: 'Staff', avatar: '/images/tg1.jpg' },
  { id: 5, name: 'David Brown', role: 'Staff', avatar: '/images/tg1.jpg' }
]

// Add to reactive variables
const showMonthDropdown = ref(false)
const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
]

// Computed properties
const miniCalendarMonth = computed(() => miniCalendarDate.value.toLocaleString('default', { month: 'long' }))
const miniCalendarYear = computed(() => miniCalendarDate.value.getFullYear())
const currentMonth = computed(() => miniCalendarDate.value.toLocaleString('default', { month: 'long' }))
const currentYear = computed(() => miniCalendarDate.value.getFullYear())
const currentDay = computed(() => miniCalendarDate.value.getDate())

const currentTask = computed(() => ({
  title: 'Water Level',
  description: 'Check the water Level for Plot 1',
  plot: '1',
  staff: [availableStaff[0]]
}))

const filteredAvailableStaff = computed(() => {
  if (!staffSearchQuery.value) return availableStaff
  
  const query = staffSearchQuery.value.toLowerCase()
  return availableStaff.filter(staff => 
    staff.name.toLowerCase().includes(query) || 
    staff.role.toLowerCase().includes(query)
  )
})

const selectedStaffDisplay = computed(() => {
  if (newEvent.value.staff.length === 0) return ''
  return newEvent.value.staff.map(staff => staff.name).join(', ')
})

const calendarDays = computed(() => {
  const year = miniCalendarDate.value.getFullYear()
  const month = miniCalendarDate.value.getMonth()

  const firstDay = new Date(year, month, 1)
  const lastDay = new Date(year, month + 1, 0)

  const days = []

  const firstDayOfWeek = firstDay.getDay() || 7
  for (let i = firstDayOfWeek - 1; i > 0; i--) {
    const date = new Date(year, month, 1 - i)
    days.push({
      day: date.getDate(),
      value: date,
      isCurrentMonth: false,
      isToday: isSameDay(date, new Date()),
      isSelected: selectedDate.value && isSameDay(date, selectedDate.value)
    })
  }

  for (let i = 1; i <= lastDay.getDate(); i++) {
    const date = new Date(year, month, i)
    days.push({
      day: i,
      value: date,
      isCurrentMonth: true,
      isToday: isSameDay(date, new Date()),
      isSelected: selectedDate.value && isSameDay(date, selectedDate.value)
    })
  }

  const remainingDays = 42 - days.length
  for (let i = 1; i <= remainingDays; i++) {
    const date = new Date(year, month + 1, i)
    days.push({
      day: i,
      value: date,
      isCurrentMonth: false,
      isToday: isSameDay(date, new Date()),
      isSelected: selectedDate.value && isSameDay(date, selectedDate.value)
    })
  }

  return days
})

// Methods
const handleProfilePictureChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      profilePicture.value = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const handleLogout = () => {
  // Implement logout logic here
  console.log('Logging out...')
}

const navigateMonth = (direction) => {
  miniCalendarDate.value = new Date(
    miniCalendarDate.value.getFullYear(),
    miniCalendarDate.value.getMonth() + direction,
    1
  )
  updateMainCalendar()
}

const navigateDate = (direction) => {
  miniCalendarDate.value = new Date(
    miniCalendarDate.value.getFullYear(),
    miniCalendarDate.value.getMonth(),
    miniCalendarDate.value.getDate() + direction
  )
  updateMainCalendar()
}

const updateMainCalendar = () => {
  selectedDay.value = miniCalendarDate.value.getDate().toString()
  updateWeekDays()
}

const updateWeekDays = () => {
  const currentDate = new Date(miniCalendarDate.value)
  const dayOfWeek = currentDate.getDay()
  const diff = currentDate.getDate() - dayOfWeek + (dayOfWeek === 0 ? -6 : 1)
  const monday = new Date(currentDate.setDate(diff))

  weekDays.value = Array.from({ length: 7 }, (_, i) => {
    const date = new Date(monday)
    date.setDate(monday.getDate() + i)
    return {
      name: date.toLocaleString('default', { weekday: 'long' }),
      date: date.getDate().toString()
    }
  })
}

const selectMiniCalendarDate = (date) => {
  selectedDate.value = date.value
  miniCalendarDate.value = new Date(date.value)
  updateMainCalendar()
}

const selectDay = (day) => {
  selectedDay.value = day.date
  const newDate = new Date(
    miniCalendarDate.value.getFullYear(),
    miniCalendarDate.value.getMonth(),
    parseInt(day.date)
  )
  miniCalendarDate.value = newDate
  selectedDate.value = newDate // This will highlight the date in mini calendar
}

const goToToday = () => {
  miniCalendarDate.value = new Date()
  updateMainCalendar()
}

const isSameDay = (date1, date2) => {
  return date1.getDate() === date2.getDate() &&
         date1.getMonth() === date2.getMonth() &&
         date1.getFullYear() === date2.getFullYear()
}

const formatHour = (hour) => {
  return `${hour % 12 || 12}:00 ${hour >= 12 ? 'PM' : 'AM'}`
}

// Hover cell methods
const hoverCell = (hour, day) => {
  hoveredCell.value = { hour, day }
}

const clearHover = () => {
  hoveredCell.value = { hour: null, day: null }
}

const openAddEventModal = (hour, day) => {
  newEvent.value.startHour = hour
  newEvent.value.day = day
  showAddEventModal.value = true
}

const closeAddEventModal = () => {
  showAddEventModal.value = false
  newEvent.value = {
    title: '',
    startHour: null,
    duration: 1,
    color: '#00A76F',
    details: '',
    day: null,
    staff: []
  }
}

const addEvent = () => {
  const event = {
    id: Date.now(),
    title: newEvent.value.title,
    startHour: newEvent.value.startHour,
    duration: newEvent.value.duration,
    day: newEvent.value.day,
    color: newEvent.value.color,
    details: newEvent.value.details,
    staff: newEvent.value.staff
  }

  events.value.push(event)  
  closeAddEventModal()
}

// Update the selectStaff function
const selectStaff = (staff) => {
  const index = modalSelectedStaff.value.findIndex(s => s.id === staff.id)
  
  if (index === -1) {
    modalSelectedStaff.value.push(staff)
  } else {
    modalSelectedStaff.value.splice(index, 1)
  }
}

// Add a new function to handle closing the staff modal
const closeStaffModal = () => {
  newEvent.value.staff = [...modalSelectedStaff.value]
  showStaffModal.value = false
  modalSelectedStaff.value = []
}

// Update the openStaffModal function
const openStaffModal = () => {
  modalSelectedStaff.value = [...newEvent.value.staff]
  showStaffModal.value = true
}

const removeStaffFromEdit = (staffId) => {
  editingTask.value.staff = editingTask.value.staff.filter(staff => staff.id !== staffId)
}

const getEventsForTimeSlot = (hour, day) => {
  return events.value.filter(event => {
    const eventEnd = event.startHour + event.duration
    return event.day === day && hour >= event.startHour && hour < eventEnd
  })
}

const getEventOffset = (event) => {
  const minutes = (event.startHour % 1) * 60
  return (minutes / 60) * 64 // 64px is the height of one hour (h-16)
}

const getEventHeight = (event) => {
  return (event.duration * 64) - 4 // 64px per hour, minus 4px for spacing
}

const formatEventTime = (event) => {
  const start = formatHour(event.startHour)
  const end = formatHour(event.startHour + event.duration)
  return `${start} - ${end}`
}

const viewTask = (task) => {
  // Handle navigation based on task type
  switch (task.title) {
    case 'Add Staff Profile':
      window.location.href = '/staff-management'
      break
    case 'Assign Task':
      window.location.href = '/calendar'
      break
    case 'Check Report':
      window.location.href = '/reports'
      break
    default:
      window.location.href = '/tasks/' + task.id
  }
}

const startEditing = () => {
  editingTask.value = {
    title: currentTask.value.title,
    description: currentTask.value.description || '',
    plot: currentTask.value.plot || '',
    staff: [...(currentTask.value.staff || [])]
  }
  isEditing.value = true
}

const cancelEditing = () => {
  isEditing.value = false
  editingTask.value = {
    title: '',
    description: '',
    plot: '1',
    staff: []
  }
}

const saveEditing = () => {
  // Update the current task with edited values
  currentTask.value = {
    ...currentTask.value,
    ...editingTask.value
  }
  isEditing.value = false
}

const hasEventsInTimeSlot = (hour, day) => {
  return getEventsForTimeSlot(hour, day).length > 0
}

const showEventDetailsModal = (event) => {
  // Update current task with event details
  currentTask.value = {
    title: event.title,
    description: event.details,
    plot: '1', // You can add a plot property to events if needed
    staff: event.staff
  }
  showEventDetails.value = true
}

const toggleMonthDropdown = () => {
  showMonthDropdown.value = !showMonthDropdown.value
  currentView.value = 'month'
}

const selectMonth = (monthIndex) => {
  const newDate = new Date(miniCalendarDate.value)
  newDate.setMonth(monthIndex)
  miniCalendarDate.value = newDate
  showMonthDropdown.value = false
  updateMainCalendar()
}

const goToFirstWeek = () => {
  const newDate = new Date(miniCalendarDate.value)
  newDate.setDate(1)
  miniCalendarDate.value = newDate
  currentView.value = 'week'
  updateMainCalendar()
}

const goToMiniCalendarDate = () => {
  miniCalendarDate.value = new Date(selectedDate.value || new Date())
  currentView.value = 'day'
  updateMainCalendar()
}

// Add click outside handler to close month dropdown
onMounted(() => {
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.month-dropdown')) {
      showMonthDropdown.value = false
    }
  })
  
  // Initialize the calendar
  updateWeekDays()
})
</script>

<style>
/* Update styles to handle overflow properly */
.time-grid {
  height: 100%;
  overflow-y: auto;
}

.event-block {
  position: absolute;
  left: 0;
  right: 0;
  z-index: 10;
  margin: 1px;
  border-radius: 1rem;
  padding: 0.5rem;
}

button {
  transition: all 0.2s;
}

.time-grid {
  height: 500px;
  overflow-y: auto;
}

/* Dropdown animations */
.settings-dropdown-enter-active,
.settings-dropdown-leave-active {
  transition: all 0.2s ease;
}

.settings-dropdown-enter-from,
.settings-dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Profile picture hover effect */
.profile-picture-hover {
  transition: opacity 0.2s ease;
}

.group:hover .profile-picture-hover {
  opacity: 1;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Apply Poppins font to everything */
* {
  font-family: 'Poppins', sans-serif;
}

/* Fix modal styling */
.modal-input {
  @apply w-full px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent;
}

.modal-label {
  @apply block text-sm font-medium text-gray-600 mb-2;
}

.modal-select {
  @apply w-full px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent bg-white;
}

/* Add these styles to the <style> section */
.modal-input,
.modal-select,
input[type="text"],
select,
textarea {
  @apply w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#00A76F] focus:border-transparent;
  font-family: 'Poppins', sans-serif;
}

.modal-label {
  @apply block text-sm font-medium text-gray-700 mb-2;
  font-family: 'Poppins', sans-serif;
}

/* Ensure modals are always on top */
.fixed {
  z-index: 100;
}

/* Add smooth transitions */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 200ms;
}

/* Add this new style for color selection */
.color-button {
  transition: all 0.3s ease;
}

/* Hover grid styles */
.group:hover .hover-grid {
  opacity: 1;
}

/* Add button animation */
@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(0, 167, 111, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(0, 167, 111, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(0, 167, 111, 0);
  }
}

.pulse {
  animation: pulse 2s infinite;
}
</style>

