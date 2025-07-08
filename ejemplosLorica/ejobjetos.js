var objEst={
    cedula:null
nombre:null
apellidos:null
nota1:null
nota2:null
nota3:null
}
var myArrayEst=[]
function saveStudents() {
    objEst.cedula = document.getElementById("cedula").value;
    objEst.nombre = document.getElementById("nombre").value;
    objEst.apellidos = document.getElementById("apellidos").value;
    objEst.nota1 = parseFloat(document.getElementById("nota1").value);
    objEst.nota2 = parseFloat(document.getElementById("nota2").value);
    objEst.nota3 = parseFloat(document.getElementById("nota3").value);
console.log(objEst);
    myArrayEst.push({...objEst});
    mostrarDatos();
}