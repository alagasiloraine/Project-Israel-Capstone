<template>
    <div class="flex gap-4 items-center p-4 bg-white/50 rounded-lg">
      <!-- Search Input -->
      <div class="relative flex-1">
        <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
        <input
          type="text"
          placeholder="Search measurements..."
          class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent text-sm text-gray-600 placeholder-gray-400 bg-white"
          v-model="searchQuery"
        />
      </div>
  
      <!-- Filter Button -->
      <div class="relative">
        <button 
          @click="toggleFilter"
          class="flex items-center gap-2 px-4 py-2.5 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50"
        >
          <Filter class="h-4 w-4 text-gray-500" />
          Filter by Range
          <ChevronDown class="h-4 w-4 text-gray-400" :class="{ 'transform rotate-180': isFilterOpen }" />
        </button>
        <!-- Filter Dropdown (to be implemented) -->
      </div>
  
      <!-- Sort Button -->
      <div class="relative">
        <button 
          @click="toggleSort"
          class="flex items-center gap-2 px-4 py-2.5 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50"
        >
          Sort by
          <ChevronDown class="h-4 w-4 text-gray-400" :class="{ 'transform rotate-180': isSortOpen }" />
        </button>
        <!-- Sort Dropdown (to be implemented) -->
      </div>
  
      <!-- Export Button -->
      <button 
        @click="handleExport"
        class="flex items-center gap-2 px-4 py-2.5 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-medium transition-colors"
      >
        <Download class="h-4 w-4" />
        Export
        <ChevronDown class="h-4 w-4" />
      </button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { Search, Filter, ChevronDown, Download } from 'lucide-vue-next'
  
  const searchQuery = ref('')
  const isFilterOpen = ref(false)
  const isSortOpen = ref(false)
  
  const toggleFilter = () => {
    isFilterOpen.value = !isFilterOpen.value
    if (isFilterOpen.value) isSortOpen.value = false
  }
  
  const toggleSort = () => {
    isSortOpen.value = !isSortOpen.value
    if (isSortOpen.value) isFilterOpen.value = false
  }
  
  const handleExport = () => {
    // Export functionality to be implemented
    console.log('Export clicked')
  }
  </script>