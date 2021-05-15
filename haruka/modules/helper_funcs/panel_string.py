from haruka import dispatcher, INTRO_IMG

if INTRO_IMG is None:
    HYPER_X_IMG = "https://telegra.ph/file/edf94be72ac27e29beacf.jpg"
else:
  HYPER_X_IMG = INTRO_IMG    
SOURCE_STRING = """
✯Im built-in python 3 to help and manage groups
✯To clone me [𝘾𝙡𝙞𝙘𝙠 𝙝𝙚𝙧𝙚](https://github.com)
✯For bot updates [𝙅𝙤𝙞𝙣 𝙃𝙚𝙧𝙚](https://t.me/)
"""

HELP = """
𝑯𝒆𝒚 𝑰𝒂𝒎  *{}*.
I'm a modular group management bot with a few fun extras! Have a look at the following for an idea of some of \
the things I can help you with
✰𝙈𝙖𝙞𝙣 𝙖𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨✰:
 ➪ /start: start the bot
 ➪ /help: PM's you this message.
 ➪ /help <module name>: PM's you info about that module.
 ➪ /settings:
  » in PM: will send you your settings for all supported modules.
  » in a group: will redirect you to pm, with all that chat's settings.
{}
And the following:
"""
