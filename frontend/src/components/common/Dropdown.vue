<template>
  <div>
    <select v-model="innerValue">
      <option value="all">{{ allLabel }}</option>
      <option v-for="item in list" :value="item">{{ item }}</option>
    </select>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  props: {
    value: {
      type: [String, Boolean],
      default: null,
    },
    allLabel: {
      type: String,
      default: null,
    },
    list: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      innerValue: this.value,
    };
  },
  watch: {
    innerValue(newValue) {
      this.$emit("input", newValue);
    },
    value(newValue) {
      this.innerValue = newValue;
    },
  },
};
</script>
