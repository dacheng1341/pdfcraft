'use client';

import React from 'react';
import { useTranslations } from 'next-intl';

export const SEOArticle: React.FC = () => {
  const t = useTranslations('common');

  return (
    <section className="w-full max-w-5xl mx-auto px-4 py-16 text-[hsl(var(--color-muted-foreground))] text-sm leading-relaxed border-t border-[hsl(var(--color-border))] mt-12 mb-8 opacity-80 hover:opacity-100 transition-opacity duration-300">
      <div className="prose prose-sm prose-invert max-w-none">
        <h2 className="text-xl font-bold mb-4 text-[hsl(var(--color-foreground))]">
          {t('seoArticle.h2', { brand: t('brand') })}
        </h2>
        <p className="mb-6">
          {t('seoArticle.h2Desc', { brand: t('brand') })}
        </p>

        <h3 className="text-lg font-semibold mb-3 text-[hsl(var(--color-foreground))]">
          {t('seoArticle.h3Advantage')}
        </h3>
        <p className="mb-6">
          {t('seoArticle.h3AdvantageDesc', { brand: t('brand') })}
        </p>

        <h3 className="text-lg font-semibold mb-3 text-[hsl(var(--color-foreground))]">
          {t('seoArticle.h3Features')}
        </h3>
        <p className="mb-4">
          {t('seoArticle.h3FeaturesDesc')}
        </p>
      </div>
    </section>
  );
};
