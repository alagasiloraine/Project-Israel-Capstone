<template>
<<<<<<< HEAD
  <div class="flex gap-6 items-center p-6 bg-gradient-to-br from-green-50 to-emerald-50 shadow-lg rounded-2xl border border-gray-300">
    <!-- Search Input -->
    <div class="relative flex-1">
      <Search class="absolute left-4 top-1/2 transform -translate-y-1/2 h-6 w-6 text-gray-800" />
      <input
        type="text"
        placeholder="Search anything here..."
        class="w-full pl-14 pr-6 py-3 rounded-2xl border-2 border-white focus:outline-none focus:ring-4 focus:ring-green-500 focus:border-transparent text-base text-gray-800 placeholder-gray-500 bg-white shadow-sm"
=======
  <div class="flex gap-4 items-center p-4 bg-white rounded-xl shadow-sm">
    <!-- Search Input -->
    <div class="relative flex-1">
      <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
      <input
        type="text"
        placeholder="Search anything here..."
        class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-200 focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 text-sm text-gray-800 placeholder-gray-400 bg-white"
>>>>>>> origin/loreng
        v-model="searchQuery"
      />
    </div>

    <!-- Filter Button -->
    <div class="relative">
      <button 
        @click="toggleFilter"
<<<<<<< HEAD
        class="flex items-center gap-3 px-6 py-3 rounded-2xl border-2 border-white bg-white text-base text-gray-800 hover:bg-gradient-to-br hover:from-green-50 hover:to-emerald-50 shadow-md"
      >
        <Filter class="h-5 w-5 text-gray-600" />
        Filter by Range
        <ChevronDown class="h-5 w-5 text-gray-500" :class="{ 'transform rotate-180': isFilterOpen }" />
      </button>
=======
        class="flex items-center gap-2 px-4 py-2 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50 hover:border-gray-300 transition-colors duration-200"
      >
        <Filter class="h-4 w-4 text-gray-400" />
        Filter by Range
        <ChevronDown 
          class="h-4 w-4 text-gray-400 transition-transform duration-200" 
          :class="{ 'transform rotate-180': isFilterOpen }" 
        />
      </button>
      
      <!-- Filter Dropdown (if needed) -->
      <div v-if="isFilterOpen" class="absolute top-full right-0 mt-2 w-64 bg-white rounded-lg shadow-lg border border-gray-200 py-2 z-50">
        <!-- Add your filter options here -->
      </div>
>>>>>>> origin/loreng
    </div>

    <!-- Sort Button -->
    <div class="relative">
      <button 
        @click="toggleSort"
<<<<<<< HEAD
        class="flex items-center gap-3 px-6 py-3 rounded-2xl border-2 border-white bg-white text-base text-gray-800 hover:bg-gradient-to-br hover:from-green-50 hover:to-emerald-50 shadow-md"
      >
        Sort by
        <ChevronDown class="h-5 w-5 text-gray-500" :class="{ 'transform rotate-180': isSortOpen }" />
      </button>
=======
        class="flex items-center gap-2 px-4 py-2 rounded-lg border border-gray-200 bg-white text-sm text-gray-700 hover:bg-gray-50 hover:border-gray-300 transition-colors duration-200"
      >
        Sort by
        <ChevronDown 
          class="h-4 w-4 text-gray-400 transition-transform duration-200" 
          :class="{ 'transform rotate-180': isSortOpen }" 
        />
      </button>
      
      <!-- Sort Dropdown (if needed) -->
      <div v-if="isSortOpen" class="absolute top-full right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 py-2 z-50">
        <!-- Add your sort options here -->
      </div>
>>>>>>> origin/loreng
    </div>

    <!-- Export Button -->
    <button 
      @click="handleExport"
<<<<<<< HEAD
      class="flex items-center gap-3 px-6 py-3 rounded-2xl bg-emerald-500 hover:bg-emerald-600 text-white text-base font-semibold shadow-md transition-transform transform hover:scale-105"
    >
      <Download class="h-5 w-5" />
      Export
      <ChevronDown class="h-5 w-5" />
=======
      class="flex items-center gap-2 px-4 py-2 rounded-lg bg-emerald-500 hover:bg-emerald-600 text-white text-sm font-medium shadow-sm transition-all duration-200 hover:shadow active:transform active:scale-95"
    >
      <Download class="h-4 w-4" />
      Export
      <ChevronDown class="h-4 w-4" />
>>>>>>> origin/loreng
    </button>
  </div>
</template>

<script setup>
<<<<<<< HEAD
import { ref } from 'vue'
=======
import { ref, onMounted, onUnmounted } from 'vue'
>>>>>>> origin/loreng
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
<<<<<<< HEAD
</script>
=======

// Close dropdowns when clicking outside
const closeDropdowns = (event) => {
  if (!event.target.closest('.relative')) {
    isFilterOpen.value = false
    isSortOpen.value = false
  }
}

// Add event listener when component is mounted
onMounted(() => {
  document.addEventListener('click', closeDropdowns)
})

// Remove event listener when component is unmounted
onUnmounted(() => {
  document.removeEventListener('click', closeDropdowns)
})
</script>

<style scoped>
/* Optional: Add transition for smoother dropdown animations */
.absolute {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

/* Ensure dropdowns are above other content */
.z-50 {
  z-index: 50;
}
</style>
>>>>>>> origin/loreng
