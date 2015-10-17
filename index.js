function searchmap(){
    var place = document.getElementById("searchloc");
    var themap = document.getElementById("googlemap");
    themap.src="https://maps.google.com/maps?hl=en&q=" + place + "&ie=UTF8&t=roadmap&z=6&iwloc=B&output=embed";
}
