# CNN_Mech_Parts
A deep learning project for classifying mechanical parts. Based on Promech2020/Mech-parts-classification-seq-model and using Mechanical Classification Benchmark dataset

### Related Work

This is a project that is inspired by Sunny Tuladhar work of making a CNN to classify mechanical parts. I just took interest and improved the original code and model to have the same precision, but working with more classes while also adding some QOL changes to make it easier to keep track of all logs and plots.

### Database

We are going to use Mechanical Classification Benchmark dataset B, that includes 18038 files from 3D warehouse and GrabCAD. Database A includes more files if needed.

#### Preparing data

The expected input is 224x224 images, so a script to take screenshots from the 3D files was included to help converting. In case this changes, just update both the script for extracting screenshots and the value of the input layer.

### CNN Architecture

Very simple architecture, similar to AlexNet. We are going to use 224x224 grey scaled images to feed it. There is a code snippet to extract 8 screenchots of 3D models. The original database was [MCB dataset B](https://mechanical-components.herokuapp.com/)

![CNN Architecture](https://i.imgur.com/4MTnMeg.png)

### Logs, Plots and Models

To help keep track of all the experiments while improving the model, I added a few callbacks to save the model and the training log.

These can be found in the models and logs folder, saved in .h5 and .csv format.

It'll also generated plots for training loss and error, aswell for validation. Lastly, it'll generate a confusion matrix of the last model trained.

![Confusion Matrix](https://i.imgur.com/0VvszSv.png)

### File structure

The current structure of files is to save your prepared data in the refined_data folder divided by datasets folders. If needed, this can be changed, just remember to change how the code will name your models, logs and plots.
