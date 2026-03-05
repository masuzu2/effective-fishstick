function show() {
    let n = document.getElementById("name").value;
    let e = document.getElementById("email").value;

    if (n === "" || e === "") {
        alert("กรอกข้อมูลให้ครบ");
        return;
    }

    document.getElementById("output").innerText = n + " | " + e;
}
