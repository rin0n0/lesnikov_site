<template>
  <!-- VK Official Logo -->
  <svg 
    v-if="name === 'vk'" 
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="currentColor"
    class="inline-block shrink-0"
  >
    <path d="M15.684 0H8.316C2.692 0 0 2.692 0 8.316v7.368C0 21.308 2.692 24 8.316 24h7.368C21.308 24 24 21.308 24 15.684V8.316C24 2.692 21.308 0 15.684 0zm3.692 17.142h-1.744c-.66 0-.864-.525-2.052-1.714-1.04-1.01-1.503-1.139-1.76-1.139-.36 0-.462.103-.462.6v1.653c0 .425-.137.6-1.25.6-1.848 0-3.9-1.125-5.342-3.21-2.17-3.076-2.766-5.385-2.766-5.86 0-.256.103-.493.6-.493h1.745c.447 0 .614.205.787.693.856 2.493 2.294 4.68 2.888 4.68.223 0 .326-.103.326-.667V10.74c-.068-1.2-.703-1.302-.703-1.727 0-.205.17-.41.444-.41h2.748c.376 0 .513.197.513.633v3.41c0 .368.163.496.273.496.223 0 .41-.128.823-.538 1.284-1.44 2.193-3.666 2.193-3.666.12-.256.325-.435.77-.435h1.743c.523 0 .633.265.52.632-.222.99-2.345 3.99-2.448 4.144-.222.342-.308.496 0 .907.222.29 1.009.983 1.522 1.581.958 1.094 1.694 2.016 1.89 2.648.197.625-.102.94-.658.94z"/>
  </svg>

  <!-- Phone Icon -->
  <svg 
    v-else-if="name === 'phone'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
  </svg>

  <!-- Location Pin Icon -->
  <svg 
    v-else-if="name === 'location'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
    <circle cx="12" cy="10" r="3"/>
  </svg>

  <!-- Mail Icon -->
  <svg 
    v-else-if="name === 'mail'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <rect width="20" height="16" x="2" y="4" rx="2"/>
    <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
  </svg>

  <!-- Telegram Icon -->
  <svg 
    v-else-if="name === 'telegram'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="currentColor"
    class="inline-block shrink-0"
  >
    <path d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l-.313 4.67c.458 0 .66-.21.916-.458l2.199-2.138 4.573 3.378c.843.464 1.448.225 1.658-.783l2.996-14.122c.307-1.23-.468-1.786-1.269-1.422z"/>
  </svg>

  <!-- Sparkle / 3D Crystal Icon -->
  <svg 
    v-else-if="name === 'crystal'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>
  </svg>

  <!-- Check Icon -->
  <svg 
    v-else-if="name === 'check'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <path d="M20 6 9 17l-5-5"/>
  </svg>
  <!-- Menu Icon -->
  <svg 
    v-else-if="name === 'menu'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <line x1="3" y1="12" x2="21" y2="12"/>
    <line x1="3" y1="6" x2="21" y2="6"/>
    <line x1="3" y1="18" x2="21" y2="18"/>
  </svg>

  <!-- Close Icon -->
  <svg 
    v-else-if="name === 'close'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <line x1="18" y1="6" x2="6" y2="18"/>
    <line x1="6" y1="6" x2="18" y2="18"/>
  </svg>

  <!-- Camera Icon -->
  <svg 
    v-else-if="name === 'camera'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/>
    <circle cx="12" cy="13" r="4"/>
  </svg>

  <!-- Graduation Icon -->
  <svg 
    v-else-if="name === 'graduation'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z" />
    <path d="M22 10v6" />
    <path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5" />
  </svg>

  <!-- Search Icon -->
  <svg 
    v-else-if="name === 'search'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <circle cx="11" cy="11" r="8"/>
    <line x1="21" y1="21" x2="16.65" y2="16.65"/>
  </svg>

  <!-- List Icon -->
  <svg 
    v-else-if="name === 'list'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <line x1="8" y1="6" x2="21" y2="6"/>
    <line x1="8" y1="12" x2="21" y2="12"/>
    <line x1="8" y1="18" x2="21" y2="18"/>
    <line x1="3" y1="6" x2="3.01" y2="6"/>
    <line x1="3" y1="12" x2="3.01" y2="12"/>
    <line x1="3" y1="18" x2="3.01" y2="18"/>
  </svg>

  <!-- Image Icon -->
  <svg 
    v-else-if="name === 'image'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
    <circle cx="8.5" cy="8.5" r="1.5"/>
    <polyline points="21 15 16 10 5 21"/>
  </svg>

  <!-- Arrow Left Icon -->
  <svg 
    v-else-if="name === 'arrow-left'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <polyline points="15 18 9 12 15 6"/>
  </svg>

  <!-- Arrow Right Icon -->
  <svg 
    v-else-if="name === 'arrow-right'"
    :width="size || 20" 
    :height="size || 20" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <polyline points="9 18 15 12 9 6"/>
  </svg>
</template>

<script setup lang="ts">
defineProps<{
  name: string
  size?: number | string
}>()
</script>
