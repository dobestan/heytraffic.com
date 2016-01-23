module.exports = {
  sass: {
    files: './heytraffic/heytraffic/static/scss/**/*.scss',
    tasks: ['compass'],
  },

  es6: {
    files: './heytraffic/heytraffic/static/es6/**/*.js',
    tasks: ['browserify'],
  },
}
