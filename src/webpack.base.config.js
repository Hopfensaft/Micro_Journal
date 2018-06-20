var path = require("path")
var webpack = require('webpack')

module.exports = {
  context: __dirname,

  entry: {
      'app': [
      'babel-polyfill',
      'react-hot-loader/patch',
      './src/index'
    ],
    // Add as many entry points as you have container-react-components here
    App: './micro_journal/templates/App',
    vendors: ['react'],
  },

  output: {
      path: path.resolve(__dirname, './journal_entries/static/bundles/local/'),
      filename: "[name]-[hash].js"
  },

  externals: [
  ], // add all vendor libs

  plugins: [
    new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),
  ], // add all common plugins here

  module: {
      rules:[{
            test:/\.css$/,
            use:['style-loader','css-loader']
        }],
    loaders: [] // add all common loaders here
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}