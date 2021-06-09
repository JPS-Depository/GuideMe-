/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	config.toolbarGroups = [
		{ name: 'document', groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'clipboard', groups: [ 'clipboard', 'undo' ] },
		{ name: 'basicstyles', groups: [ 'basicstyles' ] },
		{ name: 'insert', groups: [ 'insert' ] }
	];

	config.removeButtons = 'SpecialChar, Image,Find,SelectAll,Scayt,Replace,Form,Checkbox,Radio,TextField,Textarea,Select,Button,ImageButton,HiddenField,CopyFormatting,RemoveFormat,Subscript,Superscript,NumberedList,BulletedList,Indent,Outdent,Blockquote,CreateDiv,JustifyLeft,JustifyRight,JustifyBlock,Language,BidiRtl,JustifyCenter,BidiLtr,Link,Unlink,Anchor,Flash,PageBreak,Iframe,Smiley,HorizontalRule,Styles,TextColor,BGColor,ShowBlocks,Format,Font,FontSize,About,Save,Templates,NewPage,Preview,Print';
	config.format_tags = 'p;h1;h2;h3;pre';
	config.extraPlugins = 'mathjax';
	config.mathJaxLib = '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML';
	// Simplify the dialog windows.
	config.removeDialogTabs = 'image:advanced;link:advanced';
	config.enterMode = CKEDITOR.ENTER_BR;
	config.shiftEnterMode = CKEDITOR.ENTER_BR;
};