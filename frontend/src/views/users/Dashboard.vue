<template>
  <div class="flex h-screen bg-[#f8f9fa] font-poppins">
    <Sidebar />
    <!-- Main Content -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <!-- Dashboard Content -->
      <main class="flex-1 overflow-y-auto bg-gradient-to-br from-green-50 to-emerald-50 p-6 relative">
        <!-- Content Container -->
        <div class="max-w-7xl mx-auto relative z-10 ml-12">
          <!-- Top Metrics Cards -->
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4 mb-8">
            <!-- Nitrogen Level -->
            <div class="bg-white/60 backdrop-blur-sm rounded-xl p-4 border border-green-100">
              <div class="flex items-center justify-between mb-2">
                <Leaf class="h-5 w-5 text-green-600" />
                <span class="text-xs font-medium text-green-600">N</span>
              </div>
              <div class="text-2xl font-bold text-gray-800">96.01</div>
              <div class="text-xs text-gray-500">Nitrogen Level (mg/kg)</div>
            </div>

            <!-- Phosphorus Level -->
            <div class="bg-white/60 backdrop-blur-sm rounded-xl p-4 border border-blue-100">
              <div class="flex items-center justify-between mb-2">
                <TestTube class="h-5 w-5 text-blue-600" />
                <span class="text-xs font-medium text-blue-600">P</span>
              </div>
              <div class="text-2xl font-bold text-gray-800">22.85</div>
              <div class="text-xs text-gray-500">Phosphorus Level (mg/kg)</div>
            </div>

            <!-- Potassium Level -->
            <div class="bg-white/60 backdrop-blur-sm rounded-xl p-4 border border-purple-100">
              <div class="flex items-center justify-between mb-2">
                <TestTubes class="h-5 w-5 text-purple-600" />
                <span class="text-xs font-medium text-purple-600">K</span>
              </div>
              <div class="text-2xl font-bold text-gray-800">87.04</div>
              <div class="text-xs text-gray-500">Potassium Level (mg/kg)</div>
            </div>

            <!-- Soil pH Level -->
            <div class="bg-white/60 backdrop-blur-sm rounded-xl p-4 border border-orange-100">
              <div class="flex items-center justify-between mb-2">
                <Beaker class="h-5 w-5 text-orange-600" />
                <span class="text-xs font-medium text-orange-600">pH</span>
              </div>
              <div class="text-2xl font-bold text-gray-800">7.22</div>
              <div class="text-xs text-gray-500">Soil pH Level</div>
            </div>

            <!-- Temperature -->
            <div class="bg-white/60 backdrop-blur-sm rounded-xl p-4 border border-red-100">
              <div class="flex items-center justify-between mb-2">
                <Thermometer class="h-5 w-5 text-red-600" />
                <span class="text-xs font-medium text-red-600">Temp</span>
              </div>
              <div class="text-2xl font-bold text-gray-800">32.52</div>
              <div class="text-xs text-gray-500">Temperature (°C)</div>
            </div>

            <!-- Humidity -->
            <div class="bg-white/60 backdrop-blur-sm rounded-xl p-4 border border-sky-100">
              <div class="flex items-center justify-between mb-2">
                <Droplets class="h-5 w-5 text-sky-600" />
                <span class="text-xs font-medium text-sky-600">RH</span>
              </div>
              <div class="text-2xl font-bold text-gray-800">76.68</div>
              <div class="text-xs text-gray-500">Humidity (%)</div>
            </div>
          </div>

          <div class="flex gap-8">
            <!-- Left Section - Metrics -->
            <div class="flex-1">
              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Regular Cards with Line Charts -->
                <template v-for="(metric, index) in metrics" :key="index">
                  <div 
                    v-if="metric.type !== 'pie'"
                    class="bg-white rounded-xl shadow-md p-6"
                  >
                    <div class="flex justify-between items-start mb-4">
                      <div>
                        <h3 class="text-lg font-medium text-gray-800">{{ metric.title }}</h3>
                        <p class="text-sm text-gray-500">Overview</p>
                      </div>
                      <component :is="metric.icon" :class="`h-6 w-6 ${metric.iconColor}`" />
                    </div>
                    <div class="text-3xl font-bold text-gray-800 mb-4">{{ metric.value }}</div>
                    <div class="h-[200px]">
                      <canvas :ref="el => { if (el) lineChartRefs[index] = el }"></canvas>
                    </div>
                  </div>
                </template>

                <!-- Motor Status Card with Pie Chart -->
                <div class="bg-white rounded-xl shadow-md p-6">
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-gray-800">Motor Status</h3>
                      <p class="text-sm text-gray-500">Overview</p>
                    </div>
                    <Power class="h-6 w-6 text-purple-500" />
                  </div>
                  <div class="h-[200px] relative">
                    <canvas ref="pieChartRef"></canvas>
                  </div>
                  <div class="flex justify-center gap-4 mt-4">
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full bg-[#2196F3] mr-2"></div>
                      <span class="text-sm text-gray-600">OFF (86.5%)</span>
                    </div>
                    <div class="flex items-center">
                      <div class="w-3 h-3 rounded-full bg-[#4CAF50] mr-2"></div>
                      <span class="text-sm text-gray-600">ON (13.5%)</span>
                    </div>
                  </div>
                </div>

                <!-- Water Level Card -->
                <div class="bg-white rounded-3xl p-8 shadow-xl">
                  <div class="flex items-center justify-between mb-4">
                    <div class="text-xl font-bold mb-14">Water Level</div>
                    <Waves class="w-6 h-6 text-[#4ade80]" />
                  </div>
                  <div class="text-sm text-gray-500 mb-6">As of now:</div>
                  
                  <!-- Water Level Pie Chart -->
                  <div class="relative w-48 h-48 mx-auto">
                    <div class="absolute inset-0 rounded-full bg-gray-100"></div>
                    <div 
                      class="absolute inset-0 rounded-full transition-all duration-1000"
                      :style="{
                        background: `conic-gradient(#3b82f6 ${waterLevel * 3.6}deg, #f3f4f6 ${waterLevel * 3.6}deg)`
                      }"
                    ></div>
                    <div class="absolute inset-4 rounded-full bg-white flex items-center justify-center">
                      <span class="text-3xl font-bold text-gray-800">{{ waterLevel }}%</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Overall Performance Section -->
          <div class="bg-white rounded-xl shadow-md p-6 mt-8">
            <div class="flex justify-between items-start mb-6">
              <div>
                <h3 class="text-lg font-medium text-gray-800">Overall Performance</h3>
                <p class="text-sm text-gray-500">Last 7 days overview</p>
              </div>
              <div class="flex flex-wrap gap-4">
                <div class="flex items-center">
                  <div class="w-3 h-3 rounded-full bg-purple-400 mr-2"></div>
                  <span class="text-sm text-gray-600">Temperature</span>
                </div>
                <div class="flex items-center">
                  <div class="w-3 h-3 rounded-full bg-orange-400 mr-2"></div>
                  <span class="text-sm text-gray-600">Humidity</span>
                </div>
                <div class="flex items-center">
                  <div class="w-3 h-3 rounded-full bg-green-400 mr-2"></div>
                  <span class="text-sm text-gray-600">Soil Moisture</span>
                </div>
                <div class="flex items-center">
                  <div class="w-3 h-3 rounded-full bg-blue-400 mr-2"></div>
                  <span class="text-sm text-gray-600">Water Level</span>
                </div>
                <div class="flex items-center">
                  <div class="w-3 h-3 rounded-full bg-red-400 mr-2"></div>
                  <span class="text-sm text-gray-600">Motor Status</span>
                </div>
              </div>
            </div>
            <div class="h-[400px]">
              <canvas ref="performanceChartRef"></canvas>
            </div>
          </div>
        </div>
      </main>
    </div>
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
  Wheat,
  MoreHorizontal,
  Leaf,
  TreePine,
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
    iconColor: 'text-green-600',
    type: 'line',
    chartData: {
      labels: ['0', '10', '20', '30', '40', '50'],
      datasets: [{
        data: [30, 40, 45, 50, 45, 45],
        borderColor: '#4CAF50',
        backgroundColor: 'rgba(76, 175, 80, 0.1)',
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
        borderColor: '#FF5722',
        backgroundColor: 'rgba(255, 87, 34, 0.1)',
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
        borderColor: '#2196F3',
        backgroundColor: 'rgba(33, 150, 243, 0.1)',
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
  // Initialize line charts
  metrics.forEach((metric, index) => {
    if (metric.type === 'line' && lineChartRefs.value[index]) {
      new Chart(lineChartRefs.value[index].getContext('2d'), {
        type: 'line',
        data: metric.chartData,
        options: lineChartOptions
      });
    }
  });

  // Initialize pie chart for motor status
  if (pieChartRef.value) {
    new Chart(pieChartRef.value.getContext('2d'), {
      type: 'pie',
      data: {
        labels: ['OFF', 'ON'],
        datasets: [{
          data: [86.5, 13.5],
          backgroundColor: ['#2196F3', '#4CAF50'],
          borderWidth: 0
        }]
      },
      options: pieChartOptions
    });
  }

  // Initialize performance chart
  if (performanceChartRef.value) {
    new Chart(performanceChartRef.value.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['19 July', '20 July', '21 July', '22 July', '23 July', '24 July', '25 July', '26 July'],
        datasets: [
          {
            label: 'Temperature',
            data: [45, 42, 40, 38, 32, 35, 38, 40],
            borderColor: '#A78BFA', // Purple
            backgroundColor: 'rgba(167, 139, 250, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#A78BFA'
          },
          {
            label: 'Humidity',
            data: [35, 38, 32, 28, 25, 30, 35, 38],
            borderColor: '#FB923C', // Orange
            backgroundColor: 'rgba(251, 146, 60, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#FB923C'
          },
          {
            label: 'Soil Moisture',
            data: [50, 48, 52, 55, 49, 47, 51, 53],
            borderColor: '#4ADE80', // Green
            backgroundColor: 'rgba(74, 222, 128, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#4ADE80'
          },
          {
            label: 'Water Level',
            data: [70, 72, 68, 75, 73, 71, 69, 74],
            borderColor: '#60A5FA', // Blue
            backgroundColor: 'rgba(96, 165, 250, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#60A5FA'
          },
          {
            label: 'Motor Status',
            data: [0, 1, 0, 1, 1, 0, 1, 0],
            borderColor: '#F87171', // Red
            backgroundColor: 'rgba(248, 113, 113, 0.1)',
            fill: true,
            tension: 0.4,
            borderWidth: 2,
            pointRadius: 4,
            pointBackgroundColor: '#F87171',
            stepped: true
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
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
            displayColors: true,
            callbacks: {
              label: function(context) {
                let label = context.dataset.label || '';
                if (label) {
                  label += ': ';
                }
                if (context.parsed.y !== null) {
                  if (label === 'Motor Status: ') {
                    label += context.parsed.y === 1 ? 'ON' : 'OFF';
                  } else {
                    label += context.parsed.y;
                  }
                }
                return label;
              }
            }
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
</style>