# Personalised Voice Assistant

This is a multi-user personalied Voice Assistant, unlike Google Assistant or Alexa or Siri.<br>

They tend to recognise only single user's voice and work on their commands only.<br>

But this voice assistant can function for multiple users. Say 4 to 5 members.<br>

## Usage

### Training of the Voice of the Users

You first have to train the Model for the recognisation of the speakers, which you may train from the SkyDocs Speaker Identification [Repo](https://github.com/SkyDocs/speaker-identification).<br>
And save the `model.h5` file locally.

### Working

For the working of the Voice Assistant, get the `model.h5`  you trained from the Speaker Identificatio Repo. <br>
And now put the `model.h5` file and the *Noise Folder* from dataset in the Personalised-voice-assistant folder. <br>
Now you have got to modify the files in the *users folder*.<br>
You may personalise the functions and the users files to match the numbers of the users.<br>

For example if you have trained the model for 3 users, then keep/edit the `user_0.py`, `user_1.py`, `user_2.py` and keep the `user_new.py`, this for the unknown/ new users.<br>

### Use your Voice Assistant

Install the requirements by running:

`pip install -r requirements.txt` or `pip3 install -r requirements.txt`

After installing the requirements and doing the necessary changes. Run: <br>

`python predict.py` or `python3 predict.py` <br>

<br>
And here you go. Say a few phrases for the model to predict and once predicted, it will welcome with your presonalised results.

## Contribution

This is a Purely open-source project, and feel free to suggest the changes.<br>

To contribute Fork it, make the changes and push a pull request and we will get back to you.


## License

Licensed under [MIT License](https://github.com/SkyDocs/personalised-voice-assistant/blob/master/LICENSE)