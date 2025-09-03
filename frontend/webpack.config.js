const path = require("path");

module.exports = {
  mode: "production",

  entry: "./src/index.js",

  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "./static/frontend/dist/"),
    publicPath: "/static/frontend/dist/",
    clean: true, // cleans /dist before each build (Webpack 5+)
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
    ],
  },

  optimization: {
    splitChunks: {
      chunks: "all",
    },
    runtimeChunk: "single",
    minimize: true,
  },
};
