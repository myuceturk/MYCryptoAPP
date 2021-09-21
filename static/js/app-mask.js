/*
 * Form Input Masking
 */
$(function () {
    $('#currency-demo').formatter({
        'pattern': '$ {{999}}-{{999}}-{{999}}.{{99}}',
        'persistent': true
    });
});