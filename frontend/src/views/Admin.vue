<template>
  <!-- Unauthorized / Browser Access Barrier Screen (Защита: вход только через Telegram) -->
  <div v-if="!isAuthorized && !loading" class="min-h-screen flex items-center justify-center p-6 select-none">
    <div class="max-w-sm w-full glass-tile rounded-[28px] p-8 text-center space-y-6 shadow-2xl">
      <div class="w-16 h-16 rounded-2xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-600 dark:text-cyan-400 flex items-center justify-center mx-auto text-2xl shadow-inner">
        <AppIcon name="close" :size="26" />
      </div>

      <div class="space-y-2">
        <h1 class="text-xl font-black uppercase tracking-tight text-gray-900 dark:text-white">
          Доступ закрыт
        </h1>
        <p class="text-xs text-slate-600 dark:text-slate-300 font-semibold leading-relaxed">
          Панель управления защищена криптографической подписью Telegram и доступна исключительно внутри официального Telegram Mini App фотографа.
        </p>
      </div>

      <div class="space-y-3 pt-2">
        <a 
          href="https://t.me/lesnikovfoto_bot" 
          target="_blank"
          class="w-full py-3.5 bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500 text-white font-black text-xs uppercase tracking-widest rounded-2xl shadow-lg flex items-center justify-center gap-2 active:scale-95 transition-all"
        >
          <span>Открыть бота в Telegram</span>
          <span>→</span>
        </a>

        <router-link 
          to="/"
          class="w-full py-3 bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/20 text-gray-900 dark:text-white font-black text-xs uppercase tracking-wider rounded-2xl border border-black/10 dark:border-white/15 block active:scale-95 transition-all"
        >
          Вернуться на сайт
        </router-link>
      </div>
    </div>
  </div>

  <!-- Authorized TMA Admin Screen (Только для верифицированного администратора) -->
  <div v-else class="min-h-screen bg-slate-950 text-slate-100 font-sans pb-24 select-none">
    <!-- Top Header -->
    <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-4 py-3.5 flex items-center justify-between shadow-sm">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center font-bold text-xs text-white shadow-inner">
          {{ userProfile.first_name ? userProfile.first_name[0] : 'В' }}
        </div>
        <div>
          <h1 class="text-sm font-bold leading-tight">
            {{ userProfile.first_name || 'Владимир' }} (Админ)
          </h1>
          <p class="text-[10px] text-emerald-400 font-medium flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            TMA Connected
          </p>
        </div>
      </div>

      <button 
        @click="refreshData"
        class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors text-xs font-semibold"
      >
        🔄 Обновить
      </button>
    </header>

    <!-- Navigation Sub-tabs (Photos vs Prices) -->
    <div class="p-4 max-w-lg mx-auto">
      <div class="grid grid-cols-2 gap-2 bg-slate-900/80 p-1.5 rounded-2xl border border-slate-800/80 shadow-inner">
        <button
          @click="activeSection = 'photos'; triggerHaptic('selection')"
          class="py-2.5 rounded-xl font-bold text-xs uppercase tracking-wider transition-all"
          :class="activeSection === 'photos' ? 'bg-cyan-600 text-white shadow-md' : 'text-slate-400 hover:text-white'"
        >
          📸 Фотографии
        </button>
        <button
          @click="activeSection = 'prices'; triggerHaptic('selection')"
          class="py-2.5 rounded-xl font-bold text-xs uppercase tracking-wider transition-all"
          :class="activeSection === 'prices' ? 'bg-cyan-600 text-white shadow-md' : 'text-slate-400 hover:text-white'"
        >
          💰 Цены и тарифы
        </button>
      </div>
    </div>

    <!-- MAIN BODY -->
    <main class="max-w-lg mx-auto px-4 space-y-6">
      <!-- Loading State -->
      <div v-if="loading" class="text-center py-20 text-slate-500 animate-pulse text-sm">
        Загрузка данных панели...
      </div>

      <!-- SECTION: PHOTOS -->
      <div v-else-if="activeSection === 'photos'" class="space-y-4">
        <!-- Category Selector -->
        <div class="space-y-1.5">
          <label class="text-[11px] font-bold uppercase tracking-wider text-slate-400">
            Выберите раздел сайта:
          </label>
          <select 
            v-model="selectedCategoryKey"
            @change="triggerHaptic('selection')"
            class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3.5 py-2.5 text-sm font-semibold focus:outline-none focus:border-cyan-500 transition-colors"
          >
            <option value="home:hero">Главная — Общая галерея ({{ (siteData.home?.hero_images || []).length }} фото)</option>
            <optgroup label="Выпускные альбомы">
              <option value="albums:kindergarten">Детский сад ({{ (siteData.albums?.kindergarten?.images || []).length }} фото)</option>
              <option value="albums:grade_4">4 класс ({{ (siteData.albums?.grade_4?.images || []).length }} фото)</option>
              <option value="albums:grade_11">9 и 11 класс ({{ (siteData.albums?.grade_11?.images || []).length }} фото)</option>
            </optgroup>
            <optgroup label="Фотосессии">
              <option value="photoshoots:wedding">Свадебная ({{ (siteData.photoshoots?.wedding?.images || []).length }} фото)</option>
              <option value="photoshoots:family">Семейная ({{ (siteData.photoshoots?.family?.images || []).length }} фото)</option>
              <option value="photoshoots:individual">Индивидуальная ({{ (siteData.photoshoots?.individual?.images || []).length }} фото)</option>
              <option value="photoshoots:maternity">В ожидании ({{ (siteData.photoshoots?.maternity?.images || []).length }} фото)</option>
              <option value="photoshoots:reportage">Репортаж ({{ (siteData.photoshoots?.reportage?.images || []).length }} фото)</option>
            </optgroup>
          </select>
        </div>

        <!-- Add Photo Button -->
        <div class="relative">
          <input 
            type="file" 
            accept="image/*" 
            ref="fileInput" 
            class="hidden" 
            @change="handleFileUpload"
          />
          <button 
            @click="triggerFileInput"
            :disabled="uploading"
            class="w-full py-3 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 active:scale-[0.99] text-white font-bold text-xs uppercase tracking-wider rounded-xl shadow-lg flex items-center justify-center gap-2 transition-all disabled:opacity-50"
          >
            <span v-if="uploading" class="animate-spin">⏳</span>
            <span v-else>➕</span>
            <span>{{ uploading ? 'Загружаем фото...' : 'Загрузить новое фото' }}</span>
          </button>
        </div>

        <!-- Photo List for Current Category -->
        <div class="space-y-2.5">
          <div 
            v-for="(img, idx) in currentCategoryImages" 
            :key="img + idx"
            class="bg-slate-900/90 border border-slate-800 rounded-2xl p-2.5 flex items-center justify-between gap-3 shadow-sm hover:border-slate-700 transition-colors"
          >
            <!-- Thumbnail with Rotation Cache Buster -->
            <div class="relative w-16 h-14 shrink-0 rounded-lg overflow-hidden bg-slate-800 border border-slate-700 flex items-center justify-center">
              <img 
                :src="'/uploads/thumbs/' + img + '?t=' + (cacheBusters[img] || globalCacheBuster)" 
                @error="(e) => (e.target as HTMLImageElement).src = '/uploads/' + img + '?t=' + (cacheBusters[img] || globalCacheBuster)"
                class="w-full h-full object-cover" 
              />
              <span class="absolute bottom-0 left-0 bg-black/70 px-1 py-0.5 text-[9px] font-mono text-white/80 rounded-tr">
                #{{ idx + 1 }}
              </span>
            </div>

            <!-- Image Info -->
            <div class="flex-1 min-w-0">
              <p class="text-xs font-mono text-slate-300 truncate">
                {{ img }}
              </p>
              <p class="text-[10px] text-slate-500">
                Позиция: {{ idx + 1 }} из {{ currentCategoryImages.length }}
              </p>
            </div>

            <!-- Action Controls (Rotate, Reorder, Delete) -->
            <div class="flex items-center gap-1">
              <!-- Rotate Left (CCW 90) -->
              <button 
                @click="rotateImage(img, -90)"
                title="Повернуть против часовой (-90°)"
                class="w-8 h-8 rounded-lg bg-slate-800 active:bg-cyan-700 text-cyan-400 font-bold text-sm flex items-center justify-center hover:bg-slate-700 transition-all"
              >
                ⟲
              </button>

              <!-- Rotate Right (CW 90) -->
              <button 
                @click="rotateImage(img, 90)"
                title="Повернуть по часовой (+90°)"
                class="w-8 h-8 rounded-lg bg-slate-800 active:bg-cyan-700 text-cyan-400 font-bold text-sm flex items-center justify-center hover:bg-slate-700 transition-all"
              >
                ⟳
              </button>

              <!-- Move Up -->
              <button 
                @click="reorderImage(img, 'up')" 
                :disabled="idx === 0"
                class="w-8 h-8 rounded-lg bg-slate-800 active:bg-slate-700 disabled:opacity-20 text-slate-300 font-bold text-xs flex items-center justify-center hover:bg-slate-700 transition-all"
              >
                ↑
              </button>

              <!-- Move Down -->
              <button 
                @click="reorderImage(img, 'down')" 
                :disabled="idx === currentCategoryImages.length - 1"
                class="w-8 h-8 rounded-lg bg-slate-800 active:bg-slate-700 disabled:opacity-20 text-slate-300 font-bold text-xs flex items-center justify-center hover:bg-slate-700 transition-all"
              >
                ↓
              </button>

              <!-- Delete -->
              <button 
                @click="deleteImage(img)"
                class="w-8 h-8 rounded-lg bg-rose-950/40 active:bg-rose-900/80 text-rose-400 font-bold text-xs flex items-center justify-center hover:bg-rose-900/60 transition-all border border-rose-900/40"
              >
                🗑
              </button>
            </div>
          </div>

          <div v-if="currentCategoryImages.length === 0" class="text-center py-10 text-slate-500 text-xs">
            В этом разделе пока нет фотографий. Нажмите «Загрузить новое фото» выше.
          </div>
        </div>
      </div>

      <!-- SECTION: PRICES -->
      <div v-else-if="activeSection === 'prices'" class="space-y-5">
        <!-- Photoshoot Hourly Rate Editor -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 space-y-3">
          <div class="flex items-center justify-between">
            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-300">
              📸 Почасовая ставка фотосессий
            </h3>
            <span class="text-[10px] text-slate-500">Все типы съемок</span>
          </div>

          <div class="space-y-2">
            <div 
              v-for="(shoot, sKey) in siteData.photoshoots" 
              :key="sKey"
              class="flex items-center justify-between gap-3 text-xs bg-slate-950 p-2.5 rounded-xl border border-slate-800/80"
            >
              <span class="font-medium text-slate-300">{{ shoot.title }}</span>
              <div class="flex items-center gap-1.5">
                <input 
                  type="text" 
                  v-model="shoot.price"
                  class="w-28 bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1 text-right text-xs font-bold text-cyan-400 focus:outline-none focus:border-cyan-500"
                />
                <button 
                  @click="saveShootPrice(sKey as string, shoot.price)"
                  class="px-2.5 py-1 bg-cyan-600 hover:bg-cyan-500 rounded-lg text-white font-bold text-[11px]"
                >
                  ОК
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Albums Models & Options Editor -->
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="text-xs font-bold uppercase tracking-wider text-slate-300">
              🎓 Модели выпускных альбомов и цены
            </h3>
            <span class="text-[10px] text-slate-500">По разворотам</span>
          </div>

          <!-- Category Selector -->
          <div class="flex gap-1.5 p-1 bg-slate-950 rounded-xl border border-slate-800">
            <button 
              v-for="cat in ['kindergarten', 'grade_4', 'grade_11']" 
              :key="cat"
              @click="selectedAlbumAdminCat = cat; triggerHaptic('selection')"
              class="flex-1 py-1.5 rounded-lg text-[11px] font-bold uppercase tracking-wider transition-all"
              :class="selectedAlbumAdminCat === cat ? 'bg-cyan-600 text-white shadow' : 'text-slate-400 hover:text-white'"
            >
              {{ cat === 'kindergarten' ? 'Детсад' : (cat === 'grade_4' ? '4 класс' : '9-11 класс') }}
            </button>
          </div>

          <!-- Models List for Selected Category -->
          <div class="space-y-3">
            <div 
              v-for="model in (siteData.albums?.[selectedAlbumAdminCat]?.models || [])" 
              :key="model.id"
              class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2.5"
            >
              <div class="flex items-center justify-between gap-2">
                <span class="text-xs font-bold text-white truncate">{{ model.name }}</span>
                <span class="text-[10px] px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-400 font-mono font-bold">{{ model.num }}</span>
              </div>

              <!-- Base Price Input -->
              <div class="flex items-center justify-between gap-2 text-xs">
                <span class="text-[11px] text-slate-400">Базовая цена (₽):</span>
                <input 
                  type="number" 
                  v-model.number="model.price"
                  class="w-24 bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1 text-right text-xs font-bold text-cyan-400 focus:outline-none focus:border-cyan-500"
                />
              </div>

              <!-- Spread Options Inputs -->
              <div v-if="model.spread_options && model.spread_options.length" class="space-y-1.5 pt-1.5 border-t border-slate-900">
                <div class="text-[10px] text-slate-500 font-semibold uppercase">Цены по разворотам (₽):</div>
                <div class="grid grid-cols-3 gap-1.5">
                  <div v-for="opt in model.spread_options" :key="opt.spreads" class="bg-slate-900 p-1.5 rounded-lg border border-slate-800 text-center">
                    <div class="text-[10px] text-slate-400">{{ opt.spreads }} разв.</div>
                    <input 
                      type="number" 
                      v-model.number="opt.price"
                      class="w-full bg-transparent text-center text-[11px] font-bold text-emerald-400 focus:outline-none"
                    />
                  </div>
                </div>
              </div>
            </div>

            <button 
              @click="saveAlbumModels(selectedAlbumAdminCat)"
              class="w-full py-3 bg-emerald-600 hover:bg-emerald-500 active:scale-98 text-white text-xs font-bold uppercase tracking-wider rounded-xl shadow-lg transition-all flex items-center justify-center gap-2"
            >
              <span>💾</span>
              <span>Сохранить изменения альбомов</span>
            </button>
          </div>
        </div>
      </div>
    </main>

    <!-- Toast Notification -->
    <div 
      v-if="toastMsg" 
      class="fixed bottom-6 left-1/2 -translate-x-1/2 bg-slate-800 border border-slate-700 text-white px-4 py-2.5 rounded-2xl text-xs font-bold shadow-2xl z-50 flex items-center gap-2 animate-bounce"
    >
      <span>{{ toastMsg }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, reactive } from 'vue'
import AppIcon from '../components/AppIcon.vue'

const activeSection = ref<'photos' | 'prices'>('photos')
const selectedCategoryKey = ref('home:hero')
const selectedAlbumAdminCat = ref('kindergarten')
const loading = ref(true)
const isAuthorized = ref(false)
const uploading = ref(false)
const toastMsg = ref('')
const fileInput = ref<HTMLInputElement | null>(null)
const cacheBusters = reactive<Record<string, number>>({})
const globalCacheBuster = ref(Date.now())

const siteData = ref<any>({
  home: { hero_images: [] },
  albums: {},
  photoshoots: {}
})

const userProfile = ref<any>({
  id: 'admin',
  first_name: 'Владимир'
})

function getTelegramInitData(): string {
  if (typeof window !== 'undefined' && (window as any).Telegram?.WebApp) {
    return (window as any).Telegram.WebApp.initData || ''
  }
  return ''
}

function triggerHaptic(type: 'selection' | 'impact' | 'notification', style: any = 'light') {
  try {
    const tg = (window as any).Telegram?.WebApp
    if (!tg?.HapticFeedback) return
    if (type === 'selection') tg.HapticFeedback.selectionChanged()
    else if (type === 'impact') tg.HapticFeedback.impactOccurred(style)
    else if (type === 'notification') tg.HapticFeedback.notificationOccurred(style)
  } catch (e) {
    // Ignore outside Telegram
  }
}

function showToast(msg: string) {
  toastMsg.value = msg
  setTimeout(() => {
    toastMsg.value = ''
  }, 2500)
}

const currentCategoryImages = computed(() => {
  const [type, id] = selectedCategoryKey.value.split(':')
  if (type === 'home') {
    return siteData.value.home?.hero_images || []
  } else if (type === 'albums') {
    return siteData.value.albums?.[id]?.images || []
  } else if (type === 'photoshoots') {
    return siteData.value.photoshoots?.[id]?.images || []
  }
  return []
})

async function refreshData() {
  const initData = getTelegramInitData()
  if (!initData) {
    isAuthorized.value = false
    loading.value = false
    return
  }

  triggerHaptic('impact', 'medium')
  loading.value = true
  try {
    const res = await fetch('/api/admin/data', {
      headers: {
        'x-telegram-init-data': initData
      }
    })
    if (res.ok) {
      siteData.value = await res.json()
      globalCacheBuster.value = Date.now()
      isAuthorized.value = true
    } else {
      isAuthorized.value = false
    }
  } catch (e) {
    console.error(e)
    isAuthorized.value = false
  } finally {
    loading.value = false
  }
}

function triggerFileInput() {
  triggerHaptic('impact', 'light')
  fileInput.value?.click()
}

async function handleFileUpload(e: Event) {
  const target = e.target as HTMLInputElement
  if (!target.files || !target.files[0]) return

  const file = target.files[0]
  const [type, id] = selectedCategoryKey.value.split(':')

  const formData = new FormData()
  formData.append('category_type', type)
  formData.append('category_id', id)
  formData.append('file', file)

  uploading.value = true
  triggerHaptic('impact', 'medium')

  try {
    const res = await fetch('/api/admin/photos/upload', {
      method: 'POST',
      headers: {
        'x-telegram-init-data': getTelegramInitData()
      },
      body: formData
    })

    if (res.ok) {
      const data = await res.json()
      siteData.value = data.data
      globalCacheBuster.value = Date.now()
      triggerHaptic('notification', 'success')
      showToast('✅ Фото успешно загружено!')
    } else {
      triggerHaptic('notification', 'error')
      showToast('❌ Ошибка загрузки')
    }
  } catch (err) {
    triggerHaptic('notification', 'error')
    showToast('❌ Ошибка сервера')
  } finally {
    uploading.value = false
    if (fileInput.value) fileInput.value.value = ''
  }
}

async function rotateImage(filename: string, degrees: number) {
  triggerHaptic('impact', 'medium')
  const [type, id] = selectedCategoryKey.value.split(':')

  try {
    const res = await fetch('/api/admin/photos/rotate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-telegram-init-data': getTelegramInitData()
      },
      body: JSON.stringify({
        category_type: type,
        category_id: id,
        filename,
        degrees
      })
    })

    if (res.ok) {
      cacheBusters[filename] = Date.now()
      triggerHaptic('notification', 'success')
      showToast(degrees > 0 ? '🔄 Повернуто по часовой (+90°)' : '🔄 Повернуто против часовой (-90°)')
    } else {
      triggerHaptic('notification', 'error')
      showToast('❌ Ошибка поворота')
    }
  } catch (e) {
    triggerHaptic('notification', 'error')
    showToast('❌ Ошибка сети')
  }
}

async function reorderImage(filename: string, direction: 'up' | 'down') {
  triggerHaptic('impact', 'light')
  const [type, id] = selectedCategoryKey.value.split(':')

  try {
    const res = await fetch('/api/admin/photos/reorder', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-telegram-init-data': getTelegramInitData()
      },
      body: JSON.stringify({
        category_type: type,
        category_id: id,
        filename,
        direction
      })
    })

    if (res.ok) {
      const data = await res.json()
      siteData.value = data.data
      triggerHaptic('selection')
    }
  } catch (e) {
    console.error(e)
  }
}

async function deleteImage(filename: string) {
  if (!confirm('Удалить эту фотографию?')) return

  triggerHaptic('impact', 'heavy')
  const [type, id] = selectedCategoryKey.value.split(':')

  try {
    const res = await fetch('/api/admin/photos/delete', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-telegram-init-data': getTelegramInitData()
      },
      body: JSON.stringify({
        category_type: type,
        category_id: id,
        filename
      })
    })

    if (res.ok) {
      const data = await res.json()
      siteData.value = data.data
      triggerHaptic('notification', 'success')
      showToast('🗑 Фото удалено')
    }
  } catch (e) {
    console.error(e)
  }
}

async function saveShootPrice(category_id: string, price: string) {
  triggerHaptic('impact', 'medium')
  try {
    const res = await fetch('/api/admin/prices', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-telegram-init-data': getTelegramInitData()
      },
      body: JSON.stringify({
        category_type: 'photoshoots',
        category_id,
        price
      })
    })

    if (res.ok) {
      triggerHaptic('notification', 'success')
      showToast('💾 Цена обновлена!')
    }
  } catch (e) {
    console.error(e)
  }
}

async function saveAlbumModels(catId: string) {
  triggerHaptic('impact', 'medium')
  try {
    const models = siteData.value.albums?.[catId]?.models || []
    const res = await fetch('/api/admin/prices', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-telegram-init-data': getTelegramInitData()
      },
      body: JSON.stringify({
        category_type: 'albums',
        category_id: catId,
        models: models
      })
    })

    if (res.ok) {
      triggerHaptic('notification', 'success')
      showToast('✅ Модели и цены сохранены!')
    } else {
      triggerHaptic('notification', 'error')
      showToast('❌ Ошибка при сохранении')
    }
  } catch (e) {
    console.error(e)
    showToast('❌ Ошибка сети')
  }
}

onMounted(async () => {
  const initData = getTelegramInitData()
  if (!initData) {
    isAuthorized.value = false
    loading.value = false
    return
  }

  if (typeof window !== 'undefined' && (window as any).Telegram?.WebApp) {
    const tg = (window as any).Telegram.WebApp
    tg.ready()
    tg.expand()
    if (tg.initDataUnsafe?.user) {
      userProfile.value = tg.initDataUnsafe.user
    }
  }
  await refreshData()
})
</script>
