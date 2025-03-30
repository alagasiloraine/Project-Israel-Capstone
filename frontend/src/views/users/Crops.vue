<!-- <template>
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
   -->

<!-- <template>
    <div>
      <h2>30-Day Weather Forecast</h2>
      <table v-if="forecast.length">
        <thead>
          <tr>
            <th v-for="(value, key) in forecast[0]" :key="key">{{ key }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in forecast" :key="index">
            <td v-for="(value, key) in row" :key="key">{{ value }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>Loading forecast data...</p>
    </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import api from '../../api/index.js'
  
  const forecast = ref([])
  
  onMounted(async () => {
    try {
      const res = await api.get('/weather/forecast')
      forecast.value = res.data.forecast
    } catch (err) {
      console.error('Error fetching forecast:', err)
    }
  })
  </script> -->

  <template>
    <div>
      <h2>7-Day Forecast</h2>
      <div v-if="weekAlignedForecast.length">
        <div v-for="day in weekAlignedForecast" :key="day.date" class="day-box">
          <strong>{{ day.dayName }}</strong><br>
          Max: {{ day.temperature_max }}°C<br>
          Min: {{ day.temperature_min }}°C<br>
          Rain: {{ day.rainfall }} mm
        </div>
      </div>
    </div>
  </template>  


  <script setup>
  import { ref, onMounted } from 'vue'
  import api from '../../api/index.js'
  
  const forecast = ref([])
  const weekAlignedForecast = ref([])
  
  function getWeekdayIndex(dateStr) {
    const date = new Date(dateStr)
    return date.getDay() // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
  }
  
  function alignForecastByWeekdays(data) {
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    const aligned = new Array(7).fill(null)
  
    const startIndex = getWeekdayIndex(data[0].date)
  
    for (let i = 0; i < data.length; i++) {
      const dayIndex = (startIndex + i) % 7
      aligned[dayIndex] = {
        ...data[i],
        dayName: days[dayIndex]
      }
    }
  
    return aligned
  }
  
  async function fetchForecast() {
    try {
      const res = await api.get('/weather/forecast') // axios auto-parses JSON
      forecast.value = res.data.forecast
      weekAlignedForecast.value = alignForecastByWeekdays(forecast.value)
    } catch (err) {
      console.error("Error fetching forecast:", err)
    }
  }

  
  onMounted(fetchForecast)
  </script>
  