<template>
<div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
  <keep-alive>
    <Sidebar />
  </keep-alive>
  <!-- Main Content -->
  <main class="flex-1 flex flex-col h-screen pt-32">
    <!-- Container Wrapper with optimized spacing -->
    <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
      <!-- Main Container -->
      <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_12px_40px_rgb(0,0,0,0.12)]">
        <!-- Content Wrapper -->
        <div class="p-0">
          <!-- Header Section with Light Green Background -->
          <div class="bg-gradient-to-r from-green-50 to-emerald-50 border-b border-green-100 rounded-t-[20px] px-6 py-6">
            <div class="flex items-center justify-between">
              <div>
                <h1 class="text-2xl font-semibold text-gray-800 mb-2">Device Recalibration</h1>
                <p class="text-sm text-gray-600">Configure and calibrate your ESP32 sensor devices</p>
              </div>
              <div class="flex items-center space-x-3">
                <div class="relative">
                  <input 
                    v-model="searchQuery"
                    type="text" 
                    placeholder="Search configurations..." 
                    class="pl-9 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent w-64 text-sm bg-white"
                  >
                  <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
                </div>
                <button @click="exportConfigurations" class="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg flex items-center space-x-2 transition-colors text-sm font-medium">
                  <Download class="w-4 h-4" />
                  <span>Export All</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Main Content Area -->
          <div class="p-6">
            <!-- 3-Column ESP32 Layout with FIXED HEIGHT -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
              <!-- ESP32-1 Container - FIXED HEIGHT -->
              <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden hover:shadow-md transition-shadow h-80">
                <!-- ESP32-1 Header -->
                <div class="p-4 border-b border-gray-100 bg-gradient-to-r from-green-50 to-emerald-50">
                  <div class="flex items-start space-x-3">
                    <div class="w-10 h-10 bg-green-100 rounded-xl flex items-center justify-center flex-shrink-0">
                      <Cpu class="w-6 h-6 text-green-600" />
                    </div>
                    <div class="flex-1 min-w-0">
                      <h2 class="text-lg font-semibold text-gray-800 mb-1">ESP32-1 SENSORS</h2>
                      <p class="text-sm text-gray-600">NPK + Soil pH Monitoring</p>
                    </div>
                  </div>
                </div>
                
                <!-- ESP32-1 Content -->
                <div class="p-4 flex-1 flex flex-col justify-between">
                  <!-- Description -->
                  <div class="mb-4">
                    <div class="flex items-center space-x-2 mb-2">
                      <div class="w-6 h-6 bg-green-100 rounded-lg flex items-center justify-center">
                        <CheckCircle class="w-3 h-3 text-green-600" />
                      </div>
                      <span class="text-sm font-medium text-gray-800">Device Status</span>
                    </div>
                    <p class="text-xs text-green-600 mb-3">Online & Connected</p>
                    <p class="text-sm text-gray-600 leading-relaxed">
                      Monitor soil nutrients (NPK) and pH levels for optimal plant growth. 
                      Configure calibration values and WiFi settings for accurate readings.
                    </p>
                  </div>
                  
                  <!-- Recalibrate Button -->
                  <button 
                    @click="openModal('esp1')" 
                    class="w-full bg-green-600 hover:bg-green-700 text-white px-4 py-3 rounded-lg text-sm font-medium transition-colors flex items-center justify-center space-x-2"
                  >
                    <Settings class="w-4 h-4" />
                    <span>Recalibrate</span>
                  </button>
                </div>
              </div>

              <!-- ESP32-2 Container - FIXED HEIGHT -->
              <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden hover:shadow-md transition-shadow h-80">
                <!-- ESP32-2 Header -->
                <div class="p-4 border-b border-gray-100 bg-gradient-to-r from-blue-50 to-indigo-50">
                  <div class="flex items-start space-x-3">
                    <div class="w-10 h-10 bg-blue-100 rounded-xl flex items-center justify-center flex-shrink-0">
                      <Cloud class="w-6 h-6 text-blue-600" />
                    </div>
                    <div class="flex-1 min-w-0">
                      <h2 class="text-lg font-semibold text-gray-800 mb-1">ESP32-2 SENSORS</h2>
                      <p class="text-sm text-gray-600">Environmental Monitoring</p>
                    </div>
                  </div>
                </div>
                
                <!-- ESP32-2 Content -->
                <div class="p-4 flex-1 flex flex-col justify-between">
                  <!-- Description -->
                  <div class="mb-4">
                    <div class="flex items-center space-x-2 mb-2">
                      <div class="w-6 h-6 bg-blue-100 rounded-lg flex items-center justify-center">
                        <BarChart3 class="w-3 h-3 text-blue-600" />
                      </div>
                      <span class="text-sm font-medium text-gray-800">Device Status</span>
                    </div>
                    <p class="text-xs text-blue-600 mb-3">Online & Connected</p>
                    <p class="text-sm text-gray-600 leading-relaxed">
                      Track temperature, humidity, and soil moisture levels. 
                      Set watering thresholds and calibrate environmental sensors for precise monitoring.
                    </p>
                  </div>
                  
                  <!-- Recalibrate Button -->
                  <button 
                    @click="openModal('esp2')" 
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white px-4 py-3 rounded-lg text-sm font-medium transition-colors flex items-center justify-center space-x-2"
                  >
                    <Settings class="w-4 h-4" />
                    <span>Recalibrate</span>
                  </button>
                </div>
              </div>

              <!-- ESP32-3 Container - FIXED HEIGHT -->
              <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden hover:shadow-md transition-shadow h-80">
                <!-- ESP32-3 Header -->
                <div class="p-4 border-b border-gray-100 bg-gradient-to-r from-cyan-50 to-teal-50">
                  <div class="flex items-start space-x-3">
                    <div class="w-10 h-10 bg-cyan-100 rounded-xl flex items-center justify-center flex-shrink-0">
                      <Droplets class="w-6 h-6 text-cyan-600" />
                    </div>
                    <div class="flex-1 min-w-0">
                      <h2 class="text-lg font-semibold text-gray-800 mb-1">ESP32-3 SENSORS</h2>
                      <p class="text-sm text-gray-600">Water Level Monitoring</p>
                    </div>
                  </div>
                </div>
                
                <!-- ESP32-3 Content -->
                <div class="p-4 flex-1 flex flex-col justify-between">
                  <!-- Description -->
                  <div class="mb-4">
                    <div class="flex items-center space-x-2 mb-2">
                      <div class="w-6 h-6 bg-cyan-100 rounded-lg flex items-center justify-center">
                        <Container class="w-3 h-3 text-cyan-600" />
                      </div>
                      <span class="text-sm font-medium text-gray-800">Device Status</span>
                    </div>
                    <p class="text-xs text-cyan-600 mb-3">Online & Connected</p>
                    <p class="text-sm text-gray-600 leading-relaxed">
                      Monitor water tank levels with ultrasonic sensors. 
                      Configure tank dimensions and alert thresholds for automated water management.
                    </p>
                  </div>
                  
                  <!-- Recalibrate Button -->
                  <button 
                    @click="openModal('esp3')" 
                    class="w-full bg-cyan-600 hover:bg-cyan-700 text-white px-4 py-3 rounded-lg text-sm font-medium transition-colors flex items-center justify-center space-x-2"
                  >
                    <Settings class="w-4 h-4" />
                    <span>Recalibrate</span>
                  </button>
                </div>
              </div>
            </div>

            <!-- Enhanced Global Actions -->
            <div class="bg-gradient-to-r from-gray-50 to-slate-50 rounded-xl p-6 border border-gray-200 shadow-sm">
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                    <Database class="w-5 h-5 text-white" />
                  </div>
                  <div>
                    <h3 class="text-lg font-semibold text-gray-800">Global Actions</h3>
                    <p class="text-sm text-gray-600">Manage all ESP32 configurations at once</p>
                  </div>
                </div>
                <div class="flex items-center space-x-2 text-sm text-gray-500">
                  <Zap class="w-4 h-4" />
                  <span>Quick Actions</span>
                </div>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <button @click="saveAllConfigurations" class="group bg-white hover:bg-green-50 border border-gray-200 hover:border-green-300 rounded-lg p-4 transition-all duration-200 hover:shadow-md">
                  <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-green-100 group-hover:bg-green-200 rounded-lg flex items-center justify-center transition-colors">
                      <Save class="w-5 h-5 text-green-600" />
                    </div>
                    <div class="text-left">
                      <h4 class="font-medium text-gray-800 group-hover:text-green-700">Save All</h4>
                      <p class="text-xs text-gray-500">Save all configurations</p>
                    </div>
                  </div>
                </button>
                
                <button @click="resetAllConfigurations" class="group bg-white hover:bg-red-50 border border-gray-200 hover:border-red-300 rounded-lg p-4 transition-all duration-200 hover:shadow-md">
                  <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-red-100 group-hover:bg-red-200 rounded-lg flex items-center justify-center transition-colors">
                      <RotateCcw class="w-5 h-5 text-red-600" />
                    </div>
                    <div class="text-left">
                      <h4 class="font-medium text-gray-800 group-hover:text-red-700">Reset All</h4>
                      <p class="text-xs text-gray-500">Reset to defaults</p>
                    </div>
                  </div>
                </button>
                
                <button @click="importConfigurations" class="group bg-white hover:bg-blue-50 border border-gray-200 hover:border-blue-300 rounded-lg p-4 transition-all duration-200 hover:shadow-md">
                  <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-blue-100 group-hover:bg-blue-200 rounded-lg flex items-center justify-center transition-colors">
                      <Upload class="w-5 h-5 text-blue-600" />
                    </div>
                    <div class="text-left">
                      <h4 class="font-medium text-gray-800 group-hover:text-blue-700">Import Config</h4>
                      <p class="text-xs text-gray-500">Import configuration file</p>
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- MODAL OVERLAY - Fixed positioning with proper z-index -->
  <div v-if="activeModal" class="fixed inset-0 z-[9999] overflow-y-auto">
    <!-- Backdrop with blur effect -->
    <div class="fixed inset-0 bg-black/50 backdrop-blur-sm transition-opacity" @click="closeModal"></div>
    
    <!-- Modal container with proper centering -->
    <div class="flex min-h-full items-center justify-center p-4">
      <!-- ESP32-1 Modal - FIXED HEIGHT AND WIDTH -->
      <div v-if="activeModal === 'esp1'" class="relative bg-white rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col">
        <!-- Modal Header - Fixed -->
        <div class="flex items-center justify-between p-6 border-b border-gray-100 flex-shrink-0">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-green-100 to-emerald-100 rounded-xl flex items-center justify-center">
              <Cpu class="w-5 h-5 text-green-600" />
            </div>
            <div>
              <h2 class="text-lg font-semibold text-gray-800">ESP32-1 Configuration</h2>
              <p class="text-sm text-gray-500">NPK + Soil pH Monitoring</p>
            </div>
          </div>
          <button @click="closeModal" class="w-8 h-8 flex items-center justify-center rounded-lg text-gray-400 hover:text-gray-600 hover:bg-gray-100 transition-colors">
            <X class="w-4 h-4" />
          </button>
        </div>

        <!-- Modal Content - Scrollable -->
        <div class="flex-1 overflow-y-auto p-6">
          <div class="space-y-6">
            <!-- WiFi and Server Settings -->
            <div class="space-y-4">
              <div class="flex items-center space-x-2 mb-3">
                <div class="w-6 h-6 bg-blue-50 rounded-lg flex items-center justify-center">
                  <Wifi class="w-3 h-3 text-blue-600" />
                </div>
                <h3 class="font-medium text-gray-800">WiFi and Server Settings</h3>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-2">WiFi SSID</label>
                  <input v-model="esp1Config.wifiSSID" type="text" class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all text-sm" placeholder="WiFi network name">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-2">WiFi Password</label>
                  <div class="relative">
                    <input v-model="esp1Config.wifiPassword" :type="showPassword.esp1 ? 'text' : 'password'" class="w-full px-3 py-2 pr-10 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all text-sm" placeholder="WiFi password">
                    <button @click="togglePassword('esp1')" type="button" class="absolute inset-y-0 right-0 flex items-center justify-center w-10 text-gray-400 hover:text-gray-600 transition-colors">
                      <EyeOff v-if="!showPassword.esp1" class="w-4 h-4" />
                      <Eye v-else class="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-600 mb-2">Server URL</label>
                <input v-model="esp1Config.serverURL" type="url" class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all text-sm" placeholder="http://192.168.x.x">
              </div>
            </div>

            <!-- NPK Sensor Offset Section -->
            <div class="space-y-4">
              <div class="flex items-center space-x-2 mb-3">
                <div class="w-6 h-6 bg-purple-50 rounded-lg flex items-center justify-center">
                  <BarChart3 class="w-3 h-3 text-purple-600" />
                </div>
                <h3 class="font-medium text-gray-800">NPK Sensor Offset Section</h3>
              </div>
              
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <!-- Nitrogen Offset -->
                <div class="relative">
                  <label class="block text-sm font-medium text-green-600 mb-2">Nitrogen (mg/kg)</label>
                  <input 
                    v-model.number="esp1Config.nitrogenOffset" 
                    type="number" 
                    step="0.1" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all text-sm" 
                    placeholder="0.0"
                    @focus="showTooltip.nitrogen = true"
                    @blur="showTooltip.nitrogen = false"
                  >
                  <!-- Simplified Tooltip -->
                  <div v-if="showTooltip.nitrogen" class="absolute z-50 top-full left-0 mt-2 w-56 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-green-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">Calibration Offset</div>
                        <div>Enter + or - value to adjust reading if sensor is slightly off</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>

                <!-- Phosphorus Offset -->
                <div class="relative">
                  <label class="block text-sm font-medium text-blue-600 mb-2">Phosphorus (mg/kg)</label>
                  <input 
                    v-model.number="esp1Config.phosphorusOffset" 
                    type="number" 
                    step="0.1" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm" 
                    placeholder="0.0"
                    @focus="showTooltip.phosphorus = true"
                    @blur="showTooltip.phosphorus = false"
                  >
                  <!-- Simplified Tooltip -->
                  <div v-if="showTooltip.phosphorus" class="absolute z-50 top-full left-0 mt-2 w-56 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-blue-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">Calibration Offset</div>
                        <div>Enter + or - value to adjust reading if sensor is slightly off</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>

                <!-- Potassium Offset -->
                <div class="relative">
                  <label class="block text-sm font-medium text-purple-600 mb-2">Potassium (mg/kg)</label>
                  <input 
                    v-model.number="esp1Config.potassiumOffset" 
                    type="number" 
                    step="0.1" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500 transition-all text-sm" 
                    placeholder="0.0"
                    @focus="showTooltip.potassium = true"
                    @blur="showTooltip.potassium = false"
                  >
                  <!-- Simplified Tooltip -->
                  <div v-if="showTooltip.potassium" class="absolute z-50 top-full left-0 mt-2 w-56 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-purple-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">Calibration Offset</div>
                        <div>Enter + or - value to adjust reading if sensor is slightly off</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Soil pH Sensor Offset Section -->
            <div class="space-y-4">
              <div class="flex items-center space-x-2 mb-3">
                <div class="w-6 h-6 bg-orange-50 rounded-lg flex items-center justify-center">
                  <Droplets class="w-3 h-3 text-orange-600" />
                </div>
                <h3 class="font-medium text-gray-800">Soil pH Sensor Offset Section</h3>
              </div>
              
              <div class="max-w-xs relative">
                <label class="block text-sm font-medium text-orange-600 mb-2">pH Offset</label>
                <input 
                  v-model.number="esp1Config.phOffset" 
                  type="number" 
                  step="0.1" 
                  class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500/20 focus:border-orange-500 transition-all text-sm" 
                  placeholder="0.0"
                  @focus="showTooltip.ph = true"
                  @blur="showTooltip.ph = false"
                >
                <!-- Fixed Tooltip for pH -->
                <div v-if="showTooltip.ph" class="absolute z-50 top-full left-0 mt-2 w-60 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                  <div class="flex items-start space-x-2">
                    <Info class="w-3 h-3 text-orange-400 flex-shrink-0 mt-0.5" />
                    <div class="leading-relaxed">
                      <div class="font-medium mb-1">pH Calibration</div>
                      <div>Enter + or - value to adjust reading</div>
                      <div class="text-gray-300 mt-1">Example: -0.3 or +0.5</div>
                    </div>
                  </div>
                  <!-- Left-aligned Arrow -->
                  <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal Footer - Fixed -->
        <div class="flex-shrink-0 p-6 border-t border-gray-100 bg-gray-50/50">
          <div class="flex flex-wrap gap-3 justify-end">
            <button @click="testSensor('esp1')" class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg text-sm font-medium transition-colors flex items-center space-x-2">
              <BarChart3 class="w-4 h-4" />
              <span>TEST SENSOR</span>
            </button>
            <button @click="applyOffsets('esp1')" class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-lg text-sm font-medium transition-colors flex items-center space-x-2">
              <Settings class="w-4 h-4" />
              <span>APPLY OFFSETS</span>
            </button>
            <button @click="saveAndReboot('esp1')" class="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg text-sm font-medium transition-colors flex items-center space-x-2">
              <Save class="w-4 h-4" />
              <span>SAVE & REBOOT</span>
            </button>
          </div>
        </div>
      </div>

      <!-- ESP32-2 Modal -->
      <div v-if="activeModal === 'esp2'" class="relative bg-white rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col">
        <!-- Modal Header - Fixed -->
        <div class="flex items-center justify-between p-6 border-b border-gray-100 flex-shrink-0">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-100 to-indigo-100 rounded-xl flex items-center justify-center">
              <Cloud class="w-5 h-5 text-blue-600" />
            </div>
            <div>
              <h2 class="text-lg font-semibold text-gray-800">ESP32-2 Configuration</h2>
              <p class="text-sm text-gray-500">Environmental Monitoring</p>
            </div>
          </div>
          <button @click="closeModal" class="w-8 h-8 flex items-center justify-center rounded-lg text-gray-400 hover:text-gray-600 hover:bg-gray-100 transition-colors">
            <X class="w-4 h-4" />
          </button>
        </div>

        <!-- Modal Content - Scrollable -->
        <div class="flex-1 overflow-y-auto p-6">
          <div class="space-y-6">
            <!-- WiFi Configuration -->
            <div class="space-y-4">
              <div class="flex items-center space-x-2 mb-3">
                <div class="w-6 h-6 bg-blue-50 rounded-lg flex items-center justify-center">
                  <Wifi class="w-3 h-3 text-blue-600" />
                </div>
                <h3 class="font-medium text-gray-800">WiFi Settings</h3>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-2">Network SSID</label>
                  <input v-model="esp2Config.wifiSSID" type="text" class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm" placeholder="WiFi network name">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-2">Password</label>
                  <div class="relative">
                    <input v-model="esp2Config.wifiPassword" :type="showPassword.esp2 ? 'text' : 'password'" class="w-full px-3 py-2 pr-10 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm" placeholder="WiFi password">
                    <button @click="togglePassword('esp2')" type="button" class="absolute inset-y-0 right-0 flex items-center justify-center w-10 text-gray-400 hover:text-gray-600 transition-colors">
                      <EyeOff v-if="!showPassword.esp2" class="w-4 h-4" />
                      <Eye v-else class="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-600 mb-2">API Endpoint</label>
                <input v-model="esp2Config.apiURL" type="url" class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm" placeholder="https://api.example.com">
              </div>
            </div>

            <!-- Environmental Sensor Calibration -->
            <div class="space-y-4">
              <div class="flex items-center space-x-2 mb-3">
                <div class="w-6 h-6 bg-purple-50 rounded-lg flex items-center justify-center">
                  <BarChart3 class="w-3 h-3 text-purple-600" />
                </div>
                <h3 class="font-medium text-gray-800">Environmental Sensors</h3>
              </div>
              
              <!-- DHT21 Temperature & Humidity Offsets -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="relative">
                  <label class="block text-sm font-medium text-red-600 mb-2">Temp Offset (°C)</label>
                  <input 
                    v-model="esp2Config.tempOffset" 
                    type="number" 
                    step="0.1" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-red-500/20 focus:border-red-500 transition-all text-sm" 
                    placeholder="0.0"
                    @focus="showTooltip.tempOffset = true"
                    @blur="showTooltip.tempOffset = false"
                  >
                  <!-- Temperature Offset Tooltip -->
                  <div v-if="showTooltip.tempOffset" class="absolute z-50 top-full left-0 mt-2 w-56 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-red-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">DHT21 Temperature</div>
                        <div>Apply if temperature is consistently off</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>
                
                <div class="relative">
                  <label class="block text-sm font-medium text-blue-600 mb-2">Humidity Offset (%)</label>
                  <input 
                    v-model="esp2Config.humidityOffset" 
                    type="number" 
                    step="0.1" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm" 
                    placeholder="0.0"
                    @focus="showTooltip.humidityOffset = true"
                    @blur="showTooltip.humidityOffset = false"
                  >
                  <!-- Humidity Offset Tooltip -->
                  <div v-if="showTooltip.humidityOffset" class="absolute z-50 top-full left-0 mt-2 w-56 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-blue-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">DHT21 Humidity</div>
                        <div>Apply if humidity reading is incorrect</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>
              </div>
              
              <!-- Auto Watering Threshold -->
              <div class="relative max-w-xs">
                <label class="block text-sm font-medium text-green-600 mb-2">Auto Watering Threshold (%)</label>
                <input 
                  v-model="esp2Config.wateringThreshold" 
                  type="number" 
                  class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all text-sm" 
                  placeholder="30"
                  @focus="showTooltip.wateringThreshold = true"
                  @blur="showTooltip.wateringThreshold = false"
                >
                <!-- Watering Threshold Tooltip -->
                <div v-if="showTooltip.wateringThreshold" class="absolute z-50 top-full left-0 mt-2 w-64 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                  <div class="flex items-start space-x-2">
                    <Info class="w-3 h-3 text-green-400 flex-shrink-0 mt-0.5" />
                    <div class="leading-relaxed">
                      <div class="font-medium mb-1">Auto Watering</div>
                      <div>If soil moisture falls below this %, the water pump will turn ON.</div>
                    </div>
                  </div>
                  <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                </div>
              </div>
              
              <!-- Soil Moisture Sensor Calibration -->
              <div class="space-y-3">
                <div class="text-sm text-gray-600 bg-blue-50 p-3 rounded-lg border border-blue-200">
                  <div class="flex items-start space-x-2">
                    <Info class="w-4 h-4 text-blue-600 flex-shrink-0 mt-0.5" />
                    <div>
                      <div class="font-medium text-blue-800 mb-1">Soil Sensor Calibration</div>
                      <div class="text-blue-700">Calibrate soil sensor: measure sensor reading in air and in water to set dry/wet reference.</div>
                    </div>
                  </div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-orange-600 mb-2">Air Value (Dry Soil)</label>
                    <input 
                      v-model="esp2Config.airValue" 
                      type="number" 
                      class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500/20 focus:border-orange-500 transition-all text-sm" 
                      placeholder="1024"
                    >
                  </div>
                  <div>
                    <label class="block text-sm font-medium text-cyan-600 mb-2">Water Value (Wet Soil)</label>
                    <input 
                      v-model="esp2Config.waterValue" 
                      type="number" 
                      class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-cyan-500/20 focus:border-cyan-500 transition-all text-sm" 
                      placeholder="0"
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal Footer - Fixed -->
        <div class="flex-shrink-0 p-6 border-t border-gray-100 bg-gray-50/50">
          <div class="flex flex-wrap gap-3 justify-end">
            <button @click="testConnection('esp2')" class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg text-sm font-medium transition-colors">
              Test
            </button>
            <button @click="calibrateSensors('esp2')" class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-lg text-sm font-medium transition-colors">
              Calibrate
            </button>
            <button @click="saveConfiguration('esp2')" class="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg text-sm font-medium transition-colors">
              Save
            </button>
          </div>
        </div>
      </div>

      <!-- ESP32-3 Modal -->
      <div v-if="activeModal === 'esp3'" class="relative bg-white rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col">
        <!-- Modal Header - Fixed -->
        <div class="flex items-center justify-between p-6 border-b border-gray-100 flex-shrink-0">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-cyan-100 to-teal-100 rounded-xl flex items-center justify-center">
              <Droplets class="w-5 h-5 text-cyan-600" />
            </div>
            <div>
              <h2 class="text-lg font-semibold text-gray-800">ESP32-3 Configuration</h2>
              <p class="text-sm text-gray-500">Water Level Monitoring</p>
            </div>
          </div>
          <button @click="closeModal" class="w-8 h-8 flex items-center justify-center rounded-lg text-gray-400 hover:text-gray-600 hover:bg-gray-100 transition-colors">
            <X class="w-4 h-4" />
          </button>
        </div>

        <!-- Modal Content - Scrollable -->
        <div class="flex-1 overflow-y-auto p-6">
          <div class="space-y-6">
            <!-- WiFi Configuration -->
            <div class="space-y-4">
              <div class="flex items-center space-x-2 mb-3">
                <div class="w-6 h-6 bg-blue-50 rounded-lg flex items-center justify-center">
                  <Wifi class="w-3 h-3 text-blue-600" />
                </div>
                <h3 class="font-medium text-gray-800">WiFi Settings</h3>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-2">Network SSID</label>
                  <input v-model="esp3Config.wifiSSID" type="text" class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-cyan-500/20 focus:border-cyan-500 transition-all text-sm" placeholder="WiFi network name">
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-600 mb-2">Password</label>
                  <div class="relative">
                    <input v-model="esp3Config.wifiPassword" :type="showPassword.esp3 ? 'text' : 'password'" class="w-full px-3 py-2 pr-10 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-cyan-500/20 focus:border-cyan-500 transition-all text-sm" placeholder="WiFi password">
                    <button @click="togglePassword('esp3')" type="button" class="absolute inset-y-0 right-0 flex items-center justify-center w-10 text-gray-400 hover:text-gray-600 transition-colors">
                      <EyeOff v-if="!showPassword.esp3" class="w-4 h-4" />
                      <Eye v-else class="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
              
              <div>
                <label class="block text-sm font-medium text-gray-600 mb-2">API Endpoint</label>
                <input v-model="esp3Config.apiURL" type="url" class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-cyan-500/20 focus:border-cyan-500 transition-all text-sm" placeholder="https://api.example.com">
              </div>
            </div>

            <!-- Tank Calibration -->
            <div class="space-y-4">
              <div class="flex items-center space-x-2 mb-3">
                <div class="w-6 h-6 bg-purple-50 rounded-lg flex items-center justify-center">
                  <BarChart3 class="w-3 h-3 text-purple-600" />
                </div>
                <h3 class="font-medium text-gray-800">Water Tank Calibration</h3>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Tank Height -->
                <div class="relative">
                  <label class="block text-sm font-medium text-cyan-600 mb-2">Tank Height (cm)</label>
                  <input 
                    v-model="esp3Config.tankHeight" 
                    type="number" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-cyan-500/20 focus:border-cyan-500 transition-all text-sm" 
                    placeholder="100"
                    @focus="showTooltip.tankHeight = true"
                    @blur="showTooltip.tankHeight = false"
                  >
                  <!-- Tank Height Tooltip -->
                  <div v-if="showTooltip.tankHeight" class="absolute z-50 top-full left-0 mt-2 w-64 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-cyan-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">Tank Height</div>
                        <div>The full vertical height of the water tank (from bottom to top edge). Used to calculate percentage level.</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>

                <!-- Alert Level -->
                <div class="relative">
                  <label class="block text-sm font-medium text-blue-600 mb-2">Alert Level (%)</label>
                  <input 
                    v-model="esp3Config.alertLevel" 
                    type="number" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm" 
                    placeholder="20"
                    @focus="showTooltip.alertLevel = true"
                    @blur="showTooltip.alertLevel = false"
                  >
                  <!-- Alert Level Tooltip -->
                  <div v-if="showTooltip.alertLevel" class="absolute z-50 top-full left-0 mt-2 w-64 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-blue-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">Alert Threshold</div>
                        <div>If water level drops below this percentage, the system triggers alerts (e.g., LED or buzzer).</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>

                <!-- Full Distance -->
                <div class="relative">
                  <label class="block text-sm font-medium text-green-600 mb-2">Full Distance (cm)</label>
                  <input 
                    v-model="esp3Config.fullDistance" 
                    type="number" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all text-sm" 
                    placeholder="5"
                    @focus="showTooltip.fullDistance = true"
                    @blur="showTooltip.fullDistance = false"
                  >
                  <!-- Full Distance Tooltip -->
                  <div v-if="showTooltip.fullDistance" class="absolute z-50 top-full left-0 mt-2 w-64 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-green-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">Full Tank Distance</div>
                        <div>The measured distance (in cm) from the ultrasonic sensor to the water surface when the tank is full.</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>

                <!-- Empty Distance -->
                <div class="relative">
                  <label class="block text-sm font-medium text-red-600 mb-2">Empty Distance (cm)</label>
                  <input 
                    v-model="esp3Config.emptyDistance" 
                    type="number" 
                    class="w-full px-3 py-2 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-red-500/20 focus:border-red-500 transition-all text-sm" 
                    placeholder="95"
                    @focus="showTooltip.emptyDistance = true"
                    @blur="showTooltip.emptyDistance = false"
                  >
                  <!-- Empty Distance Tooltip -->
                  <div v-if="showTooltip.emptyDistance" class="absolute z-50 top-full left-0 mt-2 w-64 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg shadow-xl pointer-events-none">
                    <div class="flex items-start space-x-2">
                      <Info class="w-3 h-3 text-red-400 flex-shrink-0 mt-0.5" />
                      <div class="leading-relaxed">
                        <div class="font-medium mb-1">Empty Tank Distance</div>
                        <div>The measured distance from the ultrasonic sensor to the tank floor when the tank is empty. Helps define 0% water level.</div>
                      </div>
                    </div>
                    <div class="absolute bottom-full left-4 w-0 h-0 border-l-4 border-r-4 border-b-4 border-transparent border-b-gray-800"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal Footer - Fixed -->
        <div class="flex-shrink-0 p-6 border-t border-gray-100 bg-gray-50/50">
          <div class="flex flex-wrap gap-3 justify-end">
            <button @click="testConnection('esp3')" class="px-4 py-2 bg-cyan-500 hover:bg-cyan-600 text-white rounded-lg text-sm font-medium transition-colors">
              Test
            </button>
            <button @click="calibrateWaterLevel('esp3')" class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg text-sm font-medium transition-colors">
              Calibrate
            </button>
            <button @click="saveConfiguration('esp3')" class="px-4 py-2 bg-gray-600 hover:bg-gray-700 text-white rounded-lg text-sm font-medium transition-colors">
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Reset Confirmation Modal -->
  <div v-if="showResetModal" class="fixed inset-0 z-[10000] overflow-y-auto">
    <!-- Backdrop with blur effect -->
    <div class="fixed inset-0 bg-black/50 backdrop-blur-sm transition-opacity" @click="cancelReset"></div>
    
    <!-- Modal container with proper centering -->
    <div class="flex min-h-full items-center justify-center p-4">
      <div class="relative bg-white rounded-2xl shadow-2xl w-full max-w-md overflow-hidden">
        <!-- Modal Header -->
        <div class="p-6 border-b border-gray-100">
          <div class="flex items-center space-x-3">
            <div class="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center">
              <RotateCcw class="w-6 h-6 text-red-600" />
            </div>
            <div>
              <h2 class="text-lg font-semibold text-gray-800">Reset All Configurations</h2>
              <p class="text-sm text-gray-500">This action cannot be undone</p>
            </div>
          </div>
        </div>

        <!-- Modal Content -->
        <div class="p-6">
          <div class="mb-4">
            <p class="text-gray-700 leading-relaxed">
              Are you sure you want to reset all ESP32 configurations to their default values? 
            </p>
            <p class="text-sm text-gray-500 mt-2">
              This will clear all WiFi settings, calibration values, and sensor configurations for all three ESP32 devices.
            </p>
          </div>
          
          <!-- Warning Box -->
          <div class="bg-red-50 border border-red-200 rounded-lg p-3 mb-4">
            <div class="flex items-start space-x-2">
              <Info class="w-4 h-4 text-red-600 flex-shrink-0 mt-0.5" />
              <div class="text-sm text-red-700">
                <div class="font-medium">Warning:</div>
                <div>All current settings will be permanently lost and cannot be recovered.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal Footer -->
        <div class="p-6 border-t border-gray-100 bg-gray-50/50">
          <div class="flex gap-3 justify-end">
            <button 
              @click="cancelReset" 
              class="px-4 py-2 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded-lg text-sm font-medium transition-colors"
            >
              Cancel
            </button>
            <button 
              @click="confirmReset" 
              class="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg text-sm font-medium transition-colors flex items-center space-x-2"
            >
              <RotateCcw class="w-4 h-4" />
              <span>Reset All</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notifications -->
  <div v-if="showToast" class="fixed bottom-4 right-4 bg-white border border-gray-200 rounded-lg shadow-lg p-4 max-w-sm z-[10000] transform transition-all duration-300" :class="toastType === 'success' ? 'border-green-200 bg-green-50' : toastType === 'error' ? 'border-red-200 bg-red-50' : 'border-blue-200 bg-blue-50'">
    <div class="flex items-center space-x-3">
      <div class="flex-shrink-0">
        <CheckCircle v-if="toastType === 'success'" class="w-5 h-5 text-green-500" />
        <XCircle v-else-if="toastType === 'error'" class="w-5 h-5 text-red-500" />
        <Info v-else class="w-5 h-5 text-blue-500" />
      </div>
      <div class="flex-1">
        <p class="text-sm font-medium" :class="toastType === 'success' ? 'text-green-800' : toastType === 'error' ? 'text-red-800' : 'text-blue-800'">{{ toastMessage }}</p>
      </div>
      <button @click="hideToast" class="flex-shrink-0 text-gray-400 hover:text-gray-600">
        <X class="w-4 h-4" />
      </button>
    </div>
  </div>
</div>
</template>

<script>
import Sidebar from '../layout/Sidebar.vue'
import { 
  Search, 
  Download, 
  Cpu, 
  Cloud, 
  Droplets, 
  CheckCircle, 
  Settings, 
  BarChart3, 
  Container, 
  Database, 
  Zap, 
  Save, 
  RotateCcw, 
  Upload, 
  X, 
  Wifi, 
  Eye, 
  EyeOff, 
  XCircle, 
  Info 
} from 'lucide-vue-next'

export default {
name: 'ReCalibration',
components: {
  Sidebar,
  Search,
  Download,
  Cpu,
  Cloud,
  Droplets,
  CheckCircle,
  Settings,
  BarChart3,
  Container,
  Database,
  Zap,
  Save,
  RotateCcw,
  Upload,
  X,
  Wifi,
  Eye,
  EyeOff,
  XCircle,
  Info
},
data() {
  return {
    // Search functionality
    searchQuery: '',
    
    // Modal control
    activeModal: null, // 'esp1', 'esp2', 'esp3', or null
    
    // Password Visibility
    showPassword: {
      esp1: false,
      esp2: false,
      esp3: false
    },
    
    // Tooltip Visibility
    showTooltip: {
      nitrogen: false,
      phosphorus: false,
      potassium: false,
      ph: false,
      tempOffset: false,
      humidityOffset: false,
      wateringThreshold: false,
      tankHeight: false,
      alertLevel: false,
      fullDistance: false,
      emptyDistance: false
    },
    
    // ESP32 #1 Configuration (NPK & pH with Offsets)
    esp1Config: {
      wifiSSID: '',
      wifiPassword: '',
      serverURL: '',
      nitrogenOffset: 0.0,
      phosphorusOffset: 0.0,
      potassiumOffset: 0.0,
      phOffset: 0.0
    },
    
    // ESP32 #2 Configuration (Moisture & DHT21)
    esp2Config: {
      wifiSSID: '',
      wifiPassword: '',
      apiURL: '',
      tempOffset: 0.0,
      humidityOffset: 0.0,
      wateringThreshold: 30,
      airValue: 1024,
      waterValue: 0
    },
    
    // ESP32 #3 Configuration (Water Level)
    esp3Config: {
      wifiSSID: '',
      wifiPassword: '',
      apiURL: '',
      tankHeight: 100,
      fullDistance: 5,
      emptyDistance: 95,
      alertLevel: 20
    },
    
    // Toast Notifications
    showToast: false,
    toastMessage: '',
    toastType: 'info', // success, error, info
    tooltipTimeout: null, // Add this line
    showResetModal: false,
  }
},

methods: {
  openModal(esp) {
    this.activeModal = esp;
    // Prevent body scroll when modal is open
    document.body.style.overflow = 'hidden';
  },
  
  closeModal() {
    this.activeModal = null;
    // Restore body scroll when modal is closed
    document.body.style.overflow = 'auto';
  },
  
  togglePassword(esp) {
    this.showPassword[esp] = !this.showPassword[esp];
  },
  
  async testSensor(esp) {
    this.showToastMessage(`Testing live sensor readings for ESP32 ${esp.slice(-1)}...`, 'info');

    try {
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Simulate sensor readings
      const mockReadings = {
        nitrogen: (Math.random() * 100 + 50).toFixed(1),
        phosphorus: (Math.random() * 50 + 20).toFixed(1),
        potassium: (Math.random() * 80 + 30).toFixed(1),
        ph: (Math.random() * 2 + 6).toFixed(1)
      };
      
      this.showToastMessage(
        `Live readings - N: ${mockReadings.nitrogen}mg/kg, P: ${mockReadings.phosphorus}mg/kg, K: ${mockReadings.potassium}mg/kg, pH: ${mockReadings.ph}`, 
        'success'
      );
    } catch (error) {
      this.showToastMessage(`Failed to read sensor data for ESP32 ${esp.slice(-1)}`, 'error');
    }
  },
  
  async applyOffsets(esp) {
    this.showToastMessage(`Applying correction offsets temporarily for ESP32 ${esp.slice(-1)}...`, 'info');
    
    try {
      const config = this[`${esp}Config`];
      
      // Validate offset values
      if (isNaN(config.nitrogenOffset) || isNaN(config.phosphorusOffset) || 
          isNaN(config.potassiumOffset) || isNaN(config.phOffset)) {
        throw new Error('Please enter valid numeric offset values');
      }
      
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      this.showToastMessage(
        `Offsets applied: N(${config.nitrogenOffset > 0 ? '+' : ''}${config.nitrogenOffset}), P(${config.phosphorusOffset > 0 ? '+' : ''}${config.phosphorusOffset}), K(${config.potassiumOffset > 0 ? '+' : ''}${config.potassiumOffset}), pH(${config.phOffset > 0 ? '+' : ''}${config.phOffset})`, 
        'success'
      );
    } catch (error) {
      this.showToastMessage(error.message || `Failed to apply offsets for ESP32 ${esp.slice(-1)}`, 'error');
    }
  },
  
  async saveAndReboot(esp) {
    this.showToastMessage(`Saving configuration and rebooting ESP32 ${esp.slice(-1)}...`, 'info');
    
    try {
      const config = this[`${esp}Config`];
      
      // Validate required fields
      if (!config.wifiSSID || !config.wifiPassword || !config.serverURL) {
        throw new Error('Please fill in all WiFi and server settings');
      }
      
      // Validate offset values
      if (isNaN(config.nitrogenOffset) || isNaN(config.phosphorusOffset) || 
          isNaN(config.potassiumOffset) || isNaN(config.phOffset)) {
        throw new Error('Please enter valid numeric offset values');
      }
      
      await new Promise(resolve => setTimeout(resolve, 3000));
      
      this.showToastMessage(`Configuration saved to Preferences and ESP32 ${esp.slice(-1)} rebooted successfully!`, 'success');
      this.closeModal(); // Close modal after successful save
    } catch (error) {
      this.showToastMessage(error.message || `Failed to save and reboot ESP32 ${esp.slice(-1)}`, 'error');
    }
  },
  
  async testConnection(esp) {
    this.showToastMessage(`Testing connection for ESP32 ${esp.slice(-1)}...`, 'info');
    
    try {
      await new Promise(resolve => setTimeout(resolve, 2000));
      this.showToastMessage(`ESP32 ${esp.slice(-1)} connection successful!`, 'success');
    } catch (error) {
      this.showToastMessage(`Connection failed for ESP32 ${esp.slice(-1)}`, 'error');
    }
  },
  
  async calibrateSensors(esp) {
    this.showToastMessage(`Calibrating sensors for ESP32 ${esp.slice(-1)}...`, 'info');
    
    try {
      await new Promise(resolve => setTimeout(resolve, 3000));
      this.showToastMessage(`Sensor calibration completed for ESP32 ${esp.slice(-1)}!`, 'success');
    } catch (error) {
      this.showToastMessage(`Calibration failed for ESP32 ${esp.slice(-1)}`, 'error');
    }
  },
  
  async calibrateWaterLevel(esp) {
    this.showToastMessage('Calibrating water level sensor...', 'info');
    
    try {
      await new Promise(resolve => setTimeout(resolve, 2500));
      this.showToastMessage('Water level calibration completed!', 'success');
    } catch (error) {
      this.showToastMessage('Water level calibration failed', 'error');
    }
  },
  
  async saveConfiguration(esp) {
    this.showToastMessage(`Saving configuration for ESP32 ${esp.slice(-1)}...`, 'info');
    
    try {
      const config = this[`${esp}Config`];
      if (!config.wifiSSID || !config.wifiPassword || !config.apiURL) {
        throw new Error('Please fill in all required fields');
      }
      
      await new Promise(resolve => setTimeout(resolve, 1500));
      this.showToastMessage(`Configuration saved for ESP32 ${esp.slice(-1)}!`, 'success');
      this.closeModal(); // Close modal after successful save
    } catch (error) {
      this.showToastMessage(error.message || `Failed to save configuration for ESP32 ${esp.slice(-1)}`, 'error');
    }
  },
  
  async saveAllConfigurations() {
    this.showToastMessage('Saving all configurations...', 'info');
    
    try {
      await new Promise(resolve => setTimeout(resolve, 3000));
      this.showToastMessage('All configurations saved successfully!', 'success');
    } catch (error) {
      this.showToastMessage('Failed to save all configurations', 'error');
    }
  },
  
  resetAllConfigurations() {
    this.showResetModal = true;
  },

  confirmReset() {
    this.esp1Config = {
      wifiSSID: '',
      wifiPassword: '',
      serverURL: '',
      nitrogenOffset: 0.0,
      phosphorusOffset: 0.0,
      potassiumOffset: 0.0,
      phOffset: 0.0
    };
    
    this.esp2Config = {
      wifiSSID: '',
      wifiPassword: '',
      apiURL: '',
      tempOffset: 0.0,
      humidityOffset: 0.0,
      wateringThreshold: 30,
      airValue: 1024,
      waterValue: 0
    };
    
    this.esp3Config = {
      wifiSSID: '',
      wifiPassword: '',
      apiURL: '',
      tankHeight: 100,
      fullDistance: 5,
      emptyDistance: 95,
      alertLevel: 20
    };
    
    this.showResetModal = false;
    this.showToastMessage('All configurations reset to defaults', 'success');
  },

  cancelReset() {
    this.showResetModal = false;
  },
  
  exportConfigurations() {
    const configurations = {
      esp1: this.esp1Config,
      esp2: this.esp2Config,
      esp3: this.esp3Config,
      exportDate: new Date().toISOString()
    };
    
    const dataStr = JSON.stringify(configurations, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = 'esp32-configurations.json';
    link.click();
    
    URL.revokeObjectURL(url);
    this.showToastMessage('Configuration exported successfully!', 'success');
  },
  
  importConfigurations() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.json';
    input.onchange = (event) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          try {
            const configs = JSON.parse(e.target.result);
            if (configs.esp1) this.esp1Config = { ...this.esp1Config, ...configs.esp1 };
            if (configs.esp2) this.esp2Config = { ...this.esp2Config, ...configs.esp2 };
            if (configs.esp3) this.esp3Config = { ...this.esp3Config, ...configs.esp3 };
            this.showToastMessage('Configuration imported successfully!', 'success');
          } catch (error) {
            this.showToastMessage('Failed to import configuration file', 'error');
          }
        };
        reader.readAsText(file);
      }
    };
    input.click();
  },
  
  showToastMessage(message, type = 'info') {
    this.toastMessage = message;
    this.toastType = type;
    this.showToast = true;
    
    setTimeout(() => {
      this.hideToast();
    }, 5000);
  },
  
  hideToast() {
    this.showToast = false;
  },

  handleTooltipShow(field) {
    // Clear any existing timeout
    if (this.tooltipTimeout) {
      clearTimeout(this.tooltipTimeout);
    }
    this.showTooltip[field] = true;
  },
  
  handleTooltipHide(field) {
    // Add small delay to prevent flickering
    this.tooltipTimeout = setTimeout(() => {
      this.showTooltip[field] = false;
    }, 50);
  }
},

mounted() {
  const savedConfigs = localStorage.getItem('esp32Configurations');
  if (savedConfigs) {
    try {
      const configs = JSON.parse(savedConfigs);
      if (configs.esp1) this.esp1Config = { ...this.esp1Config, ...configs.esp1 };
      if (configs.esp2) this.esp2Config = { ...this.esp2Config, ...configs.esp2 };
      if (configs.esp3) this.esp3Config = { ...this.esp3Config, ...configs.esp3 };
    } catch (error) {
      console.error('Failed to load saved configurations:', error);
    }
  }
},

beforeUnmount() {
  // Ensure body scroll is restored when component is destroyed
  document.body.style.overflow = 'auto';
},

watch: {
  esp1Config: {
    handler(newVal) {
      const configs = JSON.parse(localStorage.getItem('esp32Configurations') || '{}');
      configs.esp1 = newVal;
      localStorage.setItem('esp32Configurations', JSON.stringify(configs));
    },
    deep: true
  },
  esp2Config: {
    handler(newVal) {
      const configs = JSON.parse(localStorage.getItem('esp32Configurations') || '{}');
      configs.esp2 = newVal;
      localStorage.setItem('esp32Configurations', JSON.stringify(configs));
    },
    deep: true
  },
  esp3Config: {
    handler(newVal) {
      const configs = JSON.parse(localStorage.getItem('esp32Configurations') || '{}');
      configs.esp3 = newVal;
      localStorage.setItem('esp32Configurations', JSON.stringify(configs));
    },
    deep: true
  }
}
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgba(20, 83, 45, 0.1);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb {
  background: rgba(20, 83, 45, 0.5);
  border-radius: 3px;
  transition: background-color 200ms;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(20, 83, 45, 0.7);
}

* {
  transition: all 200ms ease-in-out;
}

@supports (-webkit-touch-callout: none) {
  .h-screen {
    height: -webkit-fill-available;
  }
}

* {
  scrollbar-width: thin;
  scrollbar-color: rgba(20, 83, 45, 0.5) rgba(20, 83, 45, 0.1);
}

input:focus,
button:focus {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}

/* Tooltip Animation */
.tooltip-enter-active,
.tooltip-leave-active {
  transition: all 0.2s ease;
}

.tooltip-enter-from,
.tooltip-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}

.tooltip-enter-to,
.tooltip-leave-from {
  opacity: 1;
  transform: translateY(0);
}

@media (max-width: 1024px) {
  .grid-cols-1.lg\\:grid-cols-3 {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .grid-cols-1.md\\:grid-cols-3 {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .grid-cols-1.md\\:grid-cols-2 {
    grid-template-columns: 1fr;
  }
  
  .text-lg {
    font-size: 1rem;
  }
  
  .space-x-3 > :not([hidden]) ~ :not([hidden]) {
    margin-left: 0.5rem;
  }
}

@media (max-width: 640px) {
  .max-w-2xl {
    max-width: 95vw;
  }
  
  .p-6 {
    padding: 1rem;
  }
  
  .space-x-3 {
    flex-direction: column;
    space: 0;
  }
  
  .space-x-3 > :not([hidden]) ~ :not([hidden]) {
    margin-left: 0;
    margin-top: 0.5rem;
  }

  .flex-wrap.gap-3 {
    flex-direction: column;
  }
  
  .flex-wrap.gap-3 button {
    width: 100%;
    justify-content: center;
  }
}

.bg-white:hover {
  transform: translateY(-1px);
}

button:hover {
  transform: translateY(-1px);
}

input:focus {
  transform: scale(1.01);
}
</style>