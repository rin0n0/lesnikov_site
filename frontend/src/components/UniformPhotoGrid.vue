<template>
  <div>
    <!-- Masonry Grid with Natural Aspect Ratios (Preserves tall vertical portraits and wide horizontal book spreads without cropping) -->
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 [column-fill:_balance]">
      <div 
        v-for="(img, idx) in images" 
        :key="img + idx"
        class="group relative overflow-hidden bg-gray-100 dark:bg-gray-800 cursor-pointer shadow-sm hover:shadow-2xl transition-all duration-300 rounded-none border border-black/5 dark:border-white/5 mb-6 break-inside-avoid"
        @click="$emit('select', idx)"
      >
        <!-- Photo with natural aspect ratio -->
        <img 
          :src="'/uploads/thumbs/' + img" 
          :alt="'Фото ' + (idx + 1)"
          @error="(e) => (e.target as HTMLImageElement).src = '/uploads/' + img"
          class="w-full h-auto block object-cover group-hover:scale-[1.02] transition-transform duration-500 ease-out rounded-none"
          loading="lazy"
        />
        
        <!-- Dark Overlay on Hover -->
        <div class="absolute inset-0 bg-black/0 group-hover:bg-black/25 transition-colors duration-300 flex items-end p-5">
          <span class="opacity-0 group-hover:opacity-100 text-white text-xs font-bold uppercase tracking-widest bg-black/60 px-3 py-1.5 backdrop-blur-sm transition-opacity duration-200">
            Увеличить фото
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  images: string[]
}>()

defineEmits<{
  (e: 'select', index: number): void
}>()
</script>
