### VirtualAssistant with Python and APIs
I would like to demonstrate the program written in the Assistant.py file
Use the code for purposes if you wish to.
Download the project files using:<br>
<code>github clone https://github.com/VIROOPAKSHC/VirtualAssistant </code>
<br>

<i><b>Description:</b></i>
This virtual assistant program demonstrates the use of Python programming language and connects with several websites through API calls and gets the info on behalf of us. 
Working on this I hope to add many things to my virtual_Assistant so that it does more help to me. <br>
<br>


Libraries used:
<ul>
  <li>pyttsx3</li>
  <li>speech_recognition</li>
  <li>datetime</li>
  <li>sys</li>
  <li>wikipedia</li>
  <li>smtplib</li>
  <li>os</li>
  <li>pyautogui</li>
  <li>webbrowser</li>
  <li>psutil</li>
  <li>pyjokes</li>
</ul>

<b><em>The control flow of the program:</em></b>:
<ul>
  <li>
    The program imports all the required libraries at the start and aliases are done for convenience throughout the usage
    imports made can be found at the top of the file <br>
    <p><code>
    import pyttsx3,datetime,sys,wikipedia,smtplib,os,pyautogui,psutil,pyjokes
    import speech_recognition as sr 
    import webbrowser as wb </code></p>
   
  </li>
  <li>
  The pyttsx3 module for text to speech is activated and the engine is started
  and assigned to a variable named engine
  <code>engine=pyttsx3.init()</code>
  The voice is set using the 'voices' Property in the engine variable and the setProperty function
    <code>
      voices=engine.getProperty('voices')
      engine.setProperty('voice',voices[0].id)
    </code>
  </li>
   
  <li>
    main function is run when the file is run directly and does not run when it is imported as a module.
    <code>__name__=="__main__"</code>
  </li>
</ul>
  
  <b>The main function calls each of the funciton defined in the program sequentially:</b>
<ol>
    <li>
    speak() function:
      Is written to handle all the speaking of the assistant through it. <br>
      It takes the content , speed as parameters and speaks the content to the user in the specified speed. <em><b> The default speed of the assistant (pyttsx3 module variable) has 200 as its speed. </b></em>
    </li>
  <li>
      The wish() function:
      Function uses the speak function and greets the user whoever is running the program
      with a <i>greeting according to the time.</i>
    </li>
  <li> 
    takeCommand() function:
      This function listens to the user through the speech_recognition module's variable and tries to convert the user's command into text as a command to execute one of the functions defined to handle the command.
      If the module is unable to understand the command it prompts the user to specify it again and the error is handled by the try-except block. 
  </li>
  <li>
      The time() function:
      <em> It is called when the word "time" is in the query </em>
      It uses the datetime module to get the time in a specific format (<code>HH:MM:SS</code>)
      and tells the user the time.
    </li>
  
  <li>The date() function:
      <em> It is called when the word "Date" is in the query </em>
      It uses the datetime module to get the date and tells the user the date.
    </li>
      <li>cpu</li>
    <li>screenshot</li>
    <li>sendmail</li>
    <li>jokes</li>
    <li>offline</li>
    <li>wikipedia</li>
    <li>search</li>
    <li>logout,shutown,restart</li>
    <li>remember</li>
 
</ol>
  
## <b>Contact me</b>
<button><a href="https://www.linkedin.com/in/viroopaksh-chekuri-9997301a7/">Chekuri Viroopaksh - LinkedIn</a></button> <br>
  <button><a href="https://twitter.com/ViroopakshC">Chekuri Viroopaksh - Twitter</a></button> <br>
  <button><a href="https://github.com/VIROOPAKSHC/">Chekuri Viroopaksh - Github</a></button> <br>
