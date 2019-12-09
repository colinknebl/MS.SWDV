module.exports = function(grunt) {
	require('jit-grunt')(grunt);

	grunt.initConfig({
		less: {
			development: {
				options: {
					compress: true,
					yuicompress: true,
					optimization: 2
				},
				files: {
					'dist/css/styles.css': 'less/styles.less' // destination file and source file
				}
			}
		},
		watch: {
			styles: {
				files: ['less/**/*.less'], // which files to watch
				tasks: ['less'],
				options: {
					nospawn: true
				}
			}
		}
	});

	// grunt.registerTask('default', ['less', 'watch']);
	grunt.registerTask('less:watch', 'Watch and compile changes to Less', [
		'less',
		'watch'
	]);
};
