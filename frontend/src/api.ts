let memoryCache: any = null

export async function fetchSiteData(forceRefresh = false) {
  // 1. Check memory cache first (0 ms)
  if (!forceRefresh && memoryCache) {
    // Revalidate in background if cache is older than 60 seconds
    revalidateInBackground()
    return memoryCache
  }

  // 2. Check localStorage / sessionStorage for instant initial load (0 ms)
  if (!forceRefresh && typeof window !== 'undefined') {
    try {
      const stored = localStorage.getItem('lesnikov_site_data')
      if (stored) {
        memoryCache = JSON.parse(stored)
        revalidateInBackground()
        return memoryCache
      }
    } catch {
      // Storage unavailable or corrupted
    }
  }

  // 3. Fallback to network fetch
  try {
    const res = await fetch('/api/data')
    if (!res.ok) throw new Error('Failed to fetch')
    const data = await res.json()
    memoryCache = data
    if (typeof window !== 'undefined') {
      try {
        localStorage.setItem('lesnikov_site_data', JSON.stringify(data))
      } catch {}
    }
    return data
  } catch (err) {
    console.error('Fetch error:', err)
    return memoryCache || null
  }
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
