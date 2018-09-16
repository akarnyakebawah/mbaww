const express = require('express'),
	app = express()

app.get('/', (req,res) => res.sendFile(__dirname + '/index.html'))

app.use('/campaign', express.static(__dirname + '/campaign'))
app.use('/assets', express.static(__dirname + '/assets'))
app.use('/tumpenganmode2017', express.static(__dirname + '/campaign/tumpenganmode2017'))
app.use('/m2m', express.static(__dirname + '/campaign/m2m'))



app.listen(3000, () => console.log('running'))
