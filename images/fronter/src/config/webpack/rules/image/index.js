import { DEBUG, SRC_DIR } from '../../../consts'
import { reImage, reStyle, staticAssetName } from '../consts'


// ...
export default {
    test: reImage,
    rules: [{
        test: /\.svg$/,
        loader: 'svg-url-loader',
        options: {
            name: staticAssetName,
            limit: 4096, // 4kb
        },           
    },{
        test: /favicon\.ico$/,    
        loader: 'file-loader',
        options: {
            name: '[name].[ext]'
            // name: '[hash:8].[ext]'            
            // limit: 4096, // 4kb
        },        
    }] 
}

