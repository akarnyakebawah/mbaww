var form = document.getElementById('imaji')
var loading = document.getElementById('loading') 

form.addEventListener('submit', handleSubmit, true)


function handleSubmit(){

	var xhr = new XMLHttpRequest()
	
	loading.style.display = "block"
	xhr.open(form.method, form.action, true)
	xhr.responseType = 'json' 
	xhr.onload = function() {
		var jsonResponse = xhr.response
		console.log(jsonResponse)
		window.location = window.location.href+'result/'+jsonResponse.filename
	}
	xhr.send(new FormData(form)) 
	event.preventDefault()
}
