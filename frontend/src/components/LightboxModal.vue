<template>
  <Teleport to="body">
    <transition name="fade">
      <div 
        v-if="isOpen" 
        class="fixed inset-0 z-[100] bg-black/95 flex flex-col justify-between p-4 md:p-8 backdrop-blur-sm select-none"
        @click.self="close"
        @keydown.esc="close"
        @keydown.left="prev"
        @keydown.right="next"
        tabindex="0"
        ref="modalRef"
      >
        <!-- Top bar -->
        <div class="flex justify-between items-center text-white/80 z-10">
          <span class="text-sm font-mono tracking-wider">
            {{ currentIndex + 1 }} / {{ images.length }}
          </span>
          <button 
            @click="close" 
            class="p-2 text-white/80 hover:text-white text-2xl hover:bg-white/10 rounded-full transition-colors"
            title="Закрыть (Esc)"
          >
            ✕
          </button>
        </div>

        <!-- Center Image + Navigation -->
        <div class="relative flex-1 flex items-center justify-center my-4 overflow-hidden">
          <!-- Prev Button -->
          <button 
            v-if="images.length > 1"
            @click.stop="prev"
            class="absolute left-2 md:left-6 p-3 text-white/70 hover:text-white hover:bg-white/10 rounded-full text-2xl transition-all z-20"
            title="Предыдущее (←)"
          >
            ‹
          </button>

          <!-- Current Image -->
          <img 
            :src="'/uploads/' + currentImage" 
            class="max-w-full max-h-[85vh] object-contain rounded-md shadow-2xl transition-all duration-200"
            :alt="'Фото ' + (currentIndex + 1)"
          />

          <!-- Next Button -->
          <button 
            v-if="images.length > 1"
            @click.stop="next"
            class="absolute right-2 md:right-6 p-3 text-white/70 hover:text-white hover:bg-white/10 rounded-full text-2xl transition-all z-20"
            title="Следующее (→)"
          >
            ›
          </button>
        </div>

        <!-- Bottom bar / Hint -->
        <div class="text-center text-xs text-white/40 tracking-wider">
          Используйте стрелки влево/вправо для навигации
        </div>
      </div>
    </transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, computed, watch, nextTick } from 'vue'

const props = defineProps<{
  images: string[]
  modelValue: number | null
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: number | null): void
}>()

const modalRef = ref<HTMLElement | null>(null)
const currentIndex = ref(0)

const isOpen = computed(() => props.modelValue !== null && props.modelValue >= 0)
const currentImage = computed(() => props.images[currentIndex.value] || '')

watch(() => props.modelValue, (newVal) => {
  if (newVal !== null && newVal >= 0) {
    currentIndex.value = newVal
    nextTick(() => modalRef.value?.focus())
  }
})

function close() {
  emit('update:modelValue', null)
}

function prev() {
  if (currentIndex.value > 0) {
    currentIndex.value--
  } else {
    currentIndex.value = props.images.length - 1
  }
}

function next() {
  if (currentIndex.value < props.images.length - 1) {
    currentIndex.value++
  } else {
    currentIndex.value = 0
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
