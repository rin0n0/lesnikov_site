<template>
  <div class="space-y-8">
    <!-- Masonry Grid with Progressive Chunk Rendering -->
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 [column-fill:_balance]">
      <div 
        v-for="(img, idx) in visibleImages" 
        :key="img + idx"
        class="group relative overflow-hidden bg-slate-200/40 dark:bg-slate-800/40 cursor-pointer shadow-sm hover:shadow-2xl transition-all duration-300 rounded-none border border-black/5 dark:border-white/5 mb-6 break-inside-avoid"
        @click="$emit('select', idx)"
      >
        <!-- Photo with natural aspect ratio, lazy loading and async decoding -->
        <img 
          :src="'/uploads/thumbs/' + img" 
          :alt="'Фото ' + (idx + 1)"
          @error="handleImgError"
          class="w-full h-auto block object-cover group-hover:scale-[1.02] transition-transform duration-500 ease-out rounded-none"
          loading="lazy"
          decoding="async"
        />
        
        <!-- Dark Overlay on Hover -->
        <div class="absolute inset-0 bg-black/0 group-hover:bg-black/25 transition-colors duration-300 flex items-end p-5">
          <span class="opacity-0 group-hover:opacity-100 text-white text-xs font-bold uppercase tracking-widest bg-black/60 px-3 py-1.5 backdrop-blur-sm transition-opacity duration-200">
            Увеличить фото
          </span>
        </div>
      </div>
    </div>

    <!-- Dynamic Infinite Scroll Sentinel & Load More Indicator -->
    <div 
      v-if="hasMore" 
      ref="sentinelRef" 
      class="flex flex-col items-center justify-center py-8 gap-3"
    >
      <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-slate-500 dark:text-slate-400">
        <span class="w-2 h-2 rounded-full bg-cyan-500 animate-ping"></span>
        <span>Загрузка новых фото ({{ visibleImages.length }} из {{ images.length }})...</span>
      </div>

      <button 
        @click="loadMore"
        class="px-6 py-2.5 rounded-xl text-xs font-bold uppercase tracking-wider liquid-card hover:bg-slate-200 dark:hover:bg-slate-800 transition-all active:scale-95 text-slate-800 dark:text-white shadow-sm"
      >
        Показать ещё (+{{ Math.min(BATCH_SIZE, images.length - visibleImages.length) }})
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'

const props = withDefaults(defineProps<{
  images: string[]
  initialBatch?: number
}>(), {
  initialBatch: 12
})

defineEmits<{
  (e: 'select', index: number): void
}>()

const BATCH_SIZE = 12
const visibleCount = ref(props.initialBatch)
const sentinelRef = ref<HTMLElement | null>(null)
let observer: IntersectionObserver | null = null

const visibleImages = computed(() => {
  return (props.images || []).slice(0, visibleCount.value)
})

const hasMore = computed(() => {
  return visibleCount.value < (props.images || []).length
})

function loadMore() {
  if (hasMore.value) {
    visibleCount.value = Math.min(props.images.length, visibleCount.value + BATCH_SIZE)
  }
}

function handleImgError(e: Event) {
  const target = e.target as HTMLImageElement
  if (target && !target.dataset.triedOriginal) {
    target.dataset.triedOriginal = 'true'
    const parts = target.src.split('/')
    const filename = parts[parts.length - 1]
    target.src = '/uploads/' + filename
  }
}

// Reset visible count when category or images prop changes
watch(() => props.images, () => {
  visibleCount.value = props.initialBatch || BATCH_SIZE
})

onMounted(() => {
  if (typeof window !== 'undefined' && 'IntersectionObserver' in window) {
    observer = new IntersectionObserver((entries) => {
      if (entries[0]?.isIntersecting && hasMore.value) {
        loadMore()
      }
    }, {
      rootMargin: '400px 0px',
      threshold: 0.01
    })

    if (sentinelRef.value) {
      observer.observe(sentinelRef.value)
    }
  }
})

watch(sentinelRef, (newEl) => {
  if (observer) {
    observer.disconnect()
    if (newEl && hasMore.value) {
      observer.observe(newEl)
    }
  }
})

onBeforeUnmount(() => {
  if (observer) {
    observer.disconnect()
  }
})
</script>
