"use strict";

//const webpack = require("webpack");
const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
//const HtmlWebpackPlugin = require("html-webpack-plugin");
const { VueLoaderPlugin } = require('vue-loader');
const ManifestPlugin = require('webpack-manifest-plugin');

const devMode = process.env.NODE_ENV !== 'production';

const PROJECT_PATH = process.cwd();
const PROJECT_DIR = path.resolve(PROJECT_PATH, '..');

module.exports = {
  entry: {
    bayonet: path.resolve(PROJECT_PATH, "src", "index.js"),
    //vendors: []
  },
  output: {
    path: path.resolve(PROJECT_DIR, "static"),
    filename: devMode ? 'js/[name].js' : 'js/[name].[hash].js',
    publicPath: '/static/'
  },
  module: {
    rules: [
      {
        enforce: "pre",
        test: /\.(js|vue)$/,
        exclude: /node_modules/,
        loader: "eslint-loader",
        options: {
          formatter: require('eslint-friendly-formatter'),
        },
      },
      {
        test: /\.js$/,
        exclude: "/node_modules/",
        use: {
          loader:  'babel-loader'
        },
      },
      {
        test: /\.vue$/,
        exclude: "/node_modules/",
        use: {
          loader:  'vue-loader',
        },
      },
      {
        test: /\.s(a|c)ss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'postcss-loader',
          {
            loader: 'sass-loader',
            options: {
              indentSyntax: true,
            },
          },
        ],
      },
      {
        test: /\.css$/,
        use: [
          devMode ? 'vue-style-loader' : MiniCssExtractPlugin.loader,
          //MiniCssExtractPlugin.loader,
          "css-loader",
        ]
      },
    ]
  },
  plugins: [
    new ManifestPlugin(),
    new MiniCssExtractPlugin({
      filename: devMode ? 'css/[name].css' : 'css/[name].[hash].css',
      chunkFilename: devMode ? 'css/[id].css' : 'css/[id].[hash].css',
    }),
    new VueLoaderPlugin(),
    //new webpack.ProvidePlugin({}),
    // new HtmlWebpackPlugin({
    //   template: path.resolve(PROJECT_PATH, 'src', 'html.ejs'),
    //   inject: true,
    //   // minify: {
    //   //     collapseWhitespace: true,
    //   //     removeComments: true,
    //   //     removeRedundantAttributes: true,
    //   //     removeScriptTypeAttributes: true,
    //   //     removeStyleLinkTypeAttributes: true
    //   // }
    // }),
  ],
  resolve: {
    extensions: [".js", ".vue", ".css"],
    modules: [
      path.resolve(PROJECT_PATH, "src"),
      "node_modules",
    ],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
    }
  },
};
