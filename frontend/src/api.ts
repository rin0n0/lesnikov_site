import defaultData from './data/defaultData.json'

let memoryCache: any = defaultData

export async function fetchSiteData(forceRefresh = false) {
  // Always trigger background sync for live updates from backend/TMA
  revalidateInBackground()

  // 1. Return in-memory cache synchronously (0 ms)
  if (!forceRefresh && memoryCache) {
    return memoryCache
  }

  // 2. Check localStorage for updated cached data (0 ms)
  if (!forceRefresh && typeof window !== 'undefined') {
    try {
      const stored = localStorage.getItem('lesnikov_site_data')
      if (stored) {
        memoryCache = JSON.parse(stored)
        return memoryCache
      }
    } catch {}
  }

  return defaultData
}

let isRevalidating = false
async function revalidateInBackground() {
  if (isRevalidating) return
  isRevalidating = true
  try {
    const res = await fetch('/api/data')
    if (res.ok) {
      const data = await res.json()
      memoryCache = data
      if (typeof window !== 'undefined') {
        try {
          localStorage.setItem('lesnikov_site_data', JSON.stringify(data))
        } catch {}
      }
    }
  } catch {
    // Silently ignore background revalidation errors
  } finally {
    isRevalidating = false
  }
}

export async function submitContact(form: { name: string, phone: string, email: string, message: string }) {
  try {
    const res = await fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })
    return res.ok
  } catch (err) {
    console.error('Failed to submit contact:', err)
    return false
  }
}
