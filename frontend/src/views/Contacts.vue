<template>
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-6 md:py-10">
    <!-- Header -->
    <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14">
      <h1 class="text-3xl sm:text-5xl md:text-6xl font-black tracking-tight mb-3 uppercase">
        Контакты
      </h1>
      <p class="text-gray-500 dark:text-gray-400 text-sm sm:text-base font-normal">
        Обсудите детали фотосессии, уточните свободные даты или закажите выпускные альбомы
      </p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-start">
      <!-- Direct Contact Channels -->
      <div class="lg:col-span-5 space-y-4">
        <h2 class="text-xs font-bold uppercase tracking-widest text-gray-400 font-semibold px-1">
          Прямая связь
        </h2>

        <!-- Phone Card -->
        <a :href="'tel:' + (contactData.phone || '+79117775700')"
          class="liquid-card p-5 rounded-2xl flex items-center gap-4 shadow-sm hover:shadow-md transition-all group block">
          <div
            class="w-12 h-12 rounded-xl bg-gray-900 dark:bg-white text-white dark:text-gray-900 flex items-center justify-center group-hover:scale-105 transition-transform shadow-sm">
            <AppIcon name="phone" :size="20" />
          </div>
          <div>
            <div class="text-[10px] uppercase tracking-wider text-gray-400 font-medium">Телефон и WhatsApp</div>
            <div class="text-base sm:text-lg font-black text-gray-900 dark:text-white mt-0.5">
              {{ contactData.phone || '+7 (911) 777-57-00' }}
            </div>
          </div>
        </a>

        <!-- Official VK Card -->
        <a :href="contactData.vk || 'https://vk.com/lesnikovfoto'" target="_blank"
          class="liquid-card p-5 rounded-2xl flex items-center gap-4 shadow-sm hover:shadow-md transition-all group block border-blue-500/20 hover:border-blue-500/50">
          <div
            class="w-12 h-12 rounded-xl bg-[#0077FF] text-white flex items-center justify-center group-hover:scale-105 transition-transform shadow-sm">
            <AppIcon name="vk" :size="22" />
          </div>
          <div>
            <div class="text-[10px] uppercase tracking-wider text-gray-400 font-medium">Группа ВКонтакте</div>
            <div class="text-base sm:text-lg font-black text-[#0077FF] mt-0.5">
              vk.com/lesnikovfoto
            </div>
          </div>
        </a>

        <!-- Location Card -->
        <div class="liquid-card p-5 rounded-2xl flex items-center gap-4 shadow-sm">
          <div
            class="w-12 h-12 rounded-xl bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-700 dark:text-gray-300">
            <AppIcon name="location" :size="20" />
          </div>
          <div>
            <div class="text-[10px] uppercase tracking-wider text-gray-400 font-medium">Локация съемок</div>
            <div class="text-sm sm:text-base font-bold text-gray-900 dark:text-white mt-0.5">
              {{ contactData.location || 'Санкт-Петербург и Ленинградская обл.' }}
            </div>
          </div>
        </div>

        <!-- Email Card -->
        <div class="liquid-card p-5 rounded-2xl flex items-center gap-4 shadow-sm">
          <div
            class="w-12 h-12 rounded-xl bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-700 dark:text-gray-300">
            <AppIcon name="mail" :size="20" />
          </div>
          <div>
            <div class="text-[10px] uppercase tracking-wider text-gray-400 font-medium">Электронная почта</div>
            <a :href="'mailto:' + (contactData.email || 'lesnikovfoto@mail.ru')"
              class="text-sm sm:text-base font-bold text-gray-900 dark:text-white hover:underline">
              {{ contactData.email || 'lesnikovfoto@mail.ru' }}
            </a>
          </div>
        </div>
      </div>

      <!-- Lead Form -->
      <div class="lg:col-span-7 liquid-card p-6 sm:p-10 rounded-2xl shadow-md">
        <h2 class="text-xl sm:text-2xl font-black tracking-tight text-gray-900 dark:text-white mb-2">
          Оставить заявку
        </h2>
        <p class="text-xs text-gray-500 dark:text-gray-400 mb-8">
          Сообщение моментально поступит в Telegram фотографа
        </p>

        <form @submit.prevent="submit" class="space-y-4">
          <div>
            <label class="block text-[11px] font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-1.5">
              Ваше имя *
            </label>
            <input v-model="form.name" required type="text" placeholder="Как к вам обращаться"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 bg-white/60 dark:bg-black/30 focus:outline-none focus:ring-2 focus:ring-gray-900 dark:focus:ring-white transition-all text-sm" />
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label
                class="block text-[11px] font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-1.5">
                Телефон *
              </label>
              <input v-model="form.phone" required type="tel" placeholder="+7 (___) ___-__-__"
                class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 bg-white/60 dark:bg-black/30 focus:outline-none focus:ring-2 focus:ring-gray-900 dark:focus:ring-white transition-all text-sm" />
            </div>
            <div>
              <label
                class="block text-[11px] font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-1.5">
                Email
              </label>
              <input v-model="form.email" type="email" placeholder="example@mail.ru"
                class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 bg-white/60 dark:bg-black/30 focus:outline-none focus:ring-2 focus:ring-gray-900 dark:focus:ring-white transition-all text-sm" />
            </div>
          </div>

          <div>
            <label class="block text-[11px] font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-1.5">
              Какая съемка или альбом интересует?
            </label>
            <textarea v-model="form.message" rows="3"
              placeholder="Например: Выпускные альбомы для 11 класса / Свадебная съемка"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 bg-white/60 dark:bg-black/30 focus:outline-none focus:ring-2 focus:ring-gray-900 dark:focus:ring-white transition-all text-sm resize-none"></textarea>
          </div>

          <button type="submit" :disabled="submitting"
            class="w-full bg-gray-900 text-white dark:bg-white dark:text-gray-900 py-3.5 rounded-xl font-bold hover:opacity-90 transition-all disabled:opacity-50 text-xs uppercase tracking-wider shadow-sm mt-2">
            {{ submitting ? 'Отправка...' : 'Отправить заявку' }}
          </button>

          <div v-if="successMsg"
            class="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-600 dark:text-emerald-400 text-xs sm:text-sm text-center font-bold flex items-center justify-center gap-2 mt-4">
            <AppIcon name="check" :size="16" />
            <span>{{ successMsg }}</span>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { fetchSiteData, submitContact } from '../api'
import AppIcon from '../components/AppIcon.vue'

const contactData = ref<any>({})
const loading = ref(true)
const submitting = ref(false)
const successMsg = ref('')

const form = ref({
  name: '',
  phone: '',
  email: '',
  message: ''
})

onMounted(async () => {
  const data = await fetchSiteData()
  if (data && data.contacts) {
    contactData.value = data.contacts
  }
  loading.value = false
})

async function submit() {
  submitting.value = true
  successMsg.value = ''

  const ok = await submitContact(form.value)
  if (ok) {
    successMsg.value = 'Заявка успешно отправлена! Владимир свяжется с вами в ближайшее время.'
    form.value = { name: '', phone: '', email: '', message: '' }
  } else {
    alert('Произошла ошибка при отправке.')
  }

  submitting.value = false
}
</script>
