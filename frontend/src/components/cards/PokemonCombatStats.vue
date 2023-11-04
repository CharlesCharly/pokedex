<template>
  <div>
    <span
      class="inline-block bg-red-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
    >
      Attack {{ pokemon.attack }}</span
    >
    <span
      class="inline-block bg-cyan-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
    >
      Defense {{ pokemon.defense }}
    </span>
    <span
      class="inline-block bg-red-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
    >
      SP Attack {{ pokemon.sp_attack }}</span
    >
    <span
      class="inline-block bg-cyan-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
    >
      SP Defense {{ pokemon.sp_defense }}</span
    >
    <span
      class="inline-block bg-red-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
    >
      HP {{ pokemon.hp }}</span
    >
    <span
      class="inline-block bg-cyan-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 ml-2"
    >
      Speed {{ pokemon.speed }}</span
    >
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
};
</script>
