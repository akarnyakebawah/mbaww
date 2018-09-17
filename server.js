const express = require('express'),
	app = express(),
	path = require('path'),
	fs = require('fs'),
	multer = require('multer'), 
	{ exec } = require('child_process'),
	random = require('randomstring')

const tmp = './tmp/'
const twibbon_vid = './twibbon_vid/'
const result = './result/'

const storage = multer.diskStorage({
	destination : (req, file, cb) => {
			cb(null, tmp)
		},
		filename: (req, file, cb) => {
			cb(null, random.generate()+'.jpg')
		}
	});

const upload = multer({storage : storage})

const convertVidFile = (vidfile, res) => {
	vidfilemp4 = vidfile.split('.')[0].concat('.mp4')
	exec('ffmpeg -i ./result/'+vidfile+' -r 30 ./result/'+vidfilemp4, (err, stdout, stderr) => {
		if(err){return;} 
		res.setHeader('Content-Type', 'application/json') 
		res.json({filename : vidfilemp4})
	})
}

app.get('/', (req,res) => res.sendFile(path.join(__dirname + '/index.html')))
app.post('/convert', upload.single('image'), (req,res,next) => {
	let imgfile = req.file.filename
	let twibbon = req.body.twibbon
	console.log(imgfile)
	let vidfile = imgfile.split('.')[0].concat('.avi')
	exec('python ./conv.py ./twibbon_vid/'+twibbon+'.mp4 ./tmp/'+imgfile+' ./result/'+vidfile, (err, stdout, stderr) => {
	 	if(err){return;} 
	 	convertVidFile(vidfile, res)
	})
})

app.use('/result', express.static(__dirname + '/result'))
app.use('/lib', express.static(__dirname + '/lib'))
app.use('/assets', express.static(__dirname + '/assets'))

// Active Campaign :
app.use('/campaign', express.static(__dirname + '/campaign'))
app.use('/tumpenganmode2017', express.static(__dirname + '/campaign/tumpenganmode2017'))
app.use('/m2m', express.static(__dirname + '/campaign/m2m'))


app.listen(3000, () => console.log('Twiggsy Running'))
