import { 
    DEBUG } from '../../consts'


/*
* Regexps for any types of styles
*/
export const reScript = /\.(js|jsx|mjs)$/
export const reStyle = /\.(styl|(le|sa|sc|s|c)ss)$/
export const reImage = /\.(bmp|gif|jpe?g|png|svg|ico)$/
export const reTmpl = /\.pug$/
export const reFont = /\.(woff(2)?|[ot]tf|eot)$/
export const reText = /\.(txt|md)$/

// ..
// export  const staticAssetName = DEBUG
//     ? '[path][name].[ext]?[hash:8]'
//     : '[hash:8].[ext]'

export  const staticAssetName = DEBUG
    ? '[path][name].[ext]'
    : '[hash:8].[ext]'

// ..
export const localIdentName = DEBUG
    ? '[name]-[local]-[hash:base64:5]'
    : '[hash:base64:5]'

// ...
export const minimizeCssOptions = {
    discardComments: { 
        removeAll: true 
    },
}  