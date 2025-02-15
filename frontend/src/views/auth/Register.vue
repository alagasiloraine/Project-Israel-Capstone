<template>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4 py-6 sm:px-6 lg:px-8 relative overflow-hidden">
    <transition name="page-transition" mode="out-in" @before-leave="beforeLeave" @enter="enter" @after-enter="afterEnter">
      <div :key="transitionKey" class="page-content" :style="contentStyle">
        <!-- Falling Leaves Animation -->
        <div class="absolute inset-0 pointer-events-none z-10 overflow-hidden">
          <div v-for="i in (isMobile ? 12 : 20)" :key="`leaf1-${i}`" 
               class="leaf absolute animate-fall"
               :style="{
                 left: `${Math.random() * 100}%`,
                 top: `${Math.random() * -200}%`,
                 animationDuration: `${15 + Math.random() * 15}s`,
                 animationDelay: `${Math.random() * -30}s`,
                 transform: `scale(${isMobile ? 0.7 : 0.95})`
               }">
            <img 
              src="/public/images/leaves-plants/fall-leaf1.png"
              alt="" 
              class="w-20 sm:w-24 h-20 sm:h-24 opacity-50"
            />
          </div>
          
          <div v-for="i in (isMobile ? 12 : 20)" :key="`leaf2-${i}`" 
               class="leaf absolute animate-fall"
               :style="{
                 left: `${Math.random() * 100}%`,
                 top: `${Math.random() * -200}%`,
                 animationDuration: `${15 + Math.random() * 15}s`,
                 animationDelay: `${Math.random() * -30}s`,
                 transform: `scale(${isMobile ? 0.7 : 0.95})`
               }">
            <img 
              src="/public/images/leaves-plants/fall-leaf2.png"
              alt="" 
              class="w-24 sm:w-28 h-24 sm:h-28 opacity-50"
            />
          </div>
        </div>

        <div class="max-w-3xl w-[95%] sm:w-[90%] md:w-[85%] lg:w-full min-h-[500px] flex shadow-xl rounded-xl overflow-hidden relative z-20">
          <!-- Left Side - Image and Branding -->
          <div class="hidden md:flex md:w-1/2 bg-[#2B5329] text-white p-6 md:p-8 flex-col justify-between relative">
            <!-- Background Image -->
            <div 
              class="absolute inset-0 bg-cover bg-center"
              style="background-image: url('/public/images/greenhouse.jpg');"
            ></div>
            <div class="absolute inset-0 bg-gradient-to-r from-[#1A3A1A] via-[#2B5329]/95 to-[#2B5329]/85"></div>
            
            <div class="relative flex flex-col items-center z-10 mt-0 pt-4 mb-auto">
              <div class="w-40 h-40 sm:w-48 sm:h-48 mb-2 relative overflow-visible">
                <img 
                  src="/images/plants.gif"
                  alt="Growing plant animation"   
                  class="w-[130%] h-[130%] max-w-none object-contain mix-blend-multiply filter brightness-100 contrast-100 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
                />
              </div>
              <h2 class="text-2xl font-bold mb-1">Harvesting Knowledge</h2>
              <p class="text-sm text-gray-200/90 mt-1 text-center font-light">Your trusted partner in crop recommendations and agricultural wisdom.</p>
            </div>

            <!-- Back to Website - Centered -->
            <div class="relative flex justify-center">
              <button 
                @click="handleBackToWebsite" 
                class="text-white hover:text-[#FFA500] flex items-center gap-1.5 transition-colors duration-300 border border-white/50 rounded-lg px-3 py-1.5 hover:bg-white/20 text-sm"
              >
                <ArrowLeft class="h-4 w-4" />
                <span class="text-sm">Back to website</span>
              </button>
            </div>
          </div>

          <!-- Right Side - Registration Form -->
          <div class="w-full md:w-1/2 bg-white p-5">
            <div class="max-w-[300px] w-full mx-auto">
              <h2 class="text-2xl font-bold text-[#2B5329] mb-2 text-center">Create an account</h2>
              <p class="text-xs text-gray-600 mb-4 text-center">Enter your personal data to create an account</p>

              <form @submit.prevent="handleSubmit" class="space-y-3">
                <div class="grid grid-cols-2 gap-3">
                  <div>
                    <label for="firstName" class="block text-sm font-medium text-gray-700 mb-1">First name</label>
                    <input
                      id="firstName"
                      type="text"
                      v-model="form.firstName"
                      required
                      class="block w-full px-3 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                    />
                  </div>
                  <div>
                    <label for="lastName" class="block text-sm font-medium text-gray-700 mb-1">Last name</label>
                    <input
                      id="lastName"
                      type="text"
                      v-model="form.lastName"
                      required
                      class="block w-full px-3 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                    />
                  </div>
                </div>

                <div>
                  <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                  <input
                    id="email"
                    type="email"
                    v-model="form.email"
                    required
                    class="block w-full px-3 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                  />
                </div>

                <div>
                  <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
                  <div class="space-y-1.5">
                    <div class="relative">
                      <input
                        id="password"
                        :type="showPassword ? 'text' : 'password'"
                        v-model="form.password"
                        required
                        @input="checkPasswordStrength"
                        class="block w-full px-3 py-1 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                      />
                      <button
                        type="button"
                        @click="showPassword = !showPassword"
                        class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500"
                      >
                        <Eye v-if="!showPassword" class="h-4 w-4" />
                        <EyeOff v-else class="h-4 w-4" />
                      </button>
                    </div>
                    
                    <!-- Password strength indicator -->
                    <div class="flex gap-1.5 h-1">
                      <div 
                        v-for="(segment, index) in 4" 
                        :key="index"
                        :class="[
                          'flex-1 rounded-full transition-all duration-300',
                          index < passwordStrength ? strengthColors[passwordStrength - 1] : 'bg-gray-200'
                        ]"
                      ></div>
                    </div>
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
                  <label for="terms" class="ml-2 text-xs text-gray-600">
                    I agree to the
                    <a href="#" class="text-[#2B5329] hover:text-[#FFA500] transition-colors">Terms & Conditions</a>
                  </label>
                </div>

                <button
                  type="submit" :disabled="isLoading"
                  class="w-full flex justify-center py-1 px-4 border border-transparent rounded-md shadow-sm text-white bg-[#2B5329] hover:bg-[#1F3D1F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#FFA500] transition-colors duration-200"
                >
                  {{ isLoading ? "Signing Up..." : "Sign Up" }}
                </button>
              </form>

              <div class="mt-4">
                <div class="relative">
                  <div class="absolute inset-0 flex items-center">
                    <div class="w-full border-t border-gray-300"></div>
                  </div>
                  <div class="relative flex justify-center text-sm">
                    <span class="px-2 bg-white text-gray-500 text-xs">Or register with</span>
                  </div>
                </div>

                <div class="mt-4 grid grid-cols-2 gap-3">
                  <button 
                    type="button"
                    class="flex items-center justify-center px-3 py-1.5 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-[#3a8a3a] hover:text-white hover:border-[#3a8a3a] hover:transform hover:-translate-y-1 transition-all duration-300"
                  >
                    <Chrome class="h-4 w-4 mr-1.5" />
                    Google
                  </button>
                  <button 
                    type="button"
                    class="flex items-center justify-center px-3 py-1.5 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-[#3a8a3a] hover:text-white hover:border-[#3a8a3a] hover:transform hover:-translate-y-1 transition-all duration-300"
                  >
                    <Facebook class="h-4 w-4 mr-1.5" />
                    Facebook
                  </button>
                </div>

                <div class="mt-4 text-center">
                  <span class="text-xs text-[#2B5329]">Already have an account? </span>
                  <button 
                    @click="handleLoginTransition"
                    class="text-[#2B5329] hover:text-[#FFA500] transition-colors inline-flex items-center gap-1 cursor-pointer"
                  >
                    <span class="text-xs font-bold">Login</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>

</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { ArrowLeft, Eye, EyeOff, Chrome, Facebook, LogIn } from 'lucide-vue-next'
import { useRouter } from 'vue-router'
import api from '../../api/index.js'

const router = useRouter()
const transitionKey = ref(0)
const contentStyle = ref({})

const form = ref({
  firstName: '',
  lastName: '',
  email: '',
  password: '',
  acceptTerms: false
})
const isLoading = ref(false);
const message = ref("");
const showPassword = ref(false)
const passwordStrength = ref(0)
const isMobile = ref(window.innerWidth < 640)

const handleResize = () => {
  isMobile.value = window.innerWidth < 640
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

const beforeLeave = (el) => {
  const { left } = el.getBoundingClientRect()
  el.style.left = left + 'px'
  el.style.position = 'absolute'
}

const enter = (el) => {
  const { left } = el.getBoundingClientRect()
  el.style.left = `${left + 50}px` 
  el.style.opacity = 0
}

const afterEnter = (el) => {
  el.style.left = ''
  el.style.position = ''
  el.style.opacity = ''
}

const handleBackToWebsite = () => {
  transitionKey.value++
  contentStyle.value = { 
    position: 'relative', 
    left: '0px', 
    transition: 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)' 
  }
  
  setTimeout(() => {
    router.push('/')
  }, 500)
}

const handleLoginTransition = () => {
  transitionKey.value++
  contentStyle.value = { 
    position: 'relative', 
    left: '0px', 
    transition: 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)' 
  }
  
  setTimeout(() => {
    router.push('/login')
  }, 500)
}

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

const handleSubmit = async () => {
  console.log("Form submitted:", form.value);

  if (!form.value.acceptTerms) {
    message.value = "You must accept the terms and conditions.";
    return;
  }

  isLoading.value = true;

  try {
    const response = await api.post("/auth/register", form.value);
    message.value = response.data.message;
    console.log("Registration success:", response.data);

    // ✅ Pass the UID in the query when navigating
    router.push(`/login/verification?uid=${response.data.userId}`);
  } catch (error) {
    message.value = error.response?.data?.detail || "Registration failed.";
    console.error("Error:", error);
  } finally {
    isLoading.value = false;
  }
};

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

:root {
  font-family: 'Poppins', sans-serif;
}

h2, p, label, input, button, a, span {
  font-family: 'Poppins', sans-serif;
}

@keyframes fall {
  0% {
    transform: translateY(-100%) rotate(0deg);
    opacity: 0;
  }
  10% {
    opacity: 0.4;
  }
  90% {
    opacity: 0.4;
  }
  100% {
    transform: translateY(100vh) rotate(360deg);
    opacity: 0;
  }
}

.animate-fall {
  animation: fall linear infinite;
  will-change: transform, opacity;
}

.leaf {
  pointer-events: none;
  z-index: 10;
}

/* Page transition styles */
.page-transition-enter-active,
.page-transition-leave-active {
  transition: opacity 0.5s ease, transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  position: absolute;
  width: 100%;
}

.page-transition-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.page-transition-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .page-content {
    padding: 1rem;
  }
}

@media (min-width: 641px) and (max-width: 1024px) {
  .page-content {
    padding: 2rem;
  }
}
</style>