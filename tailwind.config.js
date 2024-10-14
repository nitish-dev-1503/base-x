/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'cornell_red': { DEFAULT: '#bf211e', 100: '#260606', 200: '#4c0d0c', 300: '#721312', 400: '#981a18', 500: '#bf211e', 600: '#e03936', 700: '#e76a68', 800: '#ef9c9a', 900: '#f7cdcd' },
        'snow': { DEFAULT: '#fcf7f8', 100: '#481b24', 200: '#913749', 300: '#c5677a', 400: '#e1afb9', 500: '#fcf7f8', 600: '#fdf9fa', 700: '#fdfbfb', 800: '#fefcfc', 900: '#fefefe' },
        'lime': { DEFAULT: '#bced09', 100: '#252f02', 200: '#4b5e03', 300: '#708e05', 400: '#96bd07', 500: '#bced09', 600: '#cdf832', 700: '#d9f965', 800: '#e6fb99', 900: '#f2fdcc' },
        'electric_indigo': { DEFAULT: '#6320ee', 100: '#130432', 200: '#270865', 300: '#3a0b97', 400: '#4d0fc9', 500: '#6320ee', 600: '#844df2', 700: '#a279f5', 800: '#c1a6f8', 900: '#e0d2fc' }
      },
      fontFamily: {
        'ubuntu': ['Ubuntu', 'sans-serif']
      }
    },
  },
  plugins: [],
}

