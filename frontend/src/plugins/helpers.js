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

    capitalizeFirstLetter(array) {
      var result = [];

      for (var i = 0; i < array.length; i++) {
        var string = array[i];

        if (string) {
          result.push(string.charAt(0).toUpperCase() + string.slice(1));
        } else {
          result.push(string);
        }
      }

      return result;
    },

    toLowerCase(string) {
      return string.toLowerCase();
    },

    scrollToTop() {
      const duration = 500;
      const start = window.scrollY;
      const startTime = performance.now();

      function scrollToTop(timestamp) {
        const elapsed = timestamp - startTime;

        window.scrollTo(0, easeInOut(elapsed, start, -start, duration));

        if (elapsed < duration) {
          requestAnimationFrame(scrollToTop);
        }
      }

      function easeInOut(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return (c / 2) * t * t + b;
        t--;
        return (-c / 2) * (t * (t - 2) - 1) + b;
      }

      requestAnimationFrame(scrollToTop);
    },
  });
};
