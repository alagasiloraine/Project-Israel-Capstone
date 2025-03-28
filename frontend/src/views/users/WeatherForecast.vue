<template>
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
  </script>