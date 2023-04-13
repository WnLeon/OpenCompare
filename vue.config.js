const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
});

module.exports = defineConfig({
  devServer: {
    //set proxy
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        ws: true,
        changOrigin: true,
        pathRewrite: {
          "^/api": "/",
          //http://localhost:5000/user/login
        },
      },
    },
  },
});
