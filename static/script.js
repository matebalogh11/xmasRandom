$(document).ready(function() {
    $( "form" ).submit(function( event ) {
        event.preventDefault();
        console.log( $( this ).serializeArray() );
        $.ajax({
            url: "/",
            method: "POST",
            dataType: "json",
            data: $(this).serializeArray(),
            success: function(response) {
                console.log(response);
                var text;
                var res = response["name"];
                if (res == "noname") {
                    text = "Kérlek adj meg egy nevet!"
                } else if (res == "wrongpass") {
                    text = "Helytelen jelszó!"
                } else if (res == "invalid") {
                    text = "Helytelen név, te nem közülünk való vagy!"
                } else if (res == "error") {
                    text = "Fatális hiba! Kérem lépjen kapcsolatba az oldal készítőjével!"
                } else {
                    text = "A párod nem más mint " + res + "!:)"
                }
                $("#message").text(text);
            }
        })
      });
})