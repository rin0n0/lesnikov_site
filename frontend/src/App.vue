<template>
  <div
    class="min-h-screen min-h-[100dvh] flex flex-col relative selection:bg-gray-900 selection:text-white dark:selection:bg-white dark:selection:text-gray-900">

    <!-- Ambient 3D Liquid Background (Original Hero Photo Blurred & Blended) -->
    <div class="fixed inset-0 pointer-events-none -z-10 overflow-hidden" aria-hidden="true">
      <img src="/bg.jpg" alt=""
        class="w-full h-full object-cover blur-[80px] scale-110 opacity-25 dark:opacity-15 transform-gpu filter" />
      <div
        class="absolute inset-0 bg-gradient-to-b from-slate-50/80 via-slate-50/92 to-slate-50 dark:from-[#080c14]/85 dark:via-[#080c14]/94 dark:to-[#080c14]">
      </div>
    </div>

    <!-- Liquid Crystal Glass Header (Single-tier on both Desktop & Mobile) -->
    <header v-if="$route.path !== '/admin'" class="fixed top-0 inset-x-0 w-full z-50 transition-all">
      <div class="header-glass pt-[env(safe-area-inset-top,0px)]">
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
            <router-link to="/"
              class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
              active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold">
              Главная
            </router-link>
            <router-link to="/albums"
              class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
              active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold">
              Выпускные альбомы
            </router-link>
            <router-link to="/photoshoots"
              class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
              active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold">
              Фотосессии
            </router-link>
            <router-link to="/contacts"
              class="px-4 py-2 rounded-xl transition-all text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5"
              active-class="bg-gray-900/10 dark:bg-white/15 text-gray-900 dark:text-white font-bold">
              Контакты
            </router-link>
          </nav>

          <!-- Right Action Elements -->
          <div class="flex items-center gap-2 sm:gap-3">
            <!-- Mobile Hamburger Toggle Button -->
            <button @click="mobileMenuOpen = !mobileMenuOpen"
              class="md:hidden w-10 h-10 rounded-xl liquid-card flex items-center justify-center text-gray-800 dark:text-white transition-all active:scale-90"
              :aria-label="mobileMenuOpen ? 'Закрыть меню' : 'Открыть меню'">
              <span v-if="!mobileMenuOpen" class="text-lg leading-none flex items-center justify-center">
                <AppIcon name="menu" :size="20" />
              </span>
              <span v-else class="text-lg leading-none flex items-center justify-center">
                <AppIcon name="close" :size="20" />
              </span>
            </button>
          </div>
        </div>
      </div>

    </header>

    <!-- Mobile 3D Liquid Glass Floating Island Modal (Полноэкранная модалка с островком по центру) -->
    <Teleport to="body">
      <transition name="modal-fade">
        <div v-if="mobileMenuOpen"
          class="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-6 glass-backdrop transition-all select-none"
          @click.self="closeMobileMenu" @keydown.esc="closeMobileMenu">
          <!-- Floating Glass Tile (Стеклянная плитка с объёмом) -->
          <div class="glass-tile w-full max-w-xs sm:max-w-sm rounded-[28px] p-6 sm:p-7 space-y-5 relative">
            <!-- Tile Header -->
            <div class="flex items-center justify-between pb-3 border-b border-black/10 dark:border-white/10">
              <div class="flex flex-col">
                <span class="text-xs sm:text-sm font-black tracking-widest uppercase text-gray-900 dark:text-white">
                  LESNIKOVFOTO
                </span>
              </div>

              <!-- Close Button -->
              <button @click="closeMobileMenu"
                class="w-8 h-8 rounded-full flex items-center justify-center text-gray-900 dark:text-white bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/20 active:scale-90 transition-all border border-black/10 dark:border-white/20 shadow-sm"
                aria-label="Закрыть меню">
                <AppIcon name="close" :size="16" />
              </button>
            </div>

            <!-- Navigation Links -->
            <nav class="flex flex-col gap-2">
              <router-link to="/" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[
                  $route.path === '/'
                    ? 'liquid-btn-active font-black shadow-md'
                    : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10'
                ]">
                <span>Главная</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>

              <router-link to="/albums" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[
                  $route.path.startsWith('/albums')
                    ? 'liquid-btn-active font-black shadow-md'
                    : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10'
                ]">
                <span>Выпускные альбомы</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>

              <router-link to="/photoshoots" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[
                  $route.path.startsWith('/photoshoots')
                    ? 'liquid-btn-active font-black shadow-md'
                    : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10'
                ]">
                <span>Фотосессии</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>

              <router-link to="/contacts" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[
                  $route.path === '/contacts'
                    ? 'liquid-btn-active font-black shadow-md'
                    : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10'
                ]">
                <span>Контакты</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>
            </nav>

            <!-- Minimal Action -->
            <div class="pt-2 border-t border-black/10 dark:border-white/10">
              <router-link to="/contacts" @click="closeMobileMenu"
                class="w-full py-3.5 bg-gray-900 text-white dark:bg-white dark:text-gray-900 rounded-2xl text-xs font-black uppercase tracking-widest text-center block shadow-lg hover:opacity-90 active:scale-98 transition-all">
                Оставить заявку
              </router-link>
            </div>
          </div>
        </div>
      </transition>
    </Teleport>

    <!-- Main Content Area -->
    <main class="flex-grow" :class="$route.path !== '/admin' ? 'pt-20 md:pt-28' : ''">
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Classic Glass Footer -->
    <footer v-if="$route.path !== '/admin'"
      class="mt-28 border-t border-gray-200/80 dark:border-gray-800/80 bg-white/60 dark:bg-gray-950/60 backdrop-blur-xl">
      <div
        class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex flex-col md:flex-row justify-between items-center gap-6 text-xs text-gray-500 dark:text-gray-400">
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

        <div
          class="flex flex-wrap justify-center items-center gap-5 uppercase tracking-wider text-[11px] font-semibold">
          <a href="https://vk.com/lesnikovfoto" target="_blank"
            class="flex items-center gap-1.5 hover:text-blue-500 transition-colors">
            <AppIcon name="vk" :size="15" />
            <span>ВКонтакте</span>
          </a>
          <a href="tel:+79117775700" class="hover:text-gray-900 dark:hover:text-white transition-colors font-mono">
            +7 (911) 777-57-00
          </a>
          <router-link to="/contacts" class="hover:text-gray-900 dark:hover:text-white transition-colors">
            Оставить заявку
          </router-link>
          <button 
            @click="scrollToTop" 
            class="flex items-center gap-1 hover:text-gray-900 dark:hover:text-white transition-colors text-[11px] font-bold uppercase tracking-wider cursor-pointer"
            title="Прокрутить в начало страницы"
          >
            <AppIcon name="arrow-up" :size="14" />
            <span>Наверх</span>
          </button>
        </div>

        <div class="text-[11px]">
          © 2026 Все права защищены.
        </div>
      </div>
    </footer>

    <!-- Floating Liquid Glass Back to Top Button (Появляется при прокрутке вниз) -->
    <transition name="fade">
      <button
        v-if="showBackToTop && $route.path !== '/admin'"
        @click="scrollToTop"
        class="fixed bottom-6 right-6 sm:bottom-8 sm:right-8 z-40 p-3.5 sm:px-4 sm:py-3 rounded-2xl glass-tile shadow-2xl hover:scale-105 active:scale-95 transition-all duration-300 flex items-center gap-2 text-xs font-black uppercase tracking-wider text-gray-900 dark:text-white group border border-black/10 dark:border-white/15 cursor-pointer"
        title="Наверх"
        aria-label="Прокрутить наверх"
      >
        <AppIcon name="arrow-up" :size="16" class="transition-transform group-hover:-translate-y-0.5" />
        <span class="hidden sm:inline">Наверх</span>
      </button>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import AppIcon from './components/AppIcon.vue'

const mobileMenuOpen = ref(false)
const showBackToTop = ref(false)

function closeMobileMenu() {
  mobileMenuOpen.value = false
}

function scrollToTop() {
  if (typeof window !== 'undefined') {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }
}

function handleScroll() {
  if (typeof window !== 'undefined') {
    showBackToTop.value = window.scrollY > 350
  }
}

onMounted(() => {
  if (typeof window !== 'undefined') {
    window.addEventListener('scroll', handleScroll, { passive: true })
  }
})

onBeforeUnmount(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('scroll', handleScroll)
  }
})
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

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-fade-enter-from .glass-tile,
.modal-fade-leave-to .glass-tile {
  transform: scale(0.92) translateY(12px);
  opacity: 0;
}

.glass-tile {
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
}
</style>
