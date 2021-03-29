module.exports = {
    scss: {
        sourcePaths: [
            './src/wagtail_project/static/scss/main.scss'
            // Add all SCSS file you want to split from main.scss
        ]
    },
    css: {
        exportPath: './src/wagtail_project/static/css'
    },
    options: {
        // SOURCEMAP
        sourceMapOptions: {
            loadMaps: true,
            largeFile: true
        },
        // SASS
        sassOptions: {
            start: {
                errLogToConsole: true,
                outputStyle: 'expanded'
            },
            end: {
                outputStyle: 'compressed'
            }
        },
        // AUTOPREFIXER
        prefixOptions: 'last 2 versions',
        // CLEAN CSS
        cleanOptions: {
            level: 2
        }
    }
};