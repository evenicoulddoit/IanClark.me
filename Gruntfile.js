"use strict";

module.exports = function(grunt) {
  var build = [
    "closure-compiler",
    "compass"
  ];

  grunt.initConfig({
    "compass": {
      dist: {
        options: {
          config: "config.rb"
        }
      }
    },
    "closure-compiler": {
      frontend: {
        closurePath: "bin/",
        js: ["./app/static/src/main.js",
             "./app/static/src/experience.js"],
        jsOutputFile: "./app/static/js/main.min.js",
        maxBuffer: 500,
        options: {
          compilation_level: "SIMPLE_OPTIMIZATIONS",
          language_in: "ECMASCRIPT5_STRICT"
        }
      }
    },
    "watch": {
      closure: {
        files: ["./app/static/src/**/*.js"],
        tasks: ["closure-compiler"]
      },
      compass: {
        files: ["./app/sass/**/*.scss"],
        tasks: ["compass"]
      }
    },
  });

  grunt.loadNpmTasks("grunt-closure-compiler");
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-contrib-compass");

  grunt.registerTask("default", build);
  grunt.registerTask("build", build);
};
