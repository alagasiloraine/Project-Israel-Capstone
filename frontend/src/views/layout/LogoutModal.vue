<!-- components/LogoutModal.vue -->
<template>
  <div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-xl p-6 max-w-sm w-full text-center">
      <h2 class="text-lg font-semibold mb-4">Are you sure you want to logout?</h2>
      <div class="flex justify-end gap-2">
        <button @click="$emit('cancel')" class="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400">
          Cancel
        </button>
        <button @click="$emit('confirm')" class="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">
          Logout
        </button>
      </div>
    </div>
  </div>
</template>
