<template>
  <div
    class="min-h-screen min-h-[100dvh] flex flex-col relative selection:bg-gray-900 selection:text-white dark:selection:bg-white dark:selection:text-gray-900">

    <!-- Ambient 3D Liquid Background (Pure CSS Mesh - 0 KB Network Overhead) -->
    <div class="fixed inset-0 pointer-events-none -z-10 overflow-hidden" aria-hidden="true">
      <div class="absolute -top-[15%] left-1/2 -translate-x-1/2 w-[1100px] h-[600px] bg-gradient-to-b from-cyan-500/10 via-blue-500/5 to-transparent rounded-full blur-[120px] dark:from-cyan-500/15 dark:via-blue-600/10 transform-gpu"></div>
      <div class="absolute bottom-0 right-0 w-[700px] h-[550px] bg-gradient-to-t from-slate-200/40 via-transparent to-transparent dark:from-slate-800/20 rounded-full blur-[100px] transform-gpu"></div>
      <div class="absolute inset-0 bg-gradient-to-b from-slate-50/80 via-slate-50/92 to-slate-50 dark:from-[#080c14]/85 dark:via-[#080c14]/94 dark:to-[#080c14]"></div>
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
          <nav class="hidden md:flex items-center gap-1 p-1 rounded-2xl liquid-card">
            <router-link to="/"
              class="px-5 py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200"
              :class="[
                $route.path === '/'
                  ? 'liquid-btn-active font-extrabold shadow-sm'
                  : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5'
              ]">
              Главная
            </router-link>

            <router-link to="/albums"
              class="px-5 py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200"
              :class="[
                $route.path.startsWith('/albums')
                  ? 'liquid-btn-active font-extrabold shadow-sm'
                  : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5'
              ]">
              Выпускные альбомы
            </router-link>

            <router-link to="/photoshoots"
              class="px-5 py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200"
              :class="[
                $route.path.startsWith('/photoshoots')
                  ? 'liquid-btn-active font-extrabold shadow-sm'
                  : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5'
              ]">
              Фотосессии
            </router-link>

            <router-link to="/contacts"
              class="px-5 py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition-all duration-200"
              :class="[
                $route.path === '/contacts'
                  ? 'liquid-btn-active font-extrabold shadow-sm'
                  : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/5'
              ]">
              Контакты
            </router-link>
          </nav>

          <!-- Right Action / Mobile Hamburger Toggle -->
          <div class="flex items-center gap-3">
            <button @click="mobileMenuOpen = !mobileMenuOpen"
              class="md:hidden w-10 h-10 rounded-2xl flex items-center justify-center liquid-card text-gray-900 dark:text-white active:scale-95 transition-all"
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

    <!-- Mobile 3D Liquid Glass Floating Island Modal -->
    <Teleport to="body">
      <transition name="modal-fade">
        <div v-if="mobileMenuOpen"
          class="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-6 glass-backdrop transition-all select-none"
          @click.self="closeMobileMenu" @keydown.esc="closeMobileMenu">
          <div class="glass-tile w-full max-w-xs sm:max-w-sm rounded-[28px] p-6 sm:p-7 space-y-5 relative">
            <div class="flex items-center justify-between pb-3 border-b border-black/10 dark:border-white/10">
              <span class="text-xs sm:text-sm font-black tracking-widest uppercase text-gray-900 dark:text-white">
                LESNIKOVFOTO
              </span>
              <button @click="closeMobileMenu"
                class="w-8 h-8 rounded-full flex items-center justify-center text-gray-900 dark:text-white bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/20 active:scale-90 transition-all border border-black/10 dark:border-white/20 shadow-sm"
                aria-label="Закрыть меню">
                <AppIcon name="close" :size="16" />
              </button>
            </div>

            <nav class="flex flex-col gap-2">
              <router-link to="/" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[$route.path === '/' ? 'liquid-btn-active font-black shadow-md' : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10']">
                <span>Главная</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>

              <router-link to="/albums" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[$route.path.startsWith('/albums') ? 'liquid-btn-active font-black shadow-md' : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10']">
                <span>Выпускные альбомы</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>

              <router-link to="/photoshoots" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[$route.path.startsWith('/photoshoots') ? 'liquid-btn-active font-black shadow-md' : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10']">
                <span>Фотосессии</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>

              <router-link to="/contacts" @click="closeMobileMenu"
                class="flex items-center justify-between px-4 py-3 rounded-2xl text-xs sm:text-sm font-extrabold uppercase tracking-wider transition-all duration-200"
                :class="[$route.path === '/contacts' ? 'liquid-btn-active font-black shadow-md' : 'text-gray-900 dark:text-white hover:bg-black/5 dark:hover:bg-white/10']">
                <span>Контакты</span>
                <span class="text-xs opacity-60">→</span>
              </router-link>
            </nav>

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

    <!-- Centered 3D Liquid Glass Island Back-to-Top -->
    <div v-if="$route.path !== '/admin'" class="w-full flex justify-center px-4 mt-16 mb-[-2rem] relative z-20">
      <button
        @click="scrollToTop"
        class="glass-tile inline-flex items-center gap-3 px-8 py-3.5 rounded-full shadow-2xl hover:scale-105 active:scale-95 transition-all duration-300 group cursor-pointer select-none"
        title="Наверх"
        aria-label="Прокрутить страницу наверх"
      >
        <AppIcon name="arrow-up" :size="16" class="transition-transform duration-300 group-hover:-translate-y-1 text-gray-900 dark:text-white" />
        <span class="text-xs font-black uppercase tracking-widest text-gray-900 dark:text-white">
          Наверх
        </span>
      </button>
    </div>

    <!-- Classic Glass Footer -->
    <footer v-if="$route.path !== '/admin'"
      class="mt-20 border-t border-gray-200/80 dark:border-gray-800/80 bg-white/60 dark:bg-gray-950/60 backdrop-blur-xl">
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

function scrollToTop() {
  if (typeof window !== 'undefined') {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }
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
