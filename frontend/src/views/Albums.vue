<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
    <!-- Header -->
    <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-10">
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight mb-2 uppercase">
        Выпускные альбомы
      </h1>
      <p class="text-xs sm:text-sm font-semibold text-slate-500 dark:text-slate-400 max-w-xl mx-auto">
        Премиальная печать, твердые страницы, индивидуальная верстка и фотосессия под ключ в детских садах и школах
      </p>
    </div>

    <!-- Category Tabs (Triangular on Mobile 2 + 1, Linear on Desktop) -->
    <div class="mb-10">
      <div class="grid grid-cols-2 sm:flex sm:justify-center gap-2.5 max-w-xl mx-auto p-1.5 rounded-2xl liquid-card">
        <button
          v-for="(tab, idx) in albumTabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          class="inline-flex items-center justify-center gap-2 px-4 sm:px-6 py-3 rounded-xl text-xs sm:text-sm font-bold uppercase tracking-wider transition-all duration-200"
          :class="[
            activeTab === tab.id 
              ? 'liquid-btn-active' 
              : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white',
            idx === 2 ? 'col-span-2 sm:col-span-1' : ''
          ]"
        >
          <CategoryIcon :name="tab.id" :size="16" />
          <span>{{ tab.label }}</span>
        </button>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="py-20 text-center text-gray-400">
      Загрузка каталога альбомов...
    </div>

    <!-- Active Category Content -->
    <div v-else-if="currentAlbumData" class="space-y-10">
      
      <!-- Section Title & View Toggle -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-gray-200/60 dark:border-gray-800/60 pb-5">
        <div>
          <h2 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-gray-900 dark:text-white">
            {{ albumTitles[activeTab] || currentAlbumData.title }}
          </h2>
          <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">
            {{ currentModels.length }} {{ getDeclension(currentModels.length, ['модель', 'модели', 'моделей']) }} альбомов с вариантами разворотов
          </p>
        </div>

        <!-- Mode Toggle (Каталог vs Фотогалерея) -->
        <div class="inline-flex p-1 rounded-xl liquid-card self-start sm:self-auto">
          <button 
            @click="viewMode = 'models'"
            class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all"
            :class="viewMode === 'models' ? 'bg-slate-900 text-white dark:bg-white dark:text-slate-900 shadow-sm' : 'text-slate-500 hover:text-slate-900 dark:hover:text-white'"
          >
            📋 Модели и цены
          </button>
          <button 
            @click="viewMode = 'gallery'"
            class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all"
            :class="viewMode === 'gallery' ? 'bg-slate-900 text-white dark:bg-white dark:text-slate-900 shadow-sm' : 'text-slate-500 hover:text-slate-900 dark:hover:text-white'"
          >
            🖼️ Все развороты
          </button>
        </div>
      </div>

      <!-- VIEW 1: CATALOG OF ALBUM MODELS -->
      <div v-if="viewMode === 'models'" class="space-y-8">
        <div 
          v-for="model in currentModels" 
          :key="model.id"
          class="liquid-card rounded-3xl p-5 sm:p-7 md:p-8 border border-white/60 dark:border-white/10 shadow-lg hover:shadow-2xl transition-all duration-300"
        >
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8 items-start">
            
            <!-- Left: Model Image Gallery / Preview -->
            <div class="lg:col-span-5 space-y-3">
              <!-- Main Cover Preview with Lightbox Trigger -->
              <div 
                class="relative aspect-[4/3] rounded-2xl overflow-hidden bg-slate-100 dark:bg-slate-800 cursor-pointer group shadow-inner border border-black/5 dark:border-white/5"
                @click="openModelLightbox(model, 0)"
              >
                <img 
                  :src="'/uploads/thumbs/' + (model.cover_image || model.images[0])" 
                  @error="(e) => (e.target as HTMLImageElement).src = '/uploads/' + (model.cover_image || model.images[0])"
                  :alt="model.name"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                  loading="lazy"
                />
                <div class="absolute inset-0 bg-black/0 group-hover:bg-black/25 transition-colors flex items-center justify-center">
                  <span class="opacity-0 group-hover:opacity-100 px-3.5 py-1.5 bg-black/70 backdrop-blur-md text-white text-xs font-bold uppercase tracking-wider rounded-lg transition-opacity">
                    🔍 Посмотреть все развороты
                  </span>
                </div>
                
                <!-- Badge on Top Left -->
                <div class="absolute top-3 left-3 bg-slate-900/80 backdrop-blur-md text-white text-[11px] font-extrabold uppercase tracking-wider px-3 py-1 rounded-lg">
                  {{ model.num || model.badge }}
                </div>
              </div>

              <!-- Thumbnails Row (Mini slider) -->
              <div v-if="model.images && model.images.length > 1" class="flex gap-2 overflow-x-auto pb-1 no-scrollbar">
                <button
                  v-for="(img, imgIdx) in model.images"
                  :key="img"
                  @click="openModelLightbox(model, imgIdx)"
                  class="w-16 h-12 shrink-0 rounded-lg overflow-hidden border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 hover:opacity-100 opacity-75 transition-opacity"
                >
                  <img 
                    :src="'/uploads/thumbs/' + img" 
                    @error="(e) => (e.target as HTMLImageElement).src = '/uploads/' + img"
                    :alt="model.name"
                    class="w-full h-full object-cover"
                    loading="lazy"
                  />
                </button>
              </div>
            </div>

            <!-- Right: Model Details, Pricing & Options -->
            <div class="lg:col-span-7 flex flex-col justify-between h-full space-y-5">
              <div>
                <!-- Specs Badges -->
                <div class="flex flex-wrap items-center gap-2 mb-2.5">
                  <span class="px-2.5 py-1 rounded-md bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 font-bold text-[11px] uppercase tracking-wide">
                    {{ model.format || 'Формат' }}
                  </span>
                  <span class="px-2.5 py-1 rounded-md bg-slate-200/70 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-medium text-[11px]">
                    {{ model.cover || 'Твердая обложка' }}
                  </span>
                </div>

                <!-- Title -->
                <h3 class="text-xl sm:text-2xl font-black text-gray-900 dark:text-white leading-tight">
                  {{ model.name }}
                </h3>

                <!-- Description Text -->
                <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 mt-3 leading-relaxed whitespace-pre-line">
                  {{ getCleanShortDesc(model.description) }}
                </p>

                <!-- Spread Options Pricing Grid (if available) -->
                <div v-if="model.spread_options && model.spread_options.length" class="mt-4 pt-4 border-t border-slate-200/60 dark:border-slate-800/80">
                  <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-2">
                    Варианты разворотов и стоимость за альбом:
                  </div>
                  <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
                    <div 
                      v-for="opt in model.spread_options" 
                      :key="opt.spreads"
                      class="p-2.5 rounded-xl bg-white/70 dark:bg-slate-900/80 border border-slate-200/60 dark:border-slate-800 text-center"
                    >
                      <div class="text-[11px] font-semibold text-slate-500 dark:text-slate-400">
                        {{ opt.spreads }} {{ getDeclension(opt.spreads, ['разворот', 'разворота', 'разворотов']) }}
                      </div>
                      <div class="text-sm font-extrabold text-gray-900 dark:text-white font-mono mt-0.5">
                        {{ formatRub(opt.price) }}
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Features Highlights -->
                <div class="mt-4 flex flex-wrap gap-x-4 gap-y-1.5 text-[11px] text-slate-500 dark:text-slate-400 font-medium">
                  <div class="flex items-center gap-1.5">
                    <span class="text-emerald-500 font-bold">✓</span>
                    <span>2 визита фотографа включены</span>
                  </div>
                  <div class="flex items-center gap-1.5">
                    <span class="text-emerald-500 font-bold">✓</span>
                    <span>Бесплатная досъемка</span>
                  </div>
                  <div class="flex items-center gap-1.5">
                    <span class="text-emerald-500 font-bold">✓</span>
                    <span>Выбор фото родителями онлайн</span>
                  </div>
                </div>
              </div>

              <!-- Bottom Price & CTA Bar -->
              <div class="pt-4 border-t border-slate-200/60 dark:border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <span class="text-[10px] uppercase tracking-wider text-slate-400 font-bold block">Стоимость:</span>
                  <span class="text-2xl sm:text-3xl font-black text-gray-900 dark:text-white font-mono">
                    {{ model.spread_options && model.spread_options.length ? 'от ' + formatRub(model.spread_options[0].price) : formatRub(model.price) }}
                  </span>
                </div>

                <router-link 
                  :to="{ path: '/contacts', query: { subject: model.name } }"
                  class="px-6 py-3 bg-gray-900 text-white dark:bg-white dark:text-gray-900 rounded-xl text-xs font-bold uppercase tracking-wider text-center hover:opacity-90 transition-all shadow-md active:scale-95"
                >
                  Заказать этот альбом
                </router-link>
              </div>

            </div>
          </div>
        </div>
      </div>

      <!-- VIEW 2: FULL PHOTO GRID OF ALL SPREADS -->
      <div v-else-if="viewMode === 'gallery'" class="space-y-6">
        <UniformPhotoGrid 
          :images="currentAlbumData.images" 
          @select="openGalleryLightbox" 
        />
      </div>

    </div>

    <!-- Lightbox Modal -->
    <LightboxModal 
      v-if="lightboxImages.length"
      :images="lightboxImages" 
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
const viewMode = ref<'models' | 'gallery'>('models')
const selectedImageIdx = ref<number | null>(null)
const customLightboxImages = ref<string[]>([])

const albumTabs = [
  { id: 'kindergarten', label: 'Детский сад' },
  { id: 'grade_4', label: '4 класс' },
  { id: 'grade_11', label: '9 и 11 класс' }
]

const albumTitles: Record<string, string> = {
  kindergarten: 'Выпускные альбомы детского сада',
  grade_4: 'Школьные альбомы для 4 класса',
  grade_11: 'Выпускные альбомы для 9 и 11 классов'
}

const currentAlbumData = computed(() => {
  if (!siteData.value || !siteData.value.albums) return null
  return siteData.value.albums[activeTab.value] || null
})

const currentModels = computed(() => {
  if (!currentAlbumData.value) return []
  return currentAlbumData.value.models || []
})

const lightboxImages = computed(() => {
  if (customLightboxImages.value.length > 0) {
    return customLightboxImages.value
  }
  return currentAlbumData.value ? currentAlbumData.value.images : []
})

function openModelLightbox(model: any, index: number) {
  customLightboxImages.value = model.images || []
  selectedImageIdx.value = index
}

function openGalleryLightbox(index: number) {
  customLightboxImages.value = []
  selectedImageIdx.value = index
}

function formatRub(num: number) {
  if (!num) return '0 ₽'
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' ₽'
}

function getDeclension(n: number, titles: [string, string, string]) {
  const cases = [2, 0, 1, 1, 1, 2]
  return titles[(n % 100 > 4 && n % 100 < 20) ? 2 : cases[(n % 10 < 5) ? n % 10 : 5]]
}

function getCleanShortDesc(desc: string) {
  if (!desc) return ''
  // Return description text without the spread price list block to avoid repetition
  const parts = desc.split(/Такой альбом можно выполнить/i)
  if (parts.length > 1) {
    const afterSpreads = parts[1].split(/В фотоальбоме/i)
    if (afterSpreads.length > 1) {
      return (parts[0] + '\nВ фотоальбоме ' + afterSpreads[1]).trim()
    }
  }
  return desc
}

onMounted(async () => {
  siteData.value = await fetchSiteData()
  loading.value = false
})
</script>

