var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('default', function() {
    console.log('set up gulp');
});

gulp.task('sass', function() {
    return gulp.src('static/static_dirs/css/main.scss')
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(gulp.dest('static/static_dirs/css/'));
});

gulp.task('sass:watch', function () {
    gulp.watch('static/static_dirs/css/main.scss', ['sass']);
});