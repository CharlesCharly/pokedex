export default {
  srcDir: "src/",
  ssr: false,

  head: {
    title: "pokedex",
    htmlAttrs: {
      lang: "en",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },

  // https://go.nuxtjs.dev/config-css
  css: ["@/assets/styles/tailwind.css"],

  // https://go.nuxtjs.dev/config-plugins
  plugins: ["@/plugins/api.js", "@/plugins/helpers.js"],

  // https://go.nuxtjs.dev/config-components
  components: true,

  // https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    "@nuxtjs/tailwindcss",
  ],

  // https://go.nuxtjs.dev/config-modules
  modules: ["@nuxtjs/axios"],

  // https://go.nuxtjs.dev/config-build
  build: {},
};
