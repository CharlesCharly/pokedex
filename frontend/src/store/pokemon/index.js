import { getField } from "vuex-map-fields";
import * as URL from "@/api/config";
import Vue from "vue";

const getDefaultState = () => ({
  pokemonList: [],
  pokemon: [],
});

export const state = () => getDefaultState();

export const getters = {
  getField,
};

export const actions = {
  async getPokemonList({ commit, state }, payload) {
    // Default URL to get the Pokemon list
    let pokemonListUrl = URL.POKEMON_LIST;

    const pokemonList = await this.$api.get(pokemonListUrl);
    commit("setPokemonList", pokemonList);
  },
};

export const mutations = {
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
};
