<template>
  <nav 
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-700 ease-out'
    ]"
    class="px-6 sm:px-12 md:px-16 lg:px-24"
  >
    <div class="max-w-[1920px] w-full mx-auto">
      <div class="relative flex justify-between items-center">
        <!-- Logo -->
        <a 
          href="#" 
          @click.prevent="scrollToSection('home')" 
          class="relative z-[60]"
        >
          <img 
            :class="[
              'transition-all duration-500 ease-in-out',
              isScrolled ? 'scale-110' : ''
            ]"
            src="/public/images/logo/logo-wot-text.png"
            alt="Project Israel Logo" 
            class="h-16 w-16 sm:h-20 sm:w-20 md:h-24 md:w-24"
          />
        </a>
        
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
          <div class="flex flex-col items-center space-y-8">
            <a 
              v-for="link in navLinks" 
              :key="link.name"
              href="#"
              @click.prevent="scrollToSection(link.section)"
              class="nav-link group relative text-xl"
            >
              <span :class="currentSection === link.section ? 'text-[#1B5E20]' : 'text-[#2E7D32] hover:text-[#1B5E20]'">
                {{ link.name }}
              </span>
              <span :class="['nav-dot', currentSection === link.section && 'active']"></span>
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
        
        <!-- Desktop Navigation Links -->
        <div 
          :class="[
            'hidden lg:block transition-all duration-700 ease-out overflow-visible',
            isScrolled 
              ? 'fixed top-0 left-0 right-0 w-screen bg-white/95 backdrop-blur-sm shadow-lg py-2' 
              : 'w-auto bg-gray-200/40 backdrop-blur-sm hover:bg-gray-300/60 rounded-2xl'
          ]"
          class="px-12 py-2"
        >
          <div 
            :class="[
              'flex items-center transition-all duration-700 ease-out relative z-[52]',
              isScrolled ? 'justify-between w-full px-6 sm:px-12 md:px-16 lg:px-24 py-1 max-w-[2560px] mx-auto' : 'justify-center space-x-12'
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
              <a
                v-for="link in navLinks"
                :key="link.name"
                href="#"
                @click.prevent="scrollToSection(link.section)"
                class="nav-link group relative"
              >
                <span :class="currentSection === link.section ? 'text-[#1B5E20]' : 'text-[#2E7D32] hover:text-[#1B5E20]'">
                  {{ link.name }}
                </span>
                <span :class="['nav-dot', currentSection === link.section && 'active']"></span>
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
        
        <!-- Desktop Auth Buttons -->
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

const emit = defineEmits(['auth'])
const isMenuOpen = ref(false)
const isScrolled = ref(false)
const currentSection = ref('home')

const navLinks = [
  { name: 'HOME', section: 'home' },
  { name: 'ABOUT', section: 'about' },
  { name: 'CROPS', section: 'crops' }
]

const scrollToSection = (sectionId) => {
  const element = document.querySelector(`.${sectionId}-section`)
  if (element) {
    const navbarHeight = 80
    const elementPosition = element.getBoundingClientRect().top
    const offsetPosition = elementPosition + window.pageYOffset - navbarHeight

    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth'
    })

    currentSection.value = sectionId
  }
  closeMenu()
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50

  const sections = ['home', 'about', 'crops']
  const navbarHeight = 80
  let closestSection = null
  let minDistance = Infinity

  sections.forEach(section => {
    const element = document.querySelector(`.${section}-section`)
    if (element) {
      const rect = element.getBoundingClientRect()
      const distance = Math.abs(rect.top - navbarHeight)
      
      if (distance < minDistance) {
        minDistance = distance
        closestSection = section
      }
    }
  })

  if (closestSection) {
    currentSection.value = closestSection
  }
}

const handleResize = () => {
  if (window.innerWidth >= 1024) {
    isMenuOpen.value = false
  }
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
  window.addEventListener('scroll', handleScroll)
  handleScroll()
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
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

@media (max-width: 768px) {
  .nav-link {
    padding: 0.5rem 0;
  }
  
  .nav-dot {
    bottom: 0;
  }
}
</style>