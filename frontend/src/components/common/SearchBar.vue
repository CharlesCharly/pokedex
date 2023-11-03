<template>
  <div>
    <input
      v-model="innerValue"
      :placeholder="placeholder"
    />
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  props: {
    value: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      innerValue: this.value,
      placeholder: "Search ...",
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
