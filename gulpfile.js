/* ** ** ** ** **
   Imports require
** ** ** ** ** */
const { src, dest, task, watch, series, parallel } = require('gulp')
const autoprefixer = require('gulp-autoprefixer')
const cleanCss = require('gulp-clean-css')
const sourcemaps = require('gulp-sourcemaps')
const concat = require('gulp-concat');
const sass = require('gulp-sass')
const browserSync = require('browser-sync')

const server = browserSync.create();



/* ** ** ** ** **
   Global variables
** ** ** ** ** */
let root = 'src/'
let source = root + 'wagtail_project/static/'

let styleWatchFiles = root + '**/*.scss'
let scriptWatchFiles = root + '**/main.min.js'
let pythonWatchFiles = root + '**/*.py'
let htmlWatchFiles = root + '**/*.html'



/* ** ** ** ** **
   Functions
** ** ** ** ** */
function styles() {
    return src([source + 'scss/main.scss'])
        .pipe(sourcemaps.init({loadMaps: true, largeFile: true}))
        .pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError))
        .pipe(autoprefixer('last 2 versions'))
        .pipe(cleanCss())
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(concat('main.min.css'))
        .pipe(sourcemaps.write('/.maps/'))
        .pipe(dest(source + 'css'))
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