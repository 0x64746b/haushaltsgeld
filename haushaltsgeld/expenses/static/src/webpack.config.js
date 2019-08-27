const path = require('path');

module.exports = {
    entry: {
        editor: './js/editor.js',
    },
    output: {
        path: path.join(__dirname, '/../dist/js'),
        filename: 'expenses.[name].bundle.js',
    }
}