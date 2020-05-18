window.setInterval("reloadIFrame();", 30000);
function reloadIFrame() {
 document.getElementById("readtemp").src="/readtemp.php";
}
