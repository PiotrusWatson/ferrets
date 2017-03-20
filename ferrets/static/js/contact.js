$("#submit").click(function() {
    $.post(
            $('#contact').attr('action'),
            { message: $('#message').val(),
            email: $('#email').val(),
            name: $('#name').val() }
        )

        .done(function(response) {
            $(".message").append("Your email was sent successfuly. Our team will be in touch!");
        })

        .fail(function(data) {
            $(".message").append("Your message failed to send. Please try again later.");
        });
});