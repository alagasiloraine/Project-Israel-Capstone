<template>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4 py-6 sm:px-6 lg:px-8 relative overflow-hidden">
    <!-- Falling Leaves Animation - Moved outside transition -->
    <div class="absolute inset-0 pointer-events-none z-0 overflow-hidden">
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

    <transition name="page-transition" mode="out-in" @before-leave="beforeLeave" @enter="enter" @after-enter="afterEnter">
      <div :key="transitionKey" class="page-content relative z-10" :style="contentStyle">
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

          <!-- Right Side - Registration Form -->
          <div class="w-full md:w-1/2 bg-white p-5">
            <div class="max-w-[300px] w-full mx-auto">
              <h2 class="text-2xl font-bold text-[#2B5329] mb-2 text-center">Create an account</h2>
              <p class="text-xs text-gray-600 mb-4 text-center">Enter your personal data to create an account</p>

              <form @submit.prevent="handleSubmit" class="space-y-3">
                <!-- <div class="flex space-x-4">
                  <button
                    type="button"
                    @click="useEmail = true"
                    :class="['px-4 py-2 border rounded-md', useEmail ? 'bg-[#2B5329] text-white' : 'bg-gray-200']"
                  >
                    Register with Email
                  </button>
                  <button
                    type="button"
                    @click="useEmail = false"
                    :class="['px-4 py-2 border rounded-md', !useEmail ? 'bg-[#2B5329] text-white' : 'bg-gray-200']"
                  >
                    Register with Phone
                  </button>
                </div> -->
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
                    class="block w-full px-3 py-1 border rounded-md"
                  />
                </div>

                <!-- Email Input -->
                <!-- <div v-if="useEmail">
                  <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                  <input
                    id="email"
                    type="email"
                    v-model="form.email"
                    required
                    class="block w-full px-3 py-1 border rounded-md"
                  />
                </div> -->

                <!-- Phone Number Input -->
                <!-- <div v-else>
                  <label for="phone" class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
                  <input
                    id="phone"
                    type="tel"
                    v-model="form.phone"
                    required
                    class="block w-full px-3 py-1 border rounded-md"
                  />
                </div> -->

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

                <div id="recaptcha-container"></div>

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

                <div class="mt-4 grid grid-cols-1 gap-3">
                  <button 
                    type="button" @click="handleGoogleRegister"
                    class="flex items-center justify-center px-3 py-1.5 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-[#3a8a3a] hover:text-white hover:border-[#3a8a3a] hover:transform hover:-translate-y-1 transition-all duration-300"
                  >
                    <Chrome class="h-4 w-4 mr-1.5" />
                    Google
                  </button>
                  <!-- <button 
                    type="button"
                    class="flex items-center justify-center px-3 py-1.5 border border-gray-300 rounded-md shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-[#3a8a3a] hover:text-white hover:border-[#3a8a3a] hover:transform hover:-translate-y-1 transition-all duration-300"
                  >
                    <Facebook class="h-4 w-4 mr-1.5" />
                    Facebook
                  </button> -->
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
        <LoadingPage 
          :is-visible="isLoading"
          title="Creating your account..."
          message="Please wait while we set up your new account"
          @loading-complete="onLoadingComplete"
        />
      </div>
    </transition>
  </div>

</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { ArrowLeft, Eye, EyeOff, Chrome, Facebook, LogIn } from 'lucide-vue-next'
import { useRouter } from 'vue-router'
import LoadingPage from '../layout/LoadingPage.vue'
import api from '../../api/index.js'
import { auth, googleProvider, signInWithPopup, RecaptchaVerifier, signInWithPhoneNumber } from "../../api/firebase.js";
import toastr from "toastr";


const router = useRouter();
const transitionKey = ref(0);
const contentStyle = ref({});
const useEmail = ref(true);


const form = ref({
  firstName: "",
  lastName: "",
  email: "",
  phone: "",
  password: "",
  acceptTerms: false,
});

const message = ref("");
const showPassword = ref(false)
const passwordStrength = ref(0)
const isMobile = ref(window.innerWidth < 640)
const isLoading = ref(false)

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

  // toastr.options = {
  //   closeButton: true,
  //   progressBar: true,
  //   positionClass: "toast-top-right",
  //   timeOut: "3000",
  // };

const handleSubmit = async () => {
  console.log("Form submitted:", form.value);

  if (!form.value.acceptTerms) {
    toastr.warning("You must accept the terms and conditions.");
    return;
  }

  if (!form.value.firstName.trim() || !form.value.lastName.trim() || !form.value.email.trim() || !form.value.password.trim()) {
    toastr.warning("All fields are required.");
    return;
  }

  if (!form.value.acceptTerms) {
    alert("You must accept the terms and conditions.");
    return;
  }

  isLoading.value = true;

  try {
    // Register user with full details
    const response = await api.post("/auth/register", form.value);

    toastr.success(`Registration successful! Verify your account.`);
    router.push(`/login/verification?uid=${response.data.userId}`);
  } catch (error) {
    console.error("General Error:", error);
    toastr.error(error.response?.data?.detail || "Registration failed. Please try again.");
  } finally {
    isLoading.value = false;
  }
};

// const handleSubmit = async () => {
//   console.log("Form submitted:", form.value);

//   if (!form.value.acceptTerms) {
//     alert("You must accept the terms and conditions.");
//     return;
//   }

//   isLoading.value = true;

//   try {
//     if (useEmail.value) {
//       // Register with Email
//       const response = await api.post("/auth/register", form.value);
//       alert("Registration successful. Check your email for verification.");
//       router.push(`/login/verification?uid=${response.data.userId}`);
//     } 
//     // else {
//     //   // Register with Phone
//     //   let phoneNumber = form.value.phone.trim();

//     //   // Log phone number for debugging
//     //   console.log("Phone number before validation:", phoneNumber);

//     //   // Ensure phone number starts with "+63" and is 12 digits long
//     //   if (/^09\d{9}$/.test(phoneNumber)) {
//     //     // Convert "09123456789" to "+639123456789"
//     //     phoneNumber = "+63" + phoneNumber.substring(1);
//     //   } else if (!/^\+639\d{9}$/.test(phoneNumber)) {
//     //     alert("Invalid phone number format. Enter a valid Philippine number (e.g., 09123456789)");
//     //     return;
//     //   }

//     //   // Log the phone number after formatting
//     //   console.log("Formatted phone number:", phoneNumber);

//     //   if (!window.recaptchaVerifier) {
//     //     window.recaptchaVerifier = new RecaptchaVerifier(auth, "recaptcha-container", {
//     //       size: "invisible",
//     //     });
//     //   }

//     //   try {
//     //     // Send OTP
//     //     const confirmation = await signInWithPhoneNumber(auth, phoneNumber, window.recaptchaVerifier);
//     //     window.confirmationResult = confirmation;
//     //     console.log("OTP sent successfully:", confirmation);
        
//     //     alert("OTP sent to your phone. Verify your OTP to complete registration.");
//     //     router.push(`/otp-verification`);
//     //   } catch (otpError) {
//     //     console.error("OTP Error:", otpError);
//     //     alert(`OTP Error: ${otpError.message}`);
//     //   }
//     // }
//   } catch (error) {
//     console.error("General Error:", error);
//     alert("Registration failed.");
//   } finally {
//     isLoading.value = false;
//   }
// }

const onLoadingComplete = () => {
  isLoading.value = false
}
  
const handleGoogleRegister = async () => {
  try {
    // 🔹 Open Google Sign-In popup
    const result = await signInWithPopup(auth, googleProvider);
    const user = result.user;

    console.log("✅ Google User:", user);

    // 🔹 Send the Firebase ID Token to the backend
    const idToken = await user.getIdToken();
    const response = await api.post("/auth/google-register", { idToken });

    console.log("✅ Backend Response:", response.data);

    const { user: userData } = response.data;

    // ✅ Ensure profile picture exists
    if (!userData.profilePicture) {
      userData.profilePicture = generateProfilePicture(userData.email);
    }

    // ✅ Save user data to localStorage
    localStorage.setItem("user", JSON.stringify(userData));

    // ✅ Display user info in UI
    user.value = userData;  // If using Vue's ref()

    toastr.success("Registration successful!");
    router.push("/dashboard");
  } catch (error) {
    console.error("❌ Google Registration Error:", error);
    toastr.error(error.response?.data?.detail || "Google registration failed.");
  }
};

// ✅ Helper function for default profile picture
const generateProfilePicture = (email) => {
  const initials = email[0].toUpperCase();
  return `https://dummyimage.com/100x100/000/fff.png&text=${initials}`;
};


</script>

<style scoped>
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
  animation-play-state: running !important;
}

.leaf {
  pointer-events: none;
  z-index: 10;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
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