There is much to be done yet,
but it has:

* Binary Sequences exercise
* Decimal Sequences exercise
* Column Reading
* Line Reading 
* Speed Words (with some texts as example reading)

Example use:

python2 main.py

 It will let you choose between exercises using default configuration found in table.py


python2 secuentialdec.py BPM=100 duration=10

 Exercises showing decimals with 100 beats per minute and duration 10 seconds



python2 secuentialbin.py BPM=100 duration=10

 the same but showing binary numbers


python2 reader.py text=random words=3 BPM=200

 line reading using a random text in exampletext folder and using 3 words


python2 reader.py text=clipboard words=3 BPM=200

 the same but it will you text in clipboard (you have to install xsel for this to work)


python2 reader.py text={filename} words=3 BPM=200

 the same but with a file


python2 speedwords.py maze=palabras timeout=800 count=10 field=0

 it will show 10 words taken from the maze palabras, max time 800 msec

 The maze structure is as follow:

  there is a folder with the maze name and inside there is a file index.txt, in each line you have a record that may have several field separated by ;
  when a word is shown, you can change the field pressing key "a"


python2 trainer.py
 it will let you choose a training sequence define in trainer_config.py


THINGS I WANT TO DO:

- Defining a way to send results to a server 
- Include more exercises (even for mental calculation)
