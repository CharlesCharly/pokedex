<template>
  <div>
    <div>
      <Header>
        <template #title>
          <p>Pokedex</p>
        </template>
      </Header>
    </div>

    <div>
      <PokedexFilters
        :search-query="searchQuery"
        :sort-filter="sortFilter"
        :is-asc="asc"
        :type-filter="typeFilter"
        :pokemon-types="pokemonTypes"
        @handleChange="handleFilters"
      />
    </div>

    <div>
      <PokemonCard
        v-for="pokemon in pokemonList"
        :key="pokemon.pokedex_number"
        :pokemon="pokemon"
      />
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { mapFields } from "vuex-map-fields";
import Header from "@/components/layout/Header.vue";
import PokedexFilters from "@/components/filters/PokedexFilters.vue";
import PokemonCard from "@/components/cards/PokemonCard.vue";

export default {
  name: "Pokedex",
  components: {
    Header,
    PokedexFilters,
    PokemonCard,
  },
  data() {
    return {
      searchQuery: "",
      sortFilter: "pokedex_number",
      typeFilter: "all",
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
    handleFilters(data) {
      this.getPokemonList({
        searchQuery: data.search,
        sortFilter: data.radiobtn,
        asc: data.checkbox,
        typeFilter: data.type,
      });
    },
  },
};
</script>
