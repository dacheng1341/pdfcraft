declare global {
  interface Window {
    zaraz?: {
      track: (eventName: string, params?: Record<string, any>) => void;
    };
    adsbygoogle?: any[];
  }
}

export function trackEvent(eventName: string, params?: Record<string, any>) {
  if (typeof window !== 'undefined' && window.zaraz) {
    try {
      window.zaraz.track(eventName, params);
    } catch (e) {
      console.warn('Zaraz tracking failed', e);
    }
  }
}

export function trackPageView(virtualPath: string) {
  if (typeof window !== 'undefined' && window.zaraz) {
    try {
      window.zaraz.track('Page View', { page_path: virtualPath });
    } catch (e) {
      console.warn('Zaraz pageview failed', e);
    }
  }
}
