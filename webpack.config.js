const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: {
    // Add here some files you want to be split from main.js
    bootstrap: "./src/wagtail_project/static/scripts/bootstrap.js",
    main: "./src/wagtail_project/static/scripts/main.js",
  },
  output: {
    path: path.resolve(__dirname, "./src/wagtail_project/static/js"),
    filename: "[name].min.js",
  },

  mode: "production",

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },

  devtool: "source-map",

  optimization: {
    minimize: true,
  },

  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
