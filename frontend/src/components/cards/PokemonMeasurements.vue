<template>
  <div>
    <span class="mr-2">
      <img src="~/assets/images/height.png" class="h-6 w-6 inline" />
      {{ pokemonHeight }} m
    </span>
    <span class="ml-2">
      <img src="~/assets/images/weight.png" class="h-6 w-6 inline" />
      {{ pokemonWeight }} kg
    </span>
  </div>
</template>

<script>
export default {
  name: "PokemonType",
  props: {
    pokemon: {
      type: Object,
      default: () => {},
    },
  },
  computed: {
    pokemonHeight() {
      return this.pokemon.height_m ? this.pokemon.height_m : "?";
    },
    pokemonWeight() {
      return this.pokemon.weight_kg ? this.pokemon.weight_kg : "?";
    },
  },
};
</script>
