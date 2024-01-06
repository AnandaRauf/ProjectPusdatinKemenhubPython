module.exports = {
<<<<<<< HEAD
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
=======
  plugins: [
    require('postcss-import'),
    require('tailwindcss'),
    require('autoprefixer'),
  ]
}
>>>>>>> 50be8c0 (Website Jasa Marga Update UI)
