import { 
    ProvidePlugin,
    DefinePlugin } from 'webpack'
import 
    MiniCssExtractPlugin from 'mini-css-extract-plugin'
import 
    WebpackAssetsManifest from 'webpack-assets-manifest'    
import 
    UglifyJsPlugin from 'uglifyjs-webpack-plugin'
import 
    OptimizeCSSAssetsPlugin from 'optimize-css-assets-webpack-plugin'

// ...
import { 
    ROOT_DIR, 
    BUILD_DIR, 
    DEBUG, 
    QUIET } from '../consts'



// 1. COMMON
// ================================
const config = {}

// .. -=1.1=-
config['mode'] =  DEBUG 
    ? 'development' 
    : 'production'

// .. -=1.3=-
config['bail'] =  !DEBUG

// .. -=1.4=-
config['cache'] =  DEBUG

// .. -=1.5=-
config['devtool'] = DEBUG 
    ? 'cheap-module-inline-source-map' 
    : 'source-map'

// .. -=1.6=-
config['target'] =  'web'

// .. -=1.7=-
config['stats'] = {
    cached: !QUIET,
    cachedAssets: !QUIET,
    chunks: !QUIET,
    chunkModules: !QUIET,
    colors: true,
    hash: !QUIET,
    modules: !QUIET,
    reasons: DEBUG,
    timings: true,
    version: !QUIET,
}

// .. -=1.8=-
// ================================
config['optimization'] = {}

// 1.8.1 Errors
config.optimization['noEmitOnErrors'] =  true

// 1.8.2 minimizer
config.optimization['minimize'] = !DEBUG

if (!DEBUG) {
    config.optimization['minimizer'] = [
        new UglifyJsPlugin({
            cache: true,
            parallel: true,
            // set to true if you want JS source maps            
            sourceMap: true,
        }),
        new OptimizeCSSAssetsPlugin({
            // ...pass
        })
    ]
}

// 1.8.3 Chunks
config.optimization['splitChunks'] = {
    cacheGroups: {
        vendors: {
            name: 'vendors',
            test: /[\\/]node_modules[\\/]/,
            chunks: 'all',
            priority: -10,
        },
        default: {
            minChunks: 2,
            priority: -20,
            reuseExistingChunk: true,
        }
    }
}




// 2. ENTRY
// ================================
config['entry'] = {}

// .. 0 context
config['context'] = ROOT_DIR

// ...lending
config.entry['lending'] = [
    `./src/lending/index.js`
]

// ...eggs
config.entry['eggs'] = [
    `./src/eggs/index.js`
]



// 3. OUTPUT
// ================================
config['output'] = {}
// ..
config.output['path'] = BUILD_DIR
config.output['publicPath'] = '/build/'
// ..
config.output['filename'] = DEBUG 
    ? '[name].js' 
    : '[name].[chunkhash:8].js'
// ..
config.output['chunkFilename'] = DEBUG
  ? '[name].chunk.js'
  : '[name].[chunkhash:8].chunk.js'


// 4. RESOLVE
// ================================
config['resolve'] = {}
// ..
config.resolve['modules'] = [
    'node_modules', 
    'src'
]


// 5. MODULE
// ================================
config['module'] = {}

// .. Make missing exports an error instead of warning
config.module['strictExportPresence'] = true

// ..
config.module['rules'] =  [
    require('./rules/script').default,
    require('./rules/style').default,
    require('./rules/tmpl').default,
    require('./rules/image').default,
    require('./rules/font').default
]



// 6. PLUGGINS
// =======================
config['plugins'] = []

// 6.1 MiniCssExtractPlugin
config.plugins.push(new MiniCssExtractPlugin({
    filename: DEBUG 
        ? '[name].css' 
        : '[name].[chunkhash:8].css',
}))

// 6.2 ProvidePlugin
config.plugins.push(new ProvidePlugin({ 
    $: 'jquery', 
    jQuery: 'jquery' 
}))

// 6.3 DefinePlugin
config.plugins.push(new DefinePlugin({
    'process.env.BROWSER': true,
    __DEV__: DEBUG,
}))

// 6.4 WebpackAssetsManifest
config.plugins.push(new WebpackAssetsManifest({
    output: `${BUILD_DIR}/manifest.json`,
    publicPath: false,
    writeToDisk: true,
}))



// 7. MIDDLEWARE
// ================================
const mwConfig = {}

// .. -==6.1-
mwConfig['publicPath'] = config.output.publicPath

// .. -=6.2=-
mwConfig['noInfo'] =  true

// .. -=6.3=-
mwConfig['quiet'] =  QUIET

// .. -=6.4=-
mwConfig['stats'] = {
    assets: false,
    colors: true,
    version: false,
    hash: false,
    timings: false,
    chunks: false,
    chunkModules: false
}


// ..
export default config
export { mwConfig }
