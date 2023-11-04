<template>
  <div>
    <div class="flex">
      <Header>
        <template #title>
          <img
            src="~/assets/images/pokeball.png"
            class="inline h-12 w-12 rotating-image"
          />
        </template>
      </Header>
    </div>

    <!-- In case we found no Pokemon -->
    <div v-if="isEmptyObject(pokemon)">
      <div>
        <div class="flex items-center justify-center mt-12 mb-12">
          <span class="text-xl font-bold">
            This Pokemon has not be found yet !
          </span>
        </div>
        <div class="flex items-center justify-center mt-12">
          <img
            src="~/assets/images/pikachu_surprised.png"
            class="h-36 w-48 inline mr-2"
          />
        </div>
      </div>
    </div>

    <!-- Display the Pokemon -->
    <div v-else>
      <!-- Pokemon image -->
      <div class="flex items-center justify-center pt-2">
        <img :src="$helpers.pokemonImgUrl(pokemon.pokedex_number)" />
      </div>

      <!-- Pokemon number -->
      <div class="flex items-center justify-center mt-2">
        <span class="font-bold text-3xl">
          # {{ $helpers.toThreeDigits(pokemon.pokedex_number) }}
        </span>

        <!-- Display if the Pokemon is legendary or not -->
        <span
          class="image-container"
          @mouseover="showTooltip"
          @mouseleave="hideTooltip"
        >
          <img :src="legendaryImg" class="h-6 w-6 inline ml-2" />
          <div class="tooltip" v-if="isTooltipVisible">
            {{ tooltipText }}
          </div>
        </span>
      </div>

      <!-- Pokemon name, generation and japanese name -->
      <div class="flex items-center justify-center font-bold text-3xl mt-4">
        {{ pokemon.name }}
      </div>
      <div class="flex items-center justify-center italic text-sm">
        <span>Generation {{ pokemon.generation }}</span>
      </div>
      <div class="flex items-center justify-center text-l mt-4 mb-4">
        <img src="~/assets/images/japan.png" class="h-6 w-6 inline mr-2" />
        {{ pokemon.japanese_name }}
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

      <!-- Classification -->
      <div class="flex items-center justify-center mb-4 mt-4">
        <span
          class="bg-transparent text-black font-semibold py-2 px-4 border border-black rounded-lg"
        >
          {{ pokemon.classification }}
        </span>
      </div>

      <!-- Combat Stats -->
      <PokemonCombatStats
        :pokemon="pokemon"
        class="flex items-center justify-center mb-4 mt-4"
      />
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { mapFields } from "vuex-map-fields";
import Header from "@/components/layout/Header.vue";
import PokemonType from "@/components/cards/PokemonType.vue";
import PokemonMeasurements from "@/components/cards/PokemonMeasurements.vue";
import PokemonCombatStats from "@/components/cards/PokemonCombatStats.vue";

export default {
  name: "PokemonDetail",
  components: {
    Header,
    PokemonType,
    PokemonMeasurements,
    PokemonCombatStats,
  },
  data() {
    return {
      isTooltipVisible: false,
    };
  },
  computed: {
    ...mapFields("pokemon", ["pokemon"]),
    legendaryImg() {
      return this.pokemon.is_legendary
        ? require(`~/assets/images/star_on.png`)
        : require(`~/assets/images/star_off.png`);
    },
    tooltipText() {
      return this.pokemon.is_legendary
        ? "This Pokemon is legendary!"
        : "This Pokemon is not legendary!";
    },
  },
  created() {
    this.getPokemonDetail(this.$route.params.id);
  },
  methods: {
    ...mapActions({
      getPokemonDetail: "pokemon/getPokemonDetail",
    }),
    isEmptyObject(obj) {
      return Object.keys(obj).length === 0;
    },
    showTooltip() {
      this.isTooltipVisible = true;
    },
    hideTooltip() {
      this.isTooltipVisible = false;
    },
  },
};
</script>
