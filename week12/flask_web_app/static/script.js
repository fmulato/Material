document.getElementById('alertBtn').addEventListener('click', function() {
    alert('Hello from JavaScript!');
});
document.getElementById("alertBtn2").addEventListener("click", function() {
    window.location.href = "/logo"; // Redireciona para a rota do Flask
});
document.getElementById("alertBtn3").addEventListener("click", function() {
    window.location.href = "/contact"; // Redireciona para a rota do Flask
});
document.getElementById("backToHome").addEventListener("click", function() {
    window.location.href = "/index.html"; // Redireciona para a rota do Flask
});
