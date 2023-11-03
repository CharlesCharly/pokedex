<template>
  <div>
    <slot name="home">
      <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
      >
        Home
      </button>
    </slot>
    <div>
      <slot name="title" />
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>
