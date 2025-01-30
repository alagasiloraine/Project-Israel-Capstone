<template>
  <div class="min-h-screen bg-white relative overflow-hidden font-poppins">
    <transition name="page-transition" mode="out-in" @before-leave="beforeLeave" @enter="enter" @after-enter="afterEnter">
      <div :key="transitionKey" class="page-content" :style="contentStyle">
        <Navbar @auth="handleAuth" />
        <!-- Wave Container -->
        <div class="absolute bottom-0 left-0 right-0 w-full h-[200px] sm:h-[300px] z-0 overflow-hidden px-6 sm:px-12 md:px-16 lg:px-24">
          <div class="wave wave-orange"></div>
          <div class="wave wave-green"></div>
        </div>

        <!-- Falling Leaves Animation -->
        <div class="absolute inset-0 pointer-events-none z-10 overflow-hidden">
          <div v-for="i in (isMobile ? 10 : 20)" :key="`leaf1-${i}`" 
               class="leaf absolute animate-fall"
               :style="{
                 left: `${Math.random() * 100}%`,
                 top: `${Math.random() * -200}%`,
                 animationDuration: `${20 + Math.random() * 20}s`,
                 animationDelay: `${Math.random() * -40}s`,
                 transform: `scale(${isMobile ? 0.6 : 1})`
               }">
            <img 
              src="/public/images/leaves-plants/fall-leaf1.png" 
              alt="" 
              class="w-16 sm:w-24 h-16 sm:h-24 opacity-60"
            />
          </div>
          
          <div v-for="i in (isMobile ? 10 : 20)" :key="`leaf2-${i}`" 
               class="leaf absolute animate-fall"
               :style="{
                 left: `${Math.random() * 100}%`,
                 top: `${Math.random() * -200}%`,
                 animationDuration: `${20 + Math.random() * 20}s`,
                 animationDelay: `${Math.random() * -40}s`,
                 transform: `scale(${isMobile ? 0.6 : 1})`
               }">
            <img 
              src="/public/images/leaves-plants/fall-leaf2.png" 
              alt="" 
              class="w-20 sm:w-28 h-20 sm:h-28 opacity-60"
            />
          </div>
        </div>

        <!-- Main Content -->
        <div class="container mx-auto px-6 sm:px-12 md:px-16 lg:px-24 min-h-screen relative z-20 flex items-center">
          <div class="flex flex-col lg:flex-row items-center justify-between w-full pt-24 lg:pt-0">
            <!-- Left Content -->
            <div class="lg:w-1/2 text-center lg:text-left mb-8 lg:mb-0">
              <h1 class="text-[#2E7D32] text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold mb-4 font-poppins tracking-wide relative">
                PROJECT ISRAEL
                <!-- Plant decorations with responsive positioning -->
                <img 
                  src="/public/images/leaves-plants/plant-decoration.png" 
                  alt=""
                  class="absolute top-0 left-[1%] w-6 sm:w-8 h-6 sm:h-8 -mt-4 hidden lg:block"
                />
                <img 
                  src="/public/images/leaves-plants/plant-decoration.png" 
                  alt=""
                  class="absolute top-0 left-[38%] w-6 sm:w-8 h-6 sm:h-8 -mt-4 hidden lg:block"
                />
                <img 
                  src="/public/images/leaves-plants/plant-decoration.png" 
                  alt=""
                  class="absolute top-0 left-[81%] w-6 sm:w-8 h-6 sm:h-8 -mt-4 hidden lg:block"
                />
              </h1>
              
              <h2 class="text-[#FFA000] text-xl sm:text-2xl md:text-3xl font-extrabold mb-4 font-poppins tracking-wide">
                GROW SMART & WATER WISELY
              </h2>
              
              <p class="text-gray-700 text-sm sm:text-base font-medium mb-8 font-poppins max-w-md mx-auto lg:mx-0">
                Your Guide to Precision Agriculture and Sustainability
              </p>

              <!-- Button with gradient -->
              <div class="relative inline-block">
                <button class="px-3 sm:px-4 py-2 sm:py-3 rounded-full text-base sm:text-lg font-bold text-white transition-all duration-300 ease-in-out bg-gradient-to-r from-[#2E7D32] to-[#D4C5A8] hover:shadow-xl hover:scale-105 hover:from-[#1B5E20] hover:to-[#E6D5B8] transform hover:-translate-y-1 flex items-center whitespace-nowrap">
                  GET STARTED
                  <span class="ml-2 inline-flex items-center justify-center bg-white rounded-full p-1 h-7 w-7 sm:h-8 sm:w-8">
                    <ArrowRight class="h-4 w-4 sm:h-5 sm:w-5 text-[#2E7D32]" />
                  </span>
                </button>
                <!-- Decorative leaves -->
                <div class="absolute -top-4 -left-2 animate-pop-scale hidden sm:block">
                  <img src="/public/images/leaves-plants/leaf-decoration.png" alt="" class="w-5 sm:w-7 h-5 sm:h-7 transform -rotate-45" />
                </div>
                <div class="absolute -top-5 left-1/2 -translate-x-1/2 animate-pop-scale hidden sm:block" style="animation-delay: 0.2s">
                  <img src="/public/images/leaves-plants/leaf-decoration.png" alt="" class="w-5 sm:w-7 h-5 sm:h-7" />
                </div>
                <div class="absolute -top-4 -right-2 animate-pop-scale hidden sm:block" style="animation-delay: 0.4s">
                  <img src="/public/images/leaves-plants/leaf-decoration.png" alt="" class="w-5 sm:w-7 h-5 sm:h-7 transform rotate-45" />
                </div>
              </div>
            </div>

            <!-- Right Content with Half Circle and Basket -->
            <div class="lg:w-1/2 relative">
              <div class="relative h-[350px] sm:h-[450px] md:h-[600px] lg:h-[700px] w-full">
                <div class="absolute right-0 transform translate-x-[15%] bottom-0">
                  <div class="relative">
                    <!-- Half circle with responsive sizing -->
                    <div class="w-[350px] h-[350px] sm:w-[450px] sm:h-[450px] md:w-[600px] md:h-[600px] lg:w-[700px] lg:h-[700px] bg-[#4CAF50] rounded-full transform translate-y-1/2">
                      <!-- Basket image with responsive positioning and sizing -->
                      <img 
                        src="/public/images/vege-basket.png" 
                        alt="Vegetable Basket" 
                        class="absolute top-[27%] left-1/2 transform -translate-x-1/2 -translate-y-[65%] w-[90%] max-w-[650px] z-20"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
  <Footer />
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowRight } from 'lucide-vue-next'
import Footer from '../layout/Footer.vue'
import Navbar from '../layout/Navbar.vue'

const router = useRouter()
const isMobile = ref(window.innerWidth < 640)
const transitionKey = ref(0)
const contentStyle = ref({})

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

const handleAuth = (type) => {
  transitionKey.value++
  contentStyle.value = { position: 'relative', left: '0px', transition: 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)' }
  
  setTimeout(() => {
    router.push(`/${type}`)
  }, 500)
}

onMounted(() => {
  window.addEventListener('resize', () => {
    isMobile.value = window.innerWidth < 640
  })
})

onUnmounted(() => {
  window.removeEventListener('resize', () => {
    isMobile.value = window.innerWidth < 640
  })
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

/* Navigation Styles */
.nav-link {
  padding: 0.5rem 0;
  font-weight: 500;
  position: relative;
}

.nav-dot {
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 6px;
  height: 6px;
  background-color: #2E7D32;
  border-radius: 9999px;
  transform: translateX(-50%) scale(0);
  transition: transform 0.3s ease-out;
}

.nav-dot.active {
  transform: translateX(-50%) scale(1);
}

/* Mobile Menu Styles */
@media (max-width: 768px) {
  .nav-link {
    padding: 0.5rem 0;
  }
  
  .nav-dot {
    bottom: 0;
  }
}

/* Base wave styles */
.wave {
  position: absolute;
  width: 200%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-repeat: repeat-x;
  background-position: 0 bottom;
  transform-origin: center bottom;
  will-change: transform;
}

.wave-orange {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 800 88.7' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M800 56.9c-155.5 0-204.9-50-405.5-49.9-200 0-250 49.9-394.5 49.9v31.8h800v-31.8z' fill='%23FFD8A8'/%3E%3C/svg%3E");
  animation: wave-right 8s cubic-bezier(0.36, 0, 0.64, 1) infinite;
  animation-delay: 0s;
  opacity: .8;
  height: 120px;
  z-index: 2;
}

.wave-green {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 800 88.7' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M800 56.9c-155.5 0-204.9-50-405.5-49.9-200 0-250 49.9-394.5 49.9v31.8h800v-31.8z' fill='%23C8E6C9'/%3E%3C/svg%3E");
  animation: wave-left 8s cubic-bezier(0.36, 0, 0.64, 1) infinite;
  animation-delay: -4s;
  opacity: .9;
  height: 140px;
  z-index: 1;
}

@keyframes wave-right {
  0% {
    transform: translateX(0) translateZ(0) scaleY(1);
  }
  50% {
    transform: translateX(-25%) translateZ(0) scaleY(0.98);
  }
  100% {
    transform: translateX(-50%) translateZ(0) scaleY(1);
  }
}

@keyframes wave-left {
  0% {
    transform: translateX(-50%) translateZ(0) scaleY(1);
  }
  50% {
    transform: translateX(-25%) translateZ(0) scaleY(0.98);
  }
  100% {
    transform: translateX(0) translateZ(0) scaleY(1);
  }
}

@keyframes fall {
  0% {
    transform: translateY(-100%) rotate(0deg);
    opacity: 0;
  }
  10% {
    opacity: 0.6;
  }
  90% {
    opacity: 0.6;
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

@keyframes pop-scale {
  0% { 
    transform: scale(0.8) rotate(var(--leaf-rotation, 0deg));
    opacity: 0.8;
  }
  50% { 
    transform: scale(1.2) rotate(var(--leaf-rotation, 0deg));
    opacity: 1;
  }
  100% {
    transform: scale(0.8) rotate(var(--leaf-rotation, 0deg));
    opacity: 0.8;
  }
}

.animate-pop-scale {
  animation: pop-scale 2s ease-in-out infinite;
}

/* Add smooth transition for mobile menu */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: opacity 0.3s ease;
}

.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
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
</style>

