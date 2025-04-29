<template>
  <div class="min-h-screen bg-white relative overflow-hidden font-poppins home-section">
    <Navbar @auth="handleAuth" />

    <transition name="page-transition" mode="out-in" @before-leave="beforeLeave" @enter="enter" @after-enter="afterEnter">
      <div :key="transitionKey" class="page-content" :style="contentStyle">
        <!-- <Navbar @auth="handleAuth" /> -->
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
        <div class="container mx-auto px-4 sm:px-6 md:px-12 lg:px-24 min-h-screen relative z-20 flex items-center">
          <div class="flex flex-col lg:flex-row items-center justify-between w-full pt-20 sm:pt-24 lg:pt-0">
            <!-- Left Content -->
            <div class="lg:w-1/2 text-left lg:text-left mb-8 lg:mb-0 px-4 sm:px-0">
              <h1 class="text-[#2E7D32] text-3xl xs:text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold mb-4 font-poppins tracking-wide relative">
                PROJECT ISRAEL
                <!-- Plant decorations with improved responsive visibility -->
                <img 
                  src="/public/images/leaves-plants/plant-decoration.png" 
                  alt=""
                  class="absolute top-0 left-[1%] w-4 xs:w-5 sm:w-6 md:w-8 h-4 xs:h-5 sm:h-6 md:h-8 -mt-4 hidden sm:block"
                />
                <img 
                  src="/public/images/leaves-plants/plant-decoration.png" 
                  alt=""
                  class="absolute top-0 left-[35%] w-4 xs:w-5 sm:w-6 md:w-8 h-4 xs:h-5 sm:h-6 md:h-8 -mt-4 hidden sm:block"
                />
                <img 
                  src="/public/images/leaves-plants/plant-decoration.png" 
                  alt=""
                  class="absolute top-0 left-[75%] w-4 xs:w-5 sm:w-6 md:w-8 h-4 xs:h-5 sm:h-6 md:h-8 -mt-4 hidden sm:block"
                />
              </h1>
              
              <h2 class="text-[#FFA000] text-lg text-left xs:text-xl sm:text-2xl md:text-3xl font-extrabold mb-4 font-poppins tracking-wide">
                GROW SMART & WATER WISELY
              </h2>
              
              <p class="text-gray-700 text-left text-xs xs:text-sm sm:text-base font-medium mb-8 font-poppins max-w-full mx-auto lg:mx-0 px-4 sm:px-0">
                Your Guide to Precision Agriculture and Sustainability
              </p>

              <!-- Button with improved mobile spacing -->
              <div class="relative inline-block px-4 sm:px-0">
                <button @click="showAuthModal = true" class="px-3 sm:px-4 py-2 sm:py-3 rounded-full text-sm xs:text-base sm:text-lg font-bold text-white transition-all duration-300 ease-in-out bg-gradient-to-r from-[#2E7D32] to-[#D4C5A8] hover:shadow-xl hover:scale-105 hover:from-[#1B5E20] hover:to-[#E6D5B8] transform hover:-translate-y-1 flex items-center whitespace-nowrap">
                  GET STARTED
                  <span class="ml-2 inline-flex items-center justify-center bg-white rounded-full p-1 h-6 w-6 xs:h-7 xs:w-7 sm:h-8 sm:w-8">
                    <ArrowRight class="h-3 w-3 xs:h-4 xs:w-4 sm:h-5 sm:w-5 text-[#2E7D32]" />
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
              <div class="relative h-[250px] xs:h-[300px] sm:h-[400px] md:h-[500px] lg:h-[700px] w-full">
                <div class="absolute right-0 transform translate-x-[15%] bottom-0">
                  <div class="relative">
                    <!-- Half circle with smoother responsive scaling -->
                    <div class="w-[250px] h-[250px] xs:w-[300px] xs:h-[300px] sm:w-[400px] sm:h-[400px] md:w-[500px] md:h-[500px] lg:w-[700px] lg:h-[700px] bg-[#4CAF50] rounded-full transform translate-y-1/2">
                      <!-- Basket image with improved responsive positioning -->
                      <img 
                        src="/public/images/vege-basket.png" 
                        alt="Vegetable Basket" 
                        class="absolute top-[27%] left-1/2 transform -translate-x-1/2 -translate-y-[65%] w-[85%] sm:w-[90%] max-w-[650px] z-20"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Enhanced Authentication Modal -->
        <Transition name="backdrop">
          <div v-if="showAuthModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-0">
            <!-- Backdrop with blur -->
            <div 
              class="fixed inset-0 transition-all duration-500 ease-in-out bg-black/50"
              :style="{
                backdropFilter: showAuthModal ? 'blur(40px) saturate(180%)' : 'blur(0px)',
                WebkitBackdropFilter: showAuthModal ? 'blur(40px) saturate(180%)' : 'blur(0px)',
                filter: showAuthModal ? 'blur(40px) saturate(180%)' : 'blur(0px)',
                opacity: showAuthModal ? 1 : 0,
                transform: 'translateZ(0)'
              }"
              @click="closeModal"
            ></div>
            
            <!-- Modal Container -->
            <Transition name="modal">
              <div 
                v-if="showAuthModal" 
                class="modal-content relative w-full max-w-md rounded-2xl bg-white p-8 shadow-xl transform transition-all duration-500 translate-z-0"
              >
                <div class="flex flex-col items-center text-center">
                  <!-- Animated Icon -->
                  <div class="mb-6 relative">
                    <div class="absolute inset-0 bg-[#2E7D32]/10 rounded-full scale-[1.2] animate-pulse-slow"></div>
                    <div class="relative rounded-full bg-[#2E7D32]/10 p-4 animate-bounce-subtle">
                      <LockIcon class="h-8 w-8 text-[#2E7D32]" />
                    </div>
                  </div>
                  
                  <!-- Content with Staggered Animation -->
                  <h2 class="mb-2 text-2xl font-bold text-gray-900 animate-fade-in-up" style="--delay: 0.2s">
                    Authentication Required
                  </h2>
                  <p class="mb-8 text-gray-600 animate-fade-in-up" style="--delay: 0.3s">
                    You need to log in or register before getting started.
                  </p>
                  
                  <!-- Buttons with Staggered Animation -->
                  <div class="w-full space-y-3">
                    <button 
                      class="w-full rounded-full bg-gradient-to-r from-[#2E7D32] to-[#D4C5A8] px-4 py-3.5 font-semibold text-white transition-all duration-300 hover:from-[#1B5E20] hover:to-[#E6D5B8] hover:shadow-lg transform hover:scale-[1.02] animate-fade-in-up"
                      style="--delay: 0.4s"
                      @click="handleModalAuth('login')"
                    >
                      Login
                    </button>
                    
                    <button 
                      class="w-full rounded-full bg-[#2E7D32]/5 px-4 py-3.5 font-semibold text-[#2E7D32] transition-all duration-300 hover:bg-[#2E7D32]/10 transform hover:scale-[1.02] animate-fade-in-up"
                      style="--delay: 0.5s"
                      @click="handleModalAuth('register')"
                    >
                      Register
                    </button>
                    
                    <button 
                      class="mt-6 w-full text-sm text-gray-500 hover:text-gray-700 transition-colors duration-300 animate-fade-in-up"
                      style="--delay: 0.6s"
                      @click="closeModal"
                    >
                      Close
                    </button>
                  </div>
                </div>
              </div>
            </Transition>
          </div>
        </Transition>
      </div>
    </transition>
  </div>

  <About />

  <!-- Organic Crops Section -->
  <OrganicSection />

  <Footer />
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowRight, LockIcon } from 'lucide-vue-next'
import Footer from '../layout/Footer.vue'
import Navbar from '../layout/Navbar.vue'
import About from './About.vue'
import OrganicSection from './OrganicSection.vue'

const router = useRouter()
const isMobile = ref(window.innerWidth < 640)
const transitionKey = ref(0)
const contentStyle = ref({})
const showAuthModal = ref(false)

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

const handleModalAuth = (type) => {
  closeModal()
  setTimeout(() => {
    handleAuth(type)
  }, 300)
}

const closeModal = () => {
  // First fade out the modal content
  const modalContent = document.querySelector('.modal-content');
  if (modalContent) {
    modalContent.style.opacity = '0';
    modalContent.style.transform = 'scale(0.95)';
  }
  
  // Add a longer delay before removing the backdrop
  setTimeout(() => {
    showAuthModal.value = false;
  }, 600); // Increased to match the backdrop transition duration
};

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

/* Enhanced Modal Animations */
.backdrop-enter-active,
.backdrop-leave-active {
  transition: all 600ms cubic-bezier(0.4, 0, 0.2, 1);
  transition-property: opacity, backdrop-filter, -webkit-backdrop-filter, filter;
}

.backdrop-enter-from,
.backdrop-leave-to {
  opacity: 0;
  backdrop-filter: blur(0px);
  -webkit-backdrop-filter: blur(0px);
  filter: blur(0px);
}

.modal-enter-active,
.modal-leave-active {
  transition: all 500ms cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

.modal-enter-to,
.modal-leave-from {
  opacity: 1;
  transform: scale(1);
}

@keyframes bounce-subtle {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-3px);
  }
}

@keyframes pulse-slow {
  0%, 100% {
    opacity: 0.5;
    transform: scale(1.2);
  }
  50% {
    opacity: 0.25;
    transform: scale(1.3);
  }
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-bounce-subtle {
  animation: bounce-subtle 2s infinite ease-in-out;
}

.animate-pulse-slow {
  animation: pulse-slow 3s infinite ease-in-out;
}

.animate-fade-in-up {
  opacity: 0;
  animation: fade-in-up 0.6s ease-out forwards;
  animation-delay: var(--delay, 0s);
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

/* Mobile Menu Styles */
@media (max-width: 768px) {
  .nav-link {
    padding: 0.5rem 0;
  }
  
  .nav-dot {
    bottom: 0;
  }
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

.fixed {
  will-change: backdrop-filter, opacity;
}

/* Browser-specific backdrop blur optimizations */
@supports (-webkit-backdrop-filter: none) or (backdrop-filter: none) {
  .backdrop-blur-\[40px\] {
    -webkit-backdrop-filter: blur(40px) saturate(180%);
    backdrop-filter: blur(40px) saturate(180%);
  }
}

/* Fallback for browsers that don't support backdrop-filter */
@supports not ((-webkit-backdrop-filter: none) or (backdrop-filter: none)) {
  .backdrop-blur-\[40px\] {
    filter: blur(40px) saturate(180%);
  }
}

/* Ensure smooth transitions in Firefox */
@-moz-document url-prefix() {
  .backdrop-blur-\[40px\] {
    backdrop-filter: blur(40px) saturate(180%);
  }
}

/* Update the transition timing */
.backdrop-enter-active,
.backdrop-leave-active {
  transition: all 600ms cubic-bezier(0.4, 0, 0.2, 1);
  transition-property: opacity, backdrop-filter, -webkit-backdrop-filter, filter;
}

.backdrop-enter-from,
.backdrop-leave-to {
  opacity: 0;
  backdrop-filter: blur(0px);
  -webkit-backdrop-filter: blur(0px);
  filter: blur(0px);
}

.translate-z-0 {
  transform: translateZ(0);
  backface-visibility: hidden;
  perspective: 1000px;
}

.bg-black\/50 {
  background-color: rgba(0, 0, 0, 0.5);
}

@media (min-width: 480px) {
  /* Extra small devices (phones, 480px and up) */
  /* Styles already handled by existing responsive classes */
}

/* Optimize animations for mobile devices */
@media (prefers-reduced-motion: reduce) {
  .animate-fall,
  .animate-pop-scale,
  .wave {
    animation: none;
  }
}

/* Improve performance on mobile */
@media (max-width: 640px) {
  .wave {
    animation-duration: 12s; /* Slower waves on mobile */
  }
  
  .leaf {
    display: none; /* Hide some leaves on mobile for better performance */
  }
}

/* Ensure smooth scaling on different devices */
@media (max-width: 360px) {
  .text-3xl {
    font-size: 1.75rem;
  }
  
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
}

/* Add support for ultra-wide screens */
@media (min-width: 2000px) {
  .container {
    max-width: 1920px;
  }
}
</style>