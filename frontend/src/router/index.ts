import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', component: () => import('../views/Home.vue') },
  { path: '/albums', component: () => import('../views/Albums.vue') },
  { path: '/photoshoots', component: () => import('../views/Photoshoots.vue') },
  { path: '/contacts', component: () => import('../views/Contacts.vue') },
  { path: '/admin', component: () => import('../views/Admin.vue') },
  { path: '/:pathMatch(.*)*', redirect: '/' }
]

export default createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})
