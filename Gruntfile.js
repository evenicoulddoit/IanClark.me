module.exports = function(grunt) {

  grunt.initConfig({
    'watch': {
      files: ['static/src/*'],
      tasks: ['closure-compiler']
    },
    'closure-compiler': {
      frontend: {
        closurePath: 'bin/',
        js: ['static/src/main.js',
             'static/src/experience.js'],
        jsOutputFile: 'static/js/main.min.js',
        maxBuffer: 500,
        options: {
          compilation_level: 'SIMPLE_OPTIMIZATIONS',
          language_in: 'ECMASCRIPT5_STRICT'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-closure-compiler');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['closure-compiler']);
  grunt.registerTask('build', ['closure-compiler']);
}
