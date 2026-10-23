import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        en_main: resolve(__dirname, 'en/index.html'),
        terminos: resolve(__dirname, 'terminos.html'),
        terminos_clean: resolve(__dirname, 'terminos/index.html'),
        // Blog Hub y Artículos Cluster SEO/GEO
        blog: resolve(__dirname, 'blog/index.html'),
        blog_cuanto_cuesta: resolve(__dirname, 'blog/cuanto-cuesta-una-pagina-web-argentina/index.html'),
        blog_google_maps: resolve(__dirname, 'blog/como-conseguir-clientes-google-maps/index.html'),
        blog_web_vs_ig: resolve(__dirname, 'blog/pagina-web-vs-instagram/index.html'),
        blog_abogados: resolve(__dirname, 'blog/paginas-web-para-abogados-argentina/index.html'),
        blog_turnos: resolve(__dirname, 'blog/como-automatizar-turnos-consultorio/index.html'),
        blog_que_negocios: resolve(__dirname, 'blog/que-negocios-necesitan-una-pagina-web/index.html'),
        blog_psicologos: resolve(__dirname, 'blog/paginas-web-para-psicologos-argentina/index.html'),
        blog_oficios: resolve(__dirname, 'blog/paginas-web-oficios-servicios-hogar/index.html'),
        blog_contables: resolve(__dirname, 'blog/paginas-web-estudios-contables-argentina/index.html'),
        blog_estetica: resolve(__dirname, 'blog/paginas-web-salones-belleza-estetica/index.html'),
        blog_eventos: resolve(__dirname, 'blog/paginas-web-salones-eventos-catering/index.html'),
        blog_fitness: resolve(__dirname, 'blog/paginas-web-personal-trainers-gimnasios/index.html'),
        blog_por_que_web: resolve(__dirname, 'blog/por-que-tener-una-pagina-web/index.html'),
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
        fitness: resolve(__dirname, 'demos/fitness/index.html'),
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
        cluster3_fitness_legacy: resolve(__dirname, 'demos/cluster-3/fitness.html'),
      },
    },
  },
});
