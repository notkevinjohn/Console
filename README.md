# Console
A Kivy Console Widget

 ![](https://github.com/notkevinjohn/Console/blob/master/docs/console.gif)

This widget was designed to provide a terminal-like output running inside a Kivy GUI app. Aside from displaying data to the screen, it also has the ability to write data to a plain text log file. This tool has proven useful in several different industrial automation and manufacturing applications. While not shown in the included animation, the Console descends from scroll view and will show a scroll bar once the content becomes larger than the current screen. 

The Console class exposes the following methods (look inside Demo.py for an example implementation). 

## message(text, color) 
displays the supplied text to the console using the specified color (or white if not specified) and also writes that same message to the log file

## message_temp(text, color) 
displays the supplied text to the console using the specified color (or white if not specified) and also writes that same message to the log file. This line will be deleted and replaced the next time a line is written to the console. 

## note(text, color) 
displays the supplied text to the console using the specified color (or white if not specified) but writes nothing to the log file. 

## note_temp(text, color) 
displays the supplied text to the console using the specified color (or white if not specified) but writes nothing to the log file. This line will be deleted and replaced the next time a line is written to the console. 


## log(text)
writes the supplied text to the log file, but does not write it to the console.  
