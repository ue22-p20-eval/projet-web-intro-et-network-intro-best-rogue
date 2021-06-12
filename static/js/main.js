

window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move", {dx:-1, dy:0});
                break;
            case 38:
                socket.emit("move", {dx:0, dy:-1});
                break;
            case 39:
                socket.emit("move", {dx:1, dy:0});
                break;
            case 40:
                socket.emit("move", {dx:0, dy:1});
                break;
        }


    };
    
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move", {dx:0, dy:-1});
    };

    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move", {dx:0, dy:1});
    };

    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move", {dx:-1, dy:0});
    };

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move", {dx:1, dy:0});
    };

    var game_over = document.getElementById("game_over");
    game_over.style.display = 'none';
    var div_to_hide = document.getElementById("flexbox");
    div_to_hide.style.display = 'flex';



    socket.on("response", function(data, data2){
        console.log(data);
        for( var i=0; i<2; i++){
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.textContent = data[i].content;
        }
        var coins = data[2];
        var life = data[3];
        var span_to_modif = document.getElementById("money");
        span_to_modif.textContent = coins;
        var span_to_modif = document.getElementById("life");
        span_to_modif.textContent = life;    
    });

    socket.on("responseM", function(data2){
        console.log(data2);
        for( var i=0; i<2; i++){
            var cell_id = "cell " + data2[i].i + "-" + data2[i].j;
            var span_to_modif = document.getElementById(cell_id);
            span_to_modif.textContent = data2[i].content;
        }
        var monster_life = data2[3];
        var span_to_modif = document.getElementById("monster_life");
        span_to_modif.textContent = monster_life;

    });

});