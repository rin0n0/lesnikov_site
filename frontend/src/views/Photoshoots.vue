<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
    <!-- Header -->
    <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-10">
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight mb-2 uppercase">
        Фотосессии
      </h1>
      <p class="text-xs sm:text-sm font-semibold text-slate-500 dark:text-slate-400 max-w-xl mx-auto">
        Свадебная, семейная, детская, индивидуальная и репортажная фотография в Санкт-Петербурге и Ленинградской области
      </p>
    </div>

    <!-- Category Tabs (2-Column Chess on Mobile 2 + 2 + 1, Linear on Desktop) -->
    <div class="mb-10">
      <div class="grid grid-cols-2 md:flex md:flex-row md:flex-nowrap md:w-fit justify-center gap-2 md:gap-2.5 max-w-md md:max-w-none mx-auto p-1.5 rounded-2xl liquid-card">
        <button
          v-for="(tab, idx) in shootTabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          class="inline-flex items-center justify-center gap-2 px-3 sm:px-4 md:px-5 py-2.5 sm:py-3 rounded-xl text-[11px] sm:text-xs md:text-sm font-bold uppercase tracking-wider transition-all duration-200 whitespace-nowrap"
          :class="[
            activeTab === tab.id 
              ? 'liquid-btn-active shadow-md' 
              : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white',
            idx === 4 ? 'col-span-2 md:col-span-1' : ''
          ]"
        >
          <CategoryIcon :name="tab.id" :size="16" />
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
      <!-- Title -->
      <div class="border-b border-gray-200/60 dark:border-gray-800/60 pb-4">
        <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-gray-900 dark:text-white">
          {{ currentShootData.title }}
        </h2>
      </div>

      <!-- Pricing Block -->
      <PriceList 
        :singlePrice="currentShootData.price" 
        :categoryTitle="currentShootData.title"
      />

      <!-- Photo Series in Natural Aspect Ratio -->
      <div>

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
