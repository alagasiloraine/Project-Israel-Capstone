<template>
  <!-- Main content with more subtle blur effect -->
  <div class="w-full bg-white rounded-lg overflow-hidden" :class="{ 'blur-sm brightness-[0.98]': showModal || showDeleteModal }">
    <AdminHeader />
    <div class="p-[30px] px-[20px]">
      <!-- Full width container to match navbar width -->
      <div class="w-full bg-white rounded-xl shadow-lg overflow-hidden border border-gray-100">
        <!-- Breadcrumb Header -->
        <!-- <div class="p-6 border-b border-gray-100">
          <h1 class="text-2xl font-semibold text-gray-900 mb-2">Manage Staff</h1>
        </div> -->

        <div class="mb-6 px-8 mt-2">
          <AdminSearchPage />
        </div>
        
        <div class="px-2">
          <!-- Updated Buttons -->
          <div class="flex justify-end mb-4 gap-2">
            <button 
              @click="showArchivePanel = true"
              class="flex items-center gap-2 px-4 py-2 text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
            >
              <Archive class="h-4 w-4" />
              <span class="font-medium">Archive</span>
            </button>
            <button 
              @click="showModal = true"
              class="flex items-center gap-2 px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
            >
              <Plus class="h-4 w-4" />
              <span class="font-medium">New</span>
            </button>
          </div>

          <div class="border border-gray-200 rounded-lg overflow-hidden">
            <div class="max-h-[400px] overflow-y-auto scrollbar-thin scrollbar-thumb-green-500 scrollbar-track-green-100">
              <table class="w-full">
                <!-- Table Header -->
                <thead class="bg-gray-100 sticky top-0 z-10">
                  <tr>
                    <th class="w-16 px-4 py-4 border-b border-r border-gray-200 rounded-tl-lg">
                      <input 
                        type="checkbox" 
                        class="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                        v-model="selectAll"
                        @change="toggleSelectAll"
                        aria-label="Select all"
                      >
                    </th>
                    <th 
                      v-for="(header, index) in headers" 
                      :key="header"
                      :class="[
                        'px-4 py-3 text-left font-bold text-gray-900 uppercase tracking-wider font-poppins border-b border-r border-gray-200 text-sm bg-gray-100',
                        index === headers.length - 1 ? 'rounded-tr-lg' : ''
                      ]"
                    >
                      <div class="flex items-center gap-2">
                        {{ header }}
                        <div v-if="header !== 'Actions'" class="flex flex-col">
                          <ChevronUp class="h-3 w-3 text-gray-400" />
                          <ChevronDown class="h-3 w-3 text-gray-400 -mt-1" />
                        </div>
                      </div>
                    </th>
                  </tr>
                </thead>

                <!-- Table Body -->
                <tbody class="divide-y divide-gray-200">
                  <tr 
                    v-for="(employee, index) in employees" 
                    :key="employee.id"
                    class="hover:bg-gray-100 transition-colors"
                  >
                    <td class="px-4 py-3 border-r border-gray-200">
                      <input 
                        type="checkbox" 
                        v-model="employee.selected"
                        class="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                      >
                    </td>
                    <td class="px-4 py-3 border-r border-gray-200">
                      <div class="flex items-center gap-3">
                        <img 
                          :src="employee.avatar" 
                          :alt="employee.name"
                          class="w-8 h-8 rounded-full object-cover border border-gray-200"
                        >
                        <span class="font-medium text-sm text-gray-900 font-poppins">{{ employee.name }}</span>
                      </div>
                    </td>
                    <td class="px-4 py-3 border-r border-gray-200">
                      <span class="text-sm text-gray-600 font-poppins">{{ employee.position }}</span>
                    </td>
                    <td class="px-4 py-3 border-r border-gray-200">
                      <span class="text-sm font-medium text-blue-600 font-poppins">{{ employee.plotAssign }}</span>
                    </td>
                    <td class="px-4 py-3 border-r border-gray-200">
                      <span class="text-sm text-gray-600 font-poppins">{{ employee.department }}</span>
                    </td>
                    <td class="px-4 py-3 border-r border-gray-200">
                      <span 
                        class="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium font-poppins"
                        :class="getStatusClass(employee.status)"
                      >
                        <span class="w-1.5 h-1.5 rounded-full mr-1.5" :class="getStatusDotClass(employee.status)"></span>
                        {{ employee.status }}
                      </span>
                    </td>
                    <td class="px-6 py-4">
                      <div class="flex items-center justify-between w-32">
                        <button 
                          class="p-2 text-gray-500 hover:text-blue-600 transition-colors"
                          title="View"
                        >
                          <Eye class="h-5 w-5" />
                        </button>
                        <button 
                          class="p-2 text-gray-500 hover:text-green-600 transition-colors"
                          title="Edit"
                        >
                          <Edit class="h-5 w-5" />
                        </button>
                        <button 
                          @click="archiveStaff(employee)"
                          class="p-2 text-gray-500 hover:text-red-600 transition-colors"
                          title="Archive"
                        >
                          <Archive class="h-5 w-5" />
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Pagination -->
        <div class="mt-6 mb-6">
          <AdminPagination />
        </div>
      </div>
    </div>

    <!-- Archive Slide-in Panel -->
    <div 
      v-if="showArchivePanel" 
      class="fixed inset-y-0 right-0 w-96 bg-white shadow-lg transform transition-transform duration-300 ease-in-out z-50"
      :class="showArchivePanel ? 'translate-x-0' : 'translate-x-full'"
    >
      <div class="h-full flex flex-col">
        <div class="p-6 border-b border-gray-200">
          <div class="flex items-center justify-between">
            <h2 class="text-lg font-semibold text-gray-900">Archived Staff</h2>
            <button 
              @click="showArchivePanel = false"
              class="text-gray-500 hover:text-gray-700"
            >
              <X class="h-5 w-5" />
            </button>
          </div>
        </div>
        
        <div class="flex-1 overflow-y-auto p-6">
          <div v-if="archivedStaff.length === 0" class="text-center text-gray-500 mt-8">
            No archived staff
          </div>
          <div 
            v-for="staff in archivedStaff" 
            :key="staff.id"
            class="mb-4 p-4 border border-gray-200 rounded-lg"
          >
            <div class="flex items-center gap-3 mb-3">
              <img 
                :src="staff.avatar" 
                :alt="staff.name"
                class="w-10 h-10 rounded-full object-cover border border-gray-200"
              >
              <div>
                <h3 class="font-medium text-gray-900">{{ staff.name }}</h3>
                <p class="text-sm text-gray-500">{{ staff.position }}</p>
              </div>
            </div>
            <div class="flex justify-end gap-2">
              <button 
                @click="unarchiveStaff(staff)"
                class="px-3 py-1.5 text-sm font-medium text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
              >
                Undo Archive
              </button>
              <button 
                @click="confirmDelete(staff)"
                class="px-3 py-1.5 text-sm font-medium text-red-600 hover:bg-red-50 rounded-lg transition-colors"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Redesigned Add New Staff Modal -->
  <div v-if="showModal" class="fixed inset-0 flex items-center justify-center z-50">
    <!-- Modal Content -->
    <div 
      class="bg-white rounded-2xl w-full max-w-md mx-4 shadow-lg transform transition-all duration-300 ease-out"
      :class="showModal ? 'scale-100 opacity-100' : 'scale-95 opacity-0'"
    >
      <div class="p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-xl font-semibold text-gray-900">Add New Staff</h2>
          <button 
            @click="showModal = false"
            class="text-gray-400 hover:text-gray-500 transition-colors"
          >
            <X class="h-5 w-5" />
          </button>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-5">
          <!-- Name Input -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
            <input
              type="text"
              v-model="newStaff.name"
              class="w-full rounded-lg border border-gray-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              placeholder="Enter staff name"
              required
            />
          </div>

          <!-- Position Dropdown -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Position</label>
            <select
              v-model="newStaff.position"
              class="w-full rounded-lg border border-gray-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              required
            >
              <option value="">Select Position</option>
              <option value="Staff">Staff</option>
            </select>
          </div>

          <!-- Plot Assign Dropdown -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Plot Assign</label>
            <select
              v-model="newStaff.plotAssign"
              class="w-full rounded-lg border border-gray-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              required
            >
              <option value="">Select Plot</option>
              <option value="Greenhouse 1">Greenhouse 1</option>
              <option value="Greenhouse 2">Greenhouse 2</option>
            </select>
          </div>

          <!-- Department Dropdown -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Department</label>
            <select
              v-model="newStaff.department"
              class="w-full rounded-lg border border-gray-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              required
            >
              <option value="">Select Department</option>
              <option value="Farming">Farming</option>
              <option value="Poultry">Poultry</option>
              <option value="Livestock">Livestock</option>
            </select>
          </div>

          <!-- Status Dropdown -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>
            <select
              v-model="newStaff.status"
              class="w-full rounded-lg border border-gray-200 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              required
            >
              <option value="">Select Status</option>
              <option value="Active">Active</option>
              <option value="Invited">Invited</option>
            </select>
          </div>

          <!-- Form Actions -->
          <div class="flex justify-end gap-3 mt-6 pt-2">
            <button
              type="button"
              @click="showModal = false"
              class="px-4 py-2 text-sm font-medium text-gray-600 hover:text-gray-700 transition-colors"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="px-4 py-2 text-sm font-medium text-white bg-green-500 hover:bg-green-600 rounded-lg transition-colors"
            >
              Add Staff
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- Redesigned Delete Confirmation Modal -->
  <div v-if="showDeleteModal" class="fixed inset-0 flex items-center justify-center z-50">
    <!-- Modal Content -->
    <div 
      class="bg-white rounded-2xl w-full max-w-sm mx-4 shadow-lg transform transition-all duration-300 ease-out"
      :class="showDeleteModal ? 'scale-100 opacity-100' : 'scale-95 opacity-0'"
    >
      <div class="p-6">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-semibold text-gray-900">Confirm Deletion</h3>
          <button 
            @click="showDeleteModal = false"
            class="text-gray-400 hover:text-gray-500 transition-colors"
          >
            <X class="h-5 w-5" />
          </button>
        </div>
        
        <p class="text-gray-600 mb-6">Are you sure you want to delete this account? This action cannot be undone.</p>
        
        <div class="flex justify-end gap-3">
          <button
            @click="showDeleteModal = false"
            class="px-4 py-2 text-sm font-medium text-gray-600 hover:text-gray-700 transition-colors"
          >
            Cancel
          </button>
          <button
            @click="deleteStaff"
            class="px-4 py-2 text-sm font-medium text-white bg-red-500 hover:bg-red-600 rounded-lg transition-colors"
          >
            Yes, Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { 
  ChevronDown, 
  ChevronUp, 
  Plus, 
  Printer, 
  Archive,
  Eye,
  Edit,
  X
} from 'lucide-vue-next'
import AdminHeader from './AdminHeader.vue'
import AdminPagination from './AdminPagination.vue'
import AdminSearchPage from './AdminSearchPage.vue'

const showModal = ref(false)
const showArchivePanel = ref(false)
const showDeleteModal = ref(false)
const staffToDelete = ref(null)
const archivedStaff = ref([])

const newStaff = ref({
  name: '',
  position: '',
  plotAssign: '',
  department: '',
  status: ''
})

const headers = [
  'Name',
  'Position',
  'Plot Assign',
  'Department',
  'Status',
  'Actions'
]

const employees = ref([
  {
    id: 3,
    selected: false,
    name: 'John Smith',
    position: 'Staff',
    plotAssign: 'Greenhouse 1',
    department: 'Farming',
    status: 'Active',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 4,
    selected: false,
    name: 'Maria Garcia',
    position: 'Staff',
    plotAssign: 'Greenhouse 2',
    department: 'Poultry',
    status: 'Active',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 5,
    selected: false,
    name: 'James Wilson',
    position: 'Staff',
    plotAssign: 'Greenhouse 1',
    department: 'Livestock',
    status: 'Active',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 6,
    selected: false,
    name: 'Sarah Johnson',
    position: 'Staff',
    plotAssign: 'Greenhouse 2',
    department: 'Farming',
    status: 'Invited',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 7,
    selected: false,
    name: 'Michael Brown',
    position: 'Staff',
    plotAssign: 'Greenhouse 1',
    department: 'Poultry',
    status: 'Active',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 8,
    selected: false,
    name: 'Emma Davis',
    position: 'Senior Staff',
    plotAssign: 'Greenhouse 2',
    department: 'Farming',
    status: 'Active',
    avatar: '/placeholder.svg?height=32&width=32'
  },
  {
    id: 9,
    selected: false,
    name: 'Robert Martinez',
    position: 'Staff Lead',
    plotAssign: 'Greenhouse 1',
    department: 'Livestock',
    status: 'Active',
    avatar: '/placeholder.svg?height=32&width=32'
  }
])

const handleSubmit = () => {
  // Add new staff logic here
  employees.value.push({
    id: employees.value.length + 1,
    selected: false,
    ...newStaff.value,
    avatar: '/placeholder.svg?height=32&width=32'
  })
  
  // Reset form and close modal
  newStaff.value = {
    name: '',
    position: '',
    plotAssign: '',
    department: '',
    status: ''
  }
  showModal.value = false
}

const archiveStaff = (staff) => {
  const index = employees.value.findIndex(e => e.id === staff.id)
  if (index !== -1) {
    const [archivedEmployee] = employees.value.splice(index, 1)
    archivedStaff.value.push(archivedEmployee)
  }
  showArchivePanel.value = true
}

const unarchiveStaff = (staff) => {
  const index = archivedStaff.value.findIndex(e => e.id === staff.id)
  if (index !== -1) {
    const [unarchivedEmployee] = archivedStaff.value.splice(index, 1)
    employees.value.push(unarchivedEmployee)
  }
}

const confirmDelete = (staff) => {
  staffToDelete.value = staff
  showDeleteModal.value = true
}

const deleteStaff = () => {
  if (staffToDelete.value) {
    const index = archivedStaff.value.findIndex(e => e.id === staffToDelete.value.id)
    if (index !== -1) {
      archivedStaff.value.splice(index, 1)
    }
  }
  showDeleteModal.value = false
  staffToDelete.value = null
}

const selectAll = ref(false)

const toggleSelectAll = () => {
  employees.value.forEach(employee => {
    employee.selected = selectAll.value
  })
}

const getStatusClass = (status) => {
  const classes = {
    'Invited': 'bg-green-50 text-green-700',
    'Absent': 'bg-gray-100 text-gray-600',
    'Active': 'bg-blue-50 text-blue-700'
  }
  return classes[status] || 'bg-gray-100 text-gray-600'
}

const getStatusDotClass = (status) => {
  const classes = {
    'Invited': 'bg-green-500',
    'Absent': 'bg-gray-500',
    'Active': 'bg-blue-500'
  }
  return classes[status] || 'bg-gray-500'
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

/* Custom Scrollbar Styles */
.scrollbar-thin::-webkit-scrollbar {
  width: 6px;
}

.scrollbar-thin::-webkit-scrollbar-track {
  background: #e5e7eb;
  border-radius: 3px;
}

.scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: #22c55e;
  border-radius: 3px;
}

.scrollbar-thin::-webkit-scrollbar-thumb:hover {
  background-color: #16a34a;
}

/* Blur effect for modal backdrop */
.blur-l {
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.brightness-\[0\.98\] {
  filter: brightness(0.98);
}
</style>