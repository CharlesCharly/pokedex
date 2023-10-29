<template>
  <dir>
    {{ pokemonList }}
  </dir>
</template>

<script>
import { mapActions } from 'vuex';
import { mapFields } from 'vuex-map-fields';

export default {
  name: "Pokedex",
  computed: {
    ...mapFields("pokemon", ["pokemonList"]),
  },
  created() {
    this.getPokemonList();
  },
  methods: {
    ...mapActions({
      getPokemonList: 'pokemon/getPokemonList'
    })
  }
};
</script>
