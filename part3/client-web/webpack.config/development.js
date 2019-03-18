"use strict";

// const path = require("path");
// const webpack = require("webpack");
const merge = require("webpack-merge");

const common = require("./common");

const development = {
  devtool: 'inline-source-map',
  watch: true,
  devServer: {
    contentBase: './public',
    hot: true
  },
  mode: "development",
};

module.exports = merge(common, development);
