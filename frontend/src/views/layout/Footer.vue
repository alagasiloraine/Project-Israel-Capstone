<template>
  <footer class="bg-green-800 py-6 relative overflow-hidden">
    <!-- Decorative Elements -->
    <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-green-500 to-yellow-400"></div>
    
    <!-- Responsive container with smart padding -->
    <div class="container mx-auto px-4 sm:px-6 md:px-8">
      <!-- Grid with improved responsive breakpoints -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 sm:gap-6 lg:gap-4 mb-4">
        <!-- Company Info -->
        <div class="space-y-2 text-center sm:text-left">
          <div class="flex items-center justify-center sm:justify-start space-x-2">
            <img 
              src="/images/logo/logo-wot-text.png" 
              alt="Project Israel Logo" 
              class="w-10 sm:w-12 h-10 sm:h-12"
            />
            <h3 class="text-white font-bold text-lg sm:text-xl">Project Israel</h3>
          </div>
          <p class="text-gray-300 text-xs leading-relaxed max-w-lg mx-auto sm:mx-0">
            Your trusted partner in precision agriculture and smart irrigation solutions. Grow smarter, conserve water, and maximize your yield with our cutting-edge technology.
          </p>
        </div>

        <!-- Quick Links -->
        <div class="text-center sm:text-left">
          <h4 class="text-green-300 font-semibold text-base mb-2 pb-1 border-b border-green-700">Quick Links</h4>
          <ul class="space-y-1">
            <li v-for="link in ['Home', 'About Us', 'Crops', 'Contact']" :key="link">
              <a href="#" class="text-gray-300 hover:text-green-200 transition-colors duration-300 flex items-center text-sm group justify-center sm:justify-start">
                <ChevronRightIcon class="w-3 h-3 mr-1 text-green-500 group-hover:translate-x-1 transition-transform duration-300" />
                {{ link }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Services -->
        <div class="text-center sm:text-left">
          <h4 class="text-green-300 font-semibold text-base mb-2 pb-1 border-b border-green-700">Our Services</h4>
          <ul class="space-y-1">
            <li v-for="service in ['Crop Recommendations', 'Smart Irrigation', 'Soil Analysis', 'Water Management']" :key="service">
              <a href="#" class="text-gray-300 hover:text-green-200 transition-colors duration-300 flex items-center text-sm group justify-center sm:justify-start">
                <CheckCircleIcon class="w-3 h-3 mr-1 text-green-500 group-hover:scale-110 transition-transform duration-300" />
                {{ service }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div class="text-center sm:text-left">
          <h4 class="text-green-300 font-semibold text-base mb-2 pb-1 border-b border-green-700">Contact Us</h4>
          <ul class="space-y-2">
            <li v-for="(icon, text) in contactInfo" :key="text" 
                class="flex items-center space-x-2 group justify-center sm:justify-start">
              <div class="bg-green-700 p-1.5 rounded-full group-hover:bg-green-600 transition-colors duration-300">
                <component :is="icon" class="w-4 h-4 text-green-300" />
              </div>
              <span class="text-gray-300 text-sm">{{ text }}</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Social Links -->
      <div class="flex justify-center space-x-4 my-4">
        <a v-for="(icon, index) in socialIcons" :key="index" 
           href="#" 
           class="bg-green-700 p-2 rounded-full text-green-300 hover:bg-green-600 hover:text-white transition-colors duration-300">
          <component :is="icon" class="w-4 h-4" />
        </a>
      </div>

      <!-- Newsletter with responsive width -->
      <div class="max-w-md mx-auto mb-4 px-4 sm:px-0">
        <h5 class="text-white text-center text-sm font-semibold mb-2">Stay Updated with Our Newsletter</h5>
        <form @submit.prevent class="flex">
          <input 
            type="email" 
            placeholder="Enter your email" 
            class="flex-grow px-3 py-1.5 text-sm rounded-l-md focus:outline-none focus:ring-2 focus:ring-green-500" 
          />
          <button 
            type="submit" 
            class="bg-green-500 text-white px-4 py-1.5 text-sm rounded-r-md hover:bg-green-600 transition-colors duration-300 whitespace-nowrap"
          >
            Subscribe
          </button>
        </form>
      </div>

      <!-- Copyright -->
      <div class="border-t border-green-700 pt-4">
        <p class="text-center text-gray-400 text-xs">
          © {{ new Date().getFullYear() }} Project Israel. All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { 
  PhoneIcon, 
  MailIcon, 
  MapPinIcon,
  FacebookIcon,
  TwitterIcon,
  InstagramIcon,
  LinkedinIcon,
  ChevronRightIcon,
  CheckCircleIcon
} from 'lucide-vue-next'

const contactInfo = {
  '09292664302': PhoneIcon,
  'maryhelpofChristiansSchool@gmail.com': MailIcon,
  'Mary Help of Christians School (INC), Don Bosco': MapPinIcon
}

const socialIcons = [FacebookIcon, TwitterIcon, InstagramIcon, LinkedinIcon]
</script>

<style scoped>
/* Enhanced responsive styles */
@media (max-width: 640px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
}

@media (min-width: 641px) and (max-width: 768px) {
  .container {
    padding-left: 1.5rem;
    padding-right: 1.5rem;
  }
}

@media (min-width: 769px) {
  .container {
    padding-left: 2rem;
    padding-right: 2rem;
  }
}
</style>