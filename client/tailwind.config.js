module.exports = {
  purge: [
    './src/components/*.vue',
    './src/views/*.vue',
    './src/App.vue',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    screens: {
      'lg': '1024px',
      'md': '720px',
      'sm': '480px',
    }
  },
  variants: {},
  plugins: [],
}