<template>
  <div v-if="items && items.length > 0" class="mb-10">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
      <div 
        v-for="(item, idx) in items" 
        :key="idx"
        class="liquid-card rounded-2xl p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition-all"
      >
        <div>
          <div class="text-[11px] uppercase tracking-wider text-gray-400 font-semibold mb-1">
            Пакет #{{ idx + 1 }}
          </div>
          <div class="text-base font-bold text-gray-900 dark:text-white leading-snug">
            {{ item.name }}
          </div>
        </div>

        <div class="mt-6 pt-4 border-t border-gray-200/50 dark:border-gray-700/50 flex items-center justify-between">
          <div>
            <div class="text-[10px] uppercase tracking-wider text-gray-400">Стоимость</div>
            <div class="text-2xl font-black text-gray-900 dark:text-white font-mono">
              {{ item.price.toLocaleString('ru-RU') }} ₽
            </div>
          </div>
          
          <router-link 
            :to="{ path: '/contacts', query: { subject: (categoryTitle ? categoryTitle + ': ' : '') + item.name } }"
            class="bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider hover:opacity-90 transition-all shadow-sm active:scale-95"
          >
            Заказать
          </router-link>
        </div>
      </div>
    </div>
  </div>
  
  <div 
    v-else-if="singlePrice" 
    class="mb-10 p-6 sm:p-8 rounded-3xl liquid-card flex flex-col md:flex-row items-start md:items-center justify-between gap-6 shadow-md border border-white/60 dark:border-white/10"
  >
    <div class="space-y-2">
      <div class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white font-mono">
        {{ Number(singlePrice).toLocaleString('ru-RU') }} ₽ <span class="text-base font-normal text-gray-400">/ час</span>
      </div>
      <div class="text-xs text-gray-600 dark:text-gray-300 flex flex-wrap gap-x-4 gap-y-1.5 pt-1">
        <span class="flex items-center gap-1.5"><AppIcon name="check" :size="12" class="text-emerald-500" /> Консультация и помощь с позированием</span>
        <span class="flex items-center gap-1.5"><AppIcon name="check" :size="12" class="text-emerald-500" /> Авторская цветокоррекция всех удачных кадров</span>
        <span class="flex items-center gap-1.5"><AppIcon name="check" :size="12" class="text-emerald-500" /> Передача через удобную онлайн-галерею</span>
      </div>
    </div>
    
    <router-link 
      :to="{ path: '/contacts', query: { subject: categoryTitle ? categoryTitle + ' фотосессия' : 'Фотосессия' } }"
      class="bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-8 py-4 rounded-2xl font-bold hover:opacity-90 transition-all shadow-lg w-full md:w-auto text-center text-xs uppercase tracking-widest active:scale-95 shrink-0"
    >
      Забронировать дату
    </router-link>
  </div>
</template>

<script setup lang="ts">
import AppIcon from './AppIcon.vue'
defineProps<{
  items?: Array<{ name: string; price: number }>
  singlePrice?: string | number
  categoryTitle?: string
}>()
</script>
