<template>
  <svg 
    xmlns="http://www.w3.org/2000/svg" 
    :width="size || 16" 
    :height="size || 16" 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    stroke-width="2" 
    stroke-linecap="round" 
    stroke-linejoin="round"
    class="inline-block shrink-0"
  >
    <!-- Kindergarten: Balloon / Blocks -->
    <g v-if="name === 'kindergarten'">
      <path d="M12 2a6 6 0 0 0-6 6c0 4 6 10 6 10s6-6 6-10a6 6 0 0 0-6-6z" />
      <circle cx="12" cy="8" r="2" />
      <path d="M12 18v4" />
    </g>

    <!-- Grade 4: Book / School -->
    <g v-else-if="name === 'grade_4'">
      <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z" />
      <path d="M6 6h10" />
      <path d="M6 10h10" />
    </g>

    <!-- Grade 11: Graduation Cap -->
    <g v-else-if="name === 'grade_11'">
      <path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z" />
      <path d="M22 10v6" />
      <path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5" />
    </g>

    <!-- Wedding: Heart / Rings -->
    <g v-else-if="name === 'wedding'">
      <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z" />
    </g>

    <!-- Family: Users Group -->
    <g v-else-if="name === 'family'">
      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
      <circle cx="9" cy="7" r="4" />
      <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
    </g>

    <!-- Individual: Single User Portrait -->
    <g v-else-if="name === 'individual'">
      <circle cx="12" cy="8" r="5" />
      <path d="M20 21a8 8 0 0 0-16 0" />
    </g>

    <!-- Maternity: Sun / New Life Sparkle -->
    <g v-else-if="name === 'maternity'">
      <circle cx="12" cy="12" r="4" />
      <path d="M12 2v2" />
      <path d="M12 20v2" />
      <path d="m4.93 4.93 1.41 1.41" />
      <path d="m17.66 17.66 1.41 1.41" />
      <path d="M2 12h2" />
      <path d="M20 12h2" />
      <path d="m6.34 17.66-1.41 1.41" />
      <path d="m19.07 4.93-1.41 1.41" />
    </g>

    <!-- Reportage: Camera / Live Action -->
    <g v-else-if="name === 'reportage'">
      <path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z" />
      <circle cx="12" cy="13" r="3" />
    </g>

    <!-- Fallback default -->
    <g v-else>
      <circle cx="12" cy="12" r="10" />
    </g>
  </svg>
</template>

<script setup lang="ts">
defineProps<{
  name: string
  size?: number | string
}>()
</script>
