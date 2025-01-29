<template>
  <div class="flex h-screen bg-[#f8f9fa] font-poppins">
    <Sidebar />

    <!-- Main Content -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <div class="flex-1 overflow-auto bg-gradient-to-br from-green-50 to-emerald-50 p-6 relative">
        
    <!-- Stats Section -->
    <div class="grid grid-cols-4 gap-6 mb-6 ml-[20px]">
        <!-- Total Predictions Card -->
        <div class="bg-white rounded-lg p-4 shadow hover:shadow-md transition-all duration-300 relative overflow-hidden border border-gray-100">
          <div class="flex justify-between items-start mb-2">
            <div class="text-xs text-gray-500">Total Predictions</div>
            <ChartBar class="w-6 h-6 text-purple-500" />
          </div>
          <div>
            <div class="text-2xl font-bold text-gray-900">1,248</div>
            <div class="text-green-600 text-sm font-medium mt-1">+12.5%</div>
          </div>
          <div class="absolute bottom-0 left-0 right-0 h-0.5 bg-purple-500"></div>
        </div>

        <!-- Planted Card -->
        <div class="bg-white rounded-lg p-4 shadow hover:shadow-md transition-all duration-300 relative overflow-hidden border border-gray-100">
          <div class="flex justify-between items-start mb-2">
            <div class="text-xs text-gray-500">Planted</div>
            <TrendingUp class="w-6 h-6 text-green-500" />
          </div>
          <div>
            <div class="text-2xl font-bold text-green-600">856</div>
            <div class="text-green-600 text-sm font-medium mt-1">+5.2%</div>
          </div>
          <div class="absolute bottom-0 left-0 right-0 h-0.5 bg-green-500"></div>
        </div>

        <!-- Success Rate Card -->
        <div class="bg-white rounded-lg p-4 shadow hover:shadow-md transition-all duration-300 relative overflow-hidden border border-gray-100">
          <div class="flex justify-between items-start mb-2">
            <div class="text-xs text-gray-500">Success Rate</div>
            <Activity class="w-6 h-6 text-blue-500" />
          </div>
          <div>
            <div class="text-2xl font-bold text-blue-600">92.4%</div>
            <div class="text-green-600 text-sm font-medium mt-1">+3.1%</div>
          </div>
          <div class="absolute bottom-0 left-0 right-0 h-0.5 bg-blue-500"></div>
        </div>

        <!-- Ongoing Card -->
        <div class="bg-white rounded-lg p-4 shadow hover:shadow-md transition-all duration-300 relative overflow-hidden border border-gray-100">
          <div class="flex justify-between items-start mb-2">
            <div class="text-xs text-gray-500">Ongoing</div>
            <ClipboardList class="w-6 h-6 text-orange-500" />
          </div>
          <div>
            <div class="text-2xl font-bold text-orange-600">234</div>
            <div class="text-red-600 text-sm font-medium mt-1">-8.2%</div>
          </div>
          <div class="absolute bottom-0 left-0 right-0 h-0.5 bg-orange-500"></div>
        </div>
      </div>

        <div class="flex gap-8">
          <!-- Prediction Form -->
          <div class="w-[700px] bg-white rounded-3xl shadow-xl p-8 relative z-10 mb-16 ml-[50px]">
            <!-- Logo -->
            <div class="flex flex-col items-center mb-4 p-1">
              <img 
                src="/images/project-israel-logo-removebg-preview.png"
                alt="Project Israel" 
                class="w-24 h-24 object-contain mt-[-25px]"
              />
              <h1 class="text-3xl font-bold text-green-500 mb-2">Crop Prediction</h1>
              <p class="text-gray-600 text-center">
                Enter your soil parameters to get personalized crop recommendations for your farm.
              </p>
            </div>

            <!-- Form Container -->
            <div class="bg-green-50 rounded-2xl p-6 shadow-inner">
              <form @submit.prevent="submitForm" class="space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- Nitrogen Level -->
                  <div class="space-y-2">
                    <label class="flex items-center text-gray-700 font-medium">
                      <Beaker class="w-5 h-5 text-green-500 mr-2" />
                      Nitrogen (N) Level
                    </label>
                    <input 
                      v-model="formData.nitrogen"
                      type="text"
                      readonly
                      class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
                      placeholder="96.01"
                    />
                  </div>

                  <!-- Phosphorus Level -->
                  <div class="space-y-2">
                    <label class="flex items-center text-gray-700 font-medium">
                      <Beaker class="w-5 h-5 text-green-500 mr-2" />
                      Phosphorus (P) Level
                    </label>
                    <input 
                      v-model="formData.phosphorus"
                      type="text"
                      readonly
                      class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
                      placeholder="22.85"
                    />
                  </div>

                  <!-- Potassium Level -->
                  <div class="space-y-2">
                    <label class="flex items-center text-gray-700 font-medium">
                      <Beaker class="w-5 h-5 text-green-500 mr-2" />
                      Potassium (K) Level
                    </label>
                    <input 
                      v-model="formData.potassium"
                      type="text"
                      readonly
                      class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
                      placeholder="87.04"
                    />
                  </div>

                  <!-- Soil pH Level -->
                  <div class="space-y-2">
                    <label class="flex items-center text-gray-700 font-medium">
                      <Droplet class="w-5 h-5 text-green-500 mr-2" />
                      Soil pH Level
                    </label>
                    <input 
                      v-model="formData.ph"
                      type="text"
                      readonly
                      class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
                      placeholder="7.22"
                    />
                  </div>

                  <!-- Soil Moisture -->
                  <div class="space-y-2">
                    <label class="flex items-center text-gray-700 font-medium">
                      <Waves class="w-5 h-5 text-green-500 mr-2" />
                      Soil Moisture
                    </label>
                    <input 
                      v-model="formData.moisture"
                      type="text"
                      readonly
                      class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
                      placeholder="45.00"
                    />
                  </div>

                  <!-- Temperature -->
                  <div class="space-y-2">
                    <label class="flex items-center text-gray-700 font-medium">
                      <Thermometer class="w-5 h-5 text-green-500 mr-2" />
                      Temperature
                    </label>
                    <input 
                      v-model="formData.temperature"
                      type="text"
                      readonly
                      class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
                      placeholder="32.52"
                    />
                  </div>

                  <!-- Humidity -->
                  <div class="space-y-2">
                    <label class="flex items-center text-gray-700 font-medium">
                      <Cloud class="w-5 h-5 text-green-500 mr-2" />
                      Humidity
                    </label>
                    <input 
                      v-model="formData.humidity"
                      type="text"
                      readonly
                      class="w-full px-4 py-2 rounded-lg border border-gray-200 bg-white focus:border-green-500 focus:ring-2 focus:ring-green-200 transition-all"
                      placeholder="76.68"
                    />
                  </div>
                </div>

                <!-- Submit Button -->
                <button 
                  type="submit"
                  class="w-full bg-green-500 hover:bg-green-600 text-white font-medium py-3 rounded-lg transition-colors flex items-center justify-center space-x-2 mt-8"
                >
                  <Sprout class="w-5 h-5" />
                  <span>Get Crop Recommendations</span>
                </button>
              </form>
            </div>
          </div>

          <!-- New Table Section -->
          <div class="w-[750px] bg-white rounded-xl shadow-xl p-6 mb-16 mr-[40px]">
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

            <div class="mb-6">
              <Pagination />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Recommendation Modal -->
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
        <!-- Backdrop -->
        <div class="fixed inset-0 bg-black/30 backdrop-blur-sm"></div>
        
        <!-- Modal Container -->
        <div class="flex min-h-full items-center justify-center p-4 ml-[220px]">
          <div 
            class="relative w-full max-w-4xl transform rounded-2xl bg-white p-6 text-left shadow-xl transition-all"
            @click.stop
          >
            <!-- Close Button -->
            <button 
              @click="closeModal"
              class="absolute right-4 top-4 rounded-full p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-600 transition-all"
            >
              <X class="h-6 w-6" />
            </button>

            <!-- Modal Header -->
            <div class="text-center mb-8">
              <h2 class="text-3xl font-bold text-gray-800 mb-2">Crop Recommendations</h2>
              <p class="text-gray-600">Based on your soil parameters</p>
            </div>

            <!-- Main Content Grid -->
            <div class="grid md:grid-cols-2 gap-6">
              <!-- Left Column - Recommended Crop -->
              <div class="space-y-6">
                <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-8 border border-green-100">
                  <div class="flex items-center gap-3 text-green-600 font-medium mb-4">
                    <Sprout class="h-6 w-6" />
                    <span class="text-lg">Recommended Crop</span>
                  </div>
                  <h3 class="text-4xl font-bold text-green-600 mb-4">{{ recommendedCrop }}</h3>
                  <p class="text-gray-600">
                    This crop has a {{ successRate }}% chance of success based on your soil composition.
                  </p>
                </div>

                <!-- Success Rate Card -->
                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm">
                  <div class="flex items-center gap-3 text-green-600 font-medium mb-4">
                    <TrendingUp class="h-6 w-6" />
                    <span class="text-lg">Success Rate</span>
                  </div>
                  <div class="flex items-end gap-2">
                    <div class="text-5xl font-bold text-green-600">{{ successRate }}</div>
                    <div class="text-2xl text-green-600 mb-1">%</div>
                  </div>
                  <p class="text-sm text-gray-500 mt-2">
                    Predicted success rate based on soil analysis
                  </p>
                </div>
              </div>

              <!-- Right Column -->
              <div class="space-y-6">
                <!-- Alternative Options -->
                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm h-full">
                  <div class="flex items-center gap-3 text-green-600 font-medium mb-6">
                    <List class="h-6 w-6" />
                    <span class="text-lg">Alternative Options</span>
                  </div>
                  <div class="space-y-4">
                    <div v-for="option in alternativeOptions" :key="option.crop" class="p-4 rounded-xl bg-gray-50 border border-gray-100">
                      <div class="flex items-center justify-between">
                        <span class="text-lg font-medium text-gray-700">{{ option.crop }}</span>
                        <span class="text-sm font-medium text-gray-500">{{ option.successRate }}%</span>
                      </div>
                      <div class="mt-2 h-2 w-full bg-gray-200 rounded-full overflow-hidden">
                        <div class="h-full bg-green-500 rounded-full" :style="{ width: `${option.successRate}%` }"></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import Pagination from './Pagination.vue'
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
  LayoutGrid
} from 'lucide-vue-next'
import Sidebar from './Sidebar.vue'

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
  { crop: 'Watermelon', successRate: 0.31 },
  { crop: 'Coffee', successRate: 0.01 }
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
  },

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

const totalPredictions = computed(() => filteredPredictions.value.length)
const totalPages = computed(() => Math.ceil(totalPredictions.value / itemsPerPage.value))

const paginatedPredictions = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return filteredPredictions.value.slice(start, end)
})

const paginationStart = computed(() => (currentPage.value - 1) * itemsPerPage.value + 1)
const paginationEnd = computed(() => Math.min(currentPage.value * itemsPerPage.value, totalPredictions.value))

const displayedPages = computed(() => {
  const pages = []
  for (let i = 1; i <= totalPages.value; i++) {
    if (i === 1 || i === totalPages.value || (i >= currentPage.value - 1 && i <= currentPage.value + 1)) {
      pages.push(i)
    }
  }
  return pages
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
</style>

