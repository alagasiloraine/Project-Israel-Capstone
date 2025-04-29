<template>
  <Transition name="fade">
    <div v-if="isVisible" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/40 backdrop-blur-[2px]">
      <div class="gradient-border relative w-[90%] max-w-md rounded-2xl p-[4px]">
        <div class="relative w-full h-full rounded-2xl bg-white/95 p-6 shadow-2xl">
          <div class="flex flex-col items-center justify-center">
            <!-- GIF Animation Container -->
            <div class="w-full max-w-md mx-auto mb-3">
              <img 
                src="/public/images/GIF/loading_plant.gif"
                alt="Loading animation"
                class="w-[200px] h-[200px] mx-auto object-contain"
              />
            </div>
            
            <!-- Loading Dots -->
            <div class="flex justify-center space-x-2 mb-4">
              <div v-for="index in 5" :key="index" class="loading-dot"></div>
            </div>

            <!-- Text Content -->
            <div class="text-center">
              <h3 class="text-xl font-bold text-[#2B5329] mb-2">{{ title }}</h3>
              <p class="text-sm font-medium text-[#2B5329]/80">{{ message }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script>
export default {
  name: 'LoadingPage',
  props: {
    isVisible: {
      type: Boolean,
      default: false
    },
    title: {
      type: String,
      default: 'Loading...'
    },
    message: {
      type: String,
      default: 'Please wait while we process your request'
    }
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

/* Loading dots animation */
.loading-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #2B5329;
  animation: dotPulse 1.4s infinite ease-in-out;
}

.loading-dot:nth-child(1) { animation-delay: 0s; }
.loading-dot:nth-child(2) { animation-delay: 0.2s; }
.loading-dot:nth-child(3) { animation-delay: 0.4s; }
.loading-dot:nth-child(4) { animation-delay: 0.6s; }
.loading-dot:nth-child(5) { animation-delay: 0.8s; }

@keyframes dotPulse {
  0%, 100% {
    transform: scale(0.3);
    opacity: 0.3;
  }
  50% {
    transform: scale(1);
    opacity: 1;
  }
}

/* Gradient border animation */
.gradient-border {
  position: relative;
  background: linear-gradient(90deg, #FFB74D, #81C784);
  background-size: 200% 200%;
  animation: gradientBorder 2s linear infinite;
}

.gradient-border::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 1rem;
  padding: 4px;
  background: linear-gradient(90deg, #FFB74D, #81C784);
  background-size: 200% 200%;
  animation: gradientBorder 2s linear infinite;
  -webkit-mask: 
    linear-gradient(#fff 0 0) content-box, 
    linear-gradient(#fff 0 0);
  mask: 
    linear-gradient(#fff 0 0) content-box, 
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

@keyframes gradientBorder {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* Responsive adjustments */
@media (min-width: 768px) {
  .loading-dot {
    width: 10px;
    height: 10px;
  }
}
</style>