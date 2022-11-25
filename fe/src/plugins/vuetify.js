import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
// import colors from "vuetify/lib/util/colors";
import '@fortawesome/fontawesome-free/css/all.css'
Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#4DAF51",
        secondary: "#B85C38",
        accent: "#82B1FF",
        error: "#FF5252",
        info: "#2196F3",
        success: "#4CAF50",
        warning: "#FFC107",
        background: '#FAFAFA',
      },
      dark: {
        primary: "#1976D2",
        secondary: "#fba92c",
        background: "#303030",
      },
    },
  },
  icons: {
    iconfont: "fa",
  },
});
