function hideTable() {
  document.getElementById("table").style.display = "none";
  document.getElementById("showButton").innerHTML = "Show Table";
  document.getElementById("showButton").onclick = showTable;
}

function showTable() {
  document.getElementById("table").style.display = "table";
  document.getElementById("showButton").innerHTML = "Hide Table";
  document.getElementById("showButton").onclick = hideTable;
}
