<template>
  <nav class="fixed top-2 mx-4 left-0 right-0 bg-gradient-to-r from-[#00A572] to-[#008F61] backdrop-blur-md bg-opacity-95 shadow-lg z-50 rounded-xl border border-transparent border-t-[3px] border-t-orange-400">
    <!-- Logo positioning -->
    <div class="absolute left-1/2 -top-2.5 transform -translate-x-1/2">
      <div class="bg-white rounded-full shadow-lg flex items-center justify-center overflow-hidden border-2 border-white/30 hover:border-white/50 transition-all duration-300" style="width: 3.5rem; height: 3.5rem;">
        <img 
          src="../../../public/images/logo/logo-wo-text.png"
          alt="Project Israel"
          class="w-full h-full object-cover transform scale-[1.3] hover:scale-[1.8] transition-all duration-500 ease-out"
          style="transform-origin: center;"
        />
      </div>
    </div>

    <div class="max-w-[1920px] mx-auto px-6 lg:px-12 pt-6 pb-3">
      <div class="flex items-center justify-between mt-6">
        <!-- Left Navigation with updated items and larger text -->
        <div class="flex items-center space-x-4 md:space-x-6 flex-wrap gap-y-2 pt-1">
          <router-link 
            v-for="item in menuItems" 
            :key="item.name"
            :to="item.href"
            :class="[
              'flex items-center px-5 py-2.5 text-base font-medium rounded-lg transition-all duration-300 hover:scale-105',
              isCurrentRoute(item.href) 
                ? 'bg-white text-[#00A572] shadow-md' 
                : 'text-white hover:bg-white/10 hover:shadow-sm'
            ]"
          >
            <component 
              :is="item.icon" 
              class="h-5 w-5 mr-2.5 transition-transform duration-300 group-hover:rotate-12"
            />
            {{ item.name }}
          </router-link>
        </div>

        <!-- User Profile Section -->
        <div class="flex items-center pt-1 group">
          <div class="relative">
            <div class="absolute inset-0 bg-gradient-to-r from-[#00A572] to-[#008F61] rounded-full blur-md opacity-0 group-hover:opacity-50 transition-opacity"></div>
            <img 
              :src="user?.profilePicture || '/public/images/profile-example.jpg'"
              class="w-10 h-10 rounded-full border-2 border-white/30 hover:border-white/60 transition-all duration-300 relative z-10 object-cover"
              alt="Profile"
            />
          </div>
        </div>
      </div>
    </div>
  </nav>

  <!-- Spacer -->
  <div class="h-28"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { 
  LayoutDashboard,
  Calendar,
  Users
} from 'lucide-vue-next'

const route = useRoute()
const user = ref(null)

const menuItems = [
  { name: 'Overview', href: '/overview', icon: LayoutDashboard },
  { name: 'Calendar', href: '/calendar', icon: Calendar },
  { name: 'User Management', href: '/staff-management', icon: Users },
]

const isCurrentRoute = (path) => {
  return route.path === path
}

onMounted(() => {
  const storedUser = localStorage.getItem("user") || sessionStorage.getItem("user")
  if (storedUser) {
    try {
      user.value = JSON.parse(storedUser)
    } catch (e) {
      console.error('Error parsing user data:', e)
    }
  }
})
</script>

<style scoped>
.router-link-active {
  position: relative;
  transform: translateZ(0);
}

.router-link-active::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: 1px;
  background: linear-gradient(to right, white, transparent);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.router-link-active:hover::after {
  transform: scaleX(1);
}

@media (max-width: 1024px) {
  nav {
    top: 3px;
    margin-left: 1rem;
    margin-right: 1rem;
  }
  
  .nav-content {
    padding: 0.75rem;
  }
}

@media (max-width: 768px) {
  nav {
    top: 2px;
    margin-left: 0.5rem;
    margin-right: 0.5rem;
  }
  
  .nav-links {
    gap: 0.5rem;
  }
}

@media (max-width: 640px) {
  nav {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
  }

  .nav-content {
    flex-direction: column;
    align-items: stretch;
    padding: 0.5rem;
  }
  
  .profile-section {
    margin-top: 0.5rem;
    justify-content: center;
  }
}

nav {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

@supports (-webkit-backdrop-filter: none) or (backdrop-filter: none) {
  nav {
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
  }
}

html {
  scroll-behavior: smooth;
}

@supports (-webkit-touch-callout: none) {
  nav {
    transform: translateZ(0);
    -webkit-font-smoothing: antialiased;
  }
}

@-moz-document url-prefix() {
  nav {
    will-change: transform;
    backface-visibility: hidden;
  }
}

* {
  -webkit-tap-highlight-color: transparent;
}

.nav-item, 
.dropdown-trigger {
  user-select: none;
}

:focus-visible {
  outline: 2px solid white;
  outline-offset: 2px;
}

@media print {
  nav {
    display: none;
  }
}
</style>