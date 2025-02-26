<template>
  <div class="min-h-screen bg-green-100 font-poppins">
    <Sidebar />
    <!-- Main Content -->
    <main class="min-h-screen bg-green-100">
      <!-- Fixed Navbar Space - matches navbar height -->
      <div class="h-[100px]"></div>
      
      <!-- Container Wrapper with increased spacing and animations -->
      <div class="w-full px-6 pt-14">
        <!-- Main Container with enhanced styling -->
        <div class="bg-white rounded-[12px] shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-200 h-[calc(100vh-180px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_8px_40px_rgb(0,0,0,0.06)]">
          <!-- Content Wrapper with improved padding -->
          <div class="p-8">
            <!-- Stats Section with adjusted sizes -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
              <!-- Total Predictions Card -->
              <div class="bg-white rounded-lg p-4 shadow-sm transition-all duration-300 border-2 border-purple-200 hover:border-purple-600 hover:shadow-md">
                <div class="flex justify-between items-start mb-1">
                  <div class="text-xs text-gray-500">Total Predictions</div>
                  <ChartBar class="w-5 h-5 text-purple-500" />
                </div>
                <div>
                  <div class="text-2xl font-bold text-gray-900">1,248</div>
                  <div class="text-green-600 text-xs font-medium mt-0.5">+12.5%</div>
                </div>
              </div>
  
              <!-- Planted Card -->
              <div class="bg-white rounded-lg p-4 shadow-sm transition-all duration-300 border-2 border-green-200 hover:border-green-600 hover:shadow-md">
                <div class="flex justify-between items-start mb-1">
                  <div class="text-xs text-gray-500">Planted</div>
                  <TrendingUp class="w-5 h-5 text-green-500" />
                </div>
                <div>
                  <div class="text-2xl font-bold text-gray-900">856</div>
                  <div class="text-green-600 text-xs font-medium mt-0.5">+5.2%</div>
                </div>
              </div>
  
              <!-- Success Rate Card -->
              <div class="bg-white rounded-lg p-4 shadow-sm transition-all duration-300 border-2 border-blue-200 hover:border-blue-600 hover:shadow-md">
                <div class="flex justify-between items-start mb-1">
                  <div class="text-xs text-gray-500">Success Rate</div>
                  <Activity class="w-5 h-5 text-blue-500" />
                </div>
                <div>
                  <div class="text-2xl font-bold text-gray-900">92.4%</div>
                  <div class="text-green-600 text-xs font-medium mt-0.5">+3.1%</div>
                </div>
              </div>
  
              <!-- Ongoing Card -->
              <div class="bg-white rounded-lg p-4 shadow-sm transition-all duration-300 border-2 border-red-200 hover:border-red-600 hover:shadow-md">
                <div class="flex justify-between items-start mb-1">
                  <div class="text-xs text-gray-500">Ongoing</div>
                  <ClipboardList class="w-5 h-5 text-red-500" />
                </div>
                <div>
                  <div class="text-2xl font-bold text-gray-900">234</div>
                  <div class="text-red-600 text-xs font-medium mt-0.5">-8.2%</div>
                </div>
              </div>
            </div>
  
            <!-- Main Content Area -->
            <div class="grid grid-cols-1 xl:grid-cols-2 gap-8">
              <!-- Modified Prediction Form -->
              <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-xl shadow-lg p-6">
                <!-- Updated Header with smaller title and subtext -->
                <div class="mb-6 text-center">
                  <h2 class="text-2xl font-bold text-green-600 mb-2">
                    Crop Recommendations
                  </h2>
                  <p class="text-sm text-gray-600">
                    Data updates in real-time based on sensor readings
                  </p>
                  <div class="w-16 h-1 bg-green-500 mx-auto rounded-full mt-3"></div>
                </div>
  
                <!-- Form Container with enhanced styling -->
                <div class="space-y-4">
                  <!-- Grid Layout for Form Fields -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <!-- Nitrogen Level -->
                    <div class="bg-white rounded-lg p-3 shadow-sm border border-green-100 hover:border-green-300 transition-all">
                      <label class="flex items-center text-gray-700 text-sm font-medium mb-1.5">
                        <Beaker class="w-4 h-4 text-green-500 mr-2" />
                        Nitrogen (N) Level
                      </label>
                      <input 
                        v-model="formData.nitrogen"
                        type="text"
                        readonly
                        class="w-full px-3 py-1.5 rounded-lg border border-gray-100 bg-white/50 focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all text-base font-medium"
                        placeholder="96.01"
                      />
                    </div>
  
                    <!-- Phosphorus Level -->
                    <div class="bg-white rounded-lg p-3 shadow-sm border border-green-100 hover:border-green-300 transition-all">
                      <label class="flex items-center text-gray-700 text-sm font-medium mb-1.5">
                        <Beaker class="w-4 h-4 text-green-500 mr-2" />
                        Phosphorus (P) Level
                      </label>
                      <input 
                        v-model="formData.phosphorus"
                        type="text"
                        readonly
                        class="w-full px-3 py-1.5 rounded-lg border border-gray-100 bg-white/50 focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all text-base font-medium"
                        placeholder="22.85"
                      />
                    </div>
  
                    <!-- Potassium Level -->
                    <div class="bg-white rounded-lg p-3 shadow-sm border border-green-100 hover:border-green-300 transition-all">
                      <label class="flex items-center text-gray-700 text-sm font-medium mb-1.5">
                        <Beaker class="w-4 h-4 text-green-500 mr-2" />
                        Potassium (K) Level
                      </label>
                      <input 
                        v-model="formData.potassium"
                        type="text"
                        readonly
                        class="w-full px-3 py-1.5 rounded-lg border border-gray-100 bg-white/50 focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all text-base font-medium"
                        placeholder="87.04"
                      />
                    </div>
  
                    <!-- Soil pH Level -->
                    <div class="bg-white rounded-lg p-3 shadow-sm border border-green-100 hover:border-green-300 transition-all">
                      <label class="flex items-center text-gray-700 text-sm font-medium mb-1.5">
                        <Droplet class="w-4 h-4 text-green-500 mr-2" />
                        Soil pH Level
                      </label>
                      <input 
                        v-model="formData.ph"
                        type="text"
                        readonly
                        class="w-full px-3 py-1.5 rounded-lg border border-gray-100 bg-white/50 focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all text-base font-medium"
                        placeholder="7.22"
                      />
                    </div>
  
                    <!-- Soil Moisture -->
                    <div class="bg-white rounded-lg p-3 shadow-sm border border-green-100 hover:border-green-300 transition-all">
                      <label class="flex items-center text-gray-700 text-sm font-medium mb-1.5">
                        <Waves class="w-4 h-4 text-green-500 mr-2" />
                        Soil Moisture
                      </label>
                      <input 
                        v-model="formData.moisture"
                        type="text"
                        readonly
                        class="w-full px-3 py-1.5 rounded-lg border border-gray-100 bg-white/50 focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all text-base font-medium"
                        placeholder="45.00"
                      />
                    </div>
  
                    <!-- Temperature -->
                    <div class="bg-white rounded-lg p-3 shadow-sm border border-green-100 hover:border-green-300 transition-all">
                      <label class="flex items-center text-gray-700 text-sm font-medium mb-1.5">
                        <Thermometer class="w-4 h-4 text-green-500 mr-2" />
                        Temperature
                      </label>
                      <input 
                        v-model="formData.temperature"
                        type="text"
                        readonly
                        class="w-full px-3 py-1.5 rounded-lg border border-gray-100 bg-white/50 focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all text-base font-medium"
                        placeholder="32.52"
                      />
                    </div>
  
                    <!-- Humidity -->
                    <div class="bg-white rounded-lg p-3 shadow-sm border border-green-100 hover:border-green-300 transition-all">
                      <label class="flex items-center text-gray-700 text-sm font-medium mb-1.5">
                        <Cloud class="w-4 h-4 text-green-500 mr-2" />
                        Humidity
                      </label>
                      <input 
                        v-model="formData.humidity"
                        type="text"
                        readonly
                        class="w-full px-3 py-1.5 rounded-lg border border-gray-100 bg-white/50 focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all text-base font-medium"
                        placeholder="76.68"
                      />
                    </div>
                  </div>
  
                  <!-- Submit Button -->
                  <button 
                    type="submit"
                    @click="submitForm"
                    class="w-full bg-green-500 hover:bg-green-600 text-white font-medium py-3 rounded-lg transition-all flex items-center justify-center space-x-2 shadow-lg hover:shadow-xl mt-4"
                  >
                    <Sprout class="w-5 h-5" />
                    <span>Get Crop Recommendations</span>
                  </button>
                </div>
              </div>
  
              <!-- Table Section -->
              <div class="bg-white rounded-xl shadow-lg p-6">
                <!-- Filter Tabs -->
                <div class="border-b border-gray-200 mb-4">
                  <div class="flex gap-1">
                    <button 
                      v-for="filter in filters" 
                      :key="filter.name"
                      :class="[
                        'px-4 py-2 text-sm font-medium transition-colors border-b-2',
                        activeFilter === filter.name 
                          ? 'border-green-500 text-green-600' 
                          : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                      ]"
                      @click="activeFilter = filter.name"
                    >
                      {{ filter.name }}
                    </button>
                  </div>
                </div>
  
                <!-- Search and Actions -->
                <div class="flex justify-between items-center mb-4">
                  <div class="relative w-64">
                    <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
                    <input 
                      type="text"
                      v-model="searchQuery"
                      placeholder="Search predictions..."
                      class="w-full pl-10 pr-4 py-1.5 text-sm border border-gray-200 rounded-md"
                    />
                  </div>
                  <div class="flex items-center gap-2">
                    <button class="p-1.5 text-gray-500 hover:bg-gray-100 rounded-md">
                      <LayoutGrid class="h-4 w-4" />
                    </button>
                    <button class="p-1.5 text-gray-500 hover:bg-gray-100 rounded-md">
                      <Filter class="h-4 w-4" />
                    </button>
                  </div>
                </div>
  
                <!-- Table -->
                <div class="overflow-x-auto">
                  <table class="w-full">
                    <thead>
                      <tr class="border-b border-gray-200">
                        <th 
                          v-for="header in tableHeaders" 
                          :key="header.key"
                          class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                        >
                          {{ header.label }}
                        </th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-100">
                      <tr 
                        v-for="prediction in paginatedPredictions" 
                        :key="prediction.id"
                        class="hover:bg-gray-50"
                      >
                        <td class="px-4 py-2 whitespace-nowrap">
                          <div class="flex items-center">
                            <Sprout class="h-4 w-4 text-green-500 mr-2" />
                            <span class="text-sm text-gray-900">
                              {{ prediction.crop }}
                            </span>
                          </div>
                        </td>
                        <td class="px-4 py-2 whitespace-nowrap">
                          <div class="flex items-center">
                            <img 
                              :src="prediction.staffAvatar" 
                              class="h-5 w-5 rounded-full mr-2"
                            />
                            <span class="text-sm text-gray-900">
                              {{ prediction.staffName }}
                            </span>
                          </div>
                        </td>
                        <td class="px-4 py-2 whitespace-nowrap text-sm text-gray-500">
                          {{ prediction.date }}
                        </td>
                        <td class="px-4 py-2 whitespace-nowrap">
                          <span class="text-sm text-green-600">
                            {{ prediction.successRate }}%
                          </span>
                        </td>
                        <td class="px-4 py-2 whitespace-nowrap">
                          <span 
                            class="px-2 py-1 text-xs font-medium rounded-full"
                            :class="getStatusClass(prediction.status)"
                          >
                            {{ prediction.status }}
                          </span>
                        </td>
                        <td class="px-4 py-2 whitespace-nowrap text-sm text-gray-500">
                          {{ prediction.harvestDate }}
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
  
                <div class="mt-4">
                  <Pagination />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  
    <!-- Enhanced Recommendation Modal with Compact Design -->
    <Transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="transform scale-95 opacity-0"
      enter-to-class="transform scale-100 opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="transform scale-100 opacity-100"
      leave-to-class="transform scale-95 opacity-0"
    >
      <div v-if="showModal" 
           class="fixed inset-0 z-50 overflow-y-auto"
           @click="closeModal">
        <!-- Enhanced Backdrop -->
        <div class="fixed inset-0 bg-black/20 backdrop-blur-[2px]"></div>
        
        <!-- Modal Container -->
        <div class="flex min-h-full items-center justify-center p-4">
          <div 
            class="relative w-full max-w-lg transform overflow-hidden rounded-2xl bg-white p-5 text-left shadow-xl transition-all"
            @click.stop
          >
  
            <!-- Modal Header -->
            <div class="text-center mb-5">
              <h2 class="text-lg font-semibold text-gray-800">Crop Recommendations</h2>
              <p class="text-xs text-gray-500 mt-0.5">Based on your soil parameters</p>
            </div>
  
            <!-- Main Content Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Left Column -->
              <div class="space-y-4">
                <!-- Primary Recommendation -->
                <div class="bg-green-50/50 rounded-lg p-4">
                  <div class="flex items-center gap-2 text-green-600 mb-3">
                    <Sprout class="h-4 w-4" />
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
                <div class="bg-white rounded-lg p-4 border border-gray-100">
                  <div class="flex items-center gap-2 text-green-600 mb-3">
                    <TrendingUp class="h-4 w-4" />
                    <span class="text-xs font-medium">Success Metrics</span>
                  </div>
                  <div class="space-y-2">
                    <div class="flex items-center justify-between">
                      <span class="text-xs text-gray-600">Soil Compatibility</span>
                      <span class="text-xs font-medium text-gray-900">98%</span>
                    </div>
                    <div class="flex items-center justify-between">
                      <span class="text-xs text-gray-600">Growth Rate</span>
                      <span class="text-xs font-medium text-gray-900">95%</span>
                    </div>
                    <div class="flex items-center justify-between">
                      <span class="text-xs text-gray-600">Yield Potential</span>
                      <span class="text-xs font-medium text-gray-900">97%</span>
                    </div>
                  </div>
                </div>
              </div>
  
              <!-- Right Column -->
              <div class="space-y-4">
                <!-- Alternative Options -->
                <div class="bg-white rounded-lg p-4 border border-gray-100">
                  <div class="flex items-center gap-2 text-green-600 mb-3">
                    <List class="h-4 w-4" />
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
                            {{ option.successRate }}%
                          </div>
                          <div class="text-[10px] text-gray-500">Success rate</div>
                        </div>
                      </div>
                      <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                        <div 
                          class="h-full bg-green-500 rounded-full transition-all" 
                          :style="{ width: `${option.successRate}%` }"
                        ></div>
                      </div>
                    </div>
                  </div>
                </div>
  
                <!-- Crop Rotation Tip -->
                <div class="bg-green-50/50 rounded-lg p-3">
                  <div class="flex items-start gap-2">
                    <div class="mt-0.5">
                      <Info class="h-3.5 w-3.5 text-green-600" />
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
            <div class="flex justify-end gap-2 mt-5 pt-4 border-t border-gray-100">
              <button 
                @click="closeModal"
                class="px-3 py-1.5 text-xs font-medium text-gray-600 hover:text-gray-800 transition-colors"
              >
                Close
              </button>
              <button 
                class="px-3 py-1.5 bg-green-500 text-white text-xs font-medium rounded-lg hover:bg-green-600 transition-colors flex items-center gap-1.5 shadow-sm"
              >
                <Download class="h-3.5 w-3.5" />
                Save Recommendation
              </button>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { 
    ChartBar, 
    ClipboardList, 
    TrendingUp, 
    Activity,
    Beaker,
    Droplet,
    Waves,
    Thermometer,
    Cloud,
    Sprout,
    X,
    List,
    Search, 
    Filter,
    ChevronLeft,
    ChevronRight,
    LayoutGrid,
    Info,
    Download
  } from 'lucide-vue-next'
  import Sidebar from '../layout/Sidebar.vue'
  import Pagination from '../layout/Pagination.vue'
  
  // Form Data
  const formData = ref({
    nitrogen: '',
    phosphorus: '',
    potassium: '',
    ph: '',
    moisture: '',
    temperature: '',
    humidity: ''
  })
  
  const showModal = ref(false)
  const recommendedCrop = ref('Chickpea')
  const successRate = ref(99.68)
  const alternativeOptions = ref([
    { crop: 'Watermelon', successRate: 95.42 },
    { crop: 'Coffee', successRate: 92.31 }
  ])
  
  const submitForm = () => {
    showModal.value = true
  }
  
  const closeModal = () => {
    showModal.value = false
  }
  
  // Table Data
  const filters = [
    { name: 'All' },
    { name: 'Planted' },
    { name: 'Ongoing' },
    { name: 'Cancelled' },
    { name: 'Harvested' }
  ]
  
  const activeFilter = ref('All')
  const searchQuery = ref('')
  const currentPage = ref(1)
  const itemsPerPage = ref(10)
  
  const tableHeaders = [
    { key: 'crop', label: 'Recommended Crop' },
    { key: 'staff', label: 'Staff' },
    { key: 'date', label: 'Date & Time' },
    { key: 'successRate', label: 'Success Rate' },
    { key: 'status', label: 'Status' },
    { key: 'harvestDate', label: 'Harvest Date' }
  ]
  
  const predictions = ref([
    {
      id: 1,
      crop: 'Chickpea',
      staffName: 'Ellie Rose Almeda',
      staffAvatar: 'https://ui-avatars.com/api/?name=John+Doe',
      date: 'Today, 2:30 PM',
      successRate: 99.68,
      status: 'Planted',
      harvestDate: 'Mar 15, 2024'
    },
    {
      id: 2,
      crop: 'Watermelon',
      staffName: 'Cy Kean Perjes',
      staffAvatar: 'https://ui-avatars.com/api/?name=Jane+Smith',
      date: 'Today, 1:15 PM',
      successRate: 95.42,
      status: 'Ongoing',
      harvestDate: 'Mar 20, 2024'
    },
    {
      id: 3,
      crop: 'Chickpea',
      staffName: 'Loraine Alagasi',
      staffAvatar: 'https://ui-avatars.com/api/?name=Jane+Smith',
      date: 'Today, 1:15 PM',
      successRate: 95.42,
      status: 'Harvested',
      harvestDate: 'Mar 20, 2024'
    },
    {
      id: 4,
      crop: 'Rice',
      staffName: 'Alagasi Loraine',
      staffAvatar: 'https://ui-avatars.com/api/?name=Jane+Smith',
      date: 'Today, 1:15 PM',
      successRate: 95.42,
      status: 'Cancelled',
      harvestDate: 'Mar 20, 2024'
    },
    {
      id: 5,
      crop: 'Watermelon',
      staffName: 'Jamyca Manibo',
      staffAvatar: 'https://ui-avatars.com/api/?name=Jane+Smith',
      date: 'Today, 1:15 PM',
      successRate: 95.42,
      status: 'Planted',
      harvestDate: 'Mar 20, 2024'
    }
  ])
  
  const filteredPredictions = computed(() => {
    let result = predictions.value
  
    // Filter by status
    if (activeFilter.value !== 'All') {
      result = result.filter(p => p.status === activeFilter.value)
    }
  
    // Filter by search query
    if (searchQuery.value) {
      const query = searchQuery.value.toLowerCase()
      result = result.filter(p => 
        p.crop.toLowerCase().includes(query) ||
        p.staffName.toLowerCase().includes(query)
      )
    }
  
    return result
  })
  
  const paginatedPredictions = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage.value
    const end = start + itemsPerPage.value
    return filteredPredictions.value.slice(start, end)
  })
  
  const getStatusClass = (status) => {
    const classes = {
      'Planted': 'bg-green-100 text-green-700',
      'Ongoing': 'bg-blue-100 text-blue-700',
      'Cancelled': 'bg-red-100 text-red-700',
      'Harvested': 'bg-gray-100 text-gray-700'
    }
    return classes[status]
  }
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  
  /* Custom scrollbar styling */
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
  
  /* Add smooth transitions */
  * {
    transition: all 200ms ease-in-out;
  }
  
  /* Remove the shimmer animation */
  .bg-gradient-to-r {
    background-size: 100% auto;
  }
  </style>
