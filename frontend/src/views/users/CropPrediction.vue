<template>
    <div class="flex h-screen bg-[#f8f9fa] font-poppins">
      <!-- Sidebar -->
      <Sidebar />
  
      <!-- Main Content -->
      <div class="flex-1 flex flex-col overflow-hidden">
        <div class="flex-1 overflow-auto bg-gradient-to-br from-green-50 to-emerald-50 p-6 relative">
          <!-- Background Pattern -->
          <!-- <div class="absolute inset-0 pattern-dots pattern-green-500 pattern-bg-white pattern-size-2 pattern-opacity-5"></div> -->
        
          <!-- Main Content -->
          <div class="max-w-2xl mx-auto bg-white rounded-3xl shadow-xl p-8 relative z-10 mt-12">
            <!-- Logo -->
            <div class="flex flex-col items-center mb-8">
              <img 
                src="/images/project-israel-logo-removebg-preview.png"
                alt="Project Israel" 
                class="w-24 h-24 object-contain mb-4"
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
                      <h3 class="text-4xl font-bold text-green-600 mb-4">Chickpea</h3>
                      <p class="text-gray-600">
                        This crop has a 99.68% chance of success based on your soil composition.
                      </p>
                    </div>
  
                    <!-- Success Rate Card -->
                    <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm">
                      <div class="flex items-center gap-3 text-green-600 font-medium mb-4">
                        <TrendingUp class="h-6 w-6" />
                        <span class="text-lg">Success Rate</span>
                      </div>
                      <div class="flex items-end gap-2">
                        <div class="text-5xl font-bold text-green-600">99.68</div>
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
                        <div class="p-4 rounded-xl bg-gray-50 border border-gray-100">
                          <div class="flex items-center justify-between">
                            <span class="text-lg font-medium text-gray-700">Watermelon</span>
                            <span class="text-sm font-medium text-gray-500">0.31%</span>
                          </div>
                          <div class="mt-2 h-2 w-full bg-gray-200 rounded-full overflow-hidden">
                            <div class="h-full bg-green-500 rounded-full" style="width: 0.31%"></div>
                          </div>
                        </div>
                        <div class="p-4 rounded-xl bg-gray-50 border border-gray-100">
                          <div class="flex items-center justify-between">
                            <span class="text-lg font-medium text-gray-700">Coffee</span>
                            <span class="text-sm font-medium text-gray-500">0.01%</span>
                          </div>
                          <div class="mt-2 h-2 w-full bg-gray-200 rounded-full overflow-hidden">
                            <div class="h-full bg-green-500 rounded-full" style="width: 0.01%"></div>
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
    </div>
  </template>
    
  <script setup>
  import { ref } from 'vue'
  import { 
    Home,
    Beaker,
    Droplet,
    Waves,
    Thermometer,
    Cloud,
    Sprout,
    X,
    TrendingUp,
    List
  } from 'lucide-vue-next'
  import Sidebar from './Sidebar.vue'
  
  const showModal = ref(false)
  const formData = ref({
    nitrogen: '',
    phosphorus: '',
    potassium: '',
    ph: '',
    moisture: '',
    temperature: '',
    humidity: ''
  })
  
  const submitForm = () => {
    showModal.value = true
  }
  
  const closeModal = () => {
    showModal.value = false
  }
  </script>
    
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
  /* Pattern Background */
  .pattern-dots {
    background-image: radial-gradient(currentColor 1px, transparent 1px);
    background-size: calc(10 * 1px) calc(10 * 1px);
  }
  
  /* Add smooth scrollbar for modal content */
  .modal-content {
    scrollbar-width: thin;
    scrollbar-color: rgba(156, 163, 175, 0.5) transparent;
  }
  
  .modal-content::-webkit-scrollbar {
    width: 6px;
  }
  
  .modal-content::-webkit-scrollbar-track {
    background: transparent;
  }
  
  .modal-content::-webkit-scrollbar-thumb {
    background-color: rgba(156, 163, 175, 0.5);
    border-radius: 3px;
  }
  </style>