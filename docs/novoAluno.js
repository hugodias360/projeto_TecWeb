document.getElementById("formNovoAluno").onsubmit=function(event){


      var dataNascimento = document.getElementById("nascimento");
      var data = idade(dataNascimento.value);
      if(data < 17){
            alert("Aluno com idade menor a 17 anos");
            return false;
      }
      var cpfCampo = document.getElementById("cpf");
      if(validaCPF(cpfCampo.value)){
            alert("Cpf invalido");
            return false;
      }
      
      var senhaCampo = document.getElementById("senha");
      var confirmarSenhaCampo = document.getElementById("confirmarSenha");
      if(senhaCampo.value != confirmarSenhaCampo.value){
            alert("Senhas não consistem");
            return false;
      }

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
  };
function idade(ano_aniversario) {
      var d = new Date();
      var data_atual = new Date(ano_aniversario);
      var ano_atual = d.getFullYear();

      quantos_anos = ano_atual - data_atual.getFullYear();

  return quantos_anos;
};
