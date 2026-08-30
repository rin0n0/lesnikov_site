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
        <div class="flex justify-end items-center text-white/80 z-10">
          <button 
            @click="close" 
            class="p-2 text-white/80 hover:text-white text-2xl hover:bg-white/10 rounded-full transition-colors"
            title="Закрыть (Esc)"
          >
            <AppIcon name="close" :size="24" />
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
            <AppIcon name="arrow-left" :size="32" />
          </button>

          <!-- Current Image -->
          <img 
            :src="'/uploads/' + currentImage" 
            class="max-w-full max-h-[85vh] object-contain rounded-md shadow-2xl"
            :style="{ 
              transform: `translate(${translateX}px, ${translateY}px) scale(${scale})`,
              transition: isDragging ? 'none' : 'transform 0.2s ease-out',
              cursor: scale > 1 ? (isDragging ? 'grabbing' : 'grab') : 'zoom-in'
            }"
            :alt="'Фото ' + (currentIndex + 1)"
            @wheel.prevent="onWheel"
            @mousedown.prevent="onMouseDown"
            @mousemove.prevent="onMouseMove"
            @mouseup="onMouseUp"
            @mouseleave="onMouseUp"
            @touchstart="onTouchStart"
            @touchmove="onTouchMove"
            @touchend="onTouchEnd"
            @dblclick="onDoubleClick"
          />

          <!-- Next Button -->
          <button 
            v-if="images.length > 1"
            @click.stop="next"
            class="absolute right-2 md:right-6 p-3 text-white/70 hover:text-white hover:bg-white/10 rounded-full text-2xl transition-all z-20"
            title="Следующее (→)"
          >
            <AppIcon name="arrow-right" :size="32" />
          </button>
        </div>

      </div>
    </transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, computed, watch, nextTick } from 'vue'
import AppIcon from './AppIcon.vue'

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

// Zoom & Pan Logic
const scale = ref(1)
const translateX = ref(0)
const translateY = ref(0)
const isDragging = ref(false)
let startX = 0
let startY = 0

// Reset zoom when image changes
watch(currentIndex, () => {
  scale.value = 1
  translateX.value = 0
  translateY.value = 0
})

function onWheel(e: WheelEvent) {
  if (e.deltaY < 0) {
    scale.value = Math.min(scale.value + 0.25, 5)
  } else {
    scale.value = Math.max(scale.value - 0.25, 1)
  }
  if (scale.value === 1) {
    translateX.value = 0
    translateY.value = 0
  }
}

function onMouseDown(e: MouseEvent) {
  if (scale.value > 1) {
    isDragging.value = true
    startX = e.clientX - translateX.value
    startY = e.clientY - translateY.value
  }
}

function onMouseMove(e: MouseEvent) {
  if (isDragging.value) {
    translateX.value = e.clientX - startX
    translateY.value = e.clientY - startY
  }
}

function onMouseUp() {
  isDragging.value = false
}

function onDoubleClick() {
  if (scale.value > 1) {
    scale.value = 1
    translateX.value = 0
    translateY.value = 0
  } else {
    scale.value = 2.5
  }
}

let initialDistance = 0
let initialScale = 1
let lastTap = 0

function getDistance(touches: TouchList) {
  const dx = touches[0].clientX - touches[1].clientX
  const dy = touches[0].clientY - touches[1].clientY
  return Math.sqrt(dx * dx + dy * dy)
}

function onTouchStart(e: TouchEvent) {
  if (e.touches.length === 2) {
    initialDistance = getDistance(e.touches)
    initialScale = scale.value
  } else if (e.touches.length === 1 && scale.value > 1) {
    isDragging.value = true
    startX = e.touches[0].clientX - translateX.value
    startY = e.touches[0].clientY - translateY.value
  }
}

function onTouchMove(e: TouchEvent) {
  if (e.touches.length === 2) {
    e.preventDefault()
    const currentDistance = getDistance(e.touches)
    const factor = currentDistance / initialDistance
    scale.value = Math.min(Math.max(initialScale * factor, 1), 5)
    if (scale.value === 1) {
      translateX.value = 0
      translateY.value = 0
    }
  } else if (e.touches.length === 1 && isDragging.value) {
    e.preventDefault()
    translateX.value = e.touches[0].clientX - startX
    translateY.value = e.touches[0].clientY - startY
  }
}

function onTouchEnd(e: TouchEvent) {
  isDragging.value = false
  if (e.changedTouches.length === 1) {
    const now = Date.now()
    if (now - lastTap < 300) {
      // Double tap
      onDoubleClick()
    }
    lastTap = now
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
