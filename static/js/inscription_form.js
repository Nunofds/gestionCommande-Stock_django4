
var form_fields = document.getElementsByTagName('input')
    form_fields[1].placeholder='Nom d\'utilisateur..';
    form_fields[2].placeholder='E-mail..';
    form_fields[3].placeholder='Mot de passe...';
    form_fields[4].placeholder='Confirmer mot de passe...';

console.log(form_fields[1])

    for (var field in form_fields){
        form_fields[field].className += ' form-control'
    }
