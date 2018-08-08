import webpack from 'webpack'
// ...
import config from '../config/webpack'

/**
 * @descr 
 * @param {null}
 * @returns {Promise<void>} promise
 */
const bundle = () => {
    return new Promise((resolve, reject) => {
        webpack(config).run((err, stats) => {

            // ..1
            if (err) {
                return reject(err)
            }

            // ..2
            console.info(
                stats.toString(config.stats)
            )

            // ..3
            if (stats.hasErrors()) {
                return reject(
                    new Error('Webpack compilation errors')
                )
            }

            // ..4
            return resolve()
        })
    })
}


// ...
export default bundle