<template>
    <div class="max-w-md mx-auto p-6 bg-white shadow rounded-xl" v-if="weather">
      <h2 class="text-xl font-semibold mb-4 text-gray-700">
        🌤 Weather in {{ weather.location }}, {{ weather.region }}
      </h2>
  
      <div class="text-4xl font-bold text-gray-900 mb-2">
        {{ weather.temperature_c }}°C / {{ weather.temperature_f }}°F
      </div>
  
      <p class="text-lg text-gray-600 mb-4">{{ weather.weather_condition }}</p>
  
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-700">
        <div>💧 Humidity: {{ weather.humidity }}%</div>
        <div>💨 Wind: {{ weather.wind_speed_ms }} m/s</div>
        <div>☁️ Cloud Cover: {{ weather.cloud_cover_percent }}%</div>
        <div>🌧 Rain: {{ weather.rain_mm }} mm</div>
        <div>🔆 UV Index: {{ weather.uv }}</div>
        <div>📊 Pressure: {{ weather.pressure_hpa }} hPa</div>
      </div>
  
      <p class="mt-4 text-xs text-gray-400">
        Last Updated: {{ weather.last_updated }}
      </p>
    </div>
  
    <div v-else class="text-center text-gray-500 mt-10">
      Connecting to weather server...
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue'
  
  const weather = ref(null)
  
  let socket
  
  onMounted(() => {
    const protocol = location.protocol === 'https:' ? 'wss' : 'ws'
    const host = 'localhost:8000'
    socket = new WebSocket(`${protocol}://${host}/api/weather/ws/weather`)
  
    socket.onopen = () => {
      console.log('[Weather WS] Connected')
    }
  
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data)
      console.log('[Weather WS] Data received:', data)
      weather.value = data
    }
  
    socket.onerror = (err) => {
      console.error('[Weather WS] Error:', err)
    }
  
    socket.onclose = () => {
      console.warn('[Weather WS] Disconnected')
    }
  })
  
  onBeforeUnmount(() => {
    if (socket) socket.close()
  })
  </script>
  
  <style scoped>
  /* You can add custom styling here if needed */
  </style>
  