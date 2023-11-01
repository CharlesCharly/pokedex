<template>
  <div>
    <div>
      <label>
        <input type="radio" v-model="sortFilter" value="pokedex_number" />
        Number
      </label>
      <label>
        <input type="radio" v-model="sortFilter" value="height_m" /> Height
      </label>
      <label>
        <input type="radio" v-model="sortFilter" value="weight_kg" /> Weight
      </label>
      <label> <input type="checkbox" v-model="asc" /> Ascending </label>
      <button @click="handleFilters">Apply Filter</button>
    </div>

    <div>
      <input
        v-model="searchQuery"
        @input="handleFilters"
        placeholder="Search..."
      />
    </div>

    <div>
      <label for="pokemonType">Pokemon Type:</label>
      <select id="pokemonType" v-model="typeFilter" @change="handleFilters">
        <option value="all_types">All Types</option>
        <option v-for="type in pokemonTypes" :value="type">{{ type }}</option>
      </select>
    </div>

    <div v-for="pokemon in pokemonList" :key="pokemon.id">
      {{ pokemon }}
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { mapFields } from "vuex-map-fields";

export default {
  name: "Pokedex",
  data() {
    return {
      searchQuery: "",
      sortFilter: "pokedex_number",
      typeFilter: "all_types",
      asc: true,
    };
  },
  computed: {
    ...mapFields("pokemon", ["pokemonList", "pokemonTypes"]),
  },
  created() {
    const searchQuery = this.searchQuery;
    const sortFilter = this.sortFilter;
    const typeFilter = this.typeFilter;
    const asc = this.asc;

    this.getPokemonTypes();
    this.getPokemonList({ searchQuery, sortFilter, typeFilter, asc });
  },
  methods: {
    ...mapActions({
      getPokemonList: "pokemon/getPokemonList",
      getPokemonTypes: "pokemon/getPokemonTypes",
    }),
    handleFilters() {
      this.getPokemonList({
        searchQuery: this.searchQuery,
        sortFilter: this.sortFilter,
        typeFilter: this.typeFilter,
        asc: this.asc,
      });
    },
  },
};
</script>
