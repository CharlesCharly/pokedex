<template>
  <div class="flex flex-col items-center justify-center">
    <div class="flex">
      <Header>
        <template #title>
          <img src="~/assets/images/pokemon.png" class="inline h-24 w-72">
        </template>
      </Header>
    </div>

    <div class="flex">
      <PokedexFilters
        :search-query="searchQuery"
        :sort-filter="sortFilter"
        :is-asc="asc"
        :type-filter="typeFilter"
        :pokemon-types="pokemonTypes"
        @handleChange="handleFilters"
      />
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 mt-8">
      <PokemonCard
        v-for="pokemon in pokemonList"
        :key="pokemon.id"
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
