<template>
  <div class="max-w-sm rounded overflow-hidden shadow-lg">
    <img :src="pokemonImgUrl(pokemon.pokedex_number)" />
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">
        #{{ pokemon.pokedex_number }} {{ pokemon.name }}
      </div>
      <p class="text-gray-700 text-base">
        Type1: {{ pokemon.type1 }} <br />
        Type2: {{ pokemon.type2 }} <br />
        Height (m): {{ pokemon.height_m }} <br />
        Weight (kg): {{ pokemon.weight_kg }} <br />
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "PokemonCard",
  props: {
    pokemon: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      imgUrl:
        "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/thumbnails-compressed/",
    };
  },
  methods: {
    pokemonImgUrl(pokedex_number) {
      return `${this.imgUrl}${this.$helpers.toThreeDigits(pokedex_number)}.png`;
    },
  },
};
</script>
