# Remove Comments
Remove comments from your code to make it more readable (sometimes)

# Running the script:
* Head to your terminal or command prompt
* Type py remove_comments.py
* Then it will prompt you which file you wish to remove the comments from
* _(You must give it the full path)_
* Then give it a name to save as so it doesn't overwrite your file.
* _(You can use a path for this but you can just type a name and it will save in the working directory)_

# Reason for making this script:
I had made a Neural Net in python with a lot of comments and wished to see it without them.

# Adapting the script for other languages:
If you have a language that isn't python you have to make a few edits to the code.

Starting at the bottom you need to change the line:

``` f = open("{}.py".format(new_filename), "w") ```

where it says ".py" you can change that to the extension of your choosing

Then on the lines:

```if((re.search("#", line) != None)): ```
```  temp_array = re.split("#", line, 1)``` 

You must change the "#" to whatever comments are in your language.

Then the initial
``` line = "#Start" ```

You should replace the "#" with whatever your comment is.

# Possible future plans:
* I could just make a question as to what comments are in your language and update accordingly
* I could add multiple file types at the end. Or just get rid of the extension so you can save it as .whatever
* This is all I can forsee for this small script for now.
* If you have any ideas, feel free to message me: dakotapowerstech@gmail.com
    
