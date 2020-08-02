const express=require('express')
const {spawn}=require('child_process')
const app=express()
const port= 8081
const cors=require('cors')

app.use(cors())
app.get('/', (req, res) => {

    var dataToSend
    // spawn new child process to call the python script
    const python=spawn('python3', ['astro.py'])
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...')
        dataToSend=data.toString()
    })
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`)
        // send data to browser
        res.send(dataToSend)
    })

})

app.listen(port, () => console.log(`Example app listening on port 
${port}!`))