<template>
  <div>
    <label>
      <input v-model="innerValue" :type="type" :value="boxId" /> {{ name }}
    </label>
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
    type: {
      type: String,
      default: null,
    },
    boxId: {
      type: String,
      default: null,
    },
    name: {
      type: String,
      default: null,
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
