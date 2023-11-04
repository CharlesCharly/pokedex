<template>
  <div>
    <RadarChart
      :series-data="combatStats"
      :xaxis-categories="combatLabel"
    />
  </div>
</template>

<script>
import RadarChart from "@/components/common/RadarChart.vue";

export default {
  name: "PokemonType",
  components: {
    RadarChart,
  },
  props: {
    pokemon: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      combatStats: [
        this.pokemon.attack,
        this.pokemon.defense,
        this.pokemon.sp_attack,
        this.pokemon.sp_defense,
        this.pokemon.hp,
        this.pokemon.speed,
      ],
      combatLabel: [
        "Attack",
        "Defense",
        "SP Attack",
        "SP Defense",
        "HP",
        "Speed",
      ],
    };
  },
};
</script>
