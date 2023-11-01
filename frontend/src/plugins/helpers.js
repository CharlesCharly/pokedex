export default ({ store }, inject) => {
  inject("helpers", {
    toThreeDigits(number) {
      // Use the String() function to convert the number to a string
      // and then use the padStart() function to ensure it has at least 3 digits
      return String(number).padStart(3, "0");
    },
  });
};
