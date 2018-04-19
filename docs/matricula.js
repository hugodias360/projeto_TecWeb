document.getElementById("formMatricula").onsubmit = function() {
    var opcao = getElementById("opcao").value
    if (opcao != APROVADO || opcao != CANCELADO)
    {
      alert("Necessário selecionar alguma opção!");
      document.form.opcao.style.background="#FF6666";
                  document.form.opcao.focus()
      return false
    }
};