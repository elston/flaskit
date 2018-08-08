import 
    webpack from 'webpack'
import 
    webpackDevMiddleware from 'webpack-dev-middleware'
import 
    proxyMiddleware from 'http-proxy-middleware'

// ...
import 
    wpConfig, { 
    mwConfig as wpMwConfig
} from '../webpack'


// .. WEBPACK
// =====================
const bundler = webpack(wpConfig)
const webpackMw = webpackDevMiddleware(bundler, wpMwConfig)


// PROXY
// =================
const proxyGlob = [
    '**'
]
const proxyConfig = {
    target: 'http://backer:8000',
}
const proxyMw = proxyMiddleware(proxyGlob, proxyConfig)


// ..CONFIG
// =================
export default {
    port: 3000,
    host: '0.0.0.0',
    open: false,
    watch: true,
    server: {
        middleware: [
            webpackMw,
            proxyMw
        ]
    }
}