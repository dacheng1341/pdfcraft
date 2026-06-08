'use client';

import React, { useEffect } from 'react';

export interface AdSenseProps {
  adSlot: string;
  className?: string;
  style?: React.CSSProperties;
  format?: 'auto' | 'fluid' | 'rectangle';
  responsive?: boolean;
}

export function refreshAds() {
  if (typeof window !== 'undefined') {
    try {
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    } catch (e) {
      console.warn('AdSense push failed', e);
    }
  }
}

export const AdSense: React.FC<AdSenseProps> = ({
  adSlot,
  className = '',
  style = { display: 'block' },
  format = 'auto',
  responsive = true,
}) => {
  useEffect(() => {
    refreshAds();
  }, []);

  return (
    <div className={`ad-container w-full overflow-hidden flex justify-center items-center my-4 ${className}`}>
      <ins
        className="adsbygoogle w-full"
        style={style}
        data-ad-client="ca-pub-XXXXXXXXXXXXXXX"
        data-ad-slot={adSlot}
        data-ad-format={format}
        data-full-width-responsive={responsive ? 'true' : 'false'}
      />
    </div>
  );
};
