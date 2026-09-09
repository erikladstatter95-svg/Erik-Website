import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        // Cluster 1
        cluster1_estetica: resolve(__dirname, 'demos/cluster-1/index.html'),
        cluster1_odontologia: resolve(__dirname, 'demos/cluster-1/odontologia.html'),
        cluster1_psicologia: resolve(__dirname, 'demos/cluster-1/psicologia.html'),
        // Cluster 2
        cluster2_vajilla: resolve(__dirname, 'demos/cluster-2/index.html'),
        cluster2_catering: resolve(__dirname, 'demos/cluster-2/catering.html'),
        cluster2_salones: resolve(__dirname, 'demos/cluster-2/salones.html'),
        // Cluster 3
        cluster3_abogados: resolve(__dirname, 'demos/cluster-3/index.html'),
        cluster3_urgencias: resolve(__dirname, 'demos/cluster-3/urgencias.html'),
        cluster3_contable: resolve(__dirname, 'demos/cluster-3/contable.html'),
        // Retrocompatibilidad
        estetica_legacy: resolve(__dirname, 'demos/estetica/index.html'),
        eventos_legacy: resolve(__dirname, 'demos/eventos/index.html'),
        abogados_legacy: resolve(__dirname, 'demos/abogados/index.html'),
        servicios_hogar_legacy: resolve(__dirname, 'demos/servicios-hogar/index.html'),
      },
    },
  },
});
