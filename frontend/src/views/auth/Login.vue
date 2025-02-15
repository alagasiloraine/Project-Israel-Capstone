<template>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 relative overflow-hidden">
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
          <div class="hidden md:flex md:w-1/2 bg-[#2B5329] text-white p-6 md:p-8 flex-col justify-end relative">
            <!-- Background Image -->
            <div 
              class="absolute inset-0 bg-cover bg-center"
              style="background-image: url('/public/images/greenhouse.jpg');"
            ></div>
            <!-- Dark gradient overlay -->
            <div class="absolute inset-0 bg-gradient-to-r from-[#1A3A1A] via-[#2B5329]/95 to-[#2B5329]/85"></div>
            
            <!-- Content -->
            <div class="relative flex flex-col items-center z-10 mt-0 pt-4 mb-auto">
              <div class="w-40 h-40 sm:w-48 sm:h-48 mb-2 relative overflow-visible">
                <img 
                  src="/images/plants.gif"
                  alt="Growing plant animation"   
                  class="w-[130%] h-[130%] max-w-none object-contain mix-blend-multiply filter brightness-100 contrast-100 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
                />
              </div>
              <h2 class="text-2xl font-bold mb-1">Welcome Back!</h2>
              <p class="text-sm text-gray-200/90 mt-1 text-center font-light">Your trusted partner in crop recommendations and agricultural wisdom.</p>
            </div>

            <div class="relative flex justify-center z-10">
              <button 
                @click="handleBackToWebsite" 
                class="text-white hover:text-[#FFA500] flex items-center gap-2 transition-colors duration-300 border border-white/50 rounded-lg px-4 py-2 hover:bg-white/20"
              >
                <ArrowLeft class="h-4 w-4" />
                <span class="text-sm">Back to website</span>
              </button>
            </div>
          </div>

          <!-- Right Side - Login Form -->
          <div class="w-full md:w-1/2 bg-white p-6 flex flex-col">
            <div class="w-[90%] max-w-xs mx-auto flex-1 flex flex-col justify-center">
              <h2 class="text-xl font-bold text-[#2B5329] text-center mb-6">Login to your Account</h2>

              <form class="space-y-4" @submit.prevent="handleLogin">
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
                      <Eye v-if="!showPassword" class="h-4 w-4" />
                      <EyeOff v-else class="h-4 w-4" />
                    </button>
                  </div>
                </div>

                <div class="flex items-center justify-between mt-2">
                  <div class="flex items-center">
                    <input
                      id="remember-me"
                      type="checkbox"
                      v-model="rememberMe"
                      class="h-4 w-4 rounded border-gray-300 cursor-pointer text-[#2B5329] focus:ring-[#2B5329] focus:ring-offset-0 checked:bg-[#2B5329] checked:border-[#2B5329] hover:border-[#2B5329]"
                    />
                    <label for="remember-me" class="ml-2 block text-sm text-gray-700 cursor-pointer">
                      Remember me
                    </label>
                  </div>
                  <router-link to="/forgotpassword" class="text-xs text-[#2B5329] hover:text-[#FFA500] transition-colors">
                    Forgot password?
                  </router-link>
                </div>

                <button 
                  type="submit" :disabled="isLoading"
                  class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-white bg-[#2B5329] hover:bg-[#1F3D1F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#FFA500] transition-colors duration-200"
                >
                  {{ isLoading ? "Signing In..." : "Sign In" }}
                </button>

                <div class="relative my-4">
                  <div class="absolute inset-0 flex items-center">
                    <div class="w-full border-t border-gray-300"></div>
                  </div>
                  <div class="relative flex justify-center text-sm">
                    <span class="px-2 bg-white text-gray-500 text-xs">Or sign in with</span>
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                  <button 
                    type="button" @click="handleGoogleLogin"
                    class="flex items-center justify-center px-3 py-1.5 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-[#3a8a3a] hover:text-white hover:border-[#3a8a3a] hover:transform hover:-translate-y-1 transition-all duration-300"
                  >
                    <Chrome class="h-5 w-5 mr-2" />
                    Google
                  </button>
                  <button 
                    type="button"
                    class="flex items-center justify-center px-3 py-1.5 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-[#3a8a3a] hover:text-white hover:border-[#3a8a3a] hover:transform hover:-translate-y-1 transition-all duration-300"
                  >
                    <Facebook class="h-5 w-5 mr-2" />
                    Facebook
                  </button>
                </div>

                <div class="text-center mt-8 mb-4">
                  <p class="text-xs text-gray-600">
                    Don't have an account? 
                    <button 
                      @click="handleRequestNow" 
                      class="text-[#2B5329] hover:text-[#FFA500] font-medium transition-colors"
                    >
                      Request Now
                    </button>
                  </p>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, Eye, EyeOff, Chrome, Facebook } from 'lucide-vue-next'
import api from '../../api/index.js'
import { auth, googleProvider, signInWithPopup } from "../../api/firebase.js";

const router = useRouter()
const email = ref('')
const password = ref('')
const showPassword = ref(false)
const isMobile = ref(window.innerWidth < 640)
const transitionKey = ref(0)
const contentStyle = ref({})
const isLoading = ref(false);
const rememberMe = ref(false)

const handleResize = () => {
  isMobile.value = window.innerWidth < 640
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
  // Check for remembered email
  const rememberedEmail = localStorage.getItem('rememberedEmail')
  if (rememberedEmail) {
    email.value = rememberedEmail
    rememberMe.value = true
  }
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

const handleRequestNow = () => {
  transitionKey.value++
  contentStyle.value = { 
    position: 'relative', 
    left: '0px', 
    transition: 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)' 
  }

  setTimeout(() => {
    router.push('/register')
  }, 500)
}

const handleLogin = async () => {
  if (!email.value || !password.value) {
    alert("Please enter both email and password.");
    return;
  }

  isLoading.value = true;

  try {
    const response = await api.post("/auth/login", {
      email: email.value,
      password: password.value,
    });
    console.log("Login successful:", response.data);
    alert("Login successful!");

    // Check if 'Remember me' is selected
    if (rememberMe.value) {
      // Save token and user data to localStorage (persist for a long time)
      localStorage.setItem("token", response.data.token);
      localStorage.setItem("userId", response.data.userId);
      // Optionally store email or other user info
      localStorage.setItem("email", email.value);
    } else {
      // Save token and user data to sessionStorage (session expires when the browser is closed)
      sessionStorage.setItem("token", response.data.token);
      sessionStorage.setItem("userId", response.data.userId);
    }

    // Navigate to dashboard
    router.push("/dashboard");
  } catch (error) {
    console.error("Login failed:", error.response?.data || error);
    alert(error.response?.data?.detail || "Login failed. Please try again.");
  } finally {
    isLoading.value = false;
  }
}

const handleGoogleLogin = async () => {
  try {
    // 🔹 Open Google Sign-In popup
    const result = await signInWithPopup(auth, googleProvider);
    const user = result.user;

    console.log("✅ Google User:", user);

    // 🔹 Send the Firebase ID Token to the backend for verification
    const idToken = await user.getIdToken();
    const response = await api.post("/auth/google-login", {
      idToken: idToken // Send the token in the request body
    });

    console.log("✅ Backend Response:", response.data);
    alert("Login successful!");

    // Redirect to dashboard after login
    router.push("/dashboard");
  } catch (error) {
    console.error("❌ Google Login Error:", error);
    alert("Google login failed. Try again.");
  }
};


</script>

<style scoped>
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

* {
  font-family: 'Poppins', sans-serif;
}

h2 {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
}

button, input, label {
  font-family: 'Poppins', sans-serif;
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

input[type="checkbox"]:checked {
  background-color: #2B5329;
  border-color: #2B5329;
}

input[type="checkbox"]:focus {
  --tw-ring-color: #2B5329;
  --tw-ring-offset-width: 0px;
}
</style>

