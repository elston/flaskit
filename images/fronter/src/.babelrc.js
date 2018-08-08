module.exports = {

  // PRESETS
  presets: [[
    // ..
    '@babel/preset-env', {
      targets: {
        node: 'current'
      }
    }

  ]],

  // PLUGINS
  plugins: [[
    // ...
    '@babel/plugin-proposal-decorators', {
      'legacy': true 
    }
    
  ]],

  // IGNORE
  ignore: [
    'node_modules', 
    'build'
  ],

};