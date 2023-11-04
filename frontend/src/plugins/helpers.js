export default ({ store }, inject) => {
  inject("helpers", {
    toThreeDigits(number) {
      // Use the String() function to convert the number to a string
      // and then use the padStart() function to ensure it has at least 3 digits
      return String(number).padStart(3, "0");
    },

    pokemonImgUrl(pokedex_number) {
      const imgUrl =
        "https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/thumbnails-compressed/";

      return `${imgUrl}${this.toThreeDigits(pokedex_number)}.png`;
    },
  });
};
