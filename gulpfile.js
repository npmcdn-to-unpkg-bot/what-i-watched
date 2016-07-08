var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('default', function() {
    console.log('set up gulp');
});

gulp.task('sass', function() {
    return gulp.src('visual/static/visual/css/main.scss')
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(gulp.dest('visual/static/visual/css/'));
});

gulp.task('sass:watch', function () {
    gulp.watch('visual/static/visual/css/main.scss', ['sass']);
});