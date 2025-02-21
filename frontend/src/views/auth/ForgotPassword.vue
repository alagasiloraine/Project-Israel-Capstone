<template>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 relative overflow-hidden">
    <!-- Falling Leaves Animation (kept the same as login) -->
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
          <h2 class="text-2xl font-bold mb-1">Reset Password</h2>
          <p class="text-sm text-gray-200/90 mt-1 text-center font-light">Don't worry! It happens. Please enter the email associated with your account.</p>
        </div>

        <div class="relative flex justify-center z-10">
          <button 
            @click="handleBackToLogin" 
            class="text-white hover:text-[#FFA500] flex items-center gap-2 transition-colors duration-300 border border-white/50 rounded-lg px-4 py-2 hover:bg-white/20"
          >
            <ArrowLeft class="h-4 w-4" />
            <span class="text-sm">Back to Login</span>
          </button>
        </div>
      </div>

      <!-- Right Side - Reset Password Form -->
      <div class="w-full md:w-1/2 bg-white p-6 flex flex-col">
        <div class="w-[90%] max-w-xs mx-auto flex-1 flex flex-col justify-center">
          <h2 class="text-xl font-bold text-[#2B5329] text-center mb-2">
            {{ currentStep === 1 ? 'Forgot Password' : 
               currentStep === 2 ? 'Verify Code' : 'Create New Password' }}
          </h2>
          <p v-if="currentStep === 1" class="text-sm text-gray-600 text-center mb-6">
            Enter your email and we'll send you a verification code to reset your password
          </p>

          <!-- Step 1: Email Input -->
          <form v-if="currentStep === 1" @submit.prevent="handleSendResetEmail" class="space-y-4">
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input 
                id="email" 
                type="email" 
                v-model="email"
                required 
                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                placeholder="Enter your email address"
              />
            </div>

            <button 
              type="submit" :disabled="isLoading"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-white bg-[#2B5329] hover:bg-[#1F3D1F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#FFA500] transition-colors duration-200"
            >
             {{ isLoading ? "Sending Verification Code..." : "Send Verification Code" }}
            </button>
          </form>

          <!-- Step 2: Verification Code -->
          <form v-if="currentStep === 2" @submit.prevent="handleVerifyCode" class="space-y-6">
            <div class="text-center">
              <h3 class="text-sm font-semibold text-[#2B5329] mb-2">Enter the 6-digit code</h3>
              <p class="text-sm text-gray-600">We sent to your email</p>
            </div>

            <div class="flex justify-center gap-2">
              <template v-for="i in 6" :key="i">
                <input
                  type="text"
                  :ref="el => codeRefs[i-1] = el"
                  v-model="verificationDigits[i-1]"
                  maxlength="1"
                  class="w-12 h-12 text-center text-lg border-2 border-gray-300 rounded-lg focus:border-[#2B5329] focus:ring-2 focus:ring-[#2B5329] focus:outline-none transition-colors"
                  @input="handleCodeInput($event, i-1)"
                  @keydown.delete="handleBackspace($event, i-1)"
                  @keydown.left="focusPrevious(i-1)"
                  @keydown.right="focusNext(i-1)"
                  @paste="handlePaste"
                />
              </template>
            </div>

            <button 
              type="submit" :disabled="isLoading"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-white bg-[#2B5329] hover:bg-[#1F3D1F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#FFA500] transition-colors duration-200"
            >
              {{ isLoading ? "Verifying Code..." : "Verify Code" }}
            </button>

            <div class="text-center mt-4">
              <p class="text-sm text-gray-600">
                Didn't receive the code? 
                <button 
                  type="button"
                  @click="handleResendCode" 
                  class="text-[#2B5329] hover:text-[#FFA500] font-medium transition-colors ml-1"
                  :disabled="resendTimer > 0"
                >
                  {{ resendTimer > 0 ? `Resend in ${resendTimer}s` : 'Resend Code' }}
                </button>
              </p>
            </div>
          </form>

          <!-- Step 3: New Password -->
          <form v-if="currentStep === 3" @submit.prevent="handleResetPassword" class="space-y-4">
            <div class="text-center mb-6">
              <p class="text-sm text-gray-600">Create a password that's both secure and easy to remember.</p>
            </div>
            <div>
              <label for="newPassword" class="block text-sm font-medium text-gray-700">New Password</label>
              <div class="relative">
                <input 
                  :type="showPassword ? 'text' : 'password'"
                  id="newPassword" 
                  v-model="newPassword"
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

            <div>
              <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirm Password</label>
              <div class="relative">
                <input 
                  :type="showConfirmPassword ? 'text' : 'password'"
                  id="confirmPassword" 
                  v-model="confirmPassword"
                  required 
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-[#2B5329] focus:border-[#2B5329]"
                />
                <button 
                  type="button"
                  @click="showConfirmPassword = !showConfirmPassword"
                  class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500"
                >
                  <Eye v-if="!showConfirmPassword" class="h-4 w-4" />
                  <EyeOff v-else class="h-4 w-4" />
                </button>
              </div>
            </div>

            <button 
              type="submit" :isLoading="false"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-white bg-[#2B5329] hover:bg-[#1F3D1F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#FFA500] transition-colors duration-200"
            >
              {{ isLoading ? "Reseting Password..." : "Reset Password" }}
            </button>
          </form>
        </div>
        <LoadingPage 
          :is-visible="isLoading"
          title="Loading..."
          message="Please wait while we set up your new account"
          @loading-complete="onLoadingComplete"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, Eye, EyeOff } from 'lucide-vue-next'
import api from '../../api/index.js'
import toastr from 'toastr'
import LoadingPage from '../layout/LoadingPage.vue'

const router = useRouter()
const currentStep = ref(1)
const email = ref('')
const verificationCode = ref('')
const newPassword = ref('')
const confirmPassword = ref('')
const showPassword = ref(false)
const showConfirmPassword = ref(false)
const isMobile = ref(window.innerWidth < 640)
const verificationDigits = ref(['', '', '', '', '', ''])
const codeRefs = ref([])
const resendTimer = ref(0)
const isLoading = ref(false);
let resendInterval = null

const handleResize = () => {
  isMobile.value = window.innerWidth < 640
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
  startResendTimer() // Start timer when verification step is shown
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  if (resendInterval) {
    clearInterval(resendInterval)
  }
})

const handleCodeInput = (event, index) => {
  const value = event.target.value
  // Only allow numbers
  if (!/^\d*$/.test(value)) {
    verificationDigits.value[index] = ''
    return
  }
  
  // Auto-advance to next input
  if (value && index < 5) {
    codeRefs.value[index + 1]?.focus()
  }
}

const handleBackspace = (event, index) => {
  if (!verificationDigits.value[index] && index > 0) {
    codeRefs.value[index - 1]?.focus()
  }
}

const focusPrevious = (index) => {
  if (index > 0) {
    codeRefs.value[index - 1]?.focus()
  }
}

const focusNext = (index) => {
  if (index < 5) {
    codeRefs.value[index + 1]?.focus()
  }
}

const handlePaste = (event) => {
  event.preventDefault()
  const pastedData = event.clipboardData.getData('text')
  const numbers = pastedData.match(/\d/g)
  if (numbers) {
    numbers.slice(0, 6).forEach((num, i) => {
      verificationDigits.value[i] = num
    })
  }
}

const startResendTimer = () => {
  resendTimer.value = 30
  resendInterval = setInterval(() => {
    if (resendTimer.value > 0) {
      resendTimer.value--
    } else {
      clearInterval(resendInterval)
    }
  }, 1000)
}

// Step 1: Request password reset
const handleSendResetEmail = async () => {
  try {
    isLoading.value = true;
    const response = await api.post("/auth/forgot-password", { email: email.value });
    toastr.success(response.data.message);
    currentStep.value = 2; // Move to verification step
  } catch (error) {
    isLoading.value = false
    console.error("Error sending reset email:", error.response?.data || error);
    toastr.error(error.response?.data?.detail || "Error sending reset email.");
  } finally {
    isLoading.value = false;
  }
};

const handleResendCode = async () => {
  isLoading.value = false;
  try {
    // Call backend to resend the verification 
    isLoading.value = false;
    // Call backend to resend the verification code to the provided email address
    const response = await api.post("/auth/forgot-password", {
      email: email.value,
    });

    toastr.success(response.data.message); // Notify the user that the code has been resent
    startResendTimer(); // Start the resend timer (e.g., 30 seconds cooldown)

  } catch (error) {
    isLoading.value = false;
    console.error("Error resending code:", error.response?.data || error);
    toastr.error(error.response?.data?.detail || "Error resending code.");
  } finally {
    isLoading.value = false;
  }
};

// ✅ Step 2: Verify the 6-digit code
const handleVerifyCode = async () => {
  isLoading.value = true;
  try {
    // Join the verification digits into a single string
    const verificationCodeString = verificationDigits.value.join('');

    const response = await api.post("/auth/verify-code", {
      email: email.value,
      code: verificationCodeString  // Send the joined code as a single string
    });

    toastr.success(response.data.message);
    currentStep.value = 3; // Move to password reset step
  } catch (error) {
    isLoading.value = false;
    console.error("Error verifying code:", error.response?.data || error);
    toastr.error(error.response?.data?.detail || "Invalid verification code.");
  } finally {
    isLoading.value = false;
  }
};


const handleResetPassword = async () => {
  isLoading.value = false; // Show loading state
  // Check if the new password and confirm password match
  if (newPassword.value !== confirmPassword.value) {
    toastr.warning('Passwords do not match!');
    return;
  }

  // Check if password meets any required criteria (e.g., length, strength)
  if (newPassword.value.length < 6) {
    toastr.warning('Password must be at least 6 characters long.');
    return;
  }
 // Show loading state
  try {
    isLoading.value = true; // Show loading state
    // Send request to backend to reset the password
    const response = await api.post("/auth/reset-password", {
      email: email.value, // User's email
      new_password: newPassword.value, // New password
    });

    toastr.success(response.data.message); // Notify the user
    router.push('/login'); // Redirect to login page after password is reset

  } catch (error) {
    isLoading.value = false; // Hide loading state
    console.error("Error resetting password:", error.response?.data || error);
    toastr.error(error.response?.data?.detail || "Error resetting password.");
  } finally {
    isLoading.value = false; // Hide loading state
  }
};

const handleBackToLogin = () => {
  router.push('/login')
}
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

/* Replace the existing input type="text" styles */
input[type="text"] {
  -webkit-appearance: none;
  appearance: none;
  margin: 0;
  caret-color: #2B5329;
  text-align: center;
  font-size: 1.25rem;
}

input[type="text"]::-webkit-outer-spin-button,
input[type="text"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="text"]:focus {
  outline: none;
  border-color: #2B5329;
}
</style>

