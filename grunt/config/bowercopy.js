module.exports = {
  options: {
    clean: true,
    destPrefix: 'dist/components/'
  },
  vendor: {
    files: {
      'js/jquery.min.js': 'jquery/dist/jquery.min.js',
      'js/jquery.min.map': 'jquery/dist/jquery.min.map',

      'js/bootstrap.min.js': 'bootstrap/dist/js/bootstrap.min.js',
      'css/bootstrap.min.css': 'bootstrap/dist/css/bootstrap.min.css',
      'css/fontawesome.min.css': 'font-awesome/css/font-awesome.min.css',

      'fonts': [
        'bootstrap/fonts/',
        'font-awesome/fonts/',
      ]
    }
  }
}
