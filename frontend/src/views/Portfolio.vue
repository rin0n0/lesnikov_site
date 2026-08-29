<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 sm:py-8">
    <!-- Section Title -->
    <div class="text-center max-w-2xl mx-auto mb-8 sm:mb-12">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold liquid-glass mb-4 text-gray-700 dark:text-gray-300">
        <AppIcon name="crystal" :size="14" />
        <span>Интерактивный каталог</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black tracking-tight mb-3">
        Портфолио & Цены
      </h1>
      <p class="text-gray-500 dark:text-gray-400 text-xs sm:text-sm">
        Переключайте направления, чтобы мгновенно увидеть актуальные тарифы и примеры фото
      </p>
    </div>

    <!-- 3D Liquid Crystal Category Tabs Bar -->
    <div class="sticky top-20 sm:top-24 z-40 py-3 mb-10 -mx-4 px-4 sm:mx-0 sm:px-0">
      <div class="liquid-glass rounded-2xl sm:rounded-full p-1.5 sm:p-2 max-w-4xl mx-auto flex items-center gap-1.5 sm:gap-2 overflow-x-auto no-scrollbar shadow-2xl">
        <button
          v-for="tab in categories"
          :key="tab.id"
          @click="selectCategory(tab.id)"
          class="inline-flex items-center gap-2 whitespace-nowrap px-4 py-2 sm:py-2.5 rounded-xl sm:rounded-full text-xs sm:text-sm font-bold transition-all duration-300 shrink-0"
          :class="activeTab === tab.id 
            ? 'liquid-glass-active scale-[1.03] shadow-md' 
            : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:bg-white/40 dark:hover:bg-white/10'"
        >
          <CategoryIcon :name="tab.id" :size="15" />
          <span>{{ tab.label }}</span>
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="py-20 text-center text-gray-400 font-mono text-sm">
      Загрузка хрустальной галереи...
    </div>

    <!-- Content for Active Category -->
    <div v-else-if="currentCategoryData" class="space-y-10">
      <!-- Category Header Card (Floating Crystal Block) -->
      <div class="liquid-glass rounded-3xl p-6 sm:p-8 flex flex-col sm:flex-row sm:items-center justify-between gap-6 shadow-xl">
        <div>
          <span class="text-xs uppercase tracking-widest text-gray-400 font-mono">
            {{ currentCategoryData.group }}
          </span>
          <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight mt-1 text-gray-900 dark:text-white">
            {{ currentCategoryData.title }}
          </h2>
        </div>
        
        <router-link 
          to="/contacts"
          class="inline-flex items-center justify-center gap-2 bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-6 py-3 rounded-2xl text-xs sm:text-sm font-bold uppercase tracking-wider hover:opacity-90 hover:scale-105 active:scale-95 transition-all shadow-md self-start sm:self-auto"
        >
          <span>Забронировать дату</span>
          <span>→</span>
        </router-link>
      </div>

      <!-- Pricing Block (Packages or Hourly) -->
      <PriceList 
        :items="currentCategoryData.items" 
        :singlePrice="currentCategoryData.price" 
      />

      <!-- Photo Gallery (3 Big Photos per row on desktop) -->
      <div>
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-gray-900 dark:bg-white"></span>
            <h3 class="text-xs sm:text-sm font-bold tracking-widest uppercase text-gray-500 dark:text-gray-400">
              Примеры съемок ({{ currentCategoryData.images.length }})
            </h3>
          </div>
          <span class="text-xs text-gray-400 font-mono">
            Кликните для полного размера
          </span>
        </div>

        <UniformPhotoGrid 
          :images="currentCategoryData.images" 
          @select="openLightbox" 
        />
      </div>
    </div>

    <!-- Lightbox Modal -->
    <LightboxModal 
      v-if="currentCategoryData"
      :images="currentCategoryData.images" 
      v-model="selectedImageIdx" 
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { fetchSiteData } from '../api'
import UniformPhotoGrid from '../components/UniformPhotoGrid.vue'
import PriceList from '../components/PriceList.vue'
import LightboxModal from '../components/LightboxModal.vue'
import CategoryIcon from '../components/CategoryIcon.vue'
import AppIcon from '../components/AppIcon.vue'

const route = useRoute()
const router = useRouter()

const siteData = ref<any>(null)
const loading = ref(true)
const activeTab = ref('kindergarten')
const selectedImageIdx = ref<number | null>(null)

const categories = [
  { id: 'kindergarten', label: 'Детский сад', group: 'Выпускные альбомы' },
  { id: 'grade_4', label: '4 класс', group: 'Школьные альбомы' },
  { id: 'grade_11', label: '9 и 11 класс', group: 'Выпускные альбомы' },
  { id: 'wedding', label: 'Свадебная', group: 'Фотосессии' },
  { id: 'family', label: 'Семейная', group: 'Фотосессии' },
  { id: 'individual', label: 'Индивидуальная', group: 'Фотосессии' },
  { id: 'maternity', label: 'В ожидании', group: 'Фотосессии' },
  { id: 'reportage', label: 'Репортажная', group: 'Фотосессии' }
]

const currentCategoryData = computed(() => {
  if (!siteData.value) return null
  
  const currentCat = categories.find(c => c.id === activeTab.value)
  if (!currentCat) return null

  // Check albums
  if (siteData.value.albums && siteData.value.albums[activeTab.value]) {
    const item = siteData.value.albums[activeTab.value]
    return {
      title: item.title,
      group: currentCat.group,
      items: item.items || [],
      images: item.images || []
    }
  }

  // Check photoshoots
  if (siteData.value.photoshoots && siteData.value.photoshoots[activeTab.value]) {
    const item = siteData.value.photoshoots[activeTab.value]
    return {
      title: item.title,
      group: currentCat.group,
      price: item.price,
      images: item.images || []
    }
  }

  return null
})

function selectCategory(id: string) {
  activeTab.value = id
  router.replace({ query: { tab: id } })
}

function openLightbox(index: number) {
  selectedImageIdx.value = index
}

onMounted(async () => {
  if (route.query.tab && typeof route.query.tab === 'string') {
    activeTab.value = route.query.tab
  }
  
  siteData.value = await fetchSiteData()
  loading.value = false
})

watch(() => route.query.tab, (newTab) => {
  if (newTab && typeof newTab === 'string') {
    activeTab.value = newTab
  }
})
</script>
