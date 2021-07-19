/* ** ** ** ** **
   Imports require
** ** ** ** ** */
const { src, dest, task, watch, series, parallel } = require('gulp')
const config = require('./gulp.config')
const autoprefixer = require('gulp-autoprefixer')
const cleanCss = require('gulp-clean-css')
const sourcemaps = require('gulp-sourcemaps')
const sass = require('gulp-sass')
var rename = require("gulp-rename");
const browserSync = require('browser-sync')

const server = browserSync.create();



/* ** ** ** ** **
   Global variables
** ** ** ** ** */
let root = 'src/'

let styleWatchFiles = root + '**/*.scss'
let scriptWatchFiles = root + '**/main.min.js'
let pythonWatchFiles = root + '**/*.py'
let htmlWatchFiles = root + '**/*.html'



/* ** ** ** ** **
   Functions
** ** ** ** ** */
function styles() {
    return src(config.scss.sourcePaths)
        .pipe(sourcemaps.init(config.options.sourceMapOptions))
        .pipe(sass(config.options.sassOptions.start).on('error', sass.logError))
        .pipe(autoprefixer(config.options.prefixOptions))
        .pipe(cleanCss())
        .pipe(sass(config.options.sassOptions.end).on('error', sass.logError))
        .pipe(rename({ suffix: '.min' }))
        .pipe(sourcemaps.write('/.maps/'))
        .pipe(dest(config.css.exportPath))
        .pipe(browserSync.stream());
}

/* ** ** ** ** **
   BrowserSync Reload
** ** ** ** ** */
function reload(done) {
    server.reload();
    done();
}
function reload_python(done) {
    setTimeout(function() {
        server.reload();
        done();
    }, 3500)
}

function serve() {
    server.init({
        notify: false,
        port: 8000,
        proxy: 'localhost:8000'
    });
}


/* ** ** ** ** **
   Watch
** ** ** ** ** */
function watchStyle() {
    watch(styleWatchFiles, series(styles, reload))
}
function watchScript() {
    watch(scriptWatchFiles, reload)
}
function watchPython() {
    watch(pythonWatchFiles, reload_python)
}
function watchHtml() {
    watch(htmlWatchFiles, reload)
}



/* ** ** ** ** **
   Run tasks
** ** ** ** ** */
exports.styles = styles
exports.reload = reload
exports.reload_python = reload_python
exports.serve = serve
exports.watchStyle = watchStyle
exports.watchScript = watchScript
exports.watchPython = watchPython
exports.watchHtml = watchHtml

let build = parallel(serve, watchPython, watchHtml, watchStyle, watchScript)
task('default', build)