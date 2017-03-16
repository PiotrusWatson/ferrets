$("#sendButton").click(function() {
    $.post(
            $('#contact-us').attr('action'),
			{ message: $('#message').val(),
			email: $('#email').val(),
			name: $('#name').val() }
		)

        .done(function(response) {
			alert("Done");
            // $(formMessages).removeClass('error');
            // $(formMessages).addClass('success');

            // $(formMessages).text(response);

            // $('#name').val('');
            // $('#email').val('');
            // $('#message').val('');
        })

        .fail(function(data) {
            // $(formMessages).removeClass('success');
            // $(formMessages).addClass('error');

            // if (data.responseText !== '') {
                // $(formMessages).text(data.responseText);
            // } else {
                // $(formMessages).text('Sorry! Soemthing went wrong. Message not sent.');
            // }
        });
});