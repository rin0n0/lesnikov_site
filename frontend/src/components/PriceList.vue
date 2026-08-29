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
            <div class="text-2xl font-black text-gray-900 dark:text-white">
              {{ item.price.toLocaleString('ru-RU') }} ₽
            </div>
          </div>
          
          <router-link 
            to="/contacts"
            class="bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider hover:opacity-90 transition-all shadow-sm"
          >
            Заказать
          </router-link>
        </div>
      </div>
    </div>
  </div>
  
  <div 
    v-else-if="singlePrice" 
    class="mb-10 p-6 sm:p-8 rounded-2xl liquid-card flex flex-col sm:flex-row items-center justify-between gap-6 shadow-sm"
  >
    <div>
      <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold">Фиксированная стоимость</div>
      <div class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white mt-1">
        {{ Number(singlePrice).toLocaleString('ru-RU') }} ₽ <span class="text-base font-normal text-gray-400">/ час</span>
      </div>
      <div class="text-xs text-gray-500 dark:text-gray-400 mt-1">
        Включает консультацию, съемку и авторскую обработку всех удачных кадров
      </div>
    </div>
    
    <router-link 
      to="/contacts"
      class="bg-gray-900 text-white dark:bg-white dark:text-gray-900 px-7 py-3.5 rounded-xl font-bold hover:opacity-90 transition-all shadow-sm w-full sm:w-auto text-center text-xs uppercase tracking-wider"
    >
      Забронировать дату
    </router-link>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  items?: Array<{ name: string; price: number }>
  singlePrice?: string | number
}>()
</script>
