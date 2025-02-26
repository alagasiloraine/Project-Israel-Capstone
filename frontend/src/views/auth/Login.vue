<!-- Login.vue -->
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
          <h2 class="text-3xl font-bold mt-[160px] mb-6">Welcome Back!</h2>
          <p class="text-lg text-gray-200 mt-4">Your trusted partner in crop recommendations and agricultural wisdom.</p>
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

      <!-- Right Side - Login Form -->
      <div class="w-full md:w-1/2 bg-white p-12">
        <div class="max-w-md w-full mx-auto">
          <h2 class="text-3xl font-bold text-gray-900 mb-8 ml-14">Login to your Account</h2>

          <form class="space-y-6" @submit.prevent="handleLogin">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input 
                id="email" 
                type="email" 
                v-model="email"
                required 
                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
              />
            </div>

            <div>
              <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
              <div class="relative">
                <input 
                  :type="showPassword ? 'text' : 'password'"
                  id="password" 
                  v-model="password"
                  required 
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
            </div>

            <div class="flex items-center justify-between">
              <a href="#" class="text-sm text-[#2B5329] hover:text-[#FFA500] transition-colors">Forgot password?</a>
            </div>

            <button 
              type="submit" 
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-white bg-[#2B5329] hover:bg-[#1F3D1F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#FFA500] transition-colors duration-200"
            >
              Get Started
            </button>

            <div class="relative my-6">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-gray-300"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="px-2 bg-white text-gray-500">Or sign in with</span>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-4">
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

            <div class="text-center mt-6">
              <p class="text-sm text-gray-600">
                Don't have an account? 
                <router-link to="/register" class="text-[#2B5329] hover:text-[#FFA500] font-medium transition-colors">
                  Request Now
                </router-link>
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, Eye, EyeOff, Chrome, Facebook } from 'lucide-vue-next'

const router = useRouter()
const email = ref('')
const password = ref('')
const showPassword = ref(false)

const handleLogin = () => {
  // Check for admin login
  if (email.value === 'admin@example.com' && password.value === 'admin123') {
    console.log('Admin login successful')
    router.push('/overview')
  }
  // Check for staff login
  else if (email.value === 'staff@example.com' && password.value === 'password123') {
    console.log('Staff login successful')
    router.push('/dashboard')
  }
  else {
    // Failed login
    console.log('Login failed')
    alert('Invalid email or password')
  }
}
</script>