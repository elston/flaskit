import { DEBUG, SRC_DIR } from '../../../consts'
import { reFont, staticAssetName } from '../consts'


// ..
export default {
    test: reFont,
    rules:[{
        test: /\.eot(\?v=\d+.\d+.\d+)?$/,
        loader:'file-loader',
        options: {    
            name: staticAssetName,
        },
    },{
        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader',
        options: {
            limit: 10000,
            mimetype: 'application/font-woff',
            name: staticAssetName,
        },
    },{
        test: /\.[ot]tf(\?v=\d+.\d+.\d+)?$/,
        loader: 'url-loader',
        options: {
            limit: 10000,
            mimetype: 'application/octet-stream',
            name: staticAssetName,
        }
    }]
}
