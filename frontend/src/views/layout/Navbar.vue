<template>
  <nav 
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-700 ease-out'
    ]"
    class="px-6 sm:px-12 md:px-16 lg:px-24"
  >
    <div class="container mx-auto">
      <div class="relative flex justify-between items-center">
        <!-- Logo -->
        <img 
          :class="[
            'transition-all duration-500 ease-in-out relative z-[60]',
            isScrolled ? 'scale-110' : ''
          ]"
          src="/public/images/logo/logo-wot-text.png"
          alt="Project Israel Logo" 
          class="h-16 w-16 sm:h-20 sm:w-20 md:h-24 md:w-24"
        />
        
        <!-- Mobile Menu Button -->
        <button 
          @click="toggleMenu"
          class="lg:hidden z-[60] p-2 text-[#2E7D32]"
          aria-label="Toggle menu"
        >
          <Menu v-if="!isMenuOpen" class="h-6 w-6" />
          <X v-else class="h-6 w-6" />
        </button>

        <!-- Mobile Menu Overlay -->
        <div 
          v-if="isMenuOpen"
          class="fixed inset-0 bg-white/95 backdrop-blur-sm z-[55] lg:hidden flex flex-col items-center justify-center"
        >
          <!-- Mobile menu content -->
          <div class="flex flex-col items-center space-y-8">
            <a 
              v-for="link in ['HOME', 'ABOUT', 'CROPS', 'CONTACT']" 
              :key="link"
              href="#" 
              class="nav-link group relative text-xl"
              @click="closeMenu"
            >
              <span :class="link === 'HOME' ? 'text-[#1B5E20]' : 'text-[#2E7D32] hover:text-[#1B5E20]'">
                {{ link }}
              </span>
              <span :class="['nav-dot', link === 'HOME' && 'active']"></span>
            </a>

            <!-- Mobile Auth Buttons -->
            <div class="flex flex-col gap-4 mt-8">
              <button 
                @click="$emit('auth', 'login')"
                class="px-8 py-2 rounded-full text-[#2E7D32] border-2 border-[#2E7D32] hover:bg-[#2E7D32] hover:text-white transition-colors duration-300 font-medium"
              >
                Login
              </button>
              <button 
                @click="$emit('auth', 'register')"
                class="px-8 py-2 rounded-full bg-[#2E7D32] text-white hover:bg-[#236B27] transition-colors duration-300 font-medium"
              >
                Sign up
              </button>
            </div>
          </div>
        </div>
        
        <!-- Desktop Navigation Links with edge-to-edge container -->
        <div 
          :class="[
            'hidden lg:block transition-all duration-700 ease-out overflow-visible',
            isScrolled 
              ? 'w-screen absolute top-0 left-0 right-0 -mx-6 sm:-mx-12 md:-mx-16 lg:-mx-24 bg-white/95 backdrop-blur-sm shadow-lg py-2' 
              : 'w-auto bg-gray-200/40 backdrop-blur-sm hover:bg-gray-300/60 rounded-2xl'
          ]"
          class="px-12 py-2"
        >
          <div 
            :class="[
              'flex items-center transition-all duration-700 ease-out relative z-[52]',
              isScrolled ? 'justify-between container mx-auto px-6 sm:px-12 md:px-16 lg:px-24 py-1' : 'justify-center space-x-12'
            ]"
          >
            <!-- Logo clone for expanded state -->
            <img 
              v-if="isScrolled"
              src="/public/images/logo/logo-wot-text.png"
              alt="Project Israel Logo" 
              class="h-16 w-16 opacity-0 invisible"
            />
            
            <!-- Navigation Links -->
            <div :class="['flex items-center', isScrolled ? 'space-x-16' : 'space-x-12']">
              <a href="#" class="nav-link group relative">
                <span class="text-[#1B5E20] transition-colors duration-300">HOME</span>
                <span class="nav-dot active"></span>
              </a>
              <a href="#" class="nav-link group relative">
                <span class="text-[#2E7D32] hover:text-[#1B5E20] transition-colors duration-300">ABOUT</span>
                <span class="nav-dot"></span>
              </a>
              <a href="#" class="nav-link group relative">
                <span class="text-[#2E7D32] hover:text-[#1B5E20] transition-colors duration-300">CROPS</span>
                <span class="nav-dot"></span>
              </a>
              <a href="#" class="nav-link group relative">
                <span class="text-[#2E7D32] hover:text-[#1B5E20] transition-colors duration-300">CONTACT</span>
                <span class="nav-dot"></span>
              </a>
            </div>

            <!-- Auth Buttons clone for expanded state -->
            <div v-if="isScrolled" class="flex gap-4 items-center opacity-0 invisible">
              <button 
                @click="$emit('auth', 'login')"
                class="px-6 py-1.5 rounded-full text-[#2E7D32] border-2 border-[#2E7D32]">
                Login
              </button>
              <button 
                @click="$emit('auth', 'register')"
                class="px-6 py-1.5 rounded-full bg-[#2E7D32] text-white">
                Sign up
              </button>
            </div>
          </div>
        </div>
        
        <!-- Desktop Auth Buttons - Fixed Right -->
        <div 
          :class="[
            'hidden lg:flex gap-4 items-center relative z-[60] transition-all duration-500',
            isScrolled ? 'scale-90' : ''
          ]"
        >
          <button 
            @click="$emit('auth', 'login')"
            class="px-6 py-1.5 rounded-full text-[#2E7D32] border-2 border-[#2E7D32] hover:bg-[#2E7D32] hover:text-white transition-colors duration-300 font-medium"
          >
            Login
          </button>
          <button 
            @click="$emit('auth', 'register')"
            class="px-6 py-1.5 rounded-full bg-[#2E7D32] text-white hover:bg-[#236B27] transition-colors duration-300 font-medium"
          >
            Sign up
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Menu, X } from 'lucide-vue-next'
import { useRouter } from 'vue-router'

const emit = defineEmits(['auth'])
const router = useRouter()
const isMenuOpen = ref(false)
const isScrolled = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

const handleResize = () => {
  if (window.innerWidth >= 1024) {
    isMenuOpen.value = false
  }
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('scroll', handleScroll)
})

</script>

<style scoped>
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
</style>

