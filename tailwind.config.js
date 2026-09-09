/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./demos/**/*.{html,js}",
    "./src/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0fdf4',
          100: '#dcfce7',
          500: '#22c55e',
          600: '#16a34a',
          700: '#15803d',
          900: '#14532d',
        },
        primary: {
          50: '#f8fafc',
          100: '#f1f5f9',
          500: '#0ea5e9',
          600: '#0284c7',
          700: '#0369a1',
          900: '#0f172a',
        },
        clinic: {
          50: '#fdf8f6',
          100: '#f2e8e5',
          200: '#eaddd7',
          400: '#c59f93',
          500: '#a8786a',
          600: '#8e5e51',
          700: '#734a3e',
          800: '#5c3b32',
          900: '#432a24',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        display: ['Plus Jakarta Sans', 'Inter', 'system-ui', 'sans-serif'],
        serif: ['Playfair Display', 'Georgia', 'serif'],
      },
      boxShadow: {
        'glow-green': '0 0 25px -5px rgba(34, 197, 94, 0.4)',
        'glow-primary': '0 0 25px -5px rgba(14, 165, 233, 0.35)',
        'glow-rose': '0 0 25px -5px rgba(168, 120, 106, 0.35)',
      }
    },
  },
  plugins: [],
}
