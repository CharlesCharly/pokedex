import { getField, updateField } from "vuex-map-fields";
import * as URL from "@/api/config";
import Vue from "vue";

const getDefaultState = () => ({
  pokemonList: [],
  pokemon: [],
  pokemonTypes: [],
});

export const state = () => getDefaultState();

export const getters = {
  getField,
};

export const actions = {
  async getPokemonList({ commit, state }, payload) {
    // Default URL to get the Pokemon list
    let pokemonListUrl = `${URL.POKEMON_LIST}?sortFilter=${payload.sortFilter}&typeFilter=${payload.typeFilter}&asc=${payload.asc}&searchQuery=${payload.searchQuery}`;

    try {
      const pokemonList = await this.$api.get(pokemonListUrl);
      commit("setPokemonList", pokemonList);
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
  }
};
