"""
Generate en/index.html with natural, persuasive English copy,
Apple-inspired design, $199 USD pricing, $20 USD/mo maintenance,
PayPal/Wise/Wire payment methods, hreflang tags, and bilingual language toggle.
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    es_html = f.read()

# We construct the complete English landing page mirroring the design and components of index.html
en_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-KWD0WYVK4J"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-KWD0WYVK4J');
  </script>

  <!-- Clarity tracking code for https://erikwebsite.com/ -->
  <script>
      (function(c,l,a,r,i,t,y){
          c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
          t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i+"?ref=bwt";
          y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
      })(window, document, "clarity", "script", "ytkayi2nwu");
  </script>

  <title>Modern, High-Converting Websites for Businesses & Pros | Erik Website</title>
  <meta name="description" content="Turn visitors into paying clients with a sleek, ultra-fast website delivered in 3 to 5 business days. Apple-inspired design, mobile-first, and direct WhatsApp / email leads.">
  <link rel="canonical" href="https://erikwebsite.com/en/">

  <!-- Hreflang SEO Tags for Multilingual Indexing -->
  <link rel="alternate" hreflang="es" href="https://erikwebsite.com/">
  <link rel="alternate" hreflang="en" href="https://erikwebsite.com/en/">
  <link rel="alternate" hreflang="x-default" href="https://erikwebsite.com/">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://erikwebsite.com/en/">
  <meta property="og:title" content="Modern, High-Converting Websites for Businesses & Pros | Erik Website">
  <meta property="og:description" content="Turn visitors into paying clients with a sleek, ultra-fast website delivered in 3 to 5 business days. Apple-inspired design, mobile-first, and direct WhatsApp / email leads.">
  <meta property="og:image" content="https://erikwebsite.com/images/og_main.jpg">
  <meta property="og:image:secure_url" content="https://erikwebsite.com/images/og_main.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Erik Website - Modern Bespoke Web Development">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="Erik Website">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://erikwebsite.com/en/">
  <meta name="twitter:title" content="Modern, High-Converting Websites for Businesses & Pros | Erik Website">
  <meta name="twitter:description" content="Turn visitors into paying clients with a sleek, ultra-fast website delivered in 3 to 5 business days. Apple-inspired design, mobile-first, and direct WhatsApp / email leads.">
  <meta name="twitter:image" content="https://erikwebsite.com/images/og_main.jpg">

  <!-- Favicon SVG -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22><rect width=%2232%22 height=%2232%22 rx=%228%22 fill=%22%23059669%22/><text x=%2216%22 y=%2222%22 font-family=%22sans-serif%22 font-size=%2218%22 font-weight=%22900%22 fill=%22white%22 text-anchor=%22middle%22>E</text></svg>">

  <!-- Google Fonts & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/src/styles/main.css">

  <!-- Schema.org ProfessionalService -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "ProfessionalService",
        "@id": "https://erikwebsite.com/en/#organization",
        "name": "Erik Website",
        "url": "https://erikwebsite.com/en/",
        "description": "Bespoke high-performance web development for businesses and independent professionals worldwide. Ultra-fast delivery, Apple-inspired aesthetics, and direct conversion channels.",
        "priceRange": "$199 USD",
        "telephone": "+5492645185359",
        "openingHoursSpecification": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          "opens": "09:00",
          "closes": "20:00"
        }
      },
      {
        "@type": "FAQPage",
        "@id": "https://erikwebsite.com/en/#faq",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How long does delivery take and what do you need from me?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Your website is live in 3 to 5 business days. You don't have to write long copy or design anything: simply send us 3 brief voice notes or notes describing your services, photos of your work, and your rates. We handle copy, high-res visual assets, and full deployment."
            }
          },
          {
            "@type": "Question",
            "name": "What payment methods are accepted for international clients?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "We accept PayPal, Wise, International Bank Wire (SWIFT/ACH), and Cryptocurrency (USDT). The setup is $199 USD (50% upfront, 50% upon final sign-off)."
            }
          },
          {
            "@type": "Question",
            "name": "How does hosting and domain management work?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "We handle domain registration, SSL certificate deployment, and ultra-fast global cloud hosting. You don't have to worry about complicated DNS or server settings."
            }
          },
          {
            "@type": "Question",
            "name": "Can I buy out the full source code and rights to self-host?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, absolutely. If at any point you wish to self-host or manage your site independently, you can acquire full ownership, code repository access, and source files for an amount equal to 10 maintenance months ($200 USD), in accordance with our Terms & Conditions."
            }
          }
        ]
      }
    ]
  }
  </script>
</head>
<body class="bg-slate-50 text-slate-800 flex flex-col min-h-screen">

  <!-- TOP MINIMALIST BANNER -->
  <div class="bg-[#1d1d1f] text-neutral-400 text-[11px] py-1.5 px-4 text-center font-normal tracking-tight border-b border-white/[0.08] flex items-center justify-center gap-2">
    <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
    <span>Bespoke Web Development for Businesses & Independent Pros Worldwide | Delivered in 3 to 5 Business Days</span>
  </div>

  <!-- NAVBAR (Apple Frosted Glass & Pill Controls) -->
  <header id="main-nav" class="sticky top-0 z-50 transition-all duration-300 bg-white/80 backdrop-blur-xl saturate-180 border-b border-black/[0.06]">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-14 sm:h-16 flex items-center justify-between py-2">
      <!-- Logo -->
      <a href="/en/" class="font-display font-bold text-base sm:text-lg text-neutral-900 tracking-[-0.02em] flex items-center">
        <span>Erik <span class="text-emerald-600 font-semibold">Website</span></span>
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden md:flex items-center gap-6 text-[13px] font-medium text-neutral-600 tracking-tight">
        <a href="#demos" class="hover:text-neutral-900 transition-colors">Live Demos</a>
        <a href="#trabajos" class="hover:text-neutral-900 transition-colors">Portfolio</a>
        <a href="#proceso" class="hover:text-neutral-900 transition-colors">How It Works</a>
        <a href="#precios" class="hover:text-neutral-900 transition-colors">Clear Pricing</a>
        <a href="/blog/" class="hover:text-emerald-600 transition-colors text-neutral-500 flex items-center gap-1">
          <span>Blog</span>
          <span class="text-[10px] bg-neutral-200/60 px-1.5 py-0.5 rounded text-neutral-600 font-semibold">ES</span>
        </a>
      </nav>

      <!-- Right Controls: Language Switcher + CTA -->
      <div class="flex items-center gap-2.5 sm:gap-3.5">
        <!-- Language Switcher Pill -->
        <div class="inline-flex items-center p-0.5 rounded-full bg-neutral-100 border border-black/[0.06] text-xs font-semibold">
          <a href="/" class="px-2.5 py-1 rounded-full text-neutral-500 hover:text-neutral-900 transition-colors" title="Ver versión en Español">ES</a>
          <span class="px-2.5 py-1 rounded-full bg-white text-neutral-900 shadow-2xs font-bold">EN</span>
        </div>

        <!-- CTA Header -->
        <a href="#precios" 
           data-wa-msg="Hello Erik! I reviewed your portfolio and would like to build a modern website for my business."
           class="inline-flex items-center gap-1.5 sm:gap-2 bg-neutral-900 hover:bg-black text-white font-medium text-xs px-3.5 py-1.5 rounded-full shadow-xs active:scale-[0.98] transition-all duration-150 cursor-pointer">
          <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/>
          </svg>
          <span>Get Started</span>
        </a>
      </div>
    </div>
  </header>

  <main class="flex-grow">

    <!-- HERO SECTION (Apple Keynote Style) -->
    <section class="relative overflow-hidden pt-12 sm:pt-20 pb-16 sm:pb-24 border-b border-black/[0.06] bg-gradient-to-b from-white via-slate-50/50 to-slate-100/30">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 text-center relative z-10">
        
        <!-- Pill Badge -->
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-50 border border-emerald-200/80 text-emerald-800 text-xs font-semibold mb-6 shadow-2xs">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          <span>BESPOKE HIGH-CONVERTING WEBSITES • $199 USD</span>
        </div>

        <!-- Main Headline -->
        <h1 class="text-3xl sm:text-5xl md:text-6xl font-extrabold font-display text-neutral-950 tracking-[-0.03em] leading-[1.1] mb-6">
          Websites designed to turn visitors into <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 to-teal-600">paying clients.</span>
        </h1>

        <!-- Subtitle -->
        <p class="text-base sm:text-xl text-neutral-600 max-w-2xl mx-auto font-light leading-relaxed mb-8">
          Clean code, Apple-inspired aesthetics, instant mobile loading, and direct WhatsApp or email leads. Live in 3 to 5 business days with zero complicated maintenance headaches.
        </p>

        <!-- CTA Buttons Group -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-4 mb-12">
          <a href="#precios" 
             class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-7 py-3.5 rounded-full bg-gradient-to-b from-emerald-500 to-emerald-600 text-white font-semibold text-sm shadow-[0_8px_20px_-6px_rgba(16,185,129,0.38)] hover:brightness-105 active:scale-[0.98] transition-all cursor-pointer">
            <span>Get Your Website ($199 USD)</span>
            <span>→</span>
          </a>
          <a href="#demos" 
             class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full bg-white hover:bg-neutral-50 text-neutral-800 font-semibold text-sm border border-black/[0.08] shadow-2xs active:scale-[0.98] transition-all cursor-pointer">
            <span>Explore Live Demos</span>
            <span>↓</span>
          </a>
        </div>

        <!-- Key Metrics Strip -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 max-w-4xl mx-auto pt-6 border-t border-black/[0.06]">
          <div class="p-3.5 rounded-2xl bg-white/70 backdrop-blur-md border border-black/[0.05] shadow-2xs">
            <span class="block text-2xl font-bold font-display text-neutral-900">3-5 Days</span>
            <span class="text-xs text-neutral-500 font-light">Guaranteed Delivery</span>
          </div>
          <div class="p-3.5 rounded-2xl bg-white/70 backdrop-blur-md border border-black/[0.05] shadow-2xs">
            <span class="block text-2xl font-bold font-display text-emerald-600">&lt; 0.8s</span>
            <span class="text-xs text-neutral-500 font-light">Ultra-Fast Mobile Speed</span>
          </div>
          <div class="p-3.5 rounded-2xl bg-white/70 backdrop-blur-md border border-black/[0.05] shadow-2xs">
            <span class="block text-2xl font-bold font-display text-neutral-900">100%</span>
            <span class="text-xs text-neutral-500 font-light">Done For You (No Stress)</span>
          </div>
          <div class="p-3.5 rounded-2xl bg-white/70 backdrop-blur-md border border-black/[0.05] shadow-2xs">
            <span class="block text-2xl font-bold font-display text-neutral-900">$199 USD</span>
            <span class="text-xs text-neutral-500 font-light">Flat Transparent Setup</span>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION: THE PROBLEM & SOLUTION -->
    <section id="solucion" class="py-16 sm:py-24 bg-white border-b border-black/[0.06]">
      <div class="max-w-6xl mx-auto px-4 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-14">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100">Why Most Websites Fail</span>
          <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-neutral-900 mt-3 mb-4 tracking-tight">
            Stop losing customers to outdated websites or noisy social feeds.
          </h2>
          <p class="text-neutral-600 text-sm sm:text-base font-light">
            When people need your service, they search on Google with money in hand. If your site is slow, confusing, or nonexistent, they instantly call your competitor.
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
          <div class="p-7 rounded-3xl bg-neutral-50/70 border border-black/[0.06] shadow-2xs flex flex-col justify-between">
            <div>
              <div class="w-10 h-10 rounded-2xl bg-rose-50 text-rose-600 flex items-center justify-center font-bold mb-4">✕</div>
              <h3 class="font-bold text-lg text-neutral-900 mb-2">Social Media Rent Trap</h3>
              <p class="text-xs sm:text-sm text-neutral-600 font-light leading-relaxed">
                Organic reach on Instagram is below 5%. Answering 40 DMs just to close 1 sale wastes your time. A dedicated website closes clients with clarity 24/7.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-black/[0.05] text-[11px] font-semibold text-rose-700">
              You don't own your social account. You own your website.
            </div>
          </div>

          <div class="p-7 rounded-3xl bg-neutral-50/70 border border-black/[0.06] shadow-2xs flex flex-col justify-between">
            <div>
              <div class="w-10 h-10 rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center font-bold mb-4">⏱</div>
              <h3 class="font-bold text-lg text-neutral-900 mb-2">Bloated WordPress Sites</h3>
              <p class="text-xs sm:text-sm text-neutral-600 font-light leading-relaxed">
                Traditional agency websites take 8 seconds to load, use 40 plugins that constantly break, and quote thousands of dollars in surprise invoices.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-black/[0.05] text-[11px] font-semibold text-amber-700">
              Our websites are built with pure, ultra-clean code that never breaks.
            </div>
          </div>

          <div class="p-7 rounded-3xl bg-emerald-50/50 border border-emerald-500/20 shadow-2xs flex flex-col justify-between">
            <div>
              <div class="w-10 h-10 rounded-2xl bg-emerald-500 text-white flex items-center justify-center font-bold mb-4">✓</div>
              <h3 class="font-bold text-lg text-neutral-900 mb-2">The Erik Website Standard</h3>
              <p class="text-xs sm:text-sm text-neutral-700 font-light leading-relaxed">
                Sub-second load speed, laser-focused copy, seamless mobile navigation, and single-tap WhatsApp / booking leads straight to your phone.
              </p>
            </div>
            <div class="mt-6 pt-4 border-t border-emerald-500/20 text-[11px] font-semibold text-emerald-800">
              Live in 3-5 days for a transparent flat fee of $199 USD.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: LIVE DEMOS (Apple Hardware Cards) -->
    <section id="demos" class="py-16 sm:py-24 bg-slate-50 border-b border-black/[0.06]">
      <div class="max-w-6xl mx-auto px-4 sm:px-6">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100">Interactive Templates</span>
            <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-neutral-900 mt-3 tracking-tight">
              Test Real Live Demos by Industry
            </h2>
          </div>
          <p class="text-neutral-500 text-sm font-light max-w-md">
            Click any demo to browse a fully functional website. Every layout is customized with your branding, photos, and rates.
          </p>
        </div>

        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          
          <!-- DEMO: LAWYERS & LEGAL -->
          <div class="group bg-white rounded-3xl border border-black/[0.06] overflow-hidden hover:shadow-lg hover:border-emerald-500/20 transition-all flex flex-col justify-between">
            <div>
              <div class="h-44 bg-neutral-100 overflow-hidden relative border-b border-black/[0.05]">
                <img src="/images/guia_web_abogados_argentina.png" alt="Lawyers Website Demo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <span class="absolute top-3 right-3 text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-neutral-900/80 backdrop-blur-md text-white">Legal Practice</span>
              </div>
              <div class="p-6">
                <h3 class="font-bold text-lg text-neutral-900 mb-2">Law Firm & Attorneys</h3>
                <p class="text-xs text-neutral-600 font-light leading-relaxed mb-4">
                  Separated practice areas (Labor, Family, Real Estate), professional credentials showcase, and instant WhatsApp consultation.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="/demos/abogados/" target="_blank" class="w-full inline-flex items-center justify-center gap-2 py-2.5 rounded-full bg-neutral-900 hover:bg-black text-white text-xs font-semibold transition-all">
                <span>View Live Demo</span>
                <span>↗</span>
              </a>
            </div>
          </div>

          <!-- DEMO: DENTAL CLINIC -->
          <div class="group bg-white rounded-3xl border border-black/[0.06] overflow-hidden hover:shadow-lg hover:border-emerald-500/20 transition-all flex flex-col justify-between">
            <div>
              <div class="h-44 bg-neutral-100 overflow-hidden relative border-b border-black/[0.05]">
                <img src="/images/automatizar_turnos_consultorio_argentina.png" alt="Dental Clinic Website Demo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <span class="absolute top-3 right-3 text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-neutral-900/80 backdrop-blur-md text-white">Healthcare</span>
              </div>
              <div class="p-6">
                <h3 class="font-bold text-lg text-neutral-900 mb-2">Dental & Medical Clinic</h3>
                <p class="text-xs text-neutral-600 font-light leading-relaxed mb-4">
                  Automated appointment booking, specialties breakdown (Orthodontics, Implants), and WhatsApp inquiry routing.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="/demos/odontologia/" target="_blank" class="w-full inline-flex items-center justify-center gap-2 py-2.5 rounded-full bg-neutral-900 hover:bg-black text-white text-xs font-semibold transition-all">
                <span>View Live Demo</span>
                <span>↗</span>
              </a>
            </div>
          </div>

          <!-- DEMO: PSYCHOLOGY -->
          <div class="group bg-white rounded-3xl border border-black/[0.06] overflow-hidden hover:shadow-lg hover:border-emerald-500/20 transition-all flex flex-col justify-between">
            <div>
              <div class="h-44 bg-neutral-100 overflow-hidden relative border-b border-black/[0.05]">
                <img src="/images/guia_web_psicologos_argentina.png" alt="Psychology Website Demo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <span class="absolute top-3 right-3 text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-neutral-900/80 backdrop-blur-md text-white">Mental Health</span>
              </div>
              <div class="p-6">
                <h3 class="font-bold text-lg text-neutral-900 mb-2">Psychologists & Therapists</h3>
                <p class="text-xs text-neutral-600 font-light leading-relaxed mb-4">
                  Warm, reassuring layout with therapeutic approach overview, online session booking, and transparent session rates.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="/demos/psicologia/" target="_blank" class="w-full inline-flex items-center justify-center gap-2 py-2.5 rounded-full bg-neutral-900 hover:bg-black text-white text-xs font-semibold transition-all">
                <span>View Live Demo</span>
                <span>↗</span>
              </a>
            </div>
          </div>

          <!-- DEMO: AESTHETICS & BEAUTY -->
          <div class="group bg-white rounded-3xl border border-black/[0.06] overflow-hidden hover:shadow-lg hover:border-emerald-500/20 transition-all flex flex-col justify-between">
            <div>
              <div class="h-44 bg-neutral-100 overflow-hidden relative border-b border-black/[0.05]">
                <img src="/images/guia_web_estetica_salones_argentina.png" alt="Beauty Clinic Demo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <span class="absolute top-3 right-3 text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-neutral-900/80 backdrop-blur-md text-white">Beauty & Spa</span>
              </div>
              <div class="p-6">
                <h3 class="font-bold text-lg text-neutral-900 mb-2">Aesthetic & Beauty Centers</h3>
                <p class="text-xs text-neutral-600 font-light leading-relaxed mb-4">
                  High-definition before/after gallery, treatment catalogs, and direct slot booking without commissions.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="/demos/estetica/" target="_blank" class="w-full inline-flex items-center justify-center gap-2 py-2.5 rounded-full bg-neutral-900 hover:bg-black text-white text-xs font-semibold transition-all">
                <span>View Live Demo</span>
                <span>↗</span>
              </a>
            </div>
          </div>

          <!-- DEMO: HOME SERVICES & TRADES -->
          <div class="group bg-white rounded-3xl border border-black/[0.06] overflow-hidden hover:shadow-lg hover:border-emerald-500/20 transition-all flex flex-col justify-between">
            <div>
              <div class="h-44 bg-neutral-100 overflow-hidden relative border-b border-black/[0.05]">
                <img src="/images/guia_web_oficios_hogar_argentina.png" alt="Emergency Services Demo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <span class="absolute top-3 right-3 text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-neutral-900/80 backdrop-blur-md text-white">Emergency Services</span>
              </div>
              <div class="p-6">
                <h3 class="font-bold text-lg text-neutral-900 mb-2">Home Services & Emergency Trades</h3>
                <p class="text-xs text-neutral-600 font-light leading-relaxed mb-4">
                  Plumbing, electrical, and locksmiths. 24/7 emergency button, local area service map, and verified credentials.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="/demos/urgencias-hogar/" target="_blank" class="w-full inline-flex items-center justify-center gap-2 py-2.5 rounded-full bg-neutral-900 hover:bg-black text-white text-xs font-semibold transition-all">
                <span>View Live Demo</span>
                <span>↗</span>
              </a>
            </div>
          </div>

          <!-- DEMO: ACCOUNTING & CONSULTING -->
          <div class="group bg-white rounded-3xl border border-black/[0.06] overflow-hidden hover:shadow-lg hover:border-emerald-500/20 transition-all flex flex-col justify-between">
            <div>
              <div class="h-44 bg-neutral-100 overflow-hidden relative border-b border-black/[0.05]">
                <img src="/images/guia_web_estudios_contables_argentina.png" alt="Accounting Firm Demo" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <span class="absolute top-3 right-3 text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full bg-neutral-900/80 backdrop-blur-md text-white">Finance & Tax</span>
              </div>
              <div class="p-6">
                <h3 class="font-bold text-lg text-neutral-900 mb-2">Accounting & Tax Advisory</h3>
                <p class="text-xs text-neutral-600 font-light leading-relaxed mb-4">
                  Institutional authority, diagnostic forms for SMEs, and transparent monthly bookkeeping plans.
                </p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <a href="/demos/contable/" target="_blank" class="w-full inline-flex items-center justify-center gap-2 py-2.5 rounded-full bg-neutral-900 hover:bg-black text-white text-xs font-semibold transition-all">
                <span>View Live Demo</span>
                <span>↗</span>
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION: HOW IT WORKS (3 Simple Steps) -->
    <section id="proceso" class="py-16 sm:py-24 bg-white border-b border-black/[0.06]">
      <div class="max-w-5xl mx-auto px-4 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-14">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100">Zero Technical Hassle</span>
          <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-neutral-900 mt-3 mb-4 tracking-tight">
            From raw idea to published website in 3 days
          </h2>
          <p class="text-neutral-500 text-sm font-light">
            You don't need to learn code, write essays, or configure servers. We take care of everything.
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
          <div class="p-6 rounded-3xl bg-neutral-50/70 border border-black/[0.06]">
            <span class="w-10 h-10 rounded-full bg-neutral-900 text-white flex items-center justify-center font-bold text-sm mb-4">1</span>
            <h3 class="font-bold text-base text-neutral-900 mb-2">Send 3 Voice Notes</h3>
            <p class="text-xs text-neutral-600 font-light leading-relaxed">
              Tell us about your services, send a couple of photos, and share your rates. That's all we need.
            </p>
          </div>

          <div class="p-6 rounded-3xl bg-neutral-50/70 border border-black/[0.06]">
            <span class="w-10 h-10 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-sm mb-4">2</span>
            <h3 class="font-bold text-base text-neutral-900 mb-2">We Build & Optimize</h3>
            <p class="text-xs text-neutral-600 font-light leading-relaxed">
              We write compelling sales copy, craft the responsive UI, optimize mobile speed, and connect your WhatsApp buttons.
            </p>
          </div>

          <div class="p-6 rounded-3xl bg-neutral-50/70 border border-black/[0.06]">
            <span class="w-10 h-10 rounded-full bg-neutral-900 text-white flex items-center justify-center font-bold text-sm mb-4">3</span>
            <h3 class="font-bold text-base text-neutral-900 mb-2">Live & Converting</h3>
            <p class="text-xs text-neutral-600 font-light leading-relaxed">
              You review the private preview, request any adjustments, and we launch your site under your custom domain.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION: CLEAR PRICING ($199 USD) -->
    <section id="precios" class="py-16 sm:py-24 bg-slate-50 border-b border-black/[0.06]">
      <div class="max-w-5xl mx-auto px-4 sm:px-6">
        
        <div class="text-center max-w-2xl mx-auto mb-14">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100">Simple & Predictable</span>
          <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-neutral-900 mt-3 mb-4 tracking-tight">
            Transparent Pricing. No Surprise Bills.
          </h2>
          <p class="text-neutral-500 text-sm font-light">
            One flat upfront fee for setup and development, plus optional worry-free monthly care.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 items-stretch max-w-4xl mx-auto">
          
          <!-- MAIN SETUP CARD ($199 USD) -->
          <div class="p-8 rounded-3xl bg-white border-2 border-emerald-500 shadow-xl relative flex flex-col justify-between">
            <div class="absolute -top-3.5 right-6 bg-neutral-900 text-emerald-400 text-[10px] font-bold uppercase tracking-wider px-3 py-1 rounded-full border border-white/[0.1]">
              MOST POPULAR
            </div>

            <div>
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Initial Setup & Build</span>
              <h3 class="text-2xl font-extrabold font-display text-neutral-900 mt-1 mb-3">Complete Website</h3>
              <p class="text-xs text-neutral-500 font-light leading-relaxed mb-6">
                Everything you need to showcase your business professionally and capture high-intent inquiries.
              </p>

              <div class="flex items-baseline gap-2 mb-6 pb-6 border-b border-black/[0.06]">
                <span class="text-4xl sm:text-5xl font-extrabold font-display text-neutral-900">$199</span>
                <span class="text-neutral-500 text-sm font-semibold">USD (One-time)</span>
              </div>

              <ul class="text-xs sm:text-sm text-neutral-700 space-y-3 font-light mb-8">
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-500 font-bold">✓</span>
                  <span><strong>Bespoke responsive design:</strong> Sub-second load time on iPhones & Android.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-500 font-bold">✓</span>
                  <span><strong>Custom domain + SSL certificate:</strong> Full technical setup included.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-500 font-bold">✓</span>
                  <span><strong>Persuasive copywriting:</strong> Written from your voice notes.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-500 font-bold">✓</span>
                  <span><strong>Direct WhatsApp / Email routing:</strong> Pre-filled quick conversion links.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-500 font-bold">✓</span>
                  <span><strong>Guaranteed delivery:</strong> Ready in 3 to 5 business days.</span>
                </li>
              </ul>
            </div>

            <a href="https://wa.me/5492645185359?text=Hello%20Erik!%20I'm%20ready%20to%20order%20my%20website%20for%20%24199%20USD." 
               target="_blank" 
               rel="noopener noreferrer"
               class="w-full inline-flex items-center justify-center gap-2 py-3.5 rounded-full bg-gradient-to-b from-emerald-500 to-emerald-600 text-white font-semibold text-sm shadow-md hover:brightness-105 active:scale-[0.98] transition-all">
              <span>Order via WhatsApp ($199 USD)</span>
              <span>→</span>
            </a>
          </div>

          <!-- MONTHLY CARE CARD ($20 USD/mo) -->
          <div class="p-8 rounded-3xl bg-neutral-900 text-white border border-white/[0.08] shadow-lg flex flex-col justify-between">
            <div>
              <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Monthly Care & Hosting</span>
              <h3 class="text-2xl font-extrabold font-display text-white mt-1 mb-3">Cloud Care Plan</h3>
              <p class="text-xs text-neutral-400 font-light leading-relaxed mb-6">
                Leave the server monitoring, security, updates, and domain renewals to us.
              </p>

              <div class="flex items-baseline gap-2 mb-6 pb-6 border-b border-white/[0.08]">
                <span class="text-4xl sm:text-5xl font-extrabold font-display text-white">$20</span>
                <span class="text-neutral-400 text-sm font-semibold">USD / month</span>
              </div>

              <div class="inline-block px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-bold mb-6">
                🎁 1st Month Included 100% Free
              </div>

              <ul class="text-xs sm:text-sm text-neutral-300 space-y-3 font-light mb-8">
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-400 font-bold">✓</span>
                  <span><strong>Ultra-fast cloud hosting</strong> with 99.9% uptime.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-400 font-bold">✓</span>
                  <span><strong>Annual domain renewal</strong> & automated SSL certificates.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-400 font-bold">✓</span>
                  <span><strong>Up to 3 content/price updates per month</strong> handled for you.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-400 font-bold">✓</span>
                  <span><strong>Continuous security backups</strong> and malware monitoring.</span>
                </li>
                <li class="flex items-start gap-2.5">
                  <span class="text-emerald-400 font-bold">✓</span>
                  <span><strong>Cancel anytime:</strong> Zero lock-in contracts.</span>
                </li>
              </ul>
            </div>

            <div class="p-4 rounded-2xl bg-white/[0.05] border border-white/[0.08] text-center">
              <span class="text-xs text-neutral-400 font-light">
                Starts from month 2. Full source buyout available for $200 USD.
              </span>
            </div>
          </div>

        </div>

        <!-- PAYMENT METHODS ACCEPTED BANNER -->
        <div class="mt-12 p-6 rounded-3xl bg-white border border-black/[0.06] shadow-2xs max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
          <div>
            <h4 class="font-bold text-neutral-900 text-sm">International Payment Methods Accepted:</h4>
            <p class="text-xs text-neutral-500 font-light">Secure, fast, and transparent invoice delivery for every project.</p>
          </div>
          <div class="flex flex-wrap items-center justify-center gap-2">
            <span class="px-3 py-1 rounded-full bg-slate-100 text-neutral-800 text-xs font-bold border border-slate-200">PayPal</span>
            <span class="px-3 py-1 rounded-full bg-slate-100 text-neutral-800 text-xs font-bold border border-slate-200">Wise</span>
            <span class="px-3 py-1 rounded-full bg-slate-100 text-neutral-800 text-xs font-bold border border-slate-200">Bank Wire (SWIFT / ACH)</span>
            <span class="px-3 py-1 rounded-full bg-slate-100 text-neutral-800 text-xs font-bold border border-slate-200">USDT / Crypto</span>
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION: FAQ -->
    <section id="faq" class="py-16 sm:py-24 bg-white border-b border-black/[0.06]">
      <div class="max-w-4xl mx-auto px-4 sm:px-6">
        <div class="text-center max-w-2xl mx-auto mb-14">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100">Got Questions?</span>
          <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-neutral-900 mt-3 mb-4 tracking-tight">
            Frequently Asked Questions
          </h2>
          <p class="text-neutral-500 text-sm font-light">
            Everything you need to know about our workflow, delivery, and pricing.
          </p>
        </div>

        <div class="space-y-4">
          
          <details class="group p-5 rounded-2xl bg-neutral-50 border border-black/[0.06] transition-all cursor-pointer">
            <summary class="font-bold text-neutral-900 text-sm sm:text-base list-none flex items-center justify-between gap-4">
              <span>How fast will my website be live?</span>
              <span class="text-neutral-400 group-open:rotate-180 transition-transform">▼</span>
            </summary>
            <p class="text-xs sm:text-sm text-neutral-600 font-light leading-relaxed mt-3 pt-3 border-t border-black/[0.05]">
              Your website is live within 3 to 5 business days once we receive your business details and initial 50% deposit. You review a private staging link before we publish it live.
            </p>
          </details>

          <details class="group p-5 rounded-2xl bg-neutral-50 border border-black/[0.06] transition-all cursor-pointer">
            <summary class="font-bold text-neutral-900 text-sm sm:text-base list-none flex items-center justify-between gap-4">
              <span>Do I need to write long texts or provide graphics?</span>
              <span class="text-neutral-400 group-open:rotate-180 transition-transform">▼</span>
            </summary>
            <p class="text-xs sm:text-sm text-neutral-600 font-light leading-relaxed mt-3 pt-3 border-t border-black/[0.05]">
              No! That is our job. Simply share 3 voice notes explaining what your business offers, who your clients are, and your prices. We curate high-resolution visuals and write persuasive copy for you.
            </p>
          </details>

          <details class="group p-5 rounded-2xl bg-neutral-50 border border-black/[0.06] transition-all cursor-pointer">
            <summary class="font-bold text-neutral-900 text-sm sm:text-base list-none flex items-center justify-between gap-4">
              <span>What happens if I want to self-host or manage the site myself later?</span>
              <span class="text-neutral-400 group-open:rotate-180 transition-transform">▼</span>
            </summary>
            <p class="text-xs sm:text-sm text-neutral-600 font-light leading-relaxed mt-3 pt-3 border-t border-black/[0.05]">
              You are never locked in. If you ever decide to take over full management, you can acquire complete ownership, code repository rights, and all production files for a single buyout equal to 10 months of maintenance ($200 USD).
            </p>
          </details>

          <details class="group p-5 rounded-2xl bg-neutral-50 border border-black/[0.06] transition-all cursor-pointer">
            <summary class="font-bold text-neutral-900 text-sm sm:text-base list-none flex items-center justify-between gap-4">
              <span>Why choose a bespoke site over Squarespace or Wix?</span>
              <span class="text-neutral-400 group-open:rotate-180 transition-transform">▼</span>
            </summary>
            <p class="text-xs sm:text-sm text-neutral-600 font-light leading-relaxed mt-3 pt-3 border-t border-black/[0.05]">
              Wix and generic builders charge high monthly fees, load slowly on mobile phones, and look template-made. Our sites are engineered with lightweight code, loading in under 0.8s, with an unmistakable Apple-level finish.
            </p>
          </details>

        </div>
      </div>
    </section>

    <!-- SECTION: FINAL CTA -->
    <section class="py-20 bg-neutral-900 text-white relative overflow-hidden">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 text-center relative z-10">
        <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-3 py-1 rounded-full mb-4 inline-block">
          Ready to Grow Your Business?
        </span>
        <h2 class="text-3xl sm:text-5xl font-extrabold font-display text-white mt-2 mb-4 tracking-tight">
          Let's build a website your clients will love.
        </h2>
        <p class="text-neutral-400 text-sm sm:text-base font-light max-w-xl mx-auto mb-8">
          Flat fee of $199 USD. Delivery in 3-5 business days. Talk directly with Erik to discuss your project.
        </p>

        <a href="https://wa.me/5492645185359?text=Hello%20Erik!%20I'm%20ready%20to%20build%20my%20website%20for%20%24199%20USD."
           target="_blank"
           rel="noopener noreferrer"
           class="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-full bg-gradient-to-b from-emerald-500 to-emerald-600 text-white font-bold text-base shadow-[0_10px_25px_-5px_rgba(16,185,129,0.5)] hover:brightness-105 active:scale-[0.98] transition-all">
          <span>Start Project via WhatsApp</span>
          <span>→</span>
        </a>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="bg-[#1d1d1f] text-neutral-400 py-12 border-t border-white/[0.08] text-xs">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <span class="font-display font-extrabold text-white text-sm">Erik <span class="text-emerald-400">Website</span></span>
        <span>•</span>
        <span>Bespoke Web Development for Businesses & Pros</span>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-6 text-neutral-400">
        <a href="#demos" class="hover:text-white transition-colors">Demos</a>
        <a href="#precios" class="hover:text-white transition-colors">Pricing</a>
        <a href="/blog/" class="hover:text-white transition-colors">Blog (ES)</a>
        <a href="/terminos" class="hover:text-white transition-colors">Terms & Conditions</a>
        <a href="https://wa.me/5492645185359?text=Hello%20Erik!%20I'd%20like%20to%20ask%20a%20question%20about%20your%20services." target="_blank" rel="noopener noreferrer" class="text-emerald-400 hover:text-emerald-300 font-semibold">WhatsApp</a>
      </div>
    </div>

    <div class="max-w-6xl mx-auto px-4 sm:px-6 mt-8 pt-8 border-t border-white/[0.05] text-center text-neutral-500 text-[11px]">
      © 2026 erikwebsite.com. Developed by Erik Ladstatter. All rights reserved.
    </div>
  </footer>

  <!-- PERSISTENT WHATSAPP FLOATING BUTTON -->
  <aside class="fixed bottom-5 right-5 z-50 flex items-center group">
    <span class="hidden sm:inline-block mr-3 bg-neutral-900/90 text-white text-xs font-medium py-1.5 px-3.5 rounded-full shadow-lg backdrop-blur-xl opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none whitespace-nowrap border border-white/[0.1]">
      Chat on WhatsApp
    </span>
    <a href="https://wa.me/5492645185359?text=Hello%20Erik!%20I'm%20interested%20in%20building%20a%20modern%20website%20for%20my%20business."
       target="_blank"
       rel="noopener noreferrer"
       class="w-14 h-14 bg-gradient-to-b from-emerald-500 to-emerald-600 shadow-[0_8px_20px_-4px_rgba(16,185,129,0.45)] text-white rounded-full flex items-center justify-center transition-transform duration-200 hover:scale-105 active:scale-95 cursor-pointer"
       aria-label="Contact Erik on WhatsApp">
      <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24">
        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/>
      </svg>
    </a>
  </aside>

  <!-- Script principal -->
  <script type="module" src="/src/js/main.js"></script>
</body>
</html>"""

with open('en/index.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

print("Generated en/index.html successfully!")
