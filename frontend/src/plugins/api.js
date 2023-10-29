export default ({ app, store }, inject) => {
  inject("api", {
    async wrapper(endpoint, params, config, verb = "$get") {
      app.$axios.setHeader("Content-Type", "application/json;charset=UTF-8");
      app.$axios.setHeader("Accept", "application/json;charset=UTF-8");
      //TO IMPROVE - Add token
      // const token = await StylePropertyMap.dispatch("auth/getIdToken");
      // app.$axios.setToken(token, "Bearer");

      return app.$axios[verb](endpoint, params, config);
    },

    async get(endpoint, params, config) {
      return app.$api.wrapper(endpoint, params, config, "$get");
    },

    async post(endpoint, params, config) {
      return app.$api.wrapper(endpoint, params, config, "$post");
    },

    async put(endpoint, params, config) {
      return app.$api.wrapper(endpoint, params, config, "$put");
    },

    async delete(endpoint, params, config) {
      return app.$api.wrapper(endpoint, params, config, "$delete");
    },

    async patch(endpoint, params, config) {
      return app.$api.wrapper(endpoint, params, config, "$patch");
    },
  });
};
