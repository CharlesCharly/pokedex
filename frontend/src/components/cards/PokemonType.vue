<template>
  <div>
    <span
      v-if="pokemon.type1"
      class="inline-block bg-cyan-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
      >{{ pokemon.type1 }}</span
    >
    <span
      v-if="pokemon.type2"
      class="inline-block bg-purple-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
      >{{ pokemon.type2 }}</span
    >
  </div>
</template>

<script>
export default {
  name: 'PokemonType',
  props: {
    pokemon: {
      type: Object,
      default: () => {},
    },
  },
}
</script>
