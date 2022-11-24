import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '@/views/HomePage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('@/views/ContactPage.vue')
  },
  {
    path: '/resume',
    name: 'resume',
    component: () => import('@/views/ResumePage.vue')
  },
  {
    path: '/research',
    name: 'research',
    component: () => import('@/views/ResearchPage.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
