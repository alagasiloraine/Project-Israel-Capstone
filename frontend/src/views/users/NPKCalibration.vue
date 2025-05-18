<template>
  <div class="h-screen flex bg-white font-inter overflow-hidden">
    <Sidebar />
    <main class="flex-1 flex flex-col h-screen pt-32">
      <div class="flex-1 w-full px-4 sm:px-6 md:px-8 lg:px-10 overflow-hidden">
        <!-- Enhanced main container with refined design -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 h-[calc(100vh-140px)] flex flex-col overflow-hidden">
          <!-- Refined header with subtle gradient and improved spacing -->
          <div class="bg-gradient-to-r from-emerald-50/30 to-white p-5 border-b border-gray-100">
            <div class="flex flex-col space-y-1.5">
              <!-- Title and breadcrumb with refined typography -->
              <div class="flex items-center justify-between">
                <div>
                  <h1 class="text-lg font-medium text-gray-800">Soil NPK Calibration</h1>
                  <div class="flex items-center text-xs text-gray-500 mt-1">
                    <span class="text-emerald-600 font-medium">NPK Calibration</span>
                    <ChevronRight class="h-3 w-3 mx-1 text-gray-400" />
                    <span class="text-gray-600">Adjust sensor readings</span>
                  </div>
                </div>
                
                <!-- Refined toggle switch with better spacing -->
                <div class="flex items-center gap-3">
                  <span class="text-xs text-gray-600">Basic Mode</span>
                  <label class="relative inline-flex items-center cursor-pointer">
                    <input type="checkbox" v-model="advancedMode" class="sr-only peer">
                    <div class="w-9 h-5 bg-gray-200 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-500"></div>
                  </label>
                  <span class="text-xs text-gray-600">Advanced Mode</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Content area with refined spacing and layout -->
          <div class="flex-1 overflow-auto p-5">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-5">
              <!-- Left Column: Soil Type Selection with refined design -->
              <div class="bg-white rounded-xl p-4 border border-gray-100 shadow-sm">
                <h2 class="text-sm font-medium text-gray-800 mb-3">Soil Type Selection</h2>
                <p class="text-xs text-gray-500 mb-4">Select your soil type to apply predefined calibration multipliers</p>
                
                <div class="space-y-2">
                  <div 
                    v-for="soil in soilTypes" 
                    :key="soil.type"
                    @click="selectSoilType(soil.type)"
                    class="flex items-center p-2.5 rounded-lg cursor-pointer transition-all duration-200 border"
                    :class="selectedSoilType === soil.type ? 'bg-emerald-50 border-emerald-200' : 'border-gray-100 hover:bg-gray-50'"
                  >
                    <div class="w-3.5 h-3.5 rounded-full mr-2.5" :style="{ backgroundColor: soil.color }"></div>
                    <span class="text-xs font-medium text-gray-700">{{ soil.type }}</span>
                    <div v-if="selectedSoilType === soil.type" class="ml-auto">
                      <CheckIcon class="h-4 w-4 text-emerald-500" />
                    </div>
                  </div>
                </div>

                <div class="mt-5">
                  <button 
                    @click="resetToDefault" 
                    class="w-full py-2 px-3 bg-gray-50 hover:bg-gray-100 text-gray-700 text-xs rounded-lg transition-colors duration-200 flex items-center justify-center border border-gray-100"
                  >
                    <RefreshCwIcon class="h-3.5 w-3.5 mr-1.5 text-gray-500" />
                    Reset to Default
                  </button>
                </div>
              </div>

              <!-- Middle Column: Calibration Controls with completely redesigned UI -->
              <div class="bg-white rounded-xl p-4 border border-gray-100 shadow-sm">
                <h2 class="text-sm font-medium text-gray-800 mb-3">Calibration Controls</h2>
                
                <div v-if="!advancedMode" class="flex flex-col items-center justify-center h-64">
                  <div class="text-center">
                    <SlidersIcon class="h-10 w-10 text-gray-300 mx-auto mb-3" />
                    <p class="text-xs text-gray-500 mb-3">Enable Advanced Mode to access manual calibration controls</p>
                    <button 
                      @click="advancedMode = true" 
                      class="py-2 px-4 bg-emerald-500 hover:bg-emerald-600 text-white text-xs rounded-lg transition-colors duration-200 shadow-sm"
                    >
                      Enable Advanced Mode
                    </button>
                  </div>
                </div>

                <div v-else class="space-y-6">
                  <!-- Nitrogen Controls with completely redesigned UI -->
                  <div class="relative bg-gradient-to-r from-green-50 to-white rounded-lg border border-gray-100 p-4 shadow-sm overflow-hidden">
                    <!-- Decorative element -->
                    <div class="absolute -right-4 -top-4 w-16 h-16 bg-green-100 rounded-full opacity-30"></div>
                    
                    <div class="flex items-center justify-between mb-3 relative">
                      <div class="flex items-center">
                        <div class="flex items-center justify-center w-6 h-6 rounded-full bg-green-100 mr-2">
                          <div class="w-2.5 h-2.5 rounded-full bg-green-500"></div>
                        </div>
                        <span class="text-sm font-medium text-gray-800">Nitrogen (N)</span>
                      </div>
                      <div class="text-xs px-2 py-1 bg-white rounded-full text-gray-600 border border-gray-100 shadow-sm">
                        Raw: {{ rawValues.n }} mg/kg
                      </div>
                    </div>
                    
                    <div class="space-y-5">
                      <!-- Multiplier control with redesigned slider -->
                      <div>
                        <div class="flex items-center justify-between mb-2">
                          <span class="text-xs text-gray-600">Multiplier</span>
                          <div class="flex items-center">
                            <button 
                              @click="decrementMultiplier('n')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-l text-gray-600"
                            >
                              <MinusIcon class="h-3 w-3" />
                            </button>
                            <input 
                              v-model.number="calibration.n.multiplier" 
                              type="number" 
                              step="0.01" 
                              min="0.5" 
                              max="2" 
                              class="w-14 px-2 py-1 text-center border-y border-gray-200 text-xs"
                            />
                            <button 
                              @click="incrementMultiplier('n')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-r text-gray-600"
                            >
                              <PlusIcon class="h-3 w-3" />
                            </button>
                          </div>
                        </div>
                        <div class="relative h-7 flex items-center">
                          <!-- Min and max labels -->
                          <span class="absolute left-0 -top-1 text-[10px] text-gray-400">0.5x</span>
                          <span class="absolute right-0 -top-1 text-[10px] text-gray-400">2.0x</span>
                          
                          <!-- Slider track background -->
                          <div class="absolute top-1/2 -translate-y-1/2 w-full h-1.5 bg-gray-200 rounded-full"></div>
                          
                          <!-- Slider track fill -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 h-1.5 bg-green-500 rounded-l-full" 
                            :style="{ width: `${((calibration.n.multiplier - 0.5) / 1.5) * 100}%`, left: '0' }"
                          ></div>
                          
                          <!-- Slider thumb with shadow and border -->
                          <div 
                            class="absolute top-0 w-5 h-5 bg-white rounded-full shadow-md border-2 border-green-500 z-10 transform -translate-y-1/2" 
                            :style="{ left: `calc(${((calibration.n.multiplier - 0.5) / 1.5) * 100}% - 10px)`, top: '50%' }"
                          ></div>
                          
                          <!-- Actual range input (invisible but functional) -->
                          <input 
                            v-model.number="calibration.n.multiplier" 
                            type="range" 
                            min="0.5" 
                            max="2" 
                            step="0.01" 
                            class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer z-20"
                          />
                        </div>
                      </div>
                      
                      <!-- Offset control with redesigned slider -->
                      <div>
                        <div class="flex items-center justify-between mb-2">
                          <span class="text-xs text-gray-600">Offset (mg/kg)</span>
                          <div class="flex items-center">
                            <button 
                              @click="decrementOffset('n')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-l text-gray-600"
                            >
                              <MinusIcon class="h-3 w-3" />
                            </button>
                            <input 
                              v-model.number="calibration.n.offset" 
                              type="number" 
                              step="1" 
                              min="-50" 
                              max="50" 
                              class="w-14 px-2 py-1 text-center border-y border-gray-200 text-xs"
                            />
                            <button 
                              @click="incrementOffset('n')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-r text-gray-600"
                            >
                              <PlusIcon class="h-3 w-3" />
                            </button>
                          </div>
                        </div>
                        <div class="relative h-7 flex items-center">
                          <!-- Min and max labels -->
                          <span class="absolute left-0 -top-1 text-[10px] text-gray-400">-50</span>
                          <span class="absolute right-0 -top-1 text-[10px] text-gray-400">+50</span>
                          
                          <!-- Center marker -->
                          <div class="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 w-0.5 h-3 bg-gray-300"></div>
                          
                          <!-- Slider track background -->
                          <div class="absolute top-1/2 -translate-y-1/2 w-full h-1.5 bg-gray-200 rounded-full"></div>
                          
                          <!-- Slider track fill -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 h-1.5 bg-green-500" 
                            :style="calibration.n.offset >= 0 ? 
                              { width: `${(calibration.n.offset / 100) * 50}%`, left: '50%' } : 
                              { width: `${(Math.abs(calibration.n.offset) / 100) * 50}%`, right: '50%' }"
                            :class="calibration.n.offset >= 0 ? 'rounded-r-full' : 'rounded-l-full'"
                          ></div>
                          
                          <!-- Slider thumb with shadow and border -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 w-5 h-5 bg-white rounded-full shadow-md border-2 border-green-500 z-10" 
                            :style="{ left: `calc(${((calibration.n.offset + 50) / 100) * 100}% - 10px)` }"
                          ></div>
                          
                          <!-- Actual range input (invisible but functional) -->
                          <input 
                            v-model.number="calibration.n.offset" 
                            type="range" 
                            min="-50" 
                            max="50" 
                            step="1" 
                            class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer z-20"
                          />
                        </div>
                      </div>
                    </div>
                    
                    <!-- Calibrated value indicator -->
                    <div class="mt-4 pt-3 border-t border-gray-100">
                      <div class="flex items-center justify-between">
                        <span class="text-xs text-gray-500">Calibrated Value:</span>
                        <span class="text-sm font-medium text-gray-800">{{ calibratedValues.n }} mg/kg</span>
                      </div>
                    </div>
                  </div>

                  <!-- Phosphorus Controls with completely redesigned UI -->
                  <div class="relative bg-gradient-to-r from-blue-50 to-white rounded-lg border border-gray-100 p-4 shadow-sm overflow-hidden">
                    <!-- Decorative element -->
                    <div class="absolute -right-4 -top-4 w-16 h-16 bg-blue-100 rounded-full opacity-30"></div>
                    
                    <div class="flex items-center justify-between mb-3 relative">
                      <div class="flex items-center">
                        <div class="flex items-center justify-center w-6 h-6 rounded-full bg-blue-100 mr-2">
                          <div class="w-2.5 h-2.5 rounded-full bg-blue-500"></div>
                        </div>
                        <span class="text-sm font-medium text-gray-800">Phosphorus (P)</span>
                      </div>
                      <div class="text-xs px-2 py-1 bg-white rounded-full text-gray-600 border border-gray-100 shadow-sm">
                        Raw: {{ rawValues.p }} mg/kg
                      </div>
                    </div>
                    
                    <div class="space-y-5">
                      <!-- Multiplier control with redesigned slider -->
                      <div>
                        <div class="flex items-center justify-between mb-2">
                          <span class="text-xs text-gray-600">Multiplier</span>
                          <div class="flex items-center">
                            <button 
                              @click="decrementMultiplier('p')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-l text-gray-600"
                            >
                              <MinusIcon class="h-3 w-3" />
                            </button>
                            <input 
                              v-model.number="calibration.p.multiplier" 
                              type="number" 
                              step="0.01" 
                              min="0.5" 
                              max="2" 
                              class="w-14 px-2 py-1 text-center border-y border-gray-200 text-xs"
                            />
                            <button 
                              @click="incrementMultiplier('p')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-r text-gray-600"
                            >
                              <PlusIcon class="h-3 w-3" />
                            </button>
                          </div>
                        </div>
                        <div class="relative h-7 flex items-center">
                          <!-- Min and max labels -->
                          <span class="absolute left-0 -top-1 text-[10px] text-gray-400">0.5x</span>
                          <span class="absolute right-0 -top-1 text-[10px] text-gray-400">2.0x</span>
                          
                          <!-- Slider track background -->
                          <div class="absolute top-1/2 -translate-y-1/2 w-full h-1.5 bg-gray-200 rounded-full"></div>
                          
                          <!-- Slider track fill -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 h-1.5 bg-blue-500 rounded-l-full" 
                            :style="{ width: `${((calibration.p.multiplier - 0.5) / 1.5) * 100}%`, left: '0' }"
                          ></div>
                          
                          <!-- Slider thumb with shadow and border -->
                          <div 
                            class="absolute top-0 w-5 h-5 bg-white rounded-full shadow-md border-2 border-blue-500 z-10 transform -translate-y-1/2" 
                            :style="{ left: `calc(${((calibration.p.multiplier - 0.5) / 1.5) * 100}% - 10px)`, top: '50%' }"
                          ></div>
                          
                          <!-- Actual range input (invisible but functional) -->
                          <input 
                            v-model.number="calibration.p.multiplier" 
                            type="range" 
                            min="0.5" 
                            max="2" 
                            step="0.01" 
                            class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer z-20"
                          />
                        </div>
                      </div>
                      
                      <!-- Offset control with redesigned slider -->
                      <div>
                        <div class="flex items-center justify-between mb-2">
                          <span class="text-xs text-gray-600">Offset (mg/kg)</span>
                          <div class="flex items-center">
                            <button 
                              @click="decrementOffset('p')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-l text-gray-600"
                            >
                              <MinusIcon class="h-3 w-3" />
                            </button>
                            <input 
                              v-model.number="calibration.p.offset" 
                              type="number" 
                              step="1" 
                              min="-50" 
                              max="50" 
                              class="w-14 px-2 py-1 text-center border-y border-gray-200 text-xs"
                            />
                            <button 
                              @click="incrementOffset('p')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-r text-gray-600"
                            >
                              <PlusIcon class="h-3 w-3" />
                            </button>
                          </div>
                        </div>
                        <div class="relative h-7 flex items-center">
                          <!-- Min and max labels -->
                          <span class="absolute left-0 -top-1 text-[10px] text-gray-400">-50</span>
                          <span class="absolute right-0 -top-1 text-[10px] text-gray-400">+50</span>
                          
                          <!-- Center marker -->
                          <div class="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 w-0.5 h-3 bg-gray-300"></div>
                          
                          <!-- Slider track background -->
                          <div class="absolute top-1/2 -translate-y-1/2 w-full h-1.5 bg-gray-200 rounded-full"></div>
                          
                          <!-- Slider track fill -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 h-1.5 bg-blue-500" 
                            :style="calibration.p.offset >= 0 ? 
                              { width: `${(calibration.p.offset / 100) * 50}%`, left: '50%' } : 
                              { width: `${(Math.abs(calibration.p.offset) / 100) * 50}%`, right: '50%' }"
                            :class="calibration.p.offset >= 0 ? 'rounded-r-full' : 'rounded-l-full'"
                          ></div>
                          
                          <!-- Slider thumb with shadow and border -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 w-5 h-5 bg-white rounded-full shadow-md border-2 border-blue-500 z-10" 
                            :style="{ left: `calc(${((calibration.p.offset + 50) / 100) * 100}% - 10px)` }"
                          ></div>
                          
                          <!-- Actual range input (invisible but functional) -->
                          <input 
                            v-model.number="calibration.p.offset" 
                            type="range" 
                            min="-50" 
                            max="50" 
                            step="1" 
                            class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer z-20"
                          />
                        </div>
                      </div>
                    </div>
                    
                    <!-- Calibrated value indicator -->
                    <div class="mt-4 pt-3 border-t border-gray-100">
                      <div class="flex items-center justify-between">
                        <span class="text-xs text-gray-500">Calibrated Value:</span>
                        <span class="text-sm font-medium text-gray-800">{{ calibratedValues.p }} mg/kg</span>
                      </div>
                    </div>
                  </div>

                  <!-- Potassium Controls with completely redesigned UI -->
                  <div class="relative bg-gradient-to-r from-purple-50 to-white rounded-lg border border-gray-100 p-4 shadow-sm overflow-hidden">
                    <!-- Decorative element -->
                    <div class="absolute -right-4 -top-4 w-16 h-16 bg-purple-100 rounded-full opacity-30"></div>
                    
                    <div class="flex items-center justify-between mb-3 relative">
                      <div class="flex items-center">
                        <div class="flex items-center justify-center w-6 h-6 rounded-full bg-purple-100 mr-2">
                          <div class="w-2.5 h-2.5 rounded-full bg-purple-500"></div>
                        </div>
                        <span class="text-sm font-medium text-gray-800">Potassium (K)</span>
                      </div>
                      <div class="text-xs px-2 py-1 bg-white rounded-full text-gray-600 border border-gray-100 shadow-sm">
                        Raw: {{ rawValues.k }} mg/kg
                      </div>
                    </div>
                    
                    <div class="space-y-5">
                      <!-- Multiplier control with redesigned slider -->
                      <div>
                        <div class="flex items-center justify-between mb-2">
                          <span class="text-xs text-gray-600">Multiplier</span>
                          <div class="flex items-center">
                            <button 
                              @click="decrementMultiplier('k')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-l text-gray-600"
                            >
                              <MinusIcon class="h-3 w-3" />
                            </button>
                            <input 
                              v-model.number="calibration.k.multiplier" 
                              type="number" 
                              step="0.01" 
                              min="0.5" 
                              max="2" 
                              class="w-14 px-2 py-1 text-center border-y border-gray-200 text-xs"
                            />
                            <button 
                              @click="incrementMultiplier('k')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-r text-gray-600"
                            >
                              <PlusIcon class="h-3 w-3" />
                            </button>
                          </div>
                        </div>
                        <div class="relative h-7 flex items-center">
                          <!-- Min and max labels -->
                          <span class="absolute left-0 -top-1 text-[10px] text-gray-400">0.5x</span>
                          <span class="absolute right-0 -top-1 text-[10px] text-gray-400">2.0x</span>
                          
                          <!-- Slider track background -->
                          <div class="absolute top-1/2 -translate-y-1/2 w-full h-1.5 bg-gray-200 rounded-full"></div>
                          
                          <!-- Slider track fill -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 h-1.5 bg-purple-500 rounded-l-full" 
                            :style="{ width: `${((calibration.k.multiplier - 0.5) / 1.5) * 100}%`, left: '0' }"
                          ></div>
                          
                          <!-- Slider thumb with shadow and border -->
                          <div 
                            class="absolute top-0 w-5 h-5 bg-white rounded-full shadow-md border-2 border-purple-500 z-10 transform -translate-y-1/2" 
                            :style="{ left: `calc(${((calibration.k.multiplier - 0.5) / 1.5) * 100}% - 10px)`, top: '50%' }"
                          ></div>
                          
                          <!-- Actual range input (invisible but functional) -->
                          <input 
                            v-model.number="calibration.k.multiplier" 
                            type="range" 
                            min="0.5" 
                            max="2" 
                            step="0.01" 
                            class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer z-20"
                          />
                        </div>
                      </div>
                      
                      <!-- Offset control with redesigned slider -->
                      <div>
                        <div class="flex items-center justify-between mb-2">
                          <span class="text-xs text-gray-600">Offset (mg/kg)</span>
                          <div class="flex items-center">
                            <button 
                              @click="decrementOffset('k')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-l text-gray-600"
                            >
                              <MinusIcon class="h-3 w-3" />
                            </button>
                            <input 
                              v-model.number="calibration.k.offset" 
                              type="number" 
                              step="1" 
                              min="-50" 
                              max="50" 
                              class="w-14 px-2 py-1 text-center border-y border-gray-200 text-xs"
                            />
                            <button 
                              @click="incrementOffset('k')" 
                              class="w-5 h-5 flex items-center justify-center bg-gray-100 hover:bg-gray-200 rounded-r text-gray-600"
                            >
                              <PlusIcon class="h-3 w-3" />
                            </button>
                          </div>
                        </div>
                        <div class="relative h-7 flex items-center">
                          <!-- Min and max labels -->
                          <span class="absolute left-0 -top-1 text-[10px] text-gray-400">-50</span>
                          <span class="absolute right-0 -top-1 text-[10px] text-gray-400">+50</span>
                          
                          <!-- Center marker -->
                          <div class="absolute top-1/2 -translate-y-1/2 left-1/2 -translate-x-1/2 w-0.5 h-3 bg-gray-300"></div>
                          
                          <!-- Slider track background -->
                          <div class="absolute top-1/2 -translate-y-1/2 w-full h-1.5 bg-gray-200 rounded-full"></div>
                          
                          <!-- Slider track fill -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 h-1.5 bg-purple-500" 
                            :style="calibration.k.offset >= 0 ? 
                              { width: `${(calibration.k.offset / 100) * 50}%`, left: '50%' } : 
                              { width: `${(Math.abs(calibration.k.offset) / 100) * 50}%`, right: '50%' }"
                            :class="calibration.k.offset >= 0 ? 'rounded-r-full' : 'rounded-l-full'"
                          ></div>
                          
                          <!-- Slider thumb with shadow and border -->
                          <div 
                            class="absolute top-1/2 -translate-y-1/2 w-5 h-5 bg-white rounded-full shadow-md border-2 border-purple-500 z-10" 
                            :style="{ left: `calc(${((calibration.k.offset + 50) / 100) * 100}% - 10px)` }"
                          ></div>
                          
                          <!-- Actual range input (invisible but functional) -->
                          <input 
                            v-model.number="calibration.k.offset" 
                            type="range" 
                            min="-50" 
                            max="50" 
                            step="1" 
                            class="absolute top-0 left-0 w-full h-full opacity-0 cursor-pointer z-20"
                          />
                        </div>
                      </div>
                    </div>
                    
                    <!-- Calibrated value indicator -->
                    <div class="mt-4 pt-3 border-t border-gray-100">
                      <div class="flex items-center justify-between">
                        <span class="text-xs text-gray-500">Calibrated Value:</span>
                        <span class="text-sm font-medium text-gray-800">{{ calibratedValues.k }} mg/kg</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Right Column: Calibrated Values with refined cards -->
              <div class="bg-white rounded-xl p-4 border border-gray-100 shadow-sm">
                <h2 class="text-sm font-medium text-gray-800 mb-3">Calibrated Values</h2>
                
                <!-- NPK Value Cards with refined design -->
                <div class="space-y-3 mb-5">
                  <!-- Nitrogen Card -->
                  <div class="bg-white border border-gray-100 rounded-lg p-3 flex items-center shadow-sm hover:shadow-md transition-shadow">
                    <div class="w-10 h-10 rounded-full bg-green-50 flex items-center justify-center mr-3 border border-green-100">
                      <span class="text-green-600 font-medium text-sm">N</span>
                    </div>
                    <div class="flex-1">
                      <div class="flex justify-between items-center">
                        <span class="text-xs text-gray-500">Nitrogen</span>
                        <span class="text-[10px] text-gray-400">Raw: {{ rawValues.n }} mg/kg</span>
                      </div>
                      <div class="flex justify-between items-center mt-0.5">
                        <span class="text-base font-semibold text-gray-800">{{ calibratedValues.n }} mg/kg</span>
                        <span 
                          class="text-[10px] px-1.5 py-0.5 rounded-full" 
                          :class="getDifferenceClass(calibratedValues.n - rawValues.n)"
                        >
                          {{ getDifferenceText(calibratedValues.n - rawValues.n) }}
                        </span>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Phosphorus Card -->
                  <div class="bg-white border border-gray-100 rounded-lg p-3 flex items-center shadow-sm hover:shadow-md transition-shadow">
                    <div class="w-10 h-10 rounded-full bg-blue-50 flex items-center justify-center mr-3 border border-blue-100">
                      <span class="text-blue-600 font-medium text-sm">P</span>
                    </div>
                    <div class="flex-1">
                      <div class="flex justify-between items-center">
                        <span class="text-xs text-gray-500">Phosphorus</span>
                        <span class="text-[10px] text-gray-400">Raw: {{ rawValues.p }} mg/kg</span>
                      </div>
                      <div class="flex justify-between items-center mt-0.5">
                        <span class="text-base font-semibold text-gray-800">{{ calibratedValues.p }} mg/kg</span>
                        <span 
                          class="text-[10px] px-1.5 py-0.5 rounded-full" 
                          :class="getDifferenceClass(calibratedValues.p - rawValues.p)"
                        >
                          {{ getDifferenceText(calibratedValues.p - rawValues.p) }}
                        </span>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Potassium Card -->
                  <div class="bg-white border border-gray-100 rounded-lg p-3 flex items-center shadow-sm hover:shadow-md transition-shadow">
                    <div class="w-10 h-10 rounded-full bg-purple-50 flex items-center justify-center mr-3 border border-purple-100">
                      <span class="text-purple-600 font-medium text-sm">K</span>
                    </div>
                    <div class="flex-1">
                      <div class="flex justify-between items-center">
                        <span class="text-xs text-gray-500">Potassium</span>
                        <span class="text-[10px] text-gray-400">Raw: {{ rawValues.k }} mg/kg</span>
                      </div>
                      <div class="flex justify-between items-center mt-0.5">
                        <span class="text-base font-semibold text-gray-800">{{ calibratedValues.k }} mg/kg</span>
                        <span 
                          class="text-[10px] px-1.5 py-0.5 rounded-full" 
                          :class="getDifferenceClass(calibratedValues.k - rawValues.k)"
                        >
                          {{ getDifferenceText(calibratedValues.k - rawValues.k) }}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Calibration Profiles with refined design -->
                <div v-if="advancedMode">
                  <div class="flex items-center justify-between mb-2.5">
                    <h3 class="text-xs font-medium text-gray-700">Calibration Profiles</h3>
                    <div class="h-px flex-1 bg-gray-100 ml-2"></div>
                  </div>
                  
                  <div class="space-y-3 mb-5">
                    <div class="flex items-center space-x-2">
                      <input 
                        v-model="profileName" 
                        type="text" 
                        placeholder="Profile name" 
                        class="flex-1 px-2.5 py-1.5 border border-gray-200 rounded-lg text-xs focus:outline-none focus:ring-1 focus:ring-emerald-500 focus:border-emerald-500"
                      />
                      <button 
                        @click="saveProfile" 
                        class="px-3 py-1.5 bg-emerald-500 hover:bg-emerald-600 text-white rounded-lg transition-colors duration-200 text-xs font-medium shadow-sm"
                        :disabled="!profileName.trim()"
                        :class="{'opacity-50 cursor-not-allowed': !profileName.trim()}"
                      >
                        Save
                      </button>
                    </div>
                    
                    <div v-if="savedProfiles.length === 0" class="text-center py-4 text-gray-400 text-xs bg-gray-50 rounded-lg border border-gray-100">
                      <SaveIcon class="h-5 w-5 mx-auto mb-1.5 text-gray-300" />
                      No saved profiles yet
                    </div>
                    
                    <div v-else class="space-y-1.5 max-h-32 overflow-y-auto pr-1">
                      <div 
                        v-for="(profile, index) in savedProfiles" 
                        :key="index"
                        class="flex items-center justify-between p-2 bg-gray-50 rounded-lg border border-gray-100 hover:bg-gray-100 transition-colors"
                      >
                        <span class="text-xs font-medium text-gray-700">{{ profile.name }}</span>
                        <div class="flex items-center space-x-1.5">
                          <button 
                            @click="loadProfile(index)" 
                            class="p-1 text-blue-500 hover:text-blue-700 hover:bg-blue-50 rounded transition-colors"
                            title="Load profile"
                          >
                            <DownloadIcon class="h-3.5 w-3.5" />
                          </button>
                          <button 
                            @click="deleteProfile(index)" 
                            class="p-1 text-red-500 hover:text-red-700 hover:bg-red-50 rounded transition-colors"
                            title="Delete profile"
                          >
                            <TrashIcon class="h-3.5 w-3.5" />
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  
                </div>
                
                <!-- Data visualization preview (when not in advanced mode) -->
                <div v-if="!advancedMode" class="mt-4">
                  <div class="flex items-center justify-between mb-2.5">
                    <h3 class="text-xs font-medium text-gray-700">NPK Distribution</h3>
                    <div class="h-px flex-1 bg-gray-100 ml-2"></div>
                  </div>
                  
                  <div class="bg-white border border-gray-100 rounded-lg p-3 shadow-sm">
                    <div class="flex items-center justify-between mb-3">
                      <div class="flex items-center space-x-3">
                        <div class="flex items-center">
                          <div class="w-2.5 h-2.5 rounded-full bg-green-500 mr-1.5"></div>
                          <span class="text-[10px] text-gray-600">N</span>
                        </div>
                        <div class="flex items-center">
                          <div class="w-2.5 h-2.5 rounded-full bg-blue-500 mr-1.5"></div>
                          <span class="text-[10px] text-gray-600">P</span>
                        </div>
                        <div class="flex items-center">
                          <div class="w-2.5 h-2.5 rounded-full bg-purple-500 mr-1.5"></div>
                          <span class="text-[10px] text-gray-600">K</span>
                        </div>
                      </div>
                      <span class="text-[10px] text-gray-400">mg/kg</span>
                    </div>
                    
                    <!-- Simple bar chart visualization -->
                    <div class="h-24 flex items-end justify-around">
                      <div class="flex flex-col items-center space-y-1 w-16">
                        <div class="w-8 bg-green-500 rounded-t transition-all duration-500" 
                             :style="{ height: `${(calibratedValues.n / 200) * 100}%` }"></div>
                        <span class="text-[10px] text-gray-500">{{ calibratedValues.n }}</span>
                      </div>
                      <div class="flex flex-col items-center space-y-1 w-16">
                        <div class="w-8 bg-blue-500 rounded-t transition-all duration-500" 
                             :style="{ height: `${(calibratedValues.p / 200) * 100}%` }"></div>
                        <span class="text-[10px] text-gray-500">{{ calibratedValues.p }}</span>
                      </div>
                      <div class="flex flex-col items-center space-y-1 w-16">
                        <div class="w-8 bg-purple-500 rounded-t transition-all duration-500" 
                             :style="{ height: `${(calibratedValues.k / 200) * 100}%` }"></div>
                        <span class="text-[10px] text-gray-500">{{ calibratedValues.k }}</span>
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
import { ref, computed, watch, onMounted } from 'vue';
import { 
  ChevronRight, 
  Check as CheckIcon, 
  RefreshCw as RefreshCwIcon,
  Sliders as SlidersIcon,
  Save as SaveIcon,
  Download as DownloadIcon,
  Trash as TrashIcon,
  Plus as PlusIcon,
  Minus as MinusIcon
} from 'lucide-vue-next';
import Sidebar from '../layout/Sidebar.vue';

// Raw sensor values (from your actual sensor data)
const rawValues = ref({
  n: 120, // Nitrogen in mg/kg
  p: 50,  // Phosphorus in mg/kg
  k: 130  // Potassium in mg/kg
});

// UI state
const advancedMode = ref(false);
const selectedSoilType = ref('');
const profileName = ref('');
const savedProfiles = ref([]);


// Soil types with predefined calibration values
const soilTypes = ref([
  { 
    type: 'Clay', 
    color: '#8B4513',
    calibration: {
      n: { multiplier: 1.1, offset: 0 },
      p: { multiplier: 0.95, offset: 0 },
      k: { multiplier: 1.0, offset: 0 }
    }
  },
  { 
    type: 'Sandy', 
    color: '#F5DEB3',
    calibration: {
      n: { multiplier: 0.9, offset: 5 },
      p: { multiplier: 1.05, offset: 0 },
      k: { multiplier: 0.95, offset: 0 }
    }
  },
  { 
    type: 'Loamy', 
    color: '#A0522D',
    calibration: {
      n: { multiplier: 1.0, offset: 0 },
      p: { multiplier: 1.0, offset: 0 },
      k: { multiplier: 1.0, offset: 0 }
    }
  },
  { 
    type: 'Silty', 
    color: '#D2B48C',
    calibration: {
      n: { multiplier: 0.95, offset: 0 },
      p: { multiplier: 1.1, offset: 0 },
      k: { multiplier: 1.05, offset: 0 }
    }
  },
  { 
    type: 'Peaty', 
    color: '#654321',
    calibration: {
      n: { multiplier: 1.2, offset: -5 },
      p: { multiplier: 0.9, offset: 0 },
      k: { multiplier: 0.85, offset: 5 }
    }
  },
  { 
    type: 'Chalky', 
    color: '#E5E4E2',
    calibration: {
      n: { multiplier: 0.85, offset: 10 },
      p: { multiplier: 1.15, offset: -5 },
      k: { multiplier: 1.1, offset: 0 }
    }
  },
  { 
    type: 'Custom', 
    color: '#808080',
    calibration: {
      n: { multiplier: 1.0, offset: 0 },
      p: { multiplier: 1.0, offset: 0 },
      k: { multiplier: 1.0, offset: 0 }
    }
  }
]);

// Current calibration settings
const calibration = ref({
  n: { multiplier: 1.0, offset: 0 },
  p: { multiplier: 1.0, offset: 0 },
  k: { multiplier: 1.0, offset: 0 }
});

// Computed calibrated values
const calibratedValues = computed(() => {
  return {
    n: Math.round((rawValues.value.n * calibration.value.n.multiplier) + calibration.value.n.offset),
    p: Math.round((rawValues.value.p * calibration.value.p.multiplier) + calibration.value.p.offset),
    k: Math.round((rawValues.value.k * calibration.value.k.multiplier) + calibration.value.k.offset)
  };
});

// Increment/decrement functions for better UX
const incrementMultiplier = (element) => {
  const value = calibration.value[element].multiplier;
  if (value < 2) {
    calibration.value[element].multiplier = Math.min(2, parseFloat((value + 0.01).toFixed(2)));
  }
};

const decrementMultiplier = (element) => {
  const value = calibration.value[element].multiplier;
  if (value > 0.5) {
    calibration.value[element].multiplier = Math.max(0.5, parseFloat((value - 0.01).toFixed(2)));
  }
};

const incrementOffset = (element) => {
  const value = calibration.value[element].offset;
  if (value < 50) {
    calibration.value[element].offset = Math.min(50, value + 1);
  }
};

const decrementOffset = (element) => {
  const value = calibration.value[element].offset;
  if (value > -50) {
    calibration.value[element].offset = Math.max(-50, value - 1);
  }
};

// Select soil type and apply its calibration
const selectSoilType = (type) => {
  selectedSoilType.value = type;
  const soilType = soilTypes.value.find(soil => soil.type === type);
  if (soilType) {
    calibration.value = JSON.parse(JSON.stringify(soilType.calibration));
  }
};

// Reset to default values
const resetToDefault = () => {
  selectedSoilType.value = '';
  calibration.value = {
    n: { multiplier: 1.0, offset: 0 },
    p: { multiplier: 1.0, offset: 0 },
    k: { multiplier: 1.0, offset: 0 }
  };
};

// Save current calibration as a profile
const saveProfile = () => {
  if (!profileName.value.trim()) return;
  
  savedProfiles.value.push({
    name: profileName.value,
    calibration: JSON.parse(JSON.stringify(calibration.value)),
    soilType: selectedSoilType.value
  });
  
  // Save to localStorage
  localStorage.setItem('npkCalibrationProfiles', JSON.stringify(savedProfiles.value));
  
  // Reset profile name
  profileName.value = '';
};

// Load a saved profile
const loadProfile = (index) => {
  const profile = savedProfiles.value[index];
  if (profile) {
    calibration.value = JSON.parse(JSON.stringify(profile.calibration));
    selectedSoilType.value = profile.soilType;
  }
};

// Delete a saved profile
const deleteProfile = (index) => {
  savedProfiles.value.splice(index, 1);
  localStorage.setItem('npkCalibrationProfiles', JSON.stringify(savedProfiles.value));
};



// Helper function to get difference class
const getDifferenceClass = (diff) => {
  if (diff > 0) return 'bg-green-50 text-green-600 border border-green-100';
  if (diff < 0) return 'bg-red-50 text-red-600 border border-red-100';
  return 'bg-gray-50 text-gray-600 border border-gray-100';
};

// Helper function to get difference text
const getDifferenceText = (diff) => {
  if (diff > 0) return `+${diff}`;
  return diff;
};

// Load saved profiles from localStorage on mount
onMounted(() => {
  const savedProfilesData = localStorage.getItem('npkCalibrationProfiles');
  if (savedProfilesData) {
    try {
      savedProfiles.value = JSON.parse(savedProfilesData);
    } catch (e) {
      console.error('Error loading saved profiles:', e);
    }
  }
});
</script>

<style>
/* Hide default slider appearance */
input[type="range"] {
  -webkit-appearance: none;
  appearance: none;
  background: transparent;
  cursor: pointer;
  width: 100%;
  height: 100%;
}

/* Remove default focus styles */
input[type="range"]:focus {
  outline: none;
}

/* Hide default thumb in Firefox */
input[type="range"]::-moz-range-thumb {
  opacity: 0;
  width: 0;
  height: 0;
}

/* Hide default thumb in Webkit */
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  opacity: 0;
  width: 0;
  height: 0;
}

/* Ensure smooth transitions */
* {
  transition: all 0.2s ease;
}

/* Improve focus styles for accessibility */
input:focus, button:focus, select:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(0, 167, 111, 0.2);
}

/* Improve button hover effects */
button {
  transition: all 0.2s ease;
}

button:active {
  transform: scale(0.98);
}

/* Improve scrollbar styling */
::-webkit-scrollbar {
  width: 4px;
  height: 4px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #9ca3af;
}

/* Add Inter font for better typography */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.font-inter {
  font-family: 'Inter', sans-serif;
}

/* Add subtle hover effects to cards */
.hover\:shadow-md {
  transition: box-shadow 0.3s ease, transform 0.2s ease;
}

.hover\:shadow-md:hover {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transform: translateY(-1px);
}

/* Improve number input appearance */
input[type="number"] {
  -moz-appearance: textfield;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Add animations for slider thumbs */
@keyframes pulse {
  0% { transform: scale(1) translateY(-50%); }
  50% { transform: scale(1.05) translateY(-50%); }
  100% { transform: scale(1) translateY(-50%); }
}

.slider-thumb-active {
  animation: pulse 1s infinite;
}
</style>
