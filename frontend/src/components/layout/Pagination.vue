<template>
  <div class="w-full my-6">
    <div class="inline-flex">
      <button
        v-if="previousPageUrl"
        class="bg-gray-300 hover:bg-blue-800 hover:text-white hover:border-transparent text-gray-800 font-bold py-2 px-4 rounded-l"
        @click="newPage(previousPageUrl)"
      >
        Prev
      </button>
      <button
        v-if="nextPageUrl"
        class="bg-gray-300 hover:bg-blue-800 hover:text-white hover:border-transparent text-gray-800 font-bold py-2 px-4 rounded-r"
        @click="newPage(nextPageUrl)"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    previousPageUrl: {
      type: String,
      default: null,
    },
    nextPageUrl: {
      type: String,
      default: null,
    },
  },
  methods: {
    newPage(pageUrl) {
      this.$emit("newPage", pageUrl)
    }
  }
};
</script>
