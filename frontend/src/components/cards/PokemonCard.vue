<template>
  <NuxtLink :to="`/pokemon/${pokemon.pokedex_number}`" target="_blank">
    <div class="rounded-lg shadow-inner m-2">
      <!-- Pokemon img -->
      <div class="flex items-center justify-center pt-2">
        <img :src="$helpers.pokemonImgUrl(pokemon.pokedex_number)" />
      </div>

      <div class="px-6 py-4">
        <!-- Pokemon number and name -->
        <div class="flex items-center justify-center font-bold text-xl mb-2">
          # {{ $helpers.toThreeDigits(pokemon.pokedex_number) }}
          {{ pokemon.name }}
        </div>

        <!-- Pokemon types -->
        <PokemonType
          :pokemon="pokemon"
          class="flex items-center justify-center mb-4 mt-4"
        />

        <!-- Pokemon height and weight -->
        <PokemonMeasurements
          :pokemon="pokemon"
          class="flex items-center justify-center mb-4 mt-4"
        />
      </div>
    </div>
  </NuxtLink>
</template>

<script>
import PokemonType from "@/components/cards/PokemonType.vue";
import PokemonMeasurements from "@/components/cards/PokemonMeasurements.vue";

export default {
  name: "PokemonCard",
  components: {
    PokemonType,
    PokemonMeasurements,
  },
  props: {
    pokemon: {
      type: Object,
      default: () => {},
    },
  },
};
</script>
