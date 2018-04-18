document.getElementById("formNovoAluno").onsubmit=function(event){
      var loginCampo = document.getElementById("login");
      if(loginCampo.value == "") {
            alert("Campo login não preenchido");
            return false;
      }
      var nomeCampo = document.getElementById("nome");
      if(nomeCampo.value == "") {
            alert("Campo nome não preenchido");
            return false;
      }
      var emailCampo = document.getElementById("email");
      if(emailCampo.value == "") {
            alert("Campo E-mail não preenchido");
            return false;
      }
      var dataNascimentoCampo = document.getElementById("nascimento");
      if(dataNascimentoCampo.value == "") {
            alert("Campo Data de Nascimento não preenchido");
            return false;
      }
      var cpfCampo = document.getElementById("cpf");
      if(cpfCampo.value == "") {
            alert("Campo cpf não preenchido");
            return false;
      }
      var senhaCampo = document.getElementById("senha");
      if(senhaCampo.value == "") {
            alert("Campo senha não preenchido");
            return false;
      }
      var confirmarSenhaCampo = document.getElementById("confirmarSenha");
      if(confirmarSenhaCampo.value == "") {
            alert("Campo Confirmar Senha não preenchido");
            return false;
      }

      if(validaCPF(cpfCampo.value)){
            alert("Cpf invalido");
            return false;
      }

      if(senhaCampo.value != confirmarSenhaCampo.value){
            alert("Senhas não consistem");
            return false;
      }
      
      if(idade(data.getFullYear()) < 17){
            alert("Aluno com idade menor a 17 anos")
      }
};
function idade(ano_aniversario) {
      var d = new Date();
      var ano_atual = d.getFullYear();
      var ano_aniversario = +ano_aniversario;

      quantos_anos = ano_atual - ano_aniversario;

  return quantos_anos;
}

function validaCPF(cpf)
  {
    var numeros, digitos, soma, i, resultado, digitos_iguais;
    digitos_iguais = 1;
    if (cpf.length < 11)
          return false;
    for (i = 0; i < cpf.length - 1; i++)
          if (cpf.charAt(i) != cpf.charAt(i + 1))
                {
                digitos_iguais = 0;
                break;
                }
    if (!digitos_iguais)
          {
          numeros = cpf.substring(0,9);
          digitos = cpf.substring(9);
          soma = 0;
          for (i = 10; i > 1; i--)
                soma += numeros.charAt(10 - i) * i;
          resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
          if (resultado != digitos.charAt(0))
                return false;
          numeros = cpf.substring(0,10);
          soma = 0;
          for (i = 11; i > 1; i--)
                soma += numeros.charAt(11 - i) * i;
          resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
          if (resultado != digitos.charAt(1))
                return false;
          return true;
          }
    else
        return false;
  }