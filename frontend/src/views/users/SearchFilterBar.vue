<template>
  <div class="flex gap-6 items-center p-6 bg-gradient-to-br from-green-50 to-emerald-50 shadow-lg rounded-2xl border border-gray-300">
    <!-- Search Input -->
    <div class="relative flex-1">
      <Search class="absolute left-4 top-1/2 transform -translate-y-1/2 h-6 w-6 text-gray-800" />
      <input
        type="text"
        placeholder="Search anything here..."
        class="w-full pl-14 pr-6 py-3 rounded-2xl border-2 border-white focus:outline-none focus:ring-4 focus:ring-green-500 focus:border-transparent text-base text-gray-800 placeholder-gray-500 bg-white shadow-sm"
        v-model="searchQuery"
      />
    </div>

    <!-- Filter Button -->
    <div class="relative">
      <button 
        @click="toggleFilter"
        class="flex items-center gap-3 px-6 py-3 rounded-2xl border-2 border-white bg-white text-base text-gray-800 hover:bg-gradient-to-br hover:from-green-50 hover:to-emerald-50 shadow-md"
      >
        <Filter class="h-5 w-5 text-gray-600" />
        Filter by Range
        <ChevronDown class="h-5 w-5 text-gray-500" :class="{ 'transform rotate-180': isFilterOpen }" />
      </button>
    </div>

    <!-- Sort Button -->
    <div class="relative">
      <button 
        @click="toggleSort"
        class="flex items-center gap-3 px-6 py-3 rounded-2xl border-2 border-white bg-white text-base text-gray-800 hover:bg-gradient-to-br hover:from-green-50 hover:to-emerald-50 shadow-md"
      >
        Sort by
        <ChevronDown class="h-5 w-5 text-gray-500" :class="{ 'transform rotate-180': isSortOpen }" />
      </button>
    </div>

    <!-- Export Button -->
    <button 
      @click="handleExport"
      class="flex items-center gap-3 px-6 py-3 rounded-2xl bg-emerald-500 hover:bg-emerald-600 text-white text-base font-semibold shadow-md transition-transform transform hover:scale-105"
    >
      <Download class="h-5 w-5" />
      Export
      <ChevronDown class="h-5 w-5" />
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
  console.log('Export clicked')
}
</script>