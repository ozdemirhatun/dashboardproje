const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", function(e) {
  e.preventDefault();

  var usernameToSend = $('#username').val();
  var passwordToSend = $('#password').val();

  var postParams = {
      'username': usernameToSend,
      'password': passwordToSend

  };

  $.post('/',postParams,function(data){
    if (request.method == 'POST')
    if ('username' in request.form)
    if ('password' in request.form)
    username = request.form['username']
    password = request.form['password']    
    return redirect(url_for('home'))
    
});
    
});

localStorage.setItem("username","asd")