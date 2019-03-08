module.exports = {
  root: true,
  env: {
    browser: true,
  },
  parserOptions: {
    parser: 'babel-eslint',
    sourceType: 'module'
  },
  plugins: [
    'html',
    'flowtype-errors'
  ],
  extends: [
    'standard',
    'plugin:vue/essential',
    'eslint:recommended'
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'flowtype-errors/show-errors': 2
    //"indent": [2, "tab"],
    //"no-tabs": 0
  }
}
