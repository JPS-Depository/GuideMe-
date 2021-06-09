$(document).ready(function () {
    
    $('#btn-upload').click(function () {
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var form_data = new FormData();
        if(imageUpload.files.length > 1){
            for(i=0; i<imageUpload.files.length; i++){
                form_data.append('images', imageUpload.files[i]);
            }
        } else {
            form_data.append('images', imageUpload.files[0]);
        }
        $('#result').text('uploading');
        $(this).attr('disabled', true);

        $.ajax({
            type: 'POST',
            url: '/upload',
            headers:{
                "X-CSRFToken": csrftoken
            },
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('#btn-upload').attr('disabled', false);
                if(($('#variablenames').val()) == 0){
                    alert("Error, no variable input");
                    return false;
                } else if(($('#variablenames').val()) == 'other'){
                    var textarea = $('#text-area1').val();
                    if (textarea == '---'){
                        $('#text-area1').text(formatUrl($('#var-name').val(), data));
                        $('#img_var').text(formatUrl($('#var-name').val(), data));
                    } else {
                        newtextarea = textarea + "; " + formatUrl($('#var-name').val(), data);
                        $('#text-area1').text(newtextarea);
                        $('#img_var').text(newtextarea);
                    }
                    var optionText = $('#var-name').val(); 
                    var optionValue = $('#var-name').val(); 
                    $('#variablenames').append($('<option>', {
                        value: optionValue,
                        text: optionText
                    }));
                    console.log('Success!');
                } else {
                    var textarea = $('#text-area1').val();
                    var variable = $('#variablenames').val();
                    var text = "[" + variable + "]=";
                    var str = textarea.split(text);
                    if (str.length > 1){
                        var newtextarea = str[0] + "[" + variable + "]=" + data + ", " + str[1];
                    } else {
                        var newtextarea = "[" + variable + "]=" + data + ", " + str;
                    }
                    $('#text-area1').text(newtextarea);
                    $('#img_var').text(newtextarea);
                }
            },
        });
    });
});

function formatUrl(varName, urls) {
    result = "[" + varName + "]=" + urls
    return result
}
