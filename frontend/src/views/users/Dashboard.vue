<template>
    <div class="flex h-screen bg-[#f8f9fa] font-poppins">
      <!-- Sidebar -->
      <div class="hidden md:flex md:flex-shrink-0">
        <div :class="[
          'flex flex-col bg-[#002B1D] transition-all duration-300 ease-in-out rounded-tr-3xl rounded-br-3xl relative',
          isCollapsed ? 'w-20' : 'w-[280px]'
        ]">
          <!-- Logo Section -->
          <div class="flex flex-col items-center px-6 py-4 border-b border-[#1a4d4f]">
            <div :class="['flex items-center justify-center transition-all duration-300', isCollapsed ? 'w-16 h-16' : 'w-24 h-24']">
              <img 
                src="/images/project-israel-logo-removebg-preview.png" 
                alt="Project Israel" 
                class="w-full h-full object-contain"
              />
            </div>
            <span class="text-white text-2xl font-semibold mt-4" :class="[isCollapsed ? 'hidden' : 'block']">
              Project Israel
            </span>
          </div>
  
          <!-- Toggle Button - Outside Sidebar -->
          <button 
            @click="toggleSidebar"
            class="absolute -right-12 top-12 px-4 py-3 rounded-lg bg-[#002B1D] hover:bg-[#1a4d4f] text-gray-300 hover:text-[#8FE3CF] transition-colors shadow-lg"
          >
            <Menu v-if="isCollapsed" class="h-5 w-5" />
            <PanelLeftClose v-else class="h-5 w-5" />
          </button>
  
          <!-- Navigation -->
          <nav class="flex-1 px-6 py-8">
            <div v-show="!isCollapsed" class="mb-8">
              <h3 class="text-sm font-semibold text-gray-400 uppercase tracking-wider">
                MENU
              </h3>
            </div>
            
            <div class="space-y-6">
              <router-link 
                v-for="item in menuItems" 
                :key="item.name"
                :to="item.href"
                :class="[
                  'flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-colors duration-150',
                  isCollapsed ? 'justify-center' : '',
                  item.current ? 'bg-[#1a4d4f] text-white' : 'text-gray-300 hover:bg-[#1a4d4f] hover:text-white'
                ]"
              >
                <component 
                  :is="item.icon" 
                  :class="[
                    'flex-shrink-0 h-5 w-5',
                    item.current ? 'text-[#8FE3CF]' : 'text-gray-400 group-hover:text-[#8FE3CF]'
                  ]"
                />
                <span 
                  :class="['ml-4 transition-opacity duration-300', isCollapsed ? 'hidden' : 'block']"
                >
                  {{ item.name }}
                </span>
              </router-link>
            </div>
          </nav>
  
          <!-- Profile Section --><!-- Profile Section -->
            <div class="border-t border-[#1a4d4f] p-6">
            <div class="flex items-center" :class="{ 'justify-center': isCollapsed }">
                <div :class="['flex items-center justify-center transition-all duration-300', isCollapsed ? 'w-16 h-16' : 'w-12 h-12']">
                <img 
                    src="/images/profile-example.jpg" 
                    class="w-full h-full rounded-full object-cover border-2 border-[#1a4d4f]" 
                    alt="Profile" 
                />
                </div>
                <div v-if="!isCollapsed" class="ml-3">
                <p class="text-sm font-medium text-white">John Doe</p>
                <p class="text-xs text-gray-400">Farmer</p>
                </div>
            </div>
            </div>
        </div>
      </div>
  
      <!-- Main Content -->
      <div class="flex-1 flex flex-col overflow-hidden">
        <!-- Search Bar -->
        <div class="bg-white border-b shadow-sm">
          <div class="px-6 py-4 flex justify-end">
            <div class="relative w-72">
              <input
                type="text"
                placeholder="Search..."
                class="w-full pl-10 pr-4 py-3 rounded-full border-2 border-gray-200 focus:outline-none focus:border-[#002B1D] text-base font-medium"
              />
              <Search class="absolute left-3 top-3.5 h-5 w-5 text-gray-600" />
            </div>
          </div>
        </div>
  
        <!-- Dashboard Content -->
        <main class="flex-1 overflow-y-auto bg-[#f8f9fa] p-6">
          <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <!-- Regular Cards with Line Charts -->
              <template v-for="(metric, index) in metrics" :key="index">
                <div 
                  v-if="metric.type !== 'pie'"
                  class="bg-white rounded-lg shadow-md p-6"
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
  
                <!-- Motor Status Card with Pie Chart -->
                <div 
                  v-else
                  class="bg-white rounded-lg shadow-md p-6"
                >
                  <div class="flex justify-between items-start mb-4">
                    <div>
                      <h3 class="text-lg font-medium text-gray-800">{{ metric.title }}</h3>
                      <p class="text-sm text-gray-500">Overview</p>
                    </div>
                    <Power class="h-6 w-6 text-purple-500" />
                  </div>
                  <div class="h-[200px] relative">
                    <canvas :ref="el => { if (el) pieChartRef = el }"></canvas>
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
              </template>
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
    Search, 
    Menu,
    PanelLeftClose,
    Sprout, 
    Thermometer, 
    Droplet, 
    Waves, 
    Power, 
    TreePine,
    TrendingUp,
    LayoutDashboard,
    Brain,
    BarChart2,
    Cpu,
    Database
  } from 'lucide-vue-next';
  
  Chart.register(...registerables);
  
  const isCollapsed = ref(false);
  const toggleSidebar = () => {
    isCollapsed.value = !isCollapsed.value;
  };
  
  const menuItems = [
    { name: 'Overview', href: '/dashboard', icon: LayoutDashboard, current: true },
    { name: 'Crop Prediction', href: '/prediction', icon: Brain, current: false },
    // { name: 'Statistics', href: '/statistics', icon: BarChart2, current: false },
    { name: 'Device Control', href: '/device', icon: Cpu, current: false },
    { name: 'Sensor Data', href: '/sensors', icon: Database, current: false },
    { name: 'Soil Analysis', href: '/soil', icon: Sprout, current: false },
  ];
  
  const lineChartRefs = ref([]);
  const pieChartRef = ref(null);
  
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
    },
    {
      title: 'Water Level',
      value: '75%',
      icon: Waves,
      iconColor: 'text-cyan-500',
      type: 'line',
      chartData: {
        labels: ['0', '10', '20', '30', '40', '50'],
        datasets: [{
          data: [70, 72, 75, 73, 75, 75],
          borderColor: '#00BCD4',
          backgroundColor: 'rgba(0, 188, 212, 0.1)',
          fill: true
        }]
      }
    },
    {
      title: 'Motor Status',
      value: 'Active',
      icon: Power,
      type: 'pie',
      chartData: {
        labels: ['OFF', 'ON'],
        datasets: [{
          data: [86.5, 13.5],
          backgroundColor: ['#2196F3', '#4CAF50'],
          borderWidth: 0
        }]
      }
    },
    {
      title: 'Best Crop',
      value: 'Rice',
      icon: TreePine,
      iconColor: 'text-orange-500',
      type: 'line',
      chartData: {
        labels: ['0', '10', '20', '30', '40', '50'],
        datasets: [{
          data: [80, 85, 90, 88, 92, 90],
          borderColor: '#FF9800',
          backgroundColor: 'rgba(255, 152, 0, 0.1)',
          fill: true
        }]
      }
    }
  ];
  
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
        data: metrics.find(m => m.type === 'pie').chartData,
        options: pieChartOptions
      });
    }
  });
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  
  /* Add any additional custom styles here */
  </style>
  
  