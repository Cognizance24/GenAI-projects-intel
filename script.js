$(document).ready(function() {
    $('#storyForm').submit(function(e) {
        e.preventDefault();

        var storyText = $('#storyText').val();
        $.ajax({
            url: '/generate_video',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ text: storyText }),
            success: function(response) {
                $('#videoContainer').html(`<video controls><source src="${response.video_path}" type="video/mp4"></video>`);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });
});