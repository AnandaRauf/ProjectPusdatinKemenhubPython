<<<<<<< HEAD
const defaultTheme = require('tailwindcss/defaultTheme');

whitelist = ["gray", "red", "orange", "yellow", "green", "teal", "blue", "purple", "pink"].reduce(
  (result, color) => result.push(`text-${color}-600`, `bg-${color}-600`, `bg-${color}-500`) && result, [])

module.exports = {
  mode: 'jit',
  purge: {
    content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    options: {
      whitelist,
    }
  },
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio')
  ],
};
=======
module.exports = {
  purge: [
    './src/**/*.html',
    './src/**/*.js',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      zIndex: {
        '-1': '-1',
      },
      flexGrow: {
        '5' : '5'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
>>>>>>> 50be8c0 (Website Jasa Marga Update UI)
