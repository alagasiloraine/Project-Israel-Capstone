<template>
  <div class="bg-gray-50/50 border-t border-gray-200 px-4 py-2 flex items-center justify-between text-sm">
    <div class="flex items-center">
      <span class="text-gray-600 mr-2">Items per page</span>
      <select 
        v-model="localItemsPerPage" 
        class="border border-gray-200 rounded-md py-1 pl-2 pr-6 focus:outline-none focus:ring-1 focus:ring-green-500 focus:border-green-500 bg-white text-sm h-8"
        @change="$emit('update:itemsPerPage', localItemsPerPage)"
      >
        <option value="10">10</option>
        <option value="20">20</option>
        <option value="30">30</option>
        <option value="40">40</option>
        <option value="50">50</option>
      </select>
    </div>

    <div class="flex items-center space-x-1">
      <button 
        @click="$emit('previous')"
        :disabled="currentPage === 1"
        class="px-2 py-1 text-sm text-gray-600 hover:text-gray-900 disabled:opacity-50 disabled:cursor-not-allowed flex items-center h-8"
      >
        Previous
      </button>
      
      <div class="flex items-center">
        <template v-for="page in displayedPages" :key="page">
          <button 
            v-if="page !== '...'"
            @click="$emit('update:currentPage', page)"
            :class="[
              'min-w-[28px] h-8 flex items-center justify-center rounded text-sm mx-0.5 transition-colors duration-150',
              currentPage === page 
                ? 'bg-gray-900 text-white' 
                : 'text-gray-600 hover:bg-gray-100'
            ]"
          >
            {{ page }}
          </button>
          <span v-else class="px-1 text-gray-400 text-sm">...</span>
        </template>
      </div>

      <button 
        @click="$emit('next')"
        :disabled="currentPage === totalPages"
        class="px-2 py-1 text-sm text-gray-600 hover:text-gray-900 disabled:opacity-50 disabled:cursor-not-allowed flex items-center h-8"
      >
        <span>Next</span>
        <svg 
          class="w-4 h-4 ml-1" 
          fill="none" 
          stroke="currentColor" 
          viewBox="0 0 24 24"
        >
          <path 
            stroke-linecap="round" 
            stroke-linejoin="round" 
            stroke-width="2" 
            d="M9 5l7 7-7 7"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  currentPage: {
    type: Number,
    required: true
  },
  totalPages: {
    type: Number,
    required: true
  },
  itemsPerPage: {
    type: Number,
    required: true
  }
})

const emit = defineEmits(['update:currentPage', 'update:itemsPerPage', 'previous', 'next'])

const localItemsPerPage = ref(props.itemsPerPage)

const displayedPages = computed(() => {
  const pages = []
  const maxVisiblePages = 5
  
  if (props.totalPages <= maxVisiblePages) {
    for (let i = 1; i <= props.totalPages; i++) {
      pages.push(i)
    }
  } else {
    pages.push(1)
    
    if (props.currentPage > 3) {
      pages.push('...')
    }
    
    const start = Math.max(2, props.currentPage - 1)
    const end = Math.min(props.totalPages - 1, props.currentPage + 1)
    
    for (let i = start; i <= end; i++) {
      pages.push(i)
    }
    
    if (props.currentPage < props.totalPages - 2) {
      pages.push('...')
    }
    
    pages.push(props.totalPages)
  }
  
  return pages
})
</script>

<style scoped>
select {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
  background-position: right 0.5rem center;
  background-repeat: no-repeat;
  background-size: 1.25em 1.25em;
  padding-right: 2rem;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
  appearance: none;
}
</style>