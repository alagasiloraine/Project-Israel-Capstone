<template>
  <div class="h-screen flex bg-gradient-to-br from-green-50 to-emerald-100 font-poppins overflow-hidden">
    <Sidebar />
    
    <!-- Main Content -->
    <main class="flex-1 flex flex-col h-screen pt-32">
      <div class="flex-1 w-full px-4 sm:px-6 lg:px-10 overflow-hidden">
        
        <!-- Main Container - Everything Inside -->
        <div class="bg-white rounded-[20px] shadow-[0_8px_30px_rgb(0,0,0,0.08)] border border-green-100 h-[calc(100vh-140px)] overflow-hidden">
          
          <!-- Header - Inside Main Container -->
          <div class="bg-gradient-to-r from-emerald-50 to-white p-6 border-b border-gray-100 rounded-t-lg">
            <h1 class="text-xl font-semibold text-gray-800 mb-1">User Profile</h1>
            <p class="text-emerald-600 mt-1 text-sm">Manage your account information and security settings</p>
          </div>

          <!-- Two Containers with Gap Inside Main Container -->
          <div class="flex gap-6 h-[calc(100%-100px)] p-6">
            
            <!-- Left Container - Profile Avatar (30% width) - MODIFIED PADDING -->
            <div class="w-[30%] bg-gradient-to-br from-gray-50 to-gray-100 rounded-[16px] border border-gray-200 overflow-y-auto">
              <div class="px-3 py-6 flex flex-col items-center">
                
                <!-- Large Profile Circle -->
                <div class="mb-6 flex flex-col items-center">
                  <div class="relative">
                    <!-- Profile Avatar Circle - Slightly Larger -->
                    <div class="w-32 h-32 rounded-full bg-white shadow-xl border-4 border-emerald-200 flex items-center justify-center text-6xl transition-all duration-300 hover:scale-105 hover:shadow-2xl mb-4">
                      {{ selectedAvatar.icon }}
                    </div>

                    <!-- Glow Effect - Match Size -->
                    <div class="absolute inset-0 w-32 h-32 rounded-full bg-emerald-200 opacity-20 blur-xl -z-10"></div>
                  </div>

                  <!-- Avatar Name -->
                  <p class="text-center text-sm font-medium text-gray-800 mb-1">{{ selectedAvatar.name }}</p>
                  <div class="w-8 h-0.5 bg-emerald-400 rounded-full"></div>
                </div>

                <!-- Avatar Selection Section -->
                <div class="w-full max-w-full">
                  <div class="text-center mb-4">
                    <h3 class="text-sm font-semibold text-gray-900 mb-2">Choose Avatar</h3>
                    <div class="w-16 h-0.5 bg-gradient-to-r from-emerald-400 to-emerald-600 rounded-full mx-auto mb-4"></div>
                  </div>
                  
                  <!-- Avatar Grid - MODIFIED SPACING -->
                  <div class="flex justify-center mb-4">
                    <div class="grid grid-cols-5 gap-4">
                      <div 
                        v-for="avatar in avatarOptions" 
                        :key="avatar.id"
                        @click="selectAvatar(avatar)"
                        :class="[ 
                          'w-14 h-14 rounded-full flex items-center justify-center text-xl cursor-pointer transition-all duration-200 border-2 bg-white shadow-sm hover:shadow-lg relative',
                          selectedAvatar.id === avatar.id 
                            ? 'border-emerald-500 bg-emerald-50 scale-110 shadow-lg ring-2 ring-emerald-200' 
                            : 'border-gray-200 hover:border-emerald-300 hover:scale-105'
                        ]"
                      >
                        {{ avatar.icon }}
                        
                        <!-- Selection indicator -->
                        <div 
                          v-if="selectedAvatar.id === avatar.id"
                          class="absolute -top-1 -right-1 w-3 h-3 bg-emerald-500 rounded-full flex items-center justify-center"
                        >
                          <CheckCircle class="w-2 h-2 text-white" />
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Instruction text - MODIFIED PADDING -->
                  <div class="text-center bg-white/50 rounded-lg p-2 border border-gray-200 mx-1">
                    <p class="text-xs font-medium text-gray-600">Select your profile character</p>
                    <p class="text-xs text-gray-500 mt-1">Choose from {{ avatarOptions.length }} available options</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right Container - Personal Info & Security (70% width) -->
            <div class="flex-1 bg-gradient-to-br from-white to-gray-50/30 rounded-[16px] border border-gray-200 overflow-y-auto">
              <div class="p-6">
                
                <!-- Personal Information Section -->
                <div class="mb-8">
                  <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
                    <div class="flex items-center mb-6">
                      <div class="w-10 h-10 bg-emerald-100 rounded-xl flex items-center justify-center mr-4">
                        <User class="w-5 h-5 text-emerald-600" />
                      </div>
                      <div>
                        <h3 class="text-base font-semibold text-gray-900">Personal Information</h3>
                        <p class="text-sm text-gray-500">Update your personal details</p>
                      </div>
                    </div>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <!-- Full Name -->
                      <div class="space-y-2">
                        <label class="text-sm font-medium text-gray-700">Full Name</label>
                        <div class="relative group">
                          <User class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400 group-focus-within:text-emerald-500 transition-colors duration-200" />
                          <input 
                            v-model="profileData.name"
                            type="text"
                            class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent bg-white transition-all duration-200 hover:border-gray-300"
                            placeholder="Enter your full name"
                          />
                        </div>
                      </div>

                      <!-- Phone Number -->
                      <div class="space-y-2">
                        <label class="text-sm font-medium text-gray-700">Phone Number</label>
                        <div class="relative group">
                          <Phone class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400 group-focus-within:text-emerald-500 transition-colors duration-200" />
                          <input 
                            v-model="profileData.phone"
                            type="tel"
                            class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent bg-white transition-all duration-200 hover:border-gray-300"
                            placeholder="Enter your phone number"
                          />
                        </div>
                      </div>
                    </div>

                    <!-- Save Button -->
                    <div class="mt-6">
                      <button 
                        @click="saveProfile"
                        class="bg-gradient-to-r from-emerald-500 to-emerald-600 text-white px-6 py-2.5 rounded-xl hover:from-emerald-600 hover:to-emerald-700 transition-all duration-200 font-medium shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 flex items-center"
                      >
                        <CheckCircle class="w-4 h-4 mr-2" />
                        Save Changes
                      </button>
                    </div>
                  </div>
                </div>

                <!-- Security Settings Section -->
                <div class="mb-8">
                  <div class="flex items-center mb-6">
                    <div class="w-10 h-10 bg-blue-100 rounded-xl flex items-center justify-center mr-4">
                      <Shield class="w-5 h-5 text-blue-600" />
                    </div>
                    <div>
                      <h3 class="text-base font-semibold text-gray-900">Security Settings</h3>
                      <p class="text-sm text-gray-500">Manage your account security</p>
                    </div>
                  </div>
                  
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    
                    <!-- Reset Password Card -->
                    <div class="bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-300 overflow-hidden group">
                      <div class="p-5">
                        <div class="flex items-center mb-4">
                          <div class="w-10 h-10 bg-blue-100 rounded-xl flex items-center justify-center mr-3 group-hover:bg-blue-200 transition-colors duration-200">
                            <Lock class="w-5 h-5 text-blue-600" />
                          </div>
                          <div>
                            <h4 class="text-sm font-semibold text-gray-900">Reset Password</h4>
                            <p class="text-xs text-gray-500">Update your account password</p>
                          </div>
                        </div>
                        
                        <!-- Show Get Started button only when form is not visible -->
                        <button 
                          v-if="!showPasswordSection"
                          @click="togglePasswordSection"
                          class="w-full bg-gradient-to-r from-blue-500 to-blue-600 text-white py-2.5 px-4 rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-200 text-sm font-medium shadow-md hover:shadow-lg transform hover:-translate-y-0.5"
                        >
                          Get Started
                        </button>
                        
                        <!-- Password Form with Show/Hide and TOP BORDER LINE -->
                        <div 
                          v-if="showPasswordSection"
                          class="mt-4 pt-4 border-t border-gray-100"
                        >
                          <div class="space-y-3">
                            <div>
                              <label class="block text-xs font-medium text-gray-700 mb-1">Current Password</label>
                              <div class="relative flex items-center">
                                <input 
                                  :type="showCurrentPassword ? 'text' : 'password'"
                                  v-model="passwordForm.current"
                                  class="w-full px-3 py-2 pr-10 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 text-sm"
                                  placeholder="Enter current password"
                                />
                                <button
                                  type="button"
                                  @click="showCurrentPassword = !showCurrentPassword"
                                  class="absolute right-3 inset-y-0 my-auto flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors duration-200 z-10"
                                >
                                  <Eye v-if="!showCurrentPassword" class="w-4 h-4" />
                                  <EyeOff v-else class="w-4 h-4" />
                                </button>
                              </div>
                            </div>
                            <div>
                              <label class="block text-xs font-medium text-gray-700 mb-1">New Password</label>
                              <div class="relative flex items-center">
                                <input 
                                  :type="showNewPassword ? 'text' : 'password'"
                                  v-model="passwordForm.new"
                                  class="w-full px-3 py-2 pr-10 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 text-sm"
                                  placeholder="Enter new password"
                                />
                                <button
                                  type="button"
                                  @click="showNewPassword = !showNewPassword"
                                  class="absolute right-3 inset-y-0 my-auto flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors duration-200 z-10"
                                >
                                  <Eye v-if="!showNewPassword" class="w-4 h-4" />
                                  <EyeOff v-else class="w-4 h-4" />
                                </button>
                              </div>
                            </div>
                            <div>
                              <label class="block text-xs font-medium text-gray-700 mb-1">Confirm Password</label>
                              <div class="relative flex items-center">
                                <input 
                                  :type="showConfirmPassword ? 'text' : 'password'"
                                  v-model="passwordForm.confirm"
                                  class="w-full px-3 py-2 pr-10 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 text-sm"
                                  placeholder="Confirm new password"
                                />
                                <button
                                  type="button"
                                  @click="showConfirmPassword = !showConfirmPassword"
                                  class="absolute right-3 inset-y-0 my-auto flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors duration-200 z-10"
                                >
                                  <Eye v-if="!showConfirmPassword" class="w-4 h-4" />
                                  <EyeOff v-else class="w-4 h-4" />
                                </button>
                              </div>
                            </div>
                          </div>
                          
                          <!-- Buttons Section with spacing -->
                          <div class="space-y-3 mt-4">
                            <!-- Update Password Button -->
                            <button 
                              @click="changePassword"
                              class="w-full bg-gradient-to-r from-blue-500 to-blue-600 text-white py-2 px-4 rounded-lg hover:from-blue-600 hover:to-blue-700 transition-all duration-200 text-sm font-medium"
                            >
                              Update Password
                            </button>
                            
                            <!-- Cancel Button - POSITIONED BELOW Update Password Button -->
                            <!-- Password Cancel Button with Visible Text -->
                            <button 
                              @click="togglePasswordSection"
                              class="w-full bg-gradient-to-r from-blue-300 to-blue-400 text-gray-700 font-semibold py-2 px-4 rounded-lg hover:from-blue-400 hover:to-blue-500 transition-all duration-200 text-sm font-medium"
                            >
                              Cancel
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>

                    <!-- Reset Pin Code Card -->
                    <div class="bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-300 overflow-hidden group">
                      <div class="p-5">
                        <div class="flex items-center mb-4">
                          <div class="w-10 h-10 bg-purple-100 rounded-xl flex items-center justify-center mr-3 group-hover:bg-purple-200 transition-colors duration-200">
                            <Shield class="w-5 h-5 text-purple-600" />
                          </div>
                          <div>
                            <h4 class="text-sm font-semibold text-gray-900">Reset Pin Code</h4>
                            <p class="text-xs text-gray-500">Update your security pin</p>
                          </div>
                        </div>
                        
                        <!-- Show Get Started button only when form is not visible -->
                        <button 
                          v-if="!showPinSection"
                          @click="togglePinSection"
                          class="w-full bg-gradient-to-r from-purple-500 to-purple-600 text-white py-2.5 px-4 rounded-xl hover:from-purple-600 hover:to-purple-700 transition-all duration-200 text-sm font-medium shadow-md hover:shadow-lg transform hover:-translate-y-0.5"
                        >
                          Get Started
                        </button>
                        
                        <!-- Pin Form with TOP BORDER LINE -->
                        <div 
                          v-if="showPinSection"
                          class="mt-4 pt-4 border-t border-gray-100"
                        >
                          <div class="space-y-3">
                            <div>
                              <label class="block text-xs font-medium text-gray-700 mb-1">Current Pin</label>
                              <div class="relative flex items-center">
                                <input 
                                  :type="showCurrentPin ? 'text' : 'password'"
                                  v-model="pinForm.current"
                                  maxlength="4"
                                  class="w-full px-3 py-2 pr-10 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent text-center text-lg tracking-widest transition-all duration-200"
                                  placeholder="••••"
                                />
                                <button
                                  type="button"
                                  @click="showCurrentPin = !showCurrentPin"
                                  class="absolute right-3 inset-y-0 my-auto flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors duration-200 z-10"
                                >
                                  <Eye v-if="!showCurrentPin" class="w-4 h-4" />
                                  <EyeOff v-else class="w-4 h-4" />
                                </button>
                              </div>
                            </div>
                            <div>
                              <label class="block text-xs font-medium text-gray-700 mb-1">New Pin</label>
                              <div class="relative flex items-center">
                                <input 
                                  :type="showNewPin ? 'text' : 'password'"
                                  v-model="pinForm.new"
                                  maxlength="4"
                                  class="w-full px-3 py-2 pr-10 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent text-center text-lg tracking-widest transition-all duration-200"
                                  placeholder="••••"
                                />
                                <button
                                  type="button"
                                  @click="showNewPin = !showNewPin"
                                  class="absolute right-3 inset-y-0 my-auto flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors duration-200 z-10"
                                >
                                  <Eye v-if="!showNewPin" class="w-4 h-4" />
                                  <EyeOff v-else class="w-4 h-4" />
                                </button>
                              </div>
                            </div>
                            <div>
                              <label class="block text-xs font-medium text-gray-700 mb-1">Confirm Pin</label>
                              <div class="relative flex items-center">
                                <input 
                                  :type="showConfirmPin ? 'text' : 'password'"
                                  v-model="pinForm.confirm"
                                  maxlength="4"
                                  class="w-full px-3 py-2 pr-10 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent text-center text-lg tracking-widest transition-all duration-200"
                                  placeholder="••••"
                                />
                                <button
                                  type="button"
                                  @click="showConfirmPin = !showConfirmPin"
                                  class="absolute right-3 inset-y-0 my-auto flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors duration-200 z-10"
                                >
                                  <Eye v-if="!showConfirmPin" class="w-4 h-4" />
                                  <EyeOff v-else class="w-4 h-4" />
                                </button>
                              </div>
                            </div>
                          </div>
                          
                          <!-- Buttons Section with spacing -->
                          <div class="space-y-3 mt-4">
                            <!-- Update Pin Button -->
                            <button 
                              @click="changePin"
                              class="w-full bg-gradient-to-r from-purple-500 to-purple-600 text-white py-2 px-4 rounded-lg hover:from-purple-600 hover:to-purple-700 transition-all duration-200 text-sm font-medium"
                            >
                              Update Pin
                            </button>
                            
                            <!-- Cancel Button - POSITIONED BELOW Update Pin Button -->
                            <!-- Pin Code Cancel Button with Visible Text -->
                              <button 
                                @click="togglePinSection"
                                class="w-full bg-gradient-to-r from-purple-300 to-purple-400 text-gray-700 font-semibold py-2 px-4 rounded-lg hover:from-purple-400 hover:to-purple-500 transition-all duration-200 text-sm font-medium"
                              >
                                Cancel
                              </button>
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                </div>

                <!-- Account Actions Section -->
                <div>
                  <!-- Header with improved icon for 'Account Actions' -->
                  <div class="flex items-center mb-6">
                    <div class="w-10 h-10 bg-red-100 rounded-xl flex items-center justify-center mr-4">
                      <UserCog class="w-5 h-5 text-red-600" />
                    </div>
                    <div>
                      <h3 class="text-base font-semibold text-gray-900">Account Actions</h3>
                      <p class="text-sm text-gray-500">Manage your account session</p>
                    </div>
                  </div>

                  <!-- Logout Section -->
                  <div class="bg-white rounded-2xl border border-red-200 shadow-sm hover:shadow-lg transition-all duration-300 overflow-hidden">
                    <div class="p-5">
                      <div class="flex items-center justify-between">
                        <div class="flex items-center">
                          <div class="w-10 h-10 bg-red-100 rounded-xl flex items-center justify-center mr-3">
                            <LogOut class="w-5 h-5 text-red-600" />
                          </div>
                          <p class="text-sm font-medium text-red-600">Sign out of your account</p>
                        </div>
                        <button 
                          @click="logout"
                          class="bg-gradient-to-r from-red-500 to-red-600 text-white py-2.5 px-8 rounded-xl hover:from-red-600 hover:to-red-700 transition-all duration-200 text-sm font-medium shadow-md hover:shadow-lg transform hover:-translate-y-0.5 min-w-[140px]"
                        >
                          Logout
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Toast Notification - Bottom Right -->
    <div 
      v-if="showToast" 
      class="fixed bottom-4 right-4 bg-white border border-gray-200 rounded-xl shadow-xl p-4 z-50 flex items-center transform transition-all duration-300 ease-in-out backdrop-blur-sm"
    >
      <div class="w-8 h-8 bg-emerald-100 rounded-lg flex items-center justify-center mr-3">
        <CheckCircle class="w-4 h-4 text-emerald-600" />
      </div>
      <span class="text-gray-900 font-medium text-sm">{{ toastMessage }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import Sidebar from '../layout/Sidebar.vue'
import { useRouter } from 'vue-router'
import { 
  User, 
  Phone, 
  Lock, 
  Shield, 
  UserCog,
  LogOut, 
  CheckCircle,
  Eye,
  EyeOff
} from 'lucide-vue-next'

const router = useRouter()
const user = ref(null)
const showToast = ref(false)
const toastMessage = ref('')
const showPasswordSection = ref(false)
const showPinSection = ref(false)

// Password visibility toggles
const showCurrentPassword = ref(false)
const showNewPassword = ref(false)
const showConfirmPassword = ref(false)

// Pin visibility toggles (add after password visibility toggles)
const showCurrentPin = ref(false)
const showNewPin = ref(false)
const showConfirmPin = ref(false)

// Avatar options with crop/plant themed characters
const avatarOptions = ref([
  { id: 1, icon: '🌱', name: 'Seedling' },
  { id: 2, icon: '🌿', name: 'Herb' },
  { id: 3, icon: '🌾', name: 'Wheat' },
  { id: 4, icon: '🌽', name: 'Corn' },
  { id: 5, icon: '🥕', name: 'Carrot' },
  { id: 6, icon: '🍅', name: 'Tomato' },
  { id: 7, icon: '🥬', name: 'Lettuce' },
  { id: 8, icon: '🌻', name: 'Sunflower' },
  { id: 9, icon: '🌳', name: 'Tree' },
  { id: 10, icon: '🍃', name: 'Leaves' },
  { id: 11, icon: '🌵', name: 'Cactus' },
  { id: 12, icon: '🌸', name: 'Blossom' },
  { id: 13, icon: '🍄', name: 'Mushroom' },
  { id: 14, icon: '🌺', name: 'Hibiscus' },
  { id: 15, icon: '🌹', name: 'Rose' },
  { id: 16, icon: '🌷', name: 'Tulip' },
  { id: 17, icon: '🥦', name: 'Broccoli' },
  { id: 18, icon: '🌶️', name: 'Pepper' },
  { id: 19, icon: '🥒', name: 'Cucumber' },
  { id: 20, icon: '🍆', name: 'Eggplant' },
  { id: 21, icon: '🥔', name: 'Potato' },
  { id: 22, icon: '🧄', name: 'Garlic' },
  { id: 23, icon: '🧅', name: 'Onion' },
  { id: 24, icon: '🥜', name: 'Peanut' }
])

const selectedAvatar = ref(avatarOptions.value[0])

const profileData = reactive({
  name: '',
  phone: ''
})

const passwordForm = reactive({
  current: '',
  new: '',
  confirm: ''
})

const pinForm = reactive({
  current: '',
  new: '',
  confirm: ''
})

const selectAvatar = (avatar) => {
  selectedAvatar.value = avatar
  showToastMessage(`Avatar changed to ${avatar.name}`)
}

const togglePasswordSection = () => {
  showPasswordSection.value = !showPasswordSection.value
  if (showPasswordSection.value) {
    showPinSection.value = false
  }
  // Reset password visibility when closing
  if (!showPasswordSection.value) {
    showCurrentPassword.value = false
    showNewPassword.value = false
    showConfirmPassword.value = false
  }
}

const togglePinSection = () => {
  showPinSection.value = !showPinSection.value
  if (showPinSection.value) {
    showPasswordSection.value = false
  }
  // Reset pin visibility when closing
  if (!showPinSection.value) {
    showCurrentPin.value = false
    showNewPin.value = false
    showConfirmPin.value = false
  }
}

const showToastMessage = (message) => {
  toastMessage.value = message
  showToast.value = true
  setTimeout(() => {
    showToast.value = false
  }, 3000)
}

const saveProfile = () => {
  if (!profileData.name.trim()) {
    showToastMessage('Please enter your name')
    return
  }
  
  if (!profileData.phone.trim()) {
    showToastMessage('Please enter your phone number')
    return
  }
  
  const updatedUser = {
    ...user.value,
    name: profileData.name,
    phone: profileData.phone,
    avatar: selectedAvatar.value
  }
  
  localStorage.setItem('user', JSON.stringify(updatedUser))
  user.value = updatedUser
  
  showToastMessage('Profile updated successfully!')
}

const changePassword = () => {
  if (!passwordForm.current || !passwordForm.new || !passwordForm.confirm) {
    showToastMessage('Please fill in all password fields')
    return
  }
  
  if (passwordForm.new !== passwordForm.confirm) {
    showToastMessage('New passwords do not match')
    return
  }
  
  if (passwordForm.new.length < 6) {
    showToastMessage('Password must be at least 6 characters')
    return
  }
  
  showPasswordSection.value = false
  passwordForm.current = ''
  passwordForm.new = ''
  passwordForm.confirm = ''
  showCurrentPassword.value = false
  showNewPassword.value = false
  showConfirmPassword.value = false
  showToastMessage('Password updated successfully!')
}

const changePin = () => {
  if (!pinForm.current || !pinForm.new || !pinForm.confirm) {
    showToastMessage('Please fill in all pin fields')
    return
  }
  
  if (pinForm.new !== pinForm.confirm) {
    showToastMessage('New pins do not match')
    return
  }
  
  if (pinForm.new.length !== 4) {
    showToastMessage('Pin must be exactly 4 digits')
    return
  }
  
  showPinSection.value = false
  pinForm.current = ''
  pinForm.new = ''
  pinForm.confirm = ''
  showCurrentPin.value = false
  showNewPin.value = false
  showConfirmPin.value = false
  showToastMessage('Pin code updated successfully!')
}

const logout = () => {
  if (confirm('Are you sure you want to logout?')) {
    localStorage.removeItem('user')
    sessionStorage.removeItem('user')
    router.push('/')
    showToastMessage('Logged out successfully!')
  }
}

onMounted(() => {
  const storedUser = localStorage.getItem('user') || sessionStorage.getItem('user')
  if (storedUser) {
    try {
      user.value = JSON.parse(storedUser)
      profileData.name = user.value.name || user.value.firstName + ' ' + user.value.lastName || ''
      profileData.phone = user.value.phone || ''
      if (user.value.avatar) {
        selectedAvatar.value = user.value.avatar
      }
    } catch (e) {
      console.error('Error parsing user data:', e)
    }
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Custom scrollbar - MODIFIED FOR BETTER POSITIONING */
::-webkit-scrollbar {
  width: 4px;
}

::-webkit-scrollbar-track {
  background: transparent;
  margin: 8px 0;
}

::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 2px;
}

::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

/* Smooth transitions */
* {
  transition: all 200ms ease-in-out;
}

/* Enhanced focus styles */
input:focus {
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

/* Enhanced button hover effects */
button:hover {
  transform: translateY(-1px);
}

button:active {
  transform: translateY(0);
}

/* Responsive adjustments - MODIFIED FOR BETTER SPACING */
@media (max-width: 1024px) {
  .w-\[30\%\] {
    width: 35%;
  }
  
  .grid-cols-1.md\\:grid-cols-2 {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .flex.gap-6 {
    flex-direction: column;
    gap: 1rem;
  }
  
  .w-\[30\%\] {
    width: 100%;
    min-height: 300px;
  }
  
  .grid-cols-4 {
    grid-template-columns: repeat(6, 1fr);
  }
  
  .w-28.h-28 {
    width: 5rem;
    height: 5rem;
  }
  
  /* MOBILE SPECIFIC PADDING ADJUSTMENTS */
  .px-3 {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
}

@media (max-width: 640px) {
  .p-6 {
    padding: 1rem;
  }
  
  .min-w-\[100px\] {
    min-width: 80px;
  }
  
  /* SMALL MOBILE ADJUSTMENTS */
  .px-3 {
    padding-left: 0.25rem;
    padding-right: 0.25rem;
  }
  
  .gap-2 {
    gap: 0.375rem;
  }
}

/* ADDITIONAL RESPONSIVE IMPROVEMENTS */
@media (max-width: 480px) {
  .grid-cols-4 {
    grid-template-columns: repeat(5, 1fr);
  }
  
  .w-11.h-11 {
    width: 2.25rem;
    height: 2.25rem;
  }
}
</style>