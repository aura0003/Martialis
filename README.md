
# **Marcus Valerius Martialis "Martialis"**
Marcus Valerius Martialis, "Martialis" is a Optical character recognition discord bot running on Google's Tesseract OCR Engine.

If you plan to modify this bot **have to**:

- Have tesseract installed on your platform as well as all the libraries and stuff
- Keep the credits, and a link to this repository in all the files that contains my code
- Keep the same license for unchanged code

## Support

Before requesting support, you should know that this bot requires you to have at least a **basic knowledge** of
Python, Google's OCR Engine (Tesseract), and the libraries involved. Do not use the bot or attempt to modify it if you don't know the basics. [Here's](https://pythondiscord.com/pages/resources) a link for resources to learn python.

If you need some help for something, do not hesitate to contact me on discord @ Aura#0003

## Disclaimer

OCR commands can take some time to get registered globally, so if you want to run batches you should use the `ocr 'link'` command via dms to ignore channel clutter.

Also make sure that all Intents are enabled both in the code and the Discord Developer Portal

![All discord intents enabled for the bot](https://cdn.discordapp.com/attachments/1074390415618359459/1074469926942806108/image.png)
```py
# Setting Intents & Prefix

intents =  discord.Intents.all()
client =  commands.Bot(command_prefix  =  '',  intents=intents)  # Command Prefix
```

Please do not open issues or pull requests about things that are written in the [TODO file](TODO.md), they are **already** under work for future versions

## How to download it
* Clone/Download the repository
    * To clone it and get the updates you can definitely use the command
      `git clone`
* Create a discord bot [here](https://discord.com/developers/applications)
* Get your bot token and place it in the `token.token` file
* Invite your bot on servers using the following invite:
  https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands&permissions=PERMISSIONS (
  Replace `YOUR_APPLICATION_ID_HERE` with the application ID and replace `PERMISSIONS` with the required permissions (8)

## How to set up

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (Windows).

Before all that though, we need to install Google's Tesseract on our system if we want the OCR to work. All installation guides can be found at https://tesseract-ocr.github.io/tessdoc/Installation.html.

Before running the bot you will need to install all the requirements with this command:

```
pip3 install -r requirements.txt
```

After that you can start it with

```
python3 bot.py
```

> **Note** You may need to replace `python` with `py`, `python3`, `python3.11`, etc. depending on what Python versions you have installed on the machine.


## Built With
* [Python 3.10.5](https://www.python.org/)

**Disclaimer**
When using the template you confirm that you have read the [license](LICENSE.md) and understand that I can take down your repository if you do not meet these requirements.
