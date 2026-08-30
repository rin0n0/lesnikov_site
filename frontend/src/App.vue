<template>
  <div class="min-h-screen flex flex-col selection:bg-gray-900 selection:text-white dark:selection:bg-white dark:selection:text-gray-900">
    
    <!-- Classic Full-Width 3D Liquid Crystal Header (Hidden in TMA Admin) -->
    <header v-if="$route.path !== '/admin'" class="fixed top-0 inset-x-0 w-full z-50 header-glass transition-all">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex justify-between items-center">
        <!-- Logo -->
        <router-link to="/" class="flex flex-col group">
          <span class="text-base sm:text-lg font-extrabold tracking-widest uppercase text-gray-900 dark:text-white">
            LESNIKOVFOTO
          </span>
          <span class="text-[10px] tracking-wider text-gray-400 uppercase -mt-0.5">
            Владимир Лесников
          </span>
        </router-link>
        
        <!-- Desktop Nav -->
        <nav class="hidden md:flex items-center gap-1 sm:gap-2 text-xs uppercase tracking-wider font-semibold">
          <router-link 
            to="/" 
            class="px-4 py-2 rounded-lg transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
            active-class="bg-gray-900/5 dark:bg-white/10 text-gray-900 dark:text-white font-bold"
          >
            Главная
          </router-link>
          <router-link 
            to="/albums" 
            class="px-4 py-2 rounded-lg transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
            active-class="bg-gray-900/5 dark:bg-white/10 text-gray-900 dark:text-white font-bold"
          >
            Выпускные альбомы
          </router-link>
          <router-link 
            to="/photoshoots" 
            class="px-4 py-2 rounded-lg transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
            active-class="bg-gray-900/5 dark:bg-white/10 text-gray-900 dark:text-white font-bold"
          >
            Фотосессии
          </router-link>
          <router-link 
            to="/contacts" 
            class="px-4 py-2 rounded-lg transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
            active-class="bg-gray-900/5 dark:bg-white/10 text-gray-900 dark:text-white font-bold"
          >
            Контакты
          </router-link>
        </nav>

        <!-- Right Side CTA & VK -->
        <div class="flex items-center gap-3">
          <a 
            href="https://vk.com/lesnikovfoto" 
            target="_blank" 
            class="w-9 h-9 rounded-xl liquid-card flex items-center justify-center text-blue-500 hover:text-blue-600 transition-colors"
            title="ВКонтакте"
          >
            <AppIcon name="vk" :size="18" />
          </a>
          
          <router-link 
            to="/contacts" 
            class="bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider hover:opacity-90 transition-all shadow-sm"
          >
            Связаться
          </router-link>
        </div>
      </div>

      <!-- Mobile Nav Row -->
      <div class="flex md:hidden justify-center border-t border-gray-200/40 dark:border-gray-800/40 py-2 px-2 gap-1 text-[11px] font-semibold uppercase tracking-wider">
        <router-link 
          to="/" 
          class="px-2.5 py-1 rounded-lg text-gray-600 dark:text-gray-300"
          active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
        >
          Главная
        </router-link>
        <router-link 
          to="/albums" 
          class="px-2.5 py-1 rounded-lg text-gray-600 dark:text-gray-300"
          active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
        >
          Альбомы
        </router-link>
        <router-link 
          to="/photoshoots" 
          class="px-2.5 py-1 rounded-lg text-gray-600 dark:text-gray-300"
          active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
        >
          Фотосессии
        </router-link>
        <router-link 
          to="/contacts" 
          class="px-2.5 py-1 rounded-lg text-gray-600 dark:text-gray-300"
          active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
        >
          Контакты
        </router-link>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow" :class="$route.path !== '/admin' ? 'pt-24 md:pt-28' : ''">
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Classic Full-Width Rectangular Footer (Hidden in TMA Admin) -->
    <footer v-if="$route.path !== '/admin'" class="mt-28 border-t border-gray-200 dark:border-gray-800 bg-white/40 dark:bg-gray-950/40 backdrop-blur-md">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex flex-col md:flex-row justify-between items-center gap-6 text-xs text-gray-500 dark:text-gray-400">
        <div class="text-center md:text-left">
          <div class="font-extrabold text-sm text-gray-900 dark:text-white tracking-widest uppercase">
            LESNIKOVFOTO
          </div>
          <div class="mt-1">
            Владимир Лесников — профессиональный фотограф
          </div>
        </div>

        <div class="flex items-center gap-6 uppercase tracking-wider text-[11px] font-semibold">
          <a href="https://vk.com/lesnikovfoto" target="_blank" class="flex items-center gap-2 hover:text-blue-500 transition-colors">
            <AppIcon name="vk" :size="15" />
            <span>ВКонтакте</span>
          </a>
          <a href="tel:+79117775700" class="hover:text-gray-900 dark:hover:text-white transition-colors">
            +7 (911) 777-57-00
          </a>
          <router-link to="/contacts" class="hover:text-gray-900 dark:hover:text-white transition-colors">
            Оставить заявку
          </router-link>
        </div>

        <div>
          © 2026 Все права защищены.
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import AppIcon from './components/AppIcon.vue'
</script>

<style>
.page-enter-active,
.page-leave-active {
  transition: opacity 0.15s ease;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
}
</style>
