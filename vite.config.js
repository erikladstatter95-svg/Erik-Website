import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        terminos: resolve(__dirname, 'terminos.html'),
        // Demos Semánticas Principales
        estetica: resolve(__dirname, 'demos/estetica/index.html'),
        odontologia: resolve(__dirname, 'demos/odontologia/index.html'),
        psicologia: resolve(__dirname, 'demos/psicologia/index.html'),
        vajilla: resolve(__dirname, 'demos/vajilla/index.html'),
        catering: resolve(__dirname, 'demos/catering/index.html'),
        salones: resolve(__dirname, 'demos/salones/index.html'),
        abogados: resolve(__dirname, 'demos/abogados/index.html'),
        urgencias_hogar: resolve(__dirname, 'demos/urgencias-hogar/index.html'),
        contable: resolve(__dirname, 'demos/contable/index.html'),
        // Retrocompatibilidad
        servicios_hogar_legacy: resolve(__dirname, 'demos/servicios-hogar/index.html'),
        eventos_legacy: resolve(__dirname, 'demos/eventos/index.html'),
        cluster1_legacy: resolve(__dirname, 'demos/cluster-1/index.html'),
        cluster1_odontologia_legacy: resolve(__dirname, 'demos/cluster-1/odontologia.html'),
        cluster1_psicologia_legacy: resolve(__dirname, 'demos/cluster-1/psicologia.html'),
        cluster2_legacy: resolve(__dirname, 'demos/cluster-2/index.html'),
        cluster2_catering_legacy: resolve(__dirname, 'demos/cluster-2/catering.html'),
        cluster2_salones_legacy: resolve(__dirname, 'demos/cluster-2/salones.html'),
        cluster3_legacy: resolve(__dirname, 'demos/cluster-3/index.html'),
        cluster3_urgencias_legacy: resolve(__dirname, 'demos/cluster-3/urgencias.html'),
        cluster3_contable_legacy: resolve(__dirname, 'demos/cluster-3/contable.html'),
      },
    },
  },
});
