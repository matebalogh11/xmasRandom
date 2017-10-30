$(document).ready(function() {
    $( "form" ).submit(function( event ) {
        event.preventDefault();
        $.ajax({
            url: "/",
            method: "POST",
            dataType: "json",
            data: $(this).serializeArray(),
            success: function(response) {
                $("form").each(function() {
                    this.reset()
                });
                var text;
                var res = response["name"];
                if (res == "noname") {
                    text = "Kérlek adj meg egy nevet mindenképp!"
                } else if (res == "wrongpass") {
                    text = "Még a jelszót sem tudtad megjegyezni..!"
                } else if (res == "invalid") {
                    text = "Helytelen név, te nem közülünk való vagy!"
                } else if (res == "error") {
                    text = "Upsz.. Kérem lépjen kapcsolatba az oldal készítőjével!"
                } else {
                    text = "A párod nem más mint " + res + "!"
                }
                $("#message").text(text);
            }
        })
      });
})