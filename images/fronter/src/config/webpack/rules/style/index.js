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
        exclude: SRC_DIR,
        loader: 'css-loader',
        options: {
            sourceMap: DEBUG,
            minimize: DEBUG 
                ? false 
                : minimizeCssOptions,
        },
    },{
        include: SRC_DIR,
        loader: 'css-loader',
        options: {
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