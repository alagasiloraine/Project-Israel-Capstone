<template>
  <div class="min-h-screen bg-white relative overflow-hidden">
    <!-- Decorative elements -->
    <div class="absolute -left-4 top-20">
      <img src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Screenshot%202025-01-10%20222641-c2lJTr5U07lKYFT46CXk3p1esF1bbf.png" alt="Decorative leaf" class="w-24 h-24 opacity-20" />
    </div>
    <div class="absolute right-10 top-10">
      <img src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Screenshot%202025-01-10%20222641-c2lJTr5U07lKYFT46CXk3p1esF1bbf.png" alt="Decorative leaf" class="w-16 h-16 opacity-20 rotate-90" />
    </div>
    
    <div class="absolute top-6 right-6 flex items-center gap-4">
    <router-link 
      to="/login" 
      class="px-6 py-2 rounded-full bg-white text-[#2B5329] border border-[#2B5329] hover:bg-[#2B5329] hover:text-white transition-colors duration-300"
    >
      Login
    </router-link>
    <router-link 
      to="/register" 
      class="px-6 py-2 rounded-full bg-[#2B5329] text-white hover:bg-[#1F3D1F] transition-colors duration-300"
    >
      Sign up
    </router-link>
  </div>

    <!-- Main content -->
    <div class="container mx-auto px-6 py-12 flex items-center min-h-screen">
      <div class="grid md:grid-cols-2 gap-12 items-center w-full">
        <!-- Left content -->
        <div class="space-y-6">
          <div>
            <p class="text-sm mb-1 flex items-center">
              <span class="text-gray-700">Exclusive offer</span>
              <span class="text-red-500 ml-2 font-medium">30% Off</span>
            </p>
            <h1 class="text-5xl font-bold text-gray-900 leading-tight">
              STAY HOME &
              <br />
              DELIVERED YOUR
              <br />
              <span class="text-emerald-500">DAILY NEEDS</span>
            </h1>
          </div>
          
          <p class="text-gray-600 text-lg">
            Vegetables contain many vitamins and minerals that are good for your health.
          </p>
          
          <button class="bg-red-500 hover:bg-red-600 text-white px-8 py-4 rounded-lg text-lg font-medium transition-all duration-300 flex items-center group">
            Shop Now
            <svg 
              xmlns="http://www.w3.org/2000/svg" 
              class="h-5 w-5 ml-2 transform group-hover:translate-x-1 transition-transform" 
              viewBox="0 0 20 20" 
              fill="currentColor"
            >
              <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>

        <!-- Right content -->
        <div class="relative h-[600px]">
          <!-- Green background circle -->
          <div class="absolute right-0 bottom-0 w-[600px] h-[600px] bg-emerald-500 rounded-full"></div>
          
          <!-- Basket and vegetables container -->
          <div class="relative h-full flex items-end justify-center">
            <!-- Woven basket -->
            <div class="woven-basket">
              <div class="accumulated-vegetables" ref="accumulatedVeggies"></div>
            </div>

            <!-- Falling vegetables -->
            <div class="vegetables-container">
              <template v-for="(veg, index) in fallingVegetables" :key="index">
                <div 
                  :class="['falling-vegetable', veg.type]"
                  :style="{ 
                    animationDelay: `${veg.delay}s`,
                    '--fall-x': `${veg.x}px`,
                    '--fall-rotation': `${veg.rotation}deg`
                  }"
                  @animationend="addToBasket(veg.type)"
                >
                  <div v-if="veg.type === 'tomato'" class="tomato-stem"></div>
                  <div v-if="veg.type === 'eggplant'" class="eggplant-stem"></div>
                  <div v-if="veg.type === 'carrot'" class="carrot-leaves"></div>
                  <div v-if="veg.type === 'cauliflower'" class="cauliflower-leaves"></div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const accumulatedVeggies = ref(null)
const vegetableTypes = ['tomato', 'eggplant', 'cauliflower', 'carrot']
const fallingVegetables = ref([])

// Initialize falling vegetables
onMounted(() => {
  setInterval(() => {
    const type = vegetableTypes[Math.floor(Math.random() * vegetableTypes.length)]
    fallingVegetables.value.push({
      type,
      delay: Math.random() * 2,
      x: Math.random() * 300 - 150,
      rotation: Math.random() * 360
    })
  }, 2000)
})

const addToBasket = (type) => {
  if (!accumulatedVeggies.value) return
  
  const veggie = document.createElement('div')
  veggie.className = `accumulated-vegetable ${type}`
  
  const x = Math.random() * 240 - 120
  const y = Math.random() * 60
  const rotation = Math.random() * 30 - 15
  
  veggie.style.transform = `translate(${x}px, ${y}px) rotate(${rotation}deg)`
  accumulatedVeggies.value.appendChild(veggie)
}
</script>

<style scoped>
/* Woven basket styles */
.woven-basket {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 500px;
  height: 250px;
  background: 
    repeating-linear-gradient(
      45deg,
      #8B4513,
      #8B4513 2px,
      #A0522D 2px,
      #A0522D 8px
    ),
    repeating-linear-gradient(
      -45deg,
      #8B4513,
      #8B4513 2px,
      #A0522D 2px,
      #A0522D 8px
    );
  border: 25px solid;
  border-image: linear-gradient(
    to bottom,
    #DEB887,
    #8B4513
  ) 1;
  border-radius: 15px 15px 0 0;
  box-shadow: 
    inset 0 0 20px rgba(0,0,0,0.3),
    0 -20px 40px rgba(0,0,0,0.2);
  overflow: hidden;
  z-index: 10;
}

.woven-basket::before {
  content: '';
  position: absolute;
  top: -25px;
  left: -25px;
  right: -25px;
  height: 40px;
  background: 
    repeating-linear-gradient(
      90deg,
      #DEB887,
      #8B4513 20px
    );
  border-radius: 10px 10px 0 0;
}

.vegetables-container {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.accumulated-vegetables {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 150px;
  pointer-events: none;
}

/* Realistic vegetable styles */
.tomato {
  width: 80px;
  height: 80px;
  background: radial-gradient(
    circle at 30% 30%,
    #ff6b6b,
    #e74c3c 60%,
    #c0392b
  );
  border-radius: 50%;
  position: relative;
  box-shadow: 
    inset -4px -4px 8px rgba(0,0,0,0.2),
    inset 4px 4px 8px rgba(255,255,255,0.2),
    0 4px 8px rgba(0,0,0,0.1);
}

.tomato::before {
  content: '';
  position: absolute;
  top: 10%;
  left: 10%;
  width: 20%;
  height: 20%;
  background: radial-gradient(
    circle at center,
    rgba(255,255,255,0.8),
    rgba(255,255,255,0) 70%
  );
  border-radius: 50%;
}

.tomato-stem {
  width: 12px;
  height: 25px;
  background: linear-gradient(to right, #27ae60, #2ecc71);
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%) rotate(-5deg);
  border-radius: 4px;
  box-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.eggplant {
  width: 65px;
  height: 130px;
  background: linear-gradient(
    135deg,
    #9b59b6,
    #8e44ad 50%,
    #6c3483
  );
  border-radius: 35px;
  position: relative;
  box-shadow: 
    inset -6px -6px 12px rgba(0,0,0,0.2),
    inset 6px 6px 12px rgba(255,255,255,0.1),
    0 4px 8px rgba(0,0,0,0.1);
}

.eggplant::before {
  content: '';
  position: absolute;
  top: 10%;
  left: 20%;
  width: 30%;
  height: 60%;
  background: linear-gradient(
    135deg,
    rgba(255,255,255,0.2),
    transparent
  );
  border-radius: 50%;
}

.eggplant-stem {
  width: 15px;
  height: 30px;
  background: linear-gradient(to right, #27ae60, #2ecc71);
  position: absolute;
  top: -25px;
  left: 50%;
  transform: translateX(-50%) rotate(5deg);
  border-radius: 4px;
  box-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.cauliflower {
  width: 110px;
  height: 110px;
  background: 
    radial-gradient(
      circle at 30% 30%,
      #f0f4f8,
      #e8f0f6 40%,
      #d4e4ef
    );
  border-radius: 50%;
  position: relative;
  box-shadow: 
    inset -4px -4px 8px rgba(0,0,0,0.1),
    inset 4px 4px 8px rgba(255,255,255,0.8),
    0 4px 8px rgba(0,0,0,0.1);
}

.cauliflower::after {
  content: '';
  position: absolute;
  inset: 5px;
  background: 
    radial-gradient(
      circle at 40% 40%,
      transparent 8px,
      #fff 9px,
      transparent 10px
    );
  background-size: 20px 20px;
  border-radius: 50%;
}

.cauliflower-leaves {
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 40px;
  background: linear-gradient(to bottom, #2ecc71, #27ae60);
  clip-path: polygon(0 0, 100% 0, 80% 100%, 20% 100%);
}

.carrot {
  width: 45px;
  height: 140px;
  background: linear-gradient(
    135deg,
    #f39c12,
    #e67e22 50%,
    #d35400
  );
  border-radius: 25px 25px 5px 5px;
  position: relative;
  box-shadow: 
    inset -4px -4px 8px rgba(0,0,0,0.2),
    inset 4px 4px 8px rgba(255,255,255,0.2),
    0 4px 8px rgba(0,0,0,0.1);
  transform: rotate(5deg);
}

.carrot::before {
  content: '';
  position: absolute;
  top: 10%;
  left: 20%;
  width: 20%;
  height: 70%;
  background: linear-gradient(
    135deg,
    rgba(255,255,255,0.3),
    transparent
  );
  border-radius: 50%;
}

.carrot-leaves {
  width: 70px;
  height: 40px;
  background: linear-gradient(
    to bottom,
    #27ae60,
    #2ecc71
  );
  position: absolute;
  top: -35px;
  left: 50%;
  transform: translateX(-50%);
  clip-path: polygon(
    50% 0%,
    0% 100%,
    20% 90%,
    40% 100%,
    60% 90%,
    80% 100%,
    100% 90%
  );
  box-shadow: 0 -2px 4px rgba(0,0,0,0.1);
}

@keyframes fallIntoBasket {
  0% {
    transform: translate(var(--fall-x), -300px) rotate(0deg);
    opacity: 0;
  }
  20% {
    opacity: 1;
  }
  100% {
    transform: translate(var(--fall-x), 500px) rotate(var(--fall-rotation));
    opacity: 1;
  }
}

.falling-vegetable {
  position: absolute;
  left: 50%;
  top: 0;
  animation: fallIntoBasket 2s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  z-index: 20;
}

@keyframes settleInBasket {
  0% {
    transform: translateY(-30px) scale(0.8);
    opacity: 0;
  }
  100% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

.accumulated-vegetable {
  animation: settleInBasket 0.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
</style>