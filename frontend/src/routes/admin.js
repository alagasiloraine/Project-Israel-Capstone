import AdminCalendar from '../views/admin/AdminCalendar.vue'
import StaffManagement from '../views/admin/StaffManagement.vue'
import AdminOverview from '../views/admin/AdminOverview.vue'

export const adminRoutes = [
  {
    path: '/calendar',
    name: 'AdminCalendar',
    component: AdminCalendar
  },
  {
    path: '/staff-management',
    name: 'StaffManagement',
    component: StaffManagement
  },
  {
    path: '/overview',
    name: 'AdminOverview',
    component: AdminOverview
  },

]