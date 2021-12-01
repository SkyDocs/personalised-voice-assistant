# Personalised Voice Assistant

A Single Personalised Voice Assistant for Multiple users.<br>

Alexa listens to all and functions to their voice, but lacks the personalised results.<br>

But this overcamed that issue.
 -  Functions on every ones voice. 	
 -  Gives pesonalised results when triggred to.

## Usage

### Training of the Voice of the Users

You first have to train the Model for the recognisation of the speakers, which you may train from the [SkyDocs Speaker Identification Repo](https://github.com/SkyDocs/speaker-identification).<br>
And save the `model.h5` file locally.

### Working

For the working of the Voice Assistant, get the `model.h5`  you trained from the Speaker Identificatio Repo. <br>
And now put the `model.h5` file and the *noise* folder from dataset in the Personalised-voice-assistant folder. <br>
Now you have got to modify the files in the *users folder*.<br>
You may personalise the functions and the users files to match the numbers of the users.<br>

For example if you have trained the model for 3 users, then keep/edit the `user_0.py`, `user_1.py`, `user_2.py` and keep the `user_new.py`, this for the unknown/ new users.<br>

### Use your Voice Assistant

Install the requirements by running:

`pip install -r requirements.txt` or `pip3 install -r requirements.txt`

Change the path to *noise* dataset in `predict.py` file to your own path to *noise* folder.

After installing the requirements and doing the necessary changes. 

#### CLI

Run:

`python voice_assistant_cli.py` or `python3 voice_assistant_cli.py` <br>

And here you go. <br>

Have a general Voice Assistant or say "recognise" to trigger the recognition process. <br>

Say a few phrases when prompted. And Boom! <br>
You got your own Personalised Voice Assistant Triggred.

## Contribution

This is a Purely open-source project, and feel free to suggest the changes.<br>

To contribute: Fork it, make the changes and push a pull request and we will get back to you.

## Demo

Watch the demo video.

[![Personalised Voice Assistant Demo Vidoe](https://img.youtube.com/vi/n09Z1OQzUiA/0.jpg)](https://www.youtube.com/watch?v=n09Z1OQzUiA)

## Recognition

This project is selected for the Finals for [Sony's Dreams To Reality contest](https://www.linkedin.com/feed/update/urn:li:activity:6869484493208608768/). 


## License

Licensed under [GNU General Public License v3.0](https://github.com/SkyDocs/personalised-voice-assistant/blob/master/LICENSE)
