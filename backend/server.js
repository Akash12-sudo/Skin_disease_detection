// const express = require('express');
// const bodyParser = require('body-parser');
// const path=require('path');
// const { loadLayersModel } = require('@tensorflow/tfjs') ;
// require('@tensorflow/tfjs-node');

// // Load the trained model
// const model =    loadLayersModel('../model-09-0.55.hdf5');

// // Create the Express app
// const app = express();

// // Use body-parser to parse incoming requests
// app.use(bodyParser.urlencoded({ extended: true }));
// app.use(bodyParser.json());

// // Define the API route
// app.get('/',(req,res)=> {

// res.sendFile(path.join(__dirname,'../frontend/index.html'));
// })

// app.post('/predict', async (req, res) => {
//   // Extract the input data from the request body
//   const input = ;

//   // Generate a prediction using the loaded model
//   const output = await model.predict(input);

//   // Send the prediction in the response
//   res.send({ output });
// });

// // Start the server
// app.listen(3000, () => {
//   console.log('Server listening on port 3000');
// });
