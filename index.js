function newloc(){
    var place = document.getElementById("searchloc").value;
    var themap = document.getElementById("googlemap");
    themap.src="https://maps.google.com/maps?hl=en&q=" + place + "&ie=UTF8&t=roadmap&z=6&iwloc=B&output=embed";
    console.log(themap.src);
}
