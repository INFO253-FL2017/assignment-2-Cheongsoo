console.log("js/script.js has been loaded!");

var contactForm = document.getElementById("contact");
contactForm.addEventListener("submit", function(event) {

	var contactDiv = document.getElementById("errors");
	contactDiv.innerHTML = localStorage.curlocation;

	contactDiv.classList.remove("error");
	contactDiv.classList.remove("send");

	event.preventDefault();

	var fname = document.getElementById("firstname").value; 
	var lname = document.getElementById("lastname").value;
	var subject = document.getElementById("subject").value;
	var message = document.getElementById("message").value;

	contactDiv.innerHTML = "Please fill in: ";
	if (fname.length == 0){
		contactDiv.innerHTML += "first name ";
	} 
	if (lname.length == 0) {
		contactDiv.innerHTML += "last name ";
	} 
	if (subject.length == 0) {
		contactDiv.innerHTML += "subject ";
	} 
	if (message.length == 0) {
		contactDiv.innerHTML += "message ";
	} 
	if (fname.length > 0 && lname.length > 0 && subject.length > 0 
		&& message.length > 0) {
		contactDiv.innerHTML= "Your message has been sent!";
	}

	if (contactDiv.innerHTML != "Your message has not been sent!") {
		contactDiv.classList.add("send");
	} 

	if {
		contactDiv.classList.add("error");
	}
	else {
		var xhttp = new XMLHttpRequest();
		xhttp.open("POST","/p",true);
		s = xhttp.send('{"name":"' + name + '","email":"' + email + '","subject":"' + subject + '","msg":"' + message + '"}')
		message = "";
		subject = "";
		output.innerHTML = 'Hi ' + name + ', your message has been sent';
		name = "";
	}	
})
