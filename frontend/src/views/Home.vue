<template>
  <div>
    <!-- Elegant Centered Business Card Bio (Визитка) -->
    <section class="px-4 pt-6 pb-12 md:pt-10 md:pb-16 max-w-4xl mx-auto text-center">
      <div class="inline-flex flex-col items-center">
        <!-- Vladimir's B&W Portrait Avatar -->
        <div class="w-32 h-32 sm:w-40 sm:h-40 rounded-full overflow-hidden border-2 border-slate-900/10 dark:border-white/20 shadow-xl mb-6 bg-slate-200 dark:bg-slate-800">
          <img 
            :src="'/uploads/home_9df4621f.jpg'" 
            alt="Владимир Лесников"
            class="w-full h-full object-cover grayscale contrast-110"
          />
        </div>

        <!-- Name & Bio -->
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight text-gray-900 dark:text-white uppercase mb-2">
          Владимир Лесников
        </h1>
        <p class="text-xs sm:text-sm font-bold uppercase tracking-widest text-slate-400 mb-8">
          Профессиональный фотограф
        </p>

        <!-- Navigation Buttons to 2 key worlds -->
        <div class="flex flex-wrap justify-center gap-3 sm:gap-4">
          <router-link 
            to="/albums" 
            class="bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-6 py-3 rounded-xl font-bold text-xs uppercase tracking-wider shadow-sm hover:opacity-90 transition-all"
          >
            Выпускные альбомы
          </router-link>
          <router-link 
            to="/photoshoots" 
            class="px-6 py-3 rounded-xl font-bold text-xs uppercase tracking-wider border border-gray-300 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
          >
            Фотосессии
          </router-link>
        </div>
      </div>
    </section>

    <!-- Straight Rectangular Natural Photo Grid -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
      <!-- Loading State -->
      <div v-if="loading" class="columns-1 sm:columns-2 lg:columns-3 gap-6">
        <div v-for="i in 6" :key="i" class="h-64 bg-gray-200 dark:bg-gray-800 animate-pulse mb-6"></div>
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
