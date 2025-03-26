<template>
    <div class="h-screen flex flex-col font-poppins">
      <AdminHeader />
      <div class="flex-grow bg-gray-100 flex items-center justify-center p-4">
        <div class="w-full max-w-5xl bg-white rounded-lg shadow-md overflow-hidden mb-[80px]">
          <!-- Profile Header -->
          <div class="bg-[#006B48] h-40 relative">
            <!-- Profile Image -->
            <div class="absolute left-1/2 transform -translate-x-1/2 -bottom-20">
              <div class="relative group">
                <div class="w-48 h-48 rounded-full border-4 border-white bg-white shadow-lg overflow-hidden">
                  <img 
                    :src="user.profilePicture || '/public/images/profile.jpg'" 
                    alt="Profile Picture"
                    class="w-full h-full object-cover"
                  />
                </div>
                <!-- Edit Profile Picture Button -->
                <button 
                  @click="openImageSelector"
                  class="absolute bottom-3 right-3 bg-white rounded-full p-2.5 shadow-md hover:bg-gray-100 transition-colors duration-200"
                >
                  <Pencil class="h-5 w-5 text-[#006B48]" />
                </button>
                <input 
                  type="file" 
                  ref="fileInput" 
                  @change="handleImageChange" 
                  accept="image/*" 
                  class="hidden"
                />
              </div>
            </div>
          </div>
  
          <!-- Profile Content -->
          <div class="pt-24 px-8 pb-8">
            <div class="text-center mb-8">
              <h1 class="text-3xl font-bold text-gray-800 mb-2">{{ user.firstName }} {{ user.lastName }}</h1>
              <span class="inline-block bg-[#006B48] text-white px-4 py-1 rounded-full text-sm font-medium">ADMIN</span>
            </div>
  
            <div class="flex justify-between max-w-4xl mx-auto">
              <!-- Contact Information -->
              <div class="flex-1 pr-8">
                <h2 class="text-xl font-semibold text-gray-700 mb-4">Contact Information</h2>
                <div class="space-y-3">
                  <div class="flex items-center">
                    <Phone class="h-5 w-5 text-[#006B48] mr-3" />
                    <span class="text-gray-600 text-lg">{{ user.contactNumber }}</span>
                  </div>
                  <div class="flex items-center">
                    <Mail class="h-5 w-5 text-[#006B48] mr-3" />
                    <span class="text-gray-600 text-lg">{{ user.email }}</span>
                  </div>
                </div>
              </div>
              
              <!-- Address -->
              <div class="flex-1 pl-8 border-l border-gray-200">
                <h2 class="text-xl font-semibold text-gray-700 mb-4">Address</h2>
                <div class="flex items-start">
                  <MapPin class="h-5 w-5 text-[#006B48] mr-3 mt-1" />
                  <span class="text-gray-600 text-lg">{{ formatAddress() }}</span>
                </div>
              </div>
            </div>
  
            <div class="mt-8 text-center">
              <button 
                @click="showEditModal = true" 
                class="bg-[#006B48] hover:bg-[#005a3d] text-white font-medium py-2.5 px-8 rounded-md transition-colors duration-200 text-lg"
              >
                Edit Profile
              </button>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Edit Profile Modal -->
      <div v-if="showEditModal" class="fixed inset-0 z-50">
        <!-- Backdrop with blur effect -->
        <div class="absolute inset-0 bg-[#006B48] bg-opacity-40 backdrop-blur-sm"></div>
        
        <!-- Modal Content -->
        <div class="relative z-10 flex items-center justify-center min-h-screen p-4">
          <div class="bg-white rounded-lg shadow-xl w-full max-w-3xl">
            <div class="p-6 border-b border-gray-200">
              <div class="flex justify-between items-center">
                <h2 class="text-2xl font-bold text-gray-800">Edit Profile</h2>
                <button @click="closeEditModal" class="text-gray-500 hover:text-gray-700">
                  <X class="h-6 w-6" />
                </button>
              </div>
            </div>
  
            <div class="p-6">
              <form @submit.prevent="saveProfile" class="space-y-4">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">First Name</label>
                    <input 
                      v-model="editForm.firstName"
                      type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#006B48] focus:border-transparent"
                    />
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Last Name</label>
                    <input 
                      v-model="editForm.lastName"
                      type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#006B48] focus:border-transparent"
                    />
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                    <input 
                      v-model="editForm.email"
                      type="email"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#006B48] focus:border-transparent"
                    />
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Contact Number</label>
                    <input 
                      v-model="editForm.contactNumber"
                      type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#006B48] focus:border-transparent"
                    />
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Province</label>
                    <input 
                      v-model="editForm.province"
                      type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#006B48] focus:border-transparent"
                    />
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">City/Municipality</label>
                    <input 
                      v-model="editForm.city"
                      type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#006B48] focus:border-transparent"
                    />
                  </div>
                  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Barangay</label>
                    <input 
                      v-model="editForm.barangay"
                      type="text"
                      class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#006B48] focus:border-transparent"
                    />
                  </div>
                </div>
              </form>
            </div>
  
            <div class="p-6 border-t border-gray-200 flex justify-end space-x-4">
              <button 
                @click="closeEditModal" 
                class="px-6 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50 transition-colors duration-200"
              >
                Cancel
              </button>
              <button 
                @click="saveProfile"
                class="px-6 py-2 bg-[#006B48] hover:bg-[#005a3d] text-white rounded-md transition-colors duration-200"
              >
                Save Changes
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive, onMounted } from 'vue'
  import { Pencil, Phone, Mail, MapPin, X } from 'lucide-vue-next'
  import AdminHeader from './AdminHeader.vue'
  
  // State
  const showEditModal = ref(false)
  const fileInput = ref(null)
  const user = reactive({
    firstName: 'Jane Heather',
    lastName: 'Gitana',
    email: 'jane@example.com',
    contactNumber: '09707074323',
    province: 'Oriental Mindoro',
    city: 'Calapan',
    barangay: 'Calapan City',
  })
  
  // Edit form
  const editForm = reactive({
    firstName: '',
    lastName: '',
    email: '',
    contactNumber: '',
    province: '',
    city: '',
    barangay: ''
  })
  
  // Methods
  const formatAddress = () => {
    return `${user.barangay}, ${user.city}, ${user.province}`
  }
  
  const openImageSelector = () => {
    fileInput.value.click()
  }
  
  const handleImageChange = (event) => {
    const file = event.target.files[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = (e) => {
        user.profilePicture = e.target.result
        // In a real app, you would upload the file to a server here
      }
      reader.readAsDataURL(file)
    }
  }
  
  const initEditForm = () => {
    editForm.firstName = user.firstName
    editForm.lastName = user.lastName
    editForm.email = user.email
    editForm.contactNumber = user.contactNumber
    editForm.province = user.province
    editForm.city = user.city
    editForm.barangay = user.barangay
  }
  
  const saveProfile = () => {
    // Update user data
    user.firstName = editForm.firstName
    user.lastName = editForm.lastName
    user.email = editForm.email
    user.contactNumber = editForm.contactNumber
    user.province = editForm.province
    user.city = editForm.city
    user.barangay = editForm.barangay
    
    // In a real app, you would save to a server here
    
    // Close modal
    showEditModal.value = false
  }
  
  const closeEditModal = () => {
    initEditForm()
    showEditModal.value = false
  }
  
  // Lifecycle hooks
  onMounted(() => {
    initEditForm()
  })
  </script>