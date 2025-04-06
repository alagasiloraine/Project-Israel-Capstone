<template>
  <div class="flex h-screen bg-[#f8f9fa] font-poppins">
    <Sidebar />
    <div class="flex-1 overflow-auto bg-gradient-to-br from-green-50 to-emerald-50 p-8">
      <!-- Top Section -->
      <div class="flex gap-6">
        <!-- Left Column - Profile Image & Info -->
        <div class="bg-white rounded-xl shadow-sm p-8 flex-1">
          <div class="flex justify-between mb-6">
            <h2 class="text-2xl font-semibold text-gray-800">Profile Information</h2>
            <button 
              @click="editMode = !editMode"
              class="flex items-center gap-2 px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
            >
              <Pencil class="w-4 h-4" />
              {{ editMode ? 'Save Changes' : 'Edit Profile' }}
            </button>
          </div>

          <div class="flex gap-8">
            <!-- Profile Image Section -->
            <div class="flex flex-col items-center">
              <div class="relative">
                <div class="w-48 h-48 rounded-full overflow-hidden bg-gray-100">
                  <img 
                    :src="user?.profilePicture " 
                    alt="Profile"
                    class="w-full h-full object-cover"
                  />
                </div>
                <button 
                  @click="triggerImageUpload"
                  class="absolute bottom-2 right-2 p-2 bg-white rounded-full shadow-lg hover:bg-gray-50"
                >
                  <Camera class="w-5 h-5 text-gray-600" />
                </button>
                <input 
                  type="file" 
                  ref="imageInput" 
                  class="hidden" 
                  accept="image/*"
                  @change="handleImageUpload"
                />
              </div>
              <!-- Status Badge -->
              <div class="mt-4">
                <span 
                  :class="[
                    'inline-flex items-center px-3 py-1 text-sm font-medium rounded-full',
                    profile.status === 'active' ? 'bg-green-100 text-green-700' :
                    profile.status === 'on-leave' ? 'bg-yellow-100 text-yellow-700' :
                    'bg-gray-100 text-gray-700'
                  ]"
                >
                  {{ profile.status.charAt(0).toUpperCase() + profile.status.slice(1) }}
                </span>
              </div>
            </div>

            <!-- Profile Info Section -->
            <div class="flex-1 space-y-4">
              <div class="grid grid-cols-2 gap-4">
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <User class="w-4 h-4 text-gray-500" />
                    Full Name
                  </label>
                  <input 
                    v-model="profile.name"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                    :value="user?.name || user?.firstName + ' ' + user?.lastName"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <Briefcase class="w-4 h-4 text-gray-500" />
                    Position
                  </label>
                  <input 
                    v-model="profile.position"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <MapPin class="w-4 h-4 text-gray-500" />
                    Address
                  </label>
                  <input 
                    v-model="profile.address"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <Phone class="w-4 h-4 text-gray-500" />
                    Phone Number
                  </label>
                  <input 
                    v-model="profile.phone"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <Mail class="w-4 h-4 text-gray-500" />
                    Email Address
                  </label>
                  <input 
                    v-model="profile.email"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                    :value="user?.email"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <Building2 class="w-4 h-4 text-gray-500" />
                    Department
                  </label>
                  <select
                    v-model="profile.department"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                  >
                    <option value="poultry">Poultry</option>
                    <option value="livestock">Livestock</option>
                    <option value="crops">Crops</option>
                    <option value="maintenance">Maintenance</option>
                  </select>
                </div>
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <Calendar class="w-4 h-4 text-gray-500" />
                    Date of Joining
                  </label>
                  <input 
                    type="date"
                    v-model="profile.joiningDate"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                    :value="user?.createdAt"
                  />
                </div>
                <div class="space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <Activity class="w-4 h-4 text-gray-500" />
                    Employment Status
                  </label>
                  <select
                    v-model="profile.status"
                    :disabled="!editMode"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50"
                  >
                    <option value="active">Active</option>
                    <option value="on-leave">On Leave</option>
                    <option value="retired">Retired</option>
                  </select>
                </div>
                <div class="col-span-2 space-y-2">
                  <label class="text-sm text-gray-600 flex items-center gap-2">
                    <FileText class="w-4 h-4 text-gray-500" />
                    About
                  </label>
                  <textarea
                    v-model="profile.about"
                    :disabled="!editMode"
                    rows="3"
                    class="w-full p-2 border rounded-lg disabled:bg-gray-50 resize-none"
                    placeholder="Add your experience, certifications, and skills..."
                  >{{user?.firstName}}</textarea>
                </div>
                <div class="col-span-2">
                  <label class="text-sm text-gray-600 block mb-2">Certifications</label>
                  <div class="flex flex-wrap gap-2">
                    <span 
                      v-for="cert in profile.certifications" 
                      :key="cert"
                      class="inline-flex items-center gap-1 px-2 py-1 bg-blue-50 text-blue-700 rounded-full text-xs font-medium"
                    >
                      <Award class="w-3 h-3" />
                      {{ cert }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column - Security Settings & Today's Schedule -->
        <div class="w-96 space-y-6">
          <div class="bg-white rounded-xl shadow-sm p-6">
            <h3 class="text-lg font-semibold text-gray-800 mb-4">Security Settings</h3>
            <div class="space-y-4">
              <button 
                @click="showPasswordModal = true"
                class="w-full flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
              >
                <div class="flex items-center gap-3">
                  <Lock class="w-5 h-5 text-gray-600" />
                  <span>Change Password</span>
                </div>
                <ChevronRight class="w-5 h-5 text-gray-400" />
              </button>
              <button 
                @click="logout"
                class="w-full flex items-center justify-between p-3 text-red-600 bg-red-50 rounded-lg hover:bg-red-100 transition-colors"
              >
                <div class="flex items-center gap-3">
                  <LogOut class="w-5 h-5" />
                  <span>Logout</span>
                </div>
                <ChevronRight class="w-5 h-5 opacity-50" />
              </button>
            </div>
          </div>

          <!-- Today's Schedule -->
          <div class="bg-white rounded-xl shadow-sm p-6">
            <h3 class="text-lg font-semibold text-gray-800 mb-4">Today's Sched</h3>
            <div class="space-y-2 divide-y divide-gray-200">
              <div v-for="task in todaysTasks" :key="task.id" class="pt-2 first:pt-0">
                <div class="text-sm font-medium">{{ task.time }}</div>
                <div class="text-sm text-gray-600 pb-2">{{ task.activity }}</div>
              </div>
            </div>

            <!-- Farmer Reminder -->
            <div class="mt-6 pt-4 border-t border-gray-200">
              <p class="text-sm text-green-800 bg-green-50 rounded-xl p-4">
                Remember to log your daily activities and update greenhouse conditions. This helps maintain optimal growing conditions and track plant progress.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Section - Calendar -->
      <div class="flex gap-6 mt-6">
        <!-- Activity History -->
        <div class="bg-white rounded-xl shadow-sm p-6 w-[300px]">
          <div class="flex justify-between items-center mb-4 border-b pb-2">
            <h3 class="text-lg font-semibold text-gray-800">Activity History</h3>
            <div class="flex items-center space-x-2">
              <button class="text-gray-600 hover:text-green-600 transition-colors" @click="prevPage" :disabled="currentPage === 1">
                <ChevronLeft class="w-5 h-5" />
              </button>
              <button class="text-gray-600 hover:text-green-600 transition-colors" @click="nextPage" :disabled="currentPage === totalPages">
                <ChevronRight class="w-5 h-5" />
              </button>
            </div>
          </div>
          <div class="overflow-hidden">
            <div class="space-y-4">
              <div v-for="activity in paginatedActivities" :key="activity.id" class="border-b last:border-0 pb-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-2">
                    <component :is="activity.icon" class="w-5 h-5 text-gray-600" />
                    <span class="text-sm font-medium">{{ activity.name }}</span>
                  </div>
                  <span class="text-xs text-gray-500">{{ activity.date }} {{ activity.time }}</span>
                </div>
                <p class="text-sm text-gray-600 mt-2">{{ activity.description }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Calendar -->
        <div class="bg-white rounded-xl shadow-sm p-6 flex-1">
          <div class="flex items-center justify-between mb-6">
            <div class="flex gap-2">
              <button 
                v-for="view in ['Day', 'Week']" 
                :key="view"
                :class="[
                  'px-3 py-1.5 text-sm rounded-md',
                  currentView === view.toLowerCase()
                    ? 'bg-green-50 text-green-600'
                    : 'text-gray-600 hover:bg-gray-50'
                ]"
                @click="setView(view.toLowerCase())"
              >
                {{ view }}
              </button>
              
              <!-- Month Dropdown -->
              <div class="relative">
                <button 
                  @click="toggleDropdown('month')"
                  :class="[
                    'px-3 py-1.5 text-sm rounded-md',
                    currentView === 'month'
                      ? 'bg-green-50 text-green-600'
                      : 'text-gray-600 hover:bg-gray-50'
                  ]"
                >
                  Month
                </button>
                <div v-if="dropdownOpen === 'month'" class="absolute z-10 mt-1 w-40 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 max-h-48 overflow-y-auto">
                  <div class="py-1" role="menu" aria-orientation="vertical">
                    <button
                      v-for="month in months"
                      :key="month"
                      @click="selectMonth(month)"
                      class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      role="menuitem"
                    >
                      {{ month }}
                    </button>
                  </div>
                </div>
              </div>

              <!-- Year Dropdown -->
              <div class="relative">
                <button 
                  @click="toggleDropdown('year')"
                  :class="[
                    'px-3 py-1.5 text-sm rounded-md',
                    currentView === 'year'
                      ? 'bg-green-50 text-green-600'
                      : 'text-gray-600 hover:bg-gray-50'
                  ]"
                >
                  Year
                </button>
                <div v-if="dropdownOpen === 'year'" class="absolute z-10 mt-1 w-24 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 max-h-48 overflow-y-auto">
                  <div class="py-1" role="menu" aria-orientation="vertical">
                    <button
                      v-for="year in years"
                      :key="year"
                      @click="selectYear(year)"
                      class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      role="menuitem"
                    >
                      {{ year }}
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <button class="p-1 text-gray-400 hover:text-green-600 transition-colors" @click="changeMonth(-1)">
                <ChevronLeft class="w-5 h-5" />
              </button>
              <div class="relative">
                <button 
                  @click="toggleDropdown('currentMonth')"
                  class="text-base font-medium hover:text-green-600 transition-colors"
                >
                  {{ currentMonth }}
                </button>
                <div v-if="dropdownOpen === 'currentMonth'" class="absolute z-10 mt-1 w-40 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 max-h-48 overflow-y-auto">
                  <div class="py-1" role="menu" aria-orientation="vertical">
                    <button
                      v-for="month in months"
                      :key="month"
                      @click="selectMonth(month)"
                      class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      role="menuitem"
                    >
                      {{ month }}
                    </button>
                  </div>
                </div>
              </div>
              <div class="relative">
                <button 
                  @click="toggleDropdown('currentYear')"
                  class="text-base font-medium hover:text-green-600 transition-colors"
                >
                  {{ currentYear }}
                </button>
                <div v-if="dropdownOpen === 'currentYear'" class="absolute z-10 mt-1 w-24 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 max-h-48 overflow-y-auto">
                  <div class="py-1" role="menu" aria-orientation="vertical">
                    <button
                      v-for="year in years"
                      :key="year"
                      @click="selectYear(year)"
                      class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                      role="menuitem"
                    >
                      {{ year }}
                    </button>
                  </div>
                </div>
              </div>
              <button class="p-1 text-gray-400 hover:text-green-600 transition-colors" @click="changeMonth(1)">
                <ChevronRight class="w-5 h-5" />
              </button>
            </div>
          </div>

          <div class="grid grid-cols-7 gap-px bg-gray-200">
            <div 
              v-for="day in ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']" 
              :key="day"
              class="bg-white p-3 text-xs font-medium text-gray-500 text-center"
            >
              {{ day }}
            </div>

            <div 
              v-for="date in 35" 
              :key="date"
              class="bg-white min-h-[100px] p-2 relative group hover:bg-gray-50"
            >
              <div 
                :class="[
                  'text-sm mb-2',
                  date === currentDate ? 'text-green-600 font-medium' : 'text-gray-700',
                  date < 3 || date > 31 ? 'text-gray-400' : ''
                ]"
              >
                {{ getDisplayDate(date) }}
              </div>

              <div class="space-y-1">
                <div 
                  v-if="hasPlanting(date)"
                  class="flex items-center gap-1 text-xs bg-green-50 text-green-600 py-1 px-2 rounded-md w-fit"
                >
                  <Sprout class="w-3 h-3" />
                  <span>Planting</span>
                  <span class="bg-green-100 text-green-700 px-1 rounded text-[10px]">2</span>
                </div>

                <div 
                  v-if="hasHarvesting(date)"
                  class="flex items-center gap-1 text-xs bg-orange-50 text-orange-600 py-1 px-2 rounded-md w-fit"
                >
                  <Wheat class="w-3 h-3" />
                  <span>Harvest</span>
                  <span class="bg-orange-100 text-orange-700 px-1 rounded text-[10px]">3</span>
                </div>

                <div 
                  v-if="hasInspection(date)"
                  class="flex items-center gap-1 text-xs bg-blue-50 text-blue-600 py-1 px-2 rounded-md w-fit"
                >
                  <ClipboardCheck class="w-3 h-3" />
                  <span>Inspection</span>
                  <span class="bg-blue-100 text-blue-700 px-1 rounded text-[10px]">1</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Password Change Modal -->
      <div v-if="showPasswordModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
        <div class="bg-white rounded-xl p-6 w-[400px]">
          <h3 class="text-lg font-semibold text-gray-800 mb-4">Change Password</h3>
          <div class="space-y-4">
            <div class="space-y-2">
              <label class="text-sm text-gray-600">Current Password</label>
              <input 
                type="password" 
                v-model="passwordForm.current"
                class="w-full p-2 border rounded-lg"
              />
            </div>
            <div class="space-y-2">
              <label class="text-sm text-gray-600">New Password</label>
              <input 
                type="password" 
                v-model="passwordForm.new"
                class="w-full p-2 border rounded-lg"
              />
            </div>
            <div class="space-y-2">
              <label class="text-sm text-gray-600">Confirm New Password</label>
              <input 
                type="password" 
                v-model="passwordForm.confirm"
                class="w-full p-2 border rounded-lg"
              />
            </div>
            <div class="flex justify-end gap-3 mt-6">
              <button 
                @click="showPasswordModal = false"
                class="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg"
              >
                Cancel
              </button>
              <button 
                @click="changePassword"
                class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600"
              >
                Update Password
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Notiflix from "notiflix";
import { 
  Camera, 
  Pencil, 
  Lock, 
  LogOut, 
  ChevronRight,
  ChevronLeft,
  Power,
  Calendar,
  Sprout,
  Wheat,
  ClipboardCheck,
  Home,
  Droplet,
  Bug,
  User,
  Building2,
  Phone,
  Mail,
  FileText,
  Activity,
  Award,
  Briefcase,
  MapPin
} from 'lucide-vue-next'
import Sidebar from '../layout/Sidebar.vue'

const router = useRouter()
const editMode = ref(false)
const showPasswordModal = ref(false)
const imageInput = ref(null)
const profileImage = ref(null)
const dropdownOpen = ref(null)

const user = ref(null);

const generateProfilePicture = (email) => {
  if (!email) return null;

  // 🔹 Extract the first letter of the email
  const initial = email.charAt(0).toUpperCase();

  // 🔹 Generate a random background color
  const colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#FFD700"];
  const backgroundColor = colors[Math.floor(Math.random() * colors.length)];

  // 🔹 Create an SVG string for the avatar
  const svg = `
    <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
      <rect width="100" height="100" fill="${backgroundColor}" />
      <text x="50%" y="55%" font-size="50" text-anchor="middle" fill="white" font-family="Arial" dy=".3em">
        ${initial}
      </text>
    </svg>
  `;

  // 🔹 Convert SVG to Data URL
  return `data:image/svg+xml;base64,${btoa(svg)}`;
};

onMounted(() => {
  const storedUser = localStorage.getItem("user") || sessionStorage.getItem("user");
  if (storedUser) {
    user.value = JSON.parse(storedUser);

    if (!user.value.profilePicture) {
      user.value.profilePicture = generateProfilePicture(user.value.email);
    }
  }
});


const profile = reactive({
  name: "",
  position: 'System Administrator',
  status: 'active',
  department: 'crops',
  joiningDate: '2023-01-15',
  address: '123 Main St, City, Country',
  phone: '+1 234 567 890',
  email: 'jane@example.com',
  about: 'Experienced farm administrator with certifications in animal care and equipment handling. Specialized in crop management and sustainable farming practices.',
  certifications: [
    'Animal Care Certified',
    'Equipment Handler',
    'Crop Management',
    'Sustainable Farming'
  ]
})

const passwordForm = reactive({
  current: '',
  new: '',
  confirm: ''
})

const activities = ref([
  {
    id: 1,
    name: 'Greenhouse Visit',
    date: '2024-01-19',
    time: '14:30',
    icon: Home,
    description: 'Conducted a routine inspection of the greenhouse facilities and checked on plant health.'
  },
  {
    id: 2,
    name: 'Planting Session',
    date: '2024-01-18',
    time: '10:15',
    icon: Sprout,
    description: 'Planted a new batch of tomato seedlings in greenhouse section A.'
  },
  {
    id: 3,
    name: 'Harvesting',
    date: '2024-01-17',
    time: '09:45',
    icon: Wheat,
    description: 'Harvested mature lettuce crops from greenhouse section C for market delivery.'
  },
  {
    id: 4,
    name: 'Irrigation Check',
    date: '2024-01-16',
    time: '16:00',
    icon: Droplet,
    description: 'Performed maintenance on the automated irrigation system and adjusted water schedules.'
  },
  {
    id: 5,
    name: 'Pest Control',
    date: '2024-01-15',
    time: '11:30',
    icon: Bug,
    description: 'Applied organic pest control measures to combat aphid infestation in cucumber plants.'
  }
])

const itemsPerPage = 3
const currentPage = ref(1)

const totalPages = computed(() => Math.ceil(activities.value.length / itemsPerPage))

const paginatedActivities = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return activities.value.slice(start, end)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const triggerImageUpload = () => {
  imageInput.value.click()
}

const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      profileImage.value = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const changePassword = () => {
  // Implement password change logic
  showPasswordModal.value = false
}


const logout = () => {
  Notiflix.Confirm.show(
    "Confirm Logout",
    "Are you sure you want to log out?",
    "Yes",
    "Cancel",
    () => {
      localStorage.removeItem("user");
      sessionStorage.removeItem("user");
      router.push("/");
      Notiflix.Notify.success("Logged out successfully!");
    }
  );
};
const currentView = ref('month')
const currentMonth = ref('January')
const currentYear = ref('2024')
const currentDate = ref(new Date().getDate())

const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
const years = Array.from({length: 11}, (_, i) => 2015 + i)

const todaysTasks = ref([
  {
    id: 1,
    time: '08:00 - 09:00',
    activity: 'Check Greenhouse Temperature',
  },
  {
    id: 2,
    time: '10:00 - 11:30',
    activity: 'Plant New Seedlings',
  },
  {
    id: 3,
    time: '14:00 - 15:00',
    activity: 'Harvest Mature Crops',
  }
])

const getDisplayDate = (date) => {
  if (date < 3) return 30 + date
  if (date > 31) return date - 31
  return date
}

const hasPlanting = (date) => date % 7 === 0
const hasHarvesting = (date) => date % 5 === 0
const hasInspection = (date) => date % 3 === 0

const toggleDropdown = (view) => {
  dropdownOpen.value = dropdownOpen.value === view ? null : view
}

const changeMonth = (direction) => {
  let currentIndex = months.indexOf(currentMonth.value)
  currentIndex += direction

  if (currentIndex < 0) {
    currentIndex = 11
    currentYear.value--
  } else if (currentIndex > 11) {
    currentIndex = 0
    currentYear.value++
  }

  currentMonth.value = months[currentIndex]
}

const setView = (view) => {
  currentView.value = view
}

const selectMonth = (month) => {
  currentMonth.value = month
  dropdownOpen.value = null
}

const selectYear = (year) => {
  currentYear.value = year
  dropdownOpen.value = null
}
</script>