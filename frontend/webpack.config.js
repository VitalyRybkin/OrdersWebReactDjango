const path = require("path");

module.exports = {
  mode: "production",

  entry: "./src/index.js",

    output: {
        filename: "[name].[contenthash].js",
        path: path.resolve(__dirname, "dist"),
        clean: true,
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
