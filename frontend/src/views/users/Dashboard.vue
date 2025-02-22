<template>
  <!-- Changed bg-[#f8f9fa] to bg-green-50 for light green background -->
  <div class="min-h-screen bg-green-50 font-poppins">
    <Sidebar />
    <!-- Main Content -->
    <main class="min-h-screen bg-white"> <!-- White background maintained -->
      <!-- Fixed Navbar Space - matches navbar height -->
      <div class="h-[100px]"></div>
      
      <!-- Container Wrapper with increased spacing and animations -->
      <div class="w-full px-6 pt-14">
        <!-- Main Container with enhanced styling -->
        <div class="bg-white rounded-[12px] shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-gray-200 h-[calc(100vh-180px)] overflow-y-auto transition-all duration-300 ease-in-out hover:shadow-[0_8px_40px_rgb(0,0,0,0.06)]">
          <!-- Content Wrapper with improved padding -->
          <div class="p-8">
            <!-- Top Metrics Cards -->
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-5 mb-8">
              <!-- Nitrogen Level with enhanced glass effect -->
              <div class="group bg-white/95 backdrop-blur-xl rounded-lg p-4 border border-gray-100/20 shadow-[0_8px_20px_rgb(0,0,0,0.06)] transition-all duration-300 hover:shadow-[0_12px_25px_rgb(0,0,0,0.08)] hover:translate-y-[-2px)] hover:bg-white/100">
                <div class="flex items-center justify-between mb-2">
                  <Leaf class="h-5 w-5 text-green-600 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-medium text-green-600">N</span>
                </div>
                <div class="text-2xl font-bold text-gray-800">96.01</div>
                <div class="text-xs text-gray-500">Nitrogen Level (mg/kg)</div>
              </div>

              <!-- Phosphorus Level -->
              <div class="group bg-white/95 backdrop-blur-xl rounded-lg p-4 border border-gray-100/20 shadow-[0_8px_20px_rgb(0,0,0,0.06)] transition-all duration-300 hover:shadow-[0_12px_25px_rgb(0,0,0,0.08)] hover:translate-y-[-2px)] hover:bg-white/100">
                <div class="flex items-center justify-between mb-2">
                  <TestTube class="h-5 w-5 text-blue-600 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-medium text-blue-600">P</span>
                </div>
                <div class="text-2xl font-bold text-gray-800">22.85</div>
                <div class="text-xs text-gray-500">Phosphorus Level (mg/kg)</div>
              </div>

              <!-- Potassium Level -->
              <div class="group bg-white/95 backdrop-blur-xl rounded-lg p-4 border border-gray-100/20 shadow-[0_8px_20px_rgb(0,0,0,0.06)] transition-all duration-300 hover:shadow-[0_12px_25px_rgb(0,0,0,0.08)] hover:translate-y-[-2px)] hover:bg-white/100">
                <div class="flex items-center justify-between mb-2">
                  <TestTubes class="h-5 w-5 text-purple-600 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-medium text-purple-600">K</span>
                </div>
                <div class="text-2xl font-bold text-gray-800">87.04</div>
                <div class="text-xs text-gray-500">Potassium Level (mg/kg)</div>
              </div>

              <!-- Soil pH Level -->
              <div class="group bg-white/95 backdrop-blur-xl rounded-lg p-4 border border-gray-100/20 shadow-[0_8px_20px_rgb(0,0,0,0.06)] transition-all duration-300 hover:shadow-[0_12px_25px_rgb(0,0,0,0.08)] hover:translate-y-[-2px)] hover:bg-white/100">
                <div class="flex items-center justify-between mb-2">
                  <Beaker class="h-5 w-5 text-orange-600 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-medium text-orange-600">pH</span>
                </div>
                <div class="text-2xl font-bold text-gray-800">7.22</div>
                <div class="text-xs text-gray-500">Soil pH Level</div>
              </div>

              <!-- Temperature -->
              <div class="group bg-white/95 backdrop-blur-xl rounded-lg p-4 border border-gray-100/20 shadow-[0_8px_20px_rgb(0,0,0,0.06)] transition-all duration-300 hover:shadow-[0_12px_25px_rgb(0,0,0,0.08)] hover:translate-y-[-2px)] hover:bg-white/100">
                <div class="flex items-center justify-between mb-2">
                  <Thermometer class="h-5 w-5 text-red-600 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-medium text-red-600">Temp</span>
                </div>
                <div class="text-2xl font-bold text-gray-800">32.52</div>
                <div class="text-xs text-gray-500">Temperature (°C)</div>
              </div>

              <!-- Humidity -->
              <div class="group bg-white/95 backdrop-blur-xl rounded-lg p-4 border border-gray-100/20 shadow-[0_8px_20px_rgb(0,0,0,0.06)] transition-all duration-300 hover:shadow-[0_12px_25px_rgb(0,0,0,0.08)] hover:translate-y-[-2px)] hover:bg-white/100">
                <div class="flex items-center justify-between mb-2">
                  <Droplets class="h-5 w-5 text-sky-600 transition-transform duration-300 group-hover:scale-110" />
                  <span class="text-xs font-medium text-sky-600">RH</span>
                </div>
                <div class="text-2xl font-bold text-gray-800">76.68</div>
                <div class="text-xs text-gray-500">Humidity (%)</div>
              </div>
            </div>
  
            <!-- Charts Section with enhanced styling -->
            <div class="grid grid-cols-1 gap-8">
              <!-- First Row - Water Level, Motor Status, and Soil Moisture -->
              <div class="grid grid-cols-4 gap-6">
                <!-- Water Level Card - Takes 1 column -->
                <div class="bg-white rounded-lg p-8 shadow-md border border-gray-200 transition-all duration-300 hover:shadow-lg hover:translate-y-[-2px)]">
                  <div class="flex items-center justify-between mb-4">
                    <div class="text-xl font-bold text-blue-600">Water Level</div>
                    <Waves class="w-6 h-6 text-blue-500 transition-transform duration-300 hover:scale-110" />
                  </div>
                  <div class="text-sm text-blue-600 mb-6">As of now:</div>
                  <div class="relative w-32 h-32 mx-auto transition-transform duration-300 hover:scale-105">
                    <div class="absolute inset-0 rounded-full bg-gray-100"></div>
                    <div 
                      class="absolute inset-0 rounded-full transition-all duration-1000"
                      :style="{
                        background: `conic-gradient(#3b82f6 ${waterLevel * 3.6}deg, #f3f4f6 ${waterLevel * 3.6}deg)`
                      }"
                    ></div>
                    <div class="absolute inset-3 rounded-full bg-white flex items-center justify-center">
                      <span class="text-3xl font-bold text-blue-600">{{ waterLevel }}%</span>
                    </div>
                  </div>
                </div>

                <!-- Motor Status Card - Takes 1 column -->
                <div class="bg-white rounded-lg p-6 shadow-md border border-gray-200 transition-all duration-300 hover:shadow-lg hover:translate-y-[-2px)]">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-purple-600">Motor Status</h3>
                      <p class="text-sm text-purple-500">Overview</p>
                    </div>
                    <Power class="h-6 w-6 text-purple-500 transition-transform duration-300 hover:scale-110" />
                  </div>
                  <div class="h-[200px] relative">
                    <canvas ref="pieChartRef"></canvas>
                  </div>
                  <div class="flex justify-center gap-4 mt-4">
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full bg-purple-300 mr-2"></div>
                      <span class="text-sm text-purple-600">OFF (86.5%)</span>
                    </div>
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full bg-purple-600 mr-2"></div>
                      <span class="text-sm text-purple-600">ON (13.5%)</span>
                    </div>
                  </div>
                </div>

                <!-- Soil Moisture Card - Takes 2 columns -->
                <div class="col-span-2 bg-white rounded-lg p-6 shadow-md border border-gray-200 transition-all duration-300 hover:shadow-lg hover:translate-y-[-2px)]">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-emerald-600">Soil Moisture</h3>
                      <p class="text-sm text-emerald-500">Overview</p>
                    </div>
                    <Sprout class="h-6 w-6 text-emerald-500 transition-transform duration-300 hover:scale-110" />
                  </div>
                  <div class="text-3xl font-bold text-emerald-600 mb-4">{{ metrics[0].value }}</div>
                  <div class="h-[200px]">
                    <canvas :ref="el => { if (el) lineChartRefs[0] = el }"></canvas>
                  </div>
                </div>
              </div>

              <!-- Second Row - Temperature and Soil pH -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Temperature Card -->
                <div 
                  v-if="metrics[1].type === 'line'"
                  class="bg-white rounded-lg p-6 shadow-md border border-gray-200 transition-all duration-300 hover:shadow-lg hover:translate-y-[-2px)]"
                >
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-red-600">{{ metrics[1].title }}</h3>
                      <p class="text-sm text-red-500">Overview</p>
                    </div>
                    <component :is="metrics[1].icon" class="h-6 w-6 text-red-500 transition-transform duration-300 hover:scale-110" />
                  </div>
                  <div class="text-3xl font-bold text-red-600 mb-4">{{ metrics[1].value }}</div>
                  <div class="h-[200px]">
                    <canvas :ref="el => { if (el) lineChartRefs[1] = el }"></canvas>
                  </div>
                </div>

                <!-- Soil pH Card -->
                <div class="bg-white rounded-lg p-6 shadow-md border border-gray-200 transition-all duration-300 hover:shadow-lg hover:translate-y-[-2px)]">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-orange-600">Soil pH</h3>
                      <p class="text-sm text-orange-500">Overview</p>
                    </div>
                    <Beaker class="h-6 w-6 text-orange-500 transition-transform duration-300 hover:scale-110" />
                  </div>
                  <div class="text-3xl font-bold text-orange-600 mb-4">7.22</div>
                  <div class="h-[200px]">
                    <canvas :ref="el => { if (el) lineChartRefs[2] = el }"></canvas>
                  </div>
                </div>
              </div>

              <!-- Third Row - Overall Performance -->
              <div class="bg-white rounded-lg p-6 shadow-md border-2 border-gray-200 transition-all duration-300 hover:shadow-lg hover:translate-y-[-2px)]">
                <div class="flex justify-between items-start mb-6">
                  <div>
                    <h3 class="text-lg font-medium text-gray-800">Overall Performance</h3>
                    <p class="text-sm text-gray-500">NPK Sensor Overview</p>
                  </div>
                  <div class="flex flex-wrap gap-4">
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full bg-green-400 mr-2"></div>
                      <span class="text-sm text-gray-600">Nitrogen</span>
                    </div>
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full bg-blue-400 mr-2"></div>
                      <span class="text-sm text-gray-600">Phosphorus</span>
                    </div>
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full bg-purple-400 mr-2"></div>
                      <span class="text-sm text-gray-600">Potassium</span>
                    </div>
                  </div>
                </div>
                <div class="h-[300px]">
                  <canvas ref="performanceChartRef"></canvas>
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
import { ref, onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';
import { 
  Sprout, 
  Thermometer, 
  Droplet, 
  Droplets,
  Waves, 
  Power,
  Leaf,
  TestTube,
  TestTubes,
  Beaker
} from 'lucide-vue-next';
import Sidebar from '../layout/Sidebar.vue'

Chart.register(...registerables);

const lineChartRefs = ref([]);
const pieChartRef = ref(null);
const performanceChartRef = ref(null);
const waterLevel = ref(75);

const metrics = [
  {
    title: 'Soil Moisture',
    value: '45%',
    icon: Sprout,
    iconColor: 'text-emerald-500',
    type: 'line',
    chartData: {
      labels: ['0', '10', '20', '30', '40', '50'],
      datasets: [{
        data: [30, 40, 45, 50, 45, 45],
        borderColor: '#10b981', // emerald-500
        backgroundColor: 'rgba(16, 185, 129, 0.1)',
        fill: true
      }]
    }
  },
  {
    title: 'Temperature',
    value: '28°C',
    icon: Thermometer,
    iconColor: 'text-red-500',
    type: 'line',
    chartData: {
      labels: ['0', '10', '20', '30', '40', '50'],
      datasets: [{
        data: [25, 27, 28, 28, 29, 28],
        borderColor: '#ef4444', // red-500
        backgroundColor: 'rgba(239, 68, 68, 0.1)',
        fill: true
      }]
    }
  },
  {
    title: 'Humidity',
    value: '65%',
    icon: Droplet,
    iconColor: 'text-blue-500',
    type: 'line',
    chartData: {
      labels: ['0', '10', '20', '30', '40', '50'],
      datasets: [{
        data: [60, 62, 65, 63, 65, 65],
        borderColor: '#3b82f6', // blue-500
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        fill: true
      }]
    }
  }
];

const lineChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    }
  },
  scales: {
    x: {
      display: true,
      grid: {
        display: false
      }
    },
    y: {
      display: true,
      beginAtZero: true,
      max: 100,
      ticks: {
        stepSize: 10
      }
    }
  },
  elements: {
    line: {
      tension: 0.4
    },
    point: {
      radius: 4
    }
  }
};

const pieChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    }
  }
};

onMounted(() => {
  // Initialize line charts with updated colors
  metrics.forEach((metric, index) => {
    if (metric.type === 'line' && lineChartRefs.value[index]) {
      new Chart(lineChartRefs.value[index].getContext('2d'), {
        type: 'line',
        data: metric.chartData,
        options: lineChartOptions
      });
    }
  });

  // Initialize pie chart for motor status with purple theme
  if (pieChartRef.value) {
    new Chart(pieChartRef.value.getContext('2d'), {
      type: 'pie',
      data: {
        labels: ['OFF', 'ON'],
        datasets: [{
          data: [86.5, 13.5],
          backgroundColor: ['#c4b5fd', '#7c3aed'], // purple-300 and purple-600
          borderWidth: 0
        }]
      },
      options: pieChartOptions
    });
  }

  // Initialize performance chart for NPK Sensor
  if (performanceChartRef.value) {
    new Chart(performanceChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['19 July', '20 July', '21 July', '22 July', '23 July', '24 July', '25 July', '26 July'],
        datasets: [
          {
            label: 'Nitrogen',
            data: [45, 42, 40, 38, 32, 35, 38, 40],
            borderColor: '#4ADE80', // Green
            backgroundColor: 'rgba(74, 222, 128, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#4ADE80'
          },
          {
            label: 'Phosphorus',
            data: [35, 38, 32, 28, 25, 30, 35, 38],
            borderColor: '#60A5FA', // Blue
            backgroundColor: 'rgba(96, 165, 250, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#60A5FA'
          },
          {
            label: 'Potassium',
            data: [50, 48, 52, 55, 49, 47, 51, 53],
            borderColor: '#A78BFA', // Purple
            backgroundColor: 'rgba(167, 139, 250, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#A78BFA'
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
            position: 'top'
          },
          tooltip: {
            mode: 'index',
            intersect: false,
            backgroundColor: 'white',
            titleColor: '#374151',
            bodyColor: '#374151',
            borderColor: '#E5E7EB',
            borderWidth: 1,
            padding: 12,
            displayColors: true
          }
        },
        scales: {
          x: {
            grid: {
              display: false
            },
            ticks: {
              color: '#6B7280'
            }
          },
          y: {
            beginAtZero: true,
            max: 100,
            ticks: {
              stepSize: 20,
              color: '#6B7280'
            },
            grid: {
              color: '#E5E7EB'
            }
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });
  }
});
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

.pattern-dots {
  background-image: radial-gradient(currentColor 1px, transparent 1px);
  background-size: calc(10 * 1px) calc(10 * 1px);
}

/* Enhanced scrollbar styling with dark green color */
.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(20, 83, 45, 0.5) transparent; /* Changed to dark green */
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  @apply bg-green-900/50 hover:bg-green-900/70 transition-colors duration-200 rounded-full;
}

/* Add smooth transitions for all elements */
* {
  @apply transition-colors duration-200;
}
</style>