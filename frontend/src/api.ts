export async function fetchSiteData() {
  try {
    const res = await fetch('/api/data')
    if (!res.ok) throw new Error('Failed to fetch')
    return await res.json()
  } catch (err) {
    console.error(err)
    return null
  }
}

export async function submitContact(form: { name: string, phone: string, email: string, message: string }) {
  const res = await fetch('/api/contact', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(form)
  })
  return res.ok
}
