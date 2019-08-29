const path = require('path');

module.exports = {
    entry: {
        editor: './js/editor.js',
        'service-worker': './js/service-worker.js'
    },
    output: {
        path: path.join(__dirname, '/../dist/js'),
        filename: 'expenses.[name].js',
    }
}