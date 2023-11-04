import { getField, updateField } from "vuex-map-fields";
import * as URL from "@/api/config";
import Vue from "vue";

const getDefaultState = () => ({
  pokemonList: [],
  previousListPage: null,
  nextListPage: null,
  sizePokemonList: null,
  pokemon: [],
  pokemonTypes: [],
});

export const state = () => getDefaultState();

export const getters = {
  getField,
};

export const actions = {
  async getPokemonList({ commit, state }, payload) {
    let pokemonListUrl;

    // If pageUrl key is part of the payload, we are using the pagination
    // The URL is already built
    if (payload.pageUrl) {
      pokemonListUrl = payload.pageUrl;
    } else {
      // Otherwise we are building the URL based on filters
      pokemonListUrl = `${URL.POKEMON_LIST}?sortFilter=${payload.sortFilter}&typeFilter=${payload.typeFilter}&asc=${payload.asc}&searchQuery=${payload.searchQuery}`;
    }

    try {
      const data = await this.$api.get(pokemonListUrl);

      commit("setPokemonList", data.results);
      commit("setPreviousListPage", data.previous);
      commit("setNextListPage", data.next);
      commit("setSizePokemonList", data.count);
    } catch (error) {
      console.error(error);
    }
  },

  async getPokemonTypes({ commit, state }, payload) {
    let pokemonTypesURL = URL.POKEMON_TYPES;

    try {
      const pokemonTypes = await this.$api.get(pokemonTypesURL);

      commit("setPokemonTypes", pokemonTypes);
    } catch (error) {
      console.error(error);
    }
  },

  async getPokemonDetail({ commit, state }, payload) {
    let pokemonDetailUrl = `${URL.POKEMON_DETAIL}${payload}`;

    try {
      const pokemonDetail = await this.$api.get(pokemonDetailUrl);

      commit("setPokemonDetail", pokemonDetail);
    } catch (error) {
      console.error(error);
    }
  },
};

export const mutations = {
  updateField,

  resetState(currentState) {
    Object.assign(currentState, getDefaultState());
  },

  setPokemonList(state, payload) {
    if (payload) {
      Vue.set(state, "pokemonList", payload);
    } else {
      Vue.set(state, "pokemonList", []);
    }
  },

  setPreviousListPage(state, payload) {
    if (payload) {
      Vue.set(state, "previousListPage", payload);
    } else {
      Vue.set(state, "previousListPage", null);
    }
  },

  setNextListPage(state, payload) {
    if (payload) {
      Vue.set(state, "nextListPage", payload);
    } else {
      Vue.set(state, "nextListPage", null);
    }
  },

  setSizePokemonList(state, payload) {
    if (payload) {
      Vue.set(state, "sizePokemonList", payload);
    } else {
      Vue.set(state, "sizePokemonList", null);
    }
  },

  setPokemonTypes(state, payload) {
    if (payload) {
      Vue.set(state, "pokemonTypes", payload);
    } else {
      Vue.set(state, "pokemonTypes", []);
    }
  },

  setPokemonDetail(state, payload) {
    if (payload) {
      Vue.set(state, "pokemon", payload);
    } else {
      Vue.set(state, "pokemon", []);
    }
  },
};
