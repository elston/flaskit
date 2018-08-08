import browserSync from 'browser-sync'
// ...
import config from '../config/browsersync'

export default () => {
    // ..
    return new Promise((resolve, reject) =>
        browserSync.create().init(
            config,
            (error, bs) => {
                // ..
                if (error){
                    console.info(error)
                    return reject(error) 
                }
                // ..
                return resolve(bs)
            },
        )
    )
}