module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      // backgroundImage: {
      //   "cardbg": require('./src/assets/images/cardbg.png')
      // },
      colors: {
        "apptext": "#4A4F60",
        "appbg": "#f6f6f9",
        "appselectedsection": "#2656FF",
        "appgreytext": "#878CA1",
        "appfiltertext": "#535E86",
        "appthead": "#878CA1"
      },
      width: {
        "220px": "220px",
        "500px": "500px"
      },
      minWidth: {
        "220px": "220px"
      },
      minHeight: {
        "half": "50vh"
      },
      height: {
        "60px": "60px",
        "progress": "5px"
      },
      boxShadow: {
        "block": "0px 4px 4px rgba(111, 135, 238, 0.3)",
        "side": "0px 0px 4px rgba(111, 135, 238, 0.3)",
        "bottom": "0px 1px 4px -2px rgba(111, 135, 238, 0.15)",
        "card": "0px 2px 10px rgba(111, 135, 238, 0.1)"
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
