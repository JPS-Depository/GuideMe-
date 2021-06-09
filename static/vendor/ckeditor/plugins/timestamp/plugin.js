CKEDITOR.plugins.add( 'timestamp', {
    icons: 'timestamp',
    init: function( ckeditor ) {
        ckeditor.addCommand( 'insertTimestamp', {
            exec: function( ckeditor ) {
                var now = new Date();
                instances.ckeditor.insertHtml( 'The current date and time is: <em>' + now.toString() + '</em>' );
            }
        });
        ckeditor.ui.addButton( 'Timestamp', {
            label: 'Insert Timestamp',
            command: 'insertTimestamp',
            toolbar: 'insert'
        });
    }
});