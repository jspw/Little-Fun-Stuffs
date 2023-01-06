# Chrome Extension : Free Facebook Message Notifier

## Problem

I was using [Free FB](free.facebook.com) in my pc using a modem (Robi SIM) as I'm _gorib_ :3 It's nice of Robi SIM company (as well as FB) as they give you this feature when you don't have internet (mb). You can browse facebook,read posts without images or videos. Basically its limited with some features.

Btw you can also send messages too and here rises a problem that you need to refresh the page every time to check if someone has texted you (though nobody texts you :3 ).

## Solution

So I have made a chrome extension to refresh the specific page every n ms to check if someone has texted you or not. Then it will rise a alert message window for you.

## How It works

It's very simple actually.

- Just went to the inspect mode and find out that every new message section is wrapped with a class named `bs bt bu bv bw bx by bz ca`.
- Used `document.getElementsByClassName()` to check if the class exists and give a alert message.
- Used `location.reload()` to refresh the page
- Made this as a chrome extension

## How To Use

- git clone `repo_url`
- Open chrome
  - Goto Settings
  - Goto Extensions
  - Turn on developer mode (top Right blue toggle button)
  - Select **Load unpacked**
  - Select the cloned repository directory
  - open free.facebook.com/messages in browser
  - Enjoy :3

### Note

- I'm using this facebook free service from **Bangladesh**. No Idea about other countries.
- I'm not sure about that hitting fb that much time can be harmful for your _facebookId_ or not (though I had used it for about a week and my profile is fine yet)
