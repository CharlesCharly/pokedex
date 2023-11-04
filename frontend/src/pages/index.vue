<template>
  <div class="flex flex-col items-center justify-center">
    <!-- Header with the logo -->
    <div class="flex">
      <Header>
        <template #title>
          <img src="~/assets/images/pokemon.png" class="inline h-24 w-72" />
        </template>
      </Header>
    </div>

    <!-- Filters block -->
    <div class="flex">
      <PokedexFilters
        :search-query="searchQuery"
        :sort-filter="sortFilter"
        :is-asc="asc"
        :type-filter="typeFilter"
        :pokemon-types="$helpers.capitalizeFirstLetter(pokemonTypes)"
        @handleChange="handleFilters"
      />
    </div>

    <!-- Display total number of results -->
    <div class="flex">
      <div class="w-full items-center justify-center mt-6">
        <span class="font-bold italic text-blue-800">
          <img src="~/assets/images/pokeball.png" class="h-4 w-4 inline" />
          {{ pokemonsFound }} Pokemons have been found !
        </span>
      </div>
    </div>

    <!-- Pokemons cards listing -->
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 mt-8"
    >
      <PokemonCard
        v-for="pokemon in pokemonList"
        :key="pokemon.id"
        :pokemon="pokemon"
      />
    </div>

    <!-- Pagination button -->
    <div class="flex">
      <Pagination
        :previous-page-url="previousListPage"
        :next-page-url="nextListPage"
        @newPage="newListingPage"
      />
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { mapFields } from "vuex-map-fields";
import Header from "@/components/layout/Header.vue";
import Pagination from "@/components/layout/Pagination.vue";
import PokedexFilters from "@/components/filters/PokedexFilters.vue";
import PokemonCard from "@/components/cards/PokemonCard.vue";

export default {
  name: "Pokedex",
  components: {
    Header,
    Pagination,
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
    ...mapFields("pokemon", [
      "pokemonList",
      "previousListPage",
      "nextListPage",
      "sizePokemonList",
      "pokemonTypes",
    ]),
    pokemonsFound() {
      return this.sizePokemonList ? this.sizePokemonList : 0;
    },
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
      const typeFilter = this.$helpers.toLowerCase(data.type)

      this.getPokemonList({
        searchQuery: data.search,
        sortFilter: data.radiobtn,
        asc: data.checkbox,
        typeFilter: typeFilter,
      });
    },
    newListingPage(pageUrl) {
      this.getPokemonList({ pageUrl });
      this.$helpers.scrollToTop();
    },
  },
};
</script>
