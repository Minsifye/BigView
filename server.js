var express = require('express');
var app = express();
let fs = require('fs')

app.get('/',pythonFunc);

function pythonFunc(){
//Using spawn to create a child thread to run python script
    var spawn = require('child_process').spawn;
    var process = spawn('python', ["./hack.py",
        
      ]);
      process.stdout.on('data', function (data) {

        const path1 = './a_cloud.png'
        const path2 = './pos_cloud.png'
        const path3 =  './neg_cloud.png'
        const path4 = './plot2.png'
        const path5 = './plot1.png'
        const path6 = './plot3.png'

        try{
          if(fs.existsSync(path1)){
            console.log(path1)
            res.send("File received");
          }
        }
        catch(err){
          console.log(err)
        }

        console.log(data);
        res.send(data.toString());
      });
}
  
    
app.listen(3000, function () {
    console.log('server running on port 3000');
  })