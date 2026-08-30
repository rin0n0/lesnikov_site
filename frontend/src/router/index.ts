import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { 
    path: '/', 
    component: () => import('../views/Home.vue'),
    meta: {
      title: 'Владимир Лесников — Фотограф в Санкт-Петербурге | Выпускные альбомы и фотосессии',
      description: 'Профессиональная фотосъемка в Санкт-Петербурге и Ленинградской области: выпускные альбомы для детских садов и школ (4, 9, 11 класс), свадебные и индивидуальные фотосессии.'
    }
  },
  { 
    path: '/albums', 
    component: () => import('../views/Albums.vue'),
    meta: {
      title: 'Выпускные альбомы в Санкт-Петербурге и ЛО — Детский сад, 4, 9, 11 классы | Владимир Лесников',
      description: 'Выпускные фотокниги и альбомы под ключ для детских садов и школ Санкт-Петербурга и ЛО. Развороты, портреты, цены и примеры работ.'
    }
  },
  { 
    path: '/photoshoots', 
    component: () => import('../views/Photoshoots.vue'),
    meta: {
      title: 'Фотосессии в Санкт-Петербурге — Свадебная, семейная, индивидуальная | Владимир Лесников',
      description: 'Профессиональные фотосессии в Санкт-Петербурге и Ленинградской области: свадьбы, love story, семейные и индивидуальные съемки, репортажи.'
    }
  },
  { 
    path: '/contacts', 
    component: () => import('../views/Contacts.vue'),
    meta: {
      title: 'Контакты и заказ съемки — Владимир Лесников | Фотограф Санкт-Петербург',
      description: 'Заказать фотосессию или выпускной альбом в Санкт-Петербурге. Прямая связь с фотографом Владимиром Лесниковым, телефон, онлайн-заявка.'
    }
  },
  { 
    path: '/admin', 
    component: () => import('../views/Admin.vue'),
    meta: {
      title: 'Панель управления — LESNIKOVFOTO',
      description: 'Панель управления сайтом и Telegram Mini App.'
    }
  },
  { path: '/:pathMatch(.*)*', redirect: '/' }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

router.afterEach((to) => {
  const title = (to.meta.title as string) || 'Владимир Лесников — Фотограф | Санкт-Петербург'
  const description = (to.meta.description as string) || 'Профессиональная фотосъемка выпускных альбомов и фотосессий в Санкт-Петербурге и ЛО. Владимир Лесников.'
  
  document.title = title
  
  let metaDesc = document.querySelector('meta[name="description"]')
  if (!metaDesc) {
    metaDesc = document.createElement('meta')
    metaDesc.setAttribute('name', 'description')
    document.head.appendChild(metaDesc)
  }
  metaDesc.setAttribute('content', description)

  let ogTitle = document.querySelector('meta[property="og:title"]')
  if (ogTitle) ogTitle.setAttribute('content', title)

  let ogDesc = document.querySelector('meta[property="og:description"]')
  if (ogDesc) ogDesc.setAttribute('content', description)
})

export default router
