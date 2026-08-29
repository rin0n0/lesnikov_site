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
</template>

<script setup lang="ts">
defineProps<{
  name: string
  size?: number | string
}>()
</script>
