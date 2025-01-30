<template>
  <div class="flex h-screen bg-gray-50">
    <Sidebar />
    
    <!-- Main Content -->
    <div class="flex-1 overflow-auto bg-gradient-to-br from-green-50 to-emerald-50 p-8">
      <!-- Search Filter Bar -->
      <div class="mb-6">
        <SearchFilterBar />
      </div>

      <!-- Header Section -->
      <div class="mb-6">
        <h1 class="text-2xl font-bold text-gray-900 mb-2">Motor Control Data Table</h1>
        <div class="flex items-center text-sm text-gray-500">
          <span class="text-purple-600">Motor Control</span>
          <ChevronRight class="h-4 w-4 mx-1" />
          <span>Data Table</span>
        </div>
      </div>

      <!-- Table Container -->
      <div class="bg-white rounded-xl shadow-[0_4px_12px_rgba(0,0,0,0.1)] overflow-hidden border border-gray-200">
        <table class="w-full border-collapse">
          <thead>
            <tr class="bg-gray-50/50">
              <th 
                v-for="header in headers" 
                :key="header.key"
                class="px-6 py-3 text-left text-sm font-semibold text-gray-700 border-b border-r border-gray-200 bg-gray-100 hover:bg-gray-200 transition-colors duration-150 cursor-pointer"
                :class="{ 'cursor-pointer hover:bg-gray-50': header.sortable }"
                @click="header.sortable ? toggleSort(header.key) : null"
              >
                <div class="flex items-center justify-between">
                  <span class="uppercase">{{ header.label }}</span>
                  <div v-if="header.sortable" class="flex flex-col ml-2">
                    <ChevronUp 
                      class="h-5 w-5 -mb-1.5" 
                      :class="sortConfig.key === header.key && !sortConfig.asc ? 'text-purple-600' : 'text-gray-400'"
                    />
                    <ChevronDown 
                      class="h-5 w-5" 
                      :class="sortConfig.key === header.key && sortConfig.asc ? 'text-purple-600' : 'text-gray-400'"
                    />
                  </div>
                </div>
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr 
              v-for="(row, index) in paginatedData" 
              :key="row.id"
              class="hover:bg-gray-50/50 transition-colors"
            >
              <td class="px-6 py-3 whitespace-nowrap text-sm font-medium text-gray-900 border-r border-gray-200">
                {{ (currentPage - 1) * itemsPerPage + index + 1 }}
              </td>
              <td class="px-6 py-3 whitespace-nowrap text-sm font-medium border-r border-gray-200">
                <span 
                  :class="row.status === 'ON' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'"
                  class="px-2 py-1 rounded-full text-sm font-medium"
                >
                  {{ row.status }}
                </span>
              </td>
              <td class="px-6 py-3 whitespace-nowrap text-sm font-medium text-gray-900 border-r border-gray-200">
                {{ row.date }}
              </td>
              <td class="px-6 py-3 whitespace-nowrap text-sm font-medium text-gray-900">
                {{ row.time }}
              </td>
            </tr>
          </tbody>
        </table>

        <div class="mb-6">
          <Pagination />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ChevronRight, ChevronUp, ChevronDown } from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'
import SearchFilterBar from './SearchFilterBar.vue'
import Pagination from '../layout/Pagination.vue'

const headers = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'status', label: 'Motor Control', sortable: true },
  { key: 'date', label: 'Date', sortable: true },
  { key: 'time', label: 'Time', sortable: true }
]

const data = ref([
  { id: 1, status: 'ON', date: '2024-05-17', time: '18:58:33' },
  { id: 2, status: 'OFF', date: '2024-05-17', time: '18:58:48' },
  { id: 3, status: 'OFF', date: '2024-05-17', time: '18:59:24' },
  { id: 4, status: 'ON', date: '2024-05-17', time: '19:00:25' },
  { id: 5, status: 'OFF', date: '2024-05-17', time: '19:01:25' },
  { id: 6, status: 'ON', date: '2024-05-17', time: '19:02:25' },
  { id: 7, status: 'OFF', date: '2024-05-17', time: '19:01:25' },
  { id: 8, status: 'ON', date: '2024-05-17', time: '19:02:25' },
])

const itemsPerPage = ref(10)
const currentPage = ref(1)
const sortConfig = ref({
  key: 'id',
  asc: true
})

const toggleSort = (key) => {
  if (sortConfig.value.key === key) {
    sortConfig.value.asc = !sortConfig.value.asc
  } else {
    sortConfig.value.key = key
    sortConfig.value.asc = true
  }
}

const sortedData = computed(() => {
  return [...data.value].sort((a, b) => {
    const aVal = a[sortConfig.value.key]
    const bVal = b[sortConfig.value.key]
    
    if (aVal < bVal) return sortConfig.value.asc ? -1 : 1
    if (aVal > bVal) return sortConfig.value.asc ? 1 : -1
    return 0
  })
})

const totalPages = computed(() => 
  Math.ceil(sortedData.value.length / itemsPerPage.value)
)

const paginatedData = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return sortedData.value.slice(start, end)
})
</script>
