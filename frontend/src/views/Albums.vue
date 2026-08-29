<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
    <!-- Header -->
    <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-10">
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight mb-2 uppercase">
        Выпускные альбомы
      </h1>
    </div>

    <!-- Category Tabs (3 clean pills) -->
    <div class="flex justify-center mb-10">
      <div class="inline-flex p-1.5 rounded-2xl liquid-card gap-1 sm:gap-2 max-w-full overflow-x-auto no-scrollbar">
        <button
          v-for="tab in albumTabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold uppercase tracking-wider transition-all duration-200 shrink-0"
          :class="activeTab === tab.id 
            ? 'liquid-btn-active' 
            : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white'"
        >
          <CategoryIcon :name="tab.id" :size="15" />
          <span>{{ tab.label }}</span>
        </button>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="py-20 text-center text-gray-400">
      Загрузка фотографий...
    </div>

    <!-- Active Album Photo Set -->
    <div v-else-if="currentAlbumData" class="space-y-6">
      <!-- Title -->
      <div class="border-b border-gray-200 dark:border-gray-800 pb-4">
        <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-gray-900 dark:text-white">
          {{ albumTitles[activeTab] || currentAlbumData.title }}
        </h2>
      </div>

      <!-- Photo Grid (Natural aspect ratio, no crop, no sideways distortion) -->
      <UniformPhotoGrid 
        :images="currentAlbumData.images" 
        @select="openLightbox" 
      />
    </div>

    <!-- Lightbox Modal -->
    <LightboxModal 
      v-if="currentAlbumData"
      :images="currentAlbumData.images" 
      v-model="selectedImageIdx" 
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { fetchSiteData } from '../api'
import UniformPhotoGrid from '../components/UniformPhotoGrid.vue'
import LightboxModal from '../components/LightboxModal.vue'
import CategoryIcon from '../components/CategoryIcon.vue'

const siteData = ref<any>(null)
const loading = ref(true)
const activeTab = ref('kindergarten')
const selectedImageIdx = ref<number | null>(null)

const albumTabs = [
  { id: 'kindergarten', label: 'Детский сад' },
  { id: 'grade_4', label: '4 класс' },
  { id: 'grade_11', label: '9 и 11 класс' }
]

const albumTitles: Record<string, string> = {
  kindergarten: 'Детский сад',
  grade_4: 'Школьные альбомы 4 класс',
  grade_11: 'Выпускные альбомы 9 и 11 класса'
}

const currentAlbumData = computed(() => {
  if (!siteData.value || !siteData.value.albums) return null
  return siteData.value.albums[activeTab.value] || null
})

function openLightbox(index: number) {
  selectedImageIdx.value = index
}

onMounted(async () => {
  siteData.value = await fetchSiteData()
  loading.value = false
})
</script>
