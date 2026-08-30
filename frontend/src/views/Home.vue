<template>
  <div>
    <!-- Elegant Centered Business Card Bio (Визитка с гео-привязкой) -->
    <section class="px-4 pt-6 pb-12 md:pt-10 md:pb-16 max-w-4xl mx-auto text-center">
      <div class="inline-flex flex-col items-center">
        
        <!-- Vladimir's Portrait Avatar with Liquid Glow -->
        <div class="relative group mb-6">
          <div class="w-32 h-32 sm:w-40 sm:h-40 rounded-full overflow-hidden border-4 border-white/80 dark:border-slate-800 shadow-2xl bg-slate-200 dark:bg-slate-800 relative z-10">
            <img 
              src="/avatar.jpg" 
              alt="Владимир Лесников"
              class="w-full h-full object-cover grayscale contrast-110 group-hover:scale-105 transition-transform duration-500"
              @error="(e) => (e.target as HTMLImageElement).src = '/uploads/home_9df4621f.jpg'"
            />
          </div>
          <div class="absolute -inset-1 bg-gradient-to-r from-cyan-500/20 to-blue-500/20 rounded-full blur-xl -z-0"></div>
        </div>

        <!-- Geolocation Chip -->
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-200/60 dark:bg-slate-800/80 text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-3 border border-slate-300/40 dark:border-slate-700/50">
          <span>📍</span>
          <span>Санкт-Петербург · Ломоносов</span>
        </div>

        <!-- Name & Bio -->
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight text-gray-900 dark:text-white uppercase mb-2">
          Владимир Лесников
        </h1>
        <p class="text-xs sm:text-sm font-bold uppercase tracking-widest text-slate-500 dark:text-slate-400 mb-6">
          Профессиональный фотограф
        </p>

        <!-- Trust Badges -->
        <div class="flex flex-wrap justify-center gap-2 mb-8 text-[11px] font-semibold text-slate-600 dark:text-slate-300">
          <span class="px-3 py-1 rounded-lg liquid-card">📸 10+ лет опыта</span>
          <span class="px-3 py-1 rounded-lg liquid-card">📚 1000+ выпускных альбомов</span>
          <span class="px-3 py-1 rounded-lg liquid-card">⚡ Быстрая отдача фото</span>
        </div>

        <!-- Navigation Buttons to 2 key worlds -->
        <div class="flex flex-wrap justify-center gap-3 sm:gap-4">
          <router-link 
            to="/albums" 
            class="bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-7 py-3.5 rounded-2xl font-bold text-xs uppercase tracking-wider shadow-lg hover:opacity-90 transition-all active:scale-95 flex items-center gap-2"
          >
            <span>🎓</span>
            <span>Выпускные альбомы</span>
          </router-link>
          <router-link 
            to="/photoshoots" 
            class="px-7 py-3.5 rounded-2xl font-bold text-xs uppercase tracking-wider liquid-card hover:bg-slate-100 dark:hover:bg-slate-800 transition-all active:scale-95 flex items-center gap-2 text-gray-800 dark:text-white"
          >
            <span>📷</span>
            <span>Фотосессии</span>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Straight Rectangular Natural Photo Grid -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-xs sm:text-sm font-bold tracking-widest uppercase text-slate-500 dark:text-slate-400">
          Избранные работы ({{ galleryImages.length }})
        </h2>
        <span class="text-xs text-slate-400">
          Кликните на фото для просмотра
        </span>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="columns-1 sm:columns-2 lg:columns-3 gap-6">
        <div v-for="i in 6" :key="i" class="h-64 bg-gray-200 dark:bg-gray-800 animate-pulse mb-6 rounded-xl"></div>
      </div>

      <!-- Photos (Excluding the bio avatar) -->
      <UniformPhotoGrid 
        v-else 
        :images="galleryImages" 
        @select="openLightbox" 
      />
    </section>

    <!-- Lightbox Modal -->
    <LightboxModal 
      :images="galleryImages" 
      v-model="selectedImageIdx" 
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { fetchSiteData } from '../api'
import UniformPhotoGrid from '../components/UniformPhotoGrid.vue'
import LightboxModal from '../components/LightboxModal.vue'

const images = ref<string[]>([])
const loading = ref(true)
const selectedImageIdx = ref<number | null>(null)

// Exclude avatar photo from general grid
const galleryImages = computed(() => {
  return images.value.filter(img => img !== 'home_9df4621f.jpg')
})

onMounted(async () => {
  const data = await fetchSiteData()
  if (data && data.home) {
    images.value = data.home.hero_images || []
  }
  loading.value = false
})

function openLightbox(index: number) {
  selectedImageIdx.value = index
}
</script>
