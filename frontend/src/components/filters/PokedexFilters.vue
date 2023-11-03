<template>
  <div>
    <div>
      <!-- Research bar -->
      <SearchBar v-model="searchValue" @input="handleChange" />

      <!-- Pokemon types -->
      <Dropdown
        v-model="dropdownValue"
        :list="pokemonTypes"
        all-label="All Types"
        @input="handleChange"
      />

      <!-- Pokedex number -->
      <RadioButton
        v-model="radioBtnValue"
        type="radio"
        box-id="pokedex_number"
        name="Number"
        @input="handleChange"
      />
      <!-- Pokemon Height -->
      <RadioButton
        v-model="radioBtnValue"
        type="radio"
        box-id="height_m"
        name="Height"
        @input="handleChange"
      />
      <!-- Pokemon Weight -->
      <RadioButton
        v-model="radioBtnValue"
        type="radio"
        box-id="weight_kg"
        name="Weight"
        @input="handleChange"
      />
      <!-- Asc / Desc option -->
      <RadioButton
        v-model="checkboxValue"
        type="checkbox"
        name="Ascending"
        @input="handleChange"
      />
    </div>
  </div>
</template>

<script>
import SearchBar from "@/components/common/SearchBar.vue";
import Dropdown from "@/components/common/Dropdown.vue";
import RadioButton from "@/components/common/RadioButton.vue";

export default {
  name: "FiltersArea",
  components: {
    SearchBar,
    Dropdown,
    RadioButton,
  },
  props: {
    searchQuery: {
      type: String,
      default: null,
    },
    sortFilter: {
      type: String,
      default: null,
    },
    isAsc: {
      type: Boolean,
      default: null,
    },
    typeFilter: {
      type: String,
      default: null,
    },
    pokemonTypes: {
      type: Array,
      default: () => [],
    },
  },
  emits: ["applyFilters"],
  data() {
    return {
      searchValue: this.searchQuery,
      radioBtnValue: this.sortFilter,
      checkboxValue: this.isAsc,
      dropdownValue: this.typeFilter,
    };
  },
  methods: {
    handleChange() {
      this.$emit("handleChange", {
        search: this.searchValue,
        radiobtn: this.radioBtnValue,
        checkbox: this.checkboxValue,
        type: this.dropdownValue,
      });
    },
  },
};
</script>
