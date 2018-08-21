import 
    MiniCssExtractPlugin from 'mini-css-extract-plugin'
import { 
    DEBUG, 
    SRC_DIR } from '../../../consts'
import { 
    reStyle, 
    minimizeCssOptions, 
    localIdentName } from '../consts'


// ...
export default {
    test: reStyle,
    include: SRC_DIR,
    rules: [{
        loader: MiniCssExtractPlugin.loader,
    },{
        loader: 'css-loader',
        options: {
            /*
            * https://github.com/webpack-contrib/css-loader#importloaders
            * 0 => no loaders (default); 
            * 1 => postcss-loader; 
            * 2 => postcss-loader, sass-loader
            */
            // importLoaders: 1,            
            // ..
            sourceMap: DEBUG,
            minimize: DEBUG 
                ? false 
                : minimizeCssOptions,
        }, 
    },{
        include: SRC_DIR,    
        test: /\.styl$/,
        loader: 'stylus-loader',
        options:{
            'resolve url':true,
        },
    }],
}