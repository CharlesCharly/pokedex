<template>
  <div>
    <div v-if="isEmptyObject(pokemon)">
      <p>This Pokemon has not be found yet !</p>
    </div>
    <div v-else>
      {{ pokemon }}
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { mapFields } from "vuex-map-fields";

export default {
  name: "PokemonDetail",
  computed: {
    ...mapFields("pokemon", ["pokemon"]),
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
    }
  },
};
</script>
