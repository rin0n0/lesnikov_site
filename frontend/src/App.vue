<template>
  <div class="min-h-screen flex flex-col relative selection:bg-gray-900 selection:text-white dark:selection:bg-white dark:selection:text-gray-900">
    
    <!-- Ambient 3D Liquid Background (Original Hero Photo Blurred & Blended) -->
    <div class="fixed inset-0 pointer-events-none -z-10 overflow-hidden" aria-hidden="true">
      <img 
        src="/bg.jpg" 
        alt="" 
        class="w-full h-full object-cover blur-[80px] scale-110 opacity-25 dark:opacity-15 transform-gpu filter"
      />
      <div class="absolute inset-0 bg-gradient-to-b from-slate-50/80 via-slate-50/92 to-slate-50 dark:from-[#080c14]/85 dark:via-[#080c14]/94 dark:to-[#080c14]"></div>
    </div>

    <!-- Liquid Crystal Glass Header (Single-tier on both Desktop & Mobile) -->
    <header v-if="$route.path !== '/admin'" class="fixed top-0 inset-x-0 w-full z-50 header-glass transition-all">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex justify-between items-center">
        
        <!-- Brand Logo with Geolocation -->
        <router-link to="/" class="flex flex-col group" @click="closeMobileMenu">
          <div class="flex items-center gap-1.5">
            <span class="text-base sm:text-lg font-extrabold tracking-widest uppercase text-gray-900 dark:text-white">
              LESNIKOVFOTO
            </span>
          </div>
          <span class="text-[10px] tracking-wider text-slate-500 dark:text-slate-400 font-medium uppercase -mt-0.5">
            Владимир Лесников <span class="text-slate-400 dark:text-slate-600">·</span> Санкт-Петербург
          </span>
        </router-link>
        
        <!-- Desktop Navigation Bar -->
        <nav class="hidden md:flex items-center gap-1 sm:gap-2 text-xs uppercase tracking-wider font-semibold">
          <router-link 
            to="/" 
            class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
            active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
          >
            Главная
          </router-link>
          <router-link 
            to="/albums" 
            class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
            active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
          >
            Выпускные альбомы
          </router-link>
          <router-link 
            to="/photoshoots" 
            class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
            active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
          >
            Фотосессии
          </router-link>
          <router-link 
            to="/contacts" 
            class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
            active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold"
          >
            Контакты
          </router-link>
        </nav>

        <!-- Right Action Elements -->
        <div class="flex items-center gap-2 sm:gap-3">
          <!-- VK icon -->
          <a 
            href="https://vk.com/lesnikovfoto" 
            target="_blank" 
            class="w-9 h-9 rounded-xl liquid-card flex items-center justify-center text-blue-500 hover:text-blue-600 transition-transform active:scale-95"
            title="Группа ВКонтакте"
          >
            <AppIcon name="vk" :size="18" />
          </a>

          <!-- Quick Phone (Desktop + Mobile) -->
          <a 
            href="tel:+79117775700" 
            class="hidden sm:flex items-center gap-1.5 px-3 py-2 rounded-xl liquid-card text-xs font-bold text-gray-700 dark:text-gray-200 hover:text-gray-900 transition-transform active:scale-95"
            title="Позвонить фотографу"
          >
            <AppIcon name="phone" :size="14" />
            <span class="font-mono">+7 (911) 777-57-00</span>
          </a>
          
          <!-- Contact Button (Desktop) -->
          <router-link 
            to="/contacts" 
            class="hidden md:inline-flex bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider hover:opacity-90 transition-all shadow-sm active:scale-95"
          >
            Связаться
          </router-link>

          <!-- Mobile Hamburger Toggle Button -->
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="md:hidden w-10 h-10 rounded-xl liquid-card flex items-center justify-center text-gray-800 dark:text-white transition-all active:scale-90"
            :aria-label="mobileMenuOpen ? 'Закрыть меню' : 'Открыть меню'"
          >
            <span v-if="!mobileMenuOpen" class="text-lg leading-none flex items-center justify-center"><AppIcon name="menu" :size="20" /></span>
            <span v-else class="text-lg leading-none flex items-center justify-center"><AppIcon name="close" :size="20" /></span>
          </button>
        </div>
      </div>

      <!-- Mobile Glass Drawer Menu -->
      <transition name="drawer">
        <div 
          v-if="mobileMenuOpen" 
          class="md:hidden border-t border-gray-200/50 dark:border-gray-800/50 bg-white/95 dark:bg-slate-950/95 backdrop-blur-2xl px-5 py-6 space-y-5 shadow-2xl"
        >
          <!-- Geo Badge -->
          <div class="flex items-center gap-2 text-xs font-semibold text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-900/80 px-3.5 py-2 rounded-xl border border-slate-200/60 dark:border-slate-800">
            <AppIcon name="location" :size="14" />
            <span>Санкт-Петербург и Ленинградская область</span>
          </div>

          <!-- Nav Links -->
          <nav class="flex flex-col gap-2">
            <router-link 
              to="/" 
              @click="closeMobileMenu"
              class="flex items-center justify-between px-4 py-3 rounded-xl text-sm font-bold uppercase tracking-wider text-gray-700 dark:text-gray-200 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors"
              active-class="bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-extrabold"
            >
              <span>Главная</span>
              <span class="text-xs opacity-60">→</span>
            </router-link>

            <router-link 
              to="/albums" 
              @click="closeMobileMenu"
              class="flex items-center justify-between px-4 py-3 rounded-xl text-sm font-bold uppercase tracking-wider text-gray-700 dark:text-gray-200 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors"
              active-class="bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-extrabold"
            >
              <span>Выпускные альбомы</span>
              <span class="text-xs opacity-60">→</span>
            </router-link>

            <router-link 
              to="/photoshoots" 
              @click="closeMobileMenu"
              class="flex items-center justify-between px-4 py-3 rounded-xl text-sm font-bold uppercase tracking-wider text-gray-700 dark:text-gray-200 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors"
              active-class="bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-extrabold"
            >
              <span>Фотосессии</span>
              <span class="text-xs opacity-60">→</span>
            </router-link>

            <router-link 
              to="/contacts" 
              @click="closeMobileMenu"
              class="flex items-center justify-between px-4 py-3 rounded-xl text-sm font-bold uppercase tracking-wider text-gray-700 dark:text-gray-200 hover:bg-slate-100 dark:hover:bg-slate-900 transition-colors"
              active-class="bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-extrabold"
            >
              <span>Контакты</span>
              <span class="text-xs opacity-60">→</span>
            </router-link>
          </nav>

          <!-- Quick Connect Buttons -->
          <div class="pt-2 border-t border-slate-200/60 dark:border-slate-800 space-y-3">
            <router-link 
              to="/contacts" 
              @click="closeMobileMenu"
              class="w-full py-3.5 bg-gray-900 text-white dark:bg-white dark:text-gray-900 rounded-xl text-xs font-bold uppercase tracking-widest text-center block shadow-lg active:scale-98 transition-all"
            >
              Оставить заявку
            </router-link>

            <div class="grid grid-cols-2 gap-2">
              <a 
                href="tel:+79117775700" 
                class="py-2.5 px-3 rounded-xl liquid-card text-xs font-bold text-center flex items-center justify-center gap-1.5 text-gray-800 dark:text-white"
              >
                <AppIcon name="phone" :size="14" />
                <span>Позвонить</span>
              </a>
              <a 
                href="https://vk.com/lesnikovfoto" 
                target="_blank"
                class="py-2.5 px-3 rounded-xl liquid-card text-xs font-bold text-center flex items-center justify-center gap-1.5 text-blue-500"
              >
                <AppIcon name="vk" :size="15" />
                <span>ВКонтакте</span>
              </a>
            </div>
          </div>
        </div>
      </transition>
    </header>

    <!-- Main Content Area -->
    <main class="flex-grow" :class="$route.path !== '/admin' ? 'pt-20 md:pt-28' : ''">
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Classic Glass Footer -->
    <footer v-if="$route.path !== '/admin'" class="mt-28 border-t border-gray-200/80 dark:border-gray-800/80 bg-white/60 dark:bg-gray-950/60 backdrop-blur-xl">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex flex-col md:flex-row justify-between items-center gap-6 text-xs text-gray-500 dark:text-gray-400">
        <div class="text-center md:text-left">
          <div class="font-extrabold text-sm text-gray-900 dark:text-white tracking-widest uppercase">
            LESNIKOVFOTO
          </div>
          <div class="mt-1 font-medium">
            Владимир Лесников — профессиональный фотограф
          </div>
          <div class="text-[11px] text-slate-400 dark:text-slate-500 mt-0.5">
            Санкт-Петербург и Ленинградская область
          </div>
        </div>

        <div class="flex flex-wrap justify-center items-center gap-5 uppercase tracking-wider text-[11px] font-semibold">
          <a href="https://vk.com/lesnikovfoto" target="_blank" class="flex items-center gap-1.5 hover:text-blue-500 transition-colors">
            <AppIcon name="vk" :size="15" />
            <span>ВКонтакте</span>
          </a>
          <a href="tel:+79117775700" class="hover:text-gray-900 dark:hover:text-white transition-colors font-mono">
            +7 (911) 777-57-00
          </a>
          <router-link to="/contacts" class="hover:text-gray-900 dark:hover:text-white transition-colors">
            Оставить заявку
          </router-link>
        </div>

        <div class="text-[11px]">
          © 2026 Все права защищены.
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import AppIcon from './components/AppIcon.vue'

const mobileMenuOpen = ref(false)

function closeMobileMenu() {
  mobileMenuOpen.value = false
}
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

.drawer-enter-active,
.drawer-leave-active {
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.drawer-enter-from,
.drawer-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>
