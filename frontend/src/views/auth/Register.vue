<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50">
    <div class="max-w-5xl w-full flex shadow-2xl rounded-2xl overflow-hidden">
      <!-- Left Side - Image and Branding -->
      <div class="hidden md:flex md:w-1/2 bg-[#2B5329] text-white p-12 flex-col justify-between relative">
        <!-- Background Image -->
        <div 
          class="absolute inset-0 bg-cover bg-center mix-blend-overlay opacity-20"
          style="background-image: url('https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80');"
        ></div>
        
        <div class="relative text-center mx-auto">
          <h2 class="text-3xl font-bold mt-[220px] mb-4">Harvesting Knowledge</h2>
          <p class="text-lg text-gray-200 mb-12">Your trusted partner in crop recommendations and agricultural wisdom.</p>
        </div>

        <!-- Back to Website - Centered -->
        <div class="relative flex justify-center">
          <router-link 
            to="/" 
            class="text-white hover:text-[#FFA500] flex items-center gap-2 transition-colors duration-300"
          >
            <ArrowLeft class="h-5 w-5" />
            <span>Back to website</span>
          </router-link>
        </div>
      </div>

      <!-- Right Side - Registration Form -->
      <div class="w-full md:w-1/2 bg-white p-12">
        <div class="max-w-md w-full mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 mb-2 ml-[90px]">Create an account</h2>
          <p class="text-gray-600 mb-8 ml-[55px]">Enter your personal data to create an account</p>

          <form @submit.prevent="handleSubmit" class="space-y-6">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label for="firstName" class="block text-sm font-medium text-gray-700">First name</label>
                <input
                  id="firstName"
                  type="text"
                  v-model="form.firstName"
                  required
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                />
              </div>
              <div>
                <label for="lastName" class="block text-sm font-medium text-gray-700">Last name</label>
                <input
                  id="lastName"
                  type="text"
                  v-model="form.lastName"
                  required
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                />
              </div>
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input
                id="email"
                type="email"
                v-model="form.email"
                required
                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
              />
            </div>

            <div>
              <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
              <div class="space-y-2">
                <div class="relative">
                  <input
                    id="password"
                    :type="showPassword ? 'text' : 'password'"
                    v-model="form.password"
                    required
                    @input="checkPasswordStrength"
                    class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                  />
                  <button
                    type="button"
                    @click="showPassword = !showPassword"
                    class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500"
                  >
                    <Eye v-if="!showPassword" class="h-5 w-5" />
                    <EyeOff v-else class="h-5 w-5" />
                  </button>
                </div>
                
                <!-- Password strength indicator -->
                <div class="flex gap-2 h-1">
                  <div 
                    v-for="(segment, index) in 4" 
                    :key="index"
                    :class="[
                      'flex-1 rounded-full transition-all duration-300',
                      index < passwordStrength ? strengthColors[passwordStrength - 1] : 'bg-gray-200'
                    ]"
                  ></div>
                </div>
                
                <!-- <p class="text-xs text-gray-500">Must be at least 8 characters</p> -->
              </div>
            </div>

            <div class="flex items-center">
              <input
                type="checkbox"
                id="terms"
                v-model="form.acceptTerms"
                required
                class="h-4 w-4 rounded border-gray-300 text-[#2B5329] focus:ring-[#2B5329]"
              />
              <label for="terms" class="ml-2 text-sm text-gray-600">
                I agree to the
                <a href="#" class="text-[#2B5329] hover:text-[#FFA500] transition-colors">Terms & Conditions</a>
              </label>
            </div>

            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-white bg-[#2B5329] hover:bg-[#1F3D1F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#FFA500] transition-colors duration-200"
            >
              Sign Up
            </button>
          </form>

          <div class="mt-6">
            <div class="relative">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-gray-300"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="px-2 bg-white text-gray-500">Or register with</span>
              </div>
            </div>

            <div class="mt-6 grid grid-cols-2 gap-4">
              <button 
                type="button"
                class="flex items-center justify-center px-4 py-2 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
              >
                <Chrome class="h-5 w-5 mr-2" />
                Google
              </button>
              <button 
                type="button"
                class="flex items-center justify-center px-4 py-2 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
              >
                <Facebook class="h-5 w-5 mr-2" />
                Facebook
              </button>
            </div>

            <div class="mt-6 text-center">
              <span class="text-[#2B5329]">Already have an account? </span>
              <router-link 
                to="/login" 
                class="text-[#2B5329] hover:text-[#FFA500] transition-colors inline-flex items-center gap-1"
              >
                <LogIn class="h-4 w-4" />
                <span>Login</span>
              </router-link>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ArrowLeft, Eye, EyeOff, Chrome, Facebook, LogIn } from 'lucide-vue-next'

const form = ref({
  firstName: '',
  lastName: '',
  email: '',
  password: '',
  acceptTerms: false
})

const showPassword = ref(false)
const passwordStrength = ref(0)

const strengthColors = [
  'bg-red-500',    // Weak
  'bg-yellow-500', // Fair
  'bg-blue-500',   // Good
  'bg-green-500'   // Strong
]

const checkPasswordStrength = () => {
  const password = form.value.password
  let strength = 0
  
  if (password.length >= 8) strength++
  if (password.match(/[A-Z]/)) strength++
  if (password.match(/[0-9]/)) strength++
  if (password.match(/[^A-Za-z0-9]/)) strength++
  
  passwordStrength.value = strength
}

const handleSubmit = () => {
  console.log('Form submitted:', form.value)
}
</script>