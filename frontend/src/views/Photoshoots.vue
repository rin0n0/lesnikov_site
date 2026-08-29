<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
    <!-- Header -->
    <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-10">
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight mb-2 uppercase">
        Фотосессии
      </h1>
    </div>

    <!-- Category Tabs -->
    <div class="flex justify-center mb-10">
      <div class="inline-flex p-1.5 rounded-2xl liquid-card gap-1 sm:gap-2 max-w-full overflow-x-auto no-scrollbar">
        <button
          v-for="tab in shootTabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          class="inline-flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold uppercase tracking-wider transition-all duration-200 shrink-0"
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
      Загрузка галереи...
    </div>

    <!-- Active Photoshoot Content -->
    <div v-else-if="currentShootData" class="space-y-10">
      <!-- Title (Clean without duplicate buttons) -->
      <div class="border-b border-gray-200 dark:border-gray-800 pb-4">
        <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-gray-900 dark:text-white">
          {{ currentShootData.title }}
        </h2>
      </div>

      <!-- Pricing Block (Single clean fixed rate) -->
      <PriceList :singlePrice="currentShootData.price" />

      <!-- Photo Series in Natural Aspect Ratio -->
      <div>
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-sm font-bold tracking-widest uppercase text-gray-500 dark:text-gray-400">
            Примеры фотографий ({{ currentShootData.images.length }})
          </h3>
          <span class="text-xs text-gray-400">
            Кликните для полного размера
          </span>
        </div>

        <UniformPhotoGrid 
          :images="currentShootData.images" 
          @select="openLightbox" 
        />
      </div>
    </div>

    <!-- Lightbox Modal -->
    <LightboxModal 
      v-if="currentShootData"
      :images="currentShootData.images" 
      v-model="selectedImageIdx" 
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { fetchSiteData } from '../api'
import UniformPhotoGrid from '../components/UniformPhotoGrid.vue'
import PriceList from '../components/PriceList.vue'
import LightboxModal from '../components/LightboxModal.vue'
import CategoryIcon from '../components/CategoryIcon.vue'

const siteData = ref<any>(null)
const loading = ref(true)
const activeTab = ref('wedding')
const selectedImageIdx = ref<number | null>(null)

const shootTabs = [
  { id: 'wedding', label: 'Свадебная' },
  { id: 'family', label: 'Семейная' },
  { id: 'individual', label: 'Индивидуальная' },
  { id: 'maternity', label: 'В ожидании' },
  { id: 'reportage', label: 'Репортаж' }
]

const currentShootData = computed(() => {
  if (!siteData.value || !siteData.value.photoshoots) return null
  return siteData.value.photoshoots[activeTab.value] || null
})

function openLightbox(index: number) {
  selectedImageIdx.value = index
}

onMounted(async () => {
  siteData.value = await fetchSiteData()
  loading.value = false
})
</script>
