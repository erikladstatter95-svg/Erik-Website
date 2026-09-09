import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        estetica: resolve(__dirname, 'demos/estetica/index.html'),
        eventos: resolve(__dirname, 'demos/eventos/index.html'),
        abogados: resolve(__dirname, 'demos/abogados/index.html'),
      },
    },
  },
});
